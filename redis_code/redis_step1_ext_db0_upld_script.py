import redis
import pandas as pd
import os
cwd = os.getcwd()
print(cwd)

# Connect to the Redis server
# Create Redis client
#r = redis.Redis(host='localhost', port=6379)
r = redis.Redis(
    host='localhost',
    port=6379,
    charset="utf-8",
    decode_responses=True
)

#r = redis.Redis(host='localhost', port=6379, db=0)


def load_csv_to_redis(file_path, name):

    # Read CSV file into a DataFrame
    df = pd.read_csv(file_path)

    for index, row in df.iterrows():
        row_id = row[name.capitalize()+'UUID']
        row_data = row.drop(name.capitalize()+'UUID').to_dict()

        # Store the data in Redis using hset
        r.hset(f'{name}:{row_id}', mapping=row_data)

        # Add the incident ID to the set
        r.sadd(name+'s', row_id)


# Function to retrieve data from redis_code

def get_data_from_redis(name):
    rows = []
    row_ids = r.smembers(name+'s')

    for row_id in row_ids:
        row = r.hgetall(f'{name}:{row_id}')
        rows.append(row)
    return rows



def main():
    # Path to the CSV file
    submissions_path = cwd+'/ccmd_data/submissions_data.csv'
    incidents_path = cwd+'/ccmd_data/incidents_data.csv'
    assessments_path = cwd + '/ccmd_data/assessments_data.csv'
    investigations_path = cwd+'/ccmd_data/investigations_data.csv'
    chmr_cro_path = cwd+'/ccmd_data/casualty_recording_organizations.csv'
    chmr_dmp_users_path = cwd+'/ccmd_data/chmr_dmp_users.csv'
    chmr_test_data_path = cwd+'/ccmd_data/chmr_test_data.csv'


    # Load CSV data into Redis (in specific set and key name)
    load_csv_to_redis(submissions_path, "submission")
    #load_csv_to_redis(incidents_path, "incident")
    #load_csv_to_redis(assessments_path, "assessment")
    #load_csv_to_redis(investigations_path, "investigation")
    #load_csv_to_redis(chmr_cro_path, "organization")
    #load_csv_to_redis(chmr_dmp_users_path, "organization")
    #load_csv_to_redis(chmr_test_data_path, "test")

    data_from_redis = get_data_from_redis("submission")
    df_data_from_redis = pd.DataFrame(data_from_redis)

    print("Test Redis DataFrame:")
    print(df_data_from_redis)
    df_data_from_redis.to_csv("/Users/gregglegarda/Desktop/test.csv")


if __name__ == "__main__":
    main()

