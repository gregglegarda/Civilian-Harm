import redis
import pandas as pd
import os
cwd = os.getcwd()

# Connect to Redis server
redis_cli = redis.Redis(
    host='localhost',
    port=6379,
    charset="utf-8",
    decode_responses=True
)

def load_csv_to_redis(file_path, name):
    # Read CSV file into a DataFrame
    df = pd.read_csv(file_path)

    for index, row in df.iterrows():
        row_id = row[name.capitalize()+'UUID']
        row_data = row.drop(name.capitalize()+'UUID').to_dict()

        # Store the data in Redis using hset
        redis_cli.hset(f'{name}:{row_id}', mapping=row_data)

        # Add the incident ID to the set
        redis_cli.sadd(name+'s', row_id)


def get_data_from_redis(name):
    rows = []
    row_ids = redis_cli.smembers(name+'s')


    for row_id in row_ids:
        row_key = f"{name}:{row_id}"
        row = redis_cli.hgetall(f'{name}:{row_key}')
        print(row)
        row_data = {k.decode(): v.decode() for k, v in row.items()}
        print(row_data)
        rows.append(row_data)
    return rows



# Example usage
submissions_path = cwd+'/redis_code/ccmd_data/submissions_data.csv'
load_csv_to_redis(submissions_path, "submission")


data_from_redis = get_data_from_redis("submission")
df_data_from_redis = pd.DataFrame(data_from_redis)

print("Test Redis DataFrame:")
print(df_data_from_redis)
