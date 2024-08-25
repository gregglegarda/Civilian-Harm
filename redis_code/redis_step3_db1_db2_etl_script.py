import redis
from datetime import datetime

# Connect to the Redis server
source_redis = redis.StrictRedis(host='localhost', port=6379, db=1)  # Source database (db0)
target_redis = redis.StrictRedis(host='localhost', port=6379, db=2)  # Target database (db1)

# Get the current timestamp
timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')


# Function to copy and add timestamp to a string key
def copy_string_key(key):
    value = source_redis.get(key)
    new_value = value.decode('utf-8') + f' | copied_at: {timestamp}'  # Append timestamp
    target_redis.set(key, new_value)


# Function to copy and add timestamp to a hash key
def copy_hash_key(key):
    hash_data = source_redis.hgetall(key)
    hash_data[b'copied_at'] = timestamp.encode('utf-8')  # Add timestamp field
    target_redis.hmset(key, hash_data)


# Function to copy and add timestamp to a list key
def copy_list_key(key):
    list_data = source_redis.lrange(key, 0, -1)
    list_data.append(timestamp.encode('utf-8'))  # Add timestamp as the last item
    target_redis.delete(key)  # Clear any existing list data in the target
    target_redis.rpush(key, *list_data)


# Function to copy a set key without adding a timestamp
def copy_set_key(key):
    set_data = source_redis.smembers(key)
    target_redis.delete(key)  # Clear any existing set data in the target
    target_redis.sadd(key, *set_data)


# Function to copy a sorted set key without adding a timestamp
def copy_sorted_set_key(key):
    sorted_set_data = source_redis.zrange(key, 0, -1, withscores=True)
    target_redis.delete(key)  # Clear any existing sorted set data in the target
    target_redis.zadd(key, dict(sorted_set_data))


# Function to determine the type of key and copy accordingly
def copy_key(key):
    key_type = source_redis.type(key).decode('utf-8')

    if key_type == 'string':
        copy_string_key(key)
    elif key_type == 'hash':
        copy_hash_key(key)
    elif key_type == 'list':
        copy_list_key(key)
    elif key_type == 'set':
        copy_set_key(key)
    elif key_type == 'zset':
        copy_sorted_set_key(key)
    else:
        print(f"Unsupported key type: {key_type} for key: {key.decode('utf-8')}")


# Get all keys from the source database
keys = source_redis.keys('*')

# Copy each key to the target database with a timestamp where applicable
for key in keys:
    copy_key(key)

print("Database copy completed with timestamp added where applicable.")
