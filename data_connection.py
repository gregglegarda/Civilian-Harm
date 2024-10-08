import dash_leaflet as dl
import app_theme
import pandas as pd
import redis

source_of_data = 'local_csv'#redis'

if source_of_data == 'redis':
    # IF SINGLE COMBATANT COMMAND...
    # CONNECT TO DATABASE
    # Connect to the Redis server
    r = redis.Redis(host='localhost', port=6379, db=2)

    # EXTRACT DATA
    # Function to retrieve data from redis_code
    def get_data_from_redis(name):
        rows = []
        row_ids = r.smembers(name+'s')
        for row_id in row_ids:
            row = r.hgetall(f'{name}:{row_id.decode()}')
            row_data = {k.decode(): v.decode() for k, v in row.items()}
            rows.append(row_data)
        return rows

    data_connection_submissions = get_data_from_redis("submission")
    data_connection_incidents = get_data_from_redis("incident")
    data_connection_investigations = get_data_from_redis("investigation")

    # TRANSFORM TO DATAFRAMES FROM THE EXTRACTION STEP
    df_submissions = pd.DataFrame(data_connection_submissions)
    df_incidents = pd.DataFrame(data_connection_incidents)
    df_investigations = pd.DataFrame(data_connection_investigations)

elif source_of_data == 'local_csv':
    # DATA FRAMES FROM CSV, NOT REDIS
    import os
    cwd = os.getcwd()
    print(cwd)
    # Path to the CSV file
    submissions_path = cwd+'/redis_code/ccmd_data/submissions_data.csv'
    incidents_path = cwd+'/redis_code/ccmd_data/incidents_data.csv'
    assessments_path = cwd + '/redis_code/ccmd_data/assessments_data.csv'
    investigations_path = cwd+'/redis_code/ccmd_data/investigations_data.csv'
    chmr_cro_path = cwd+'/redis_code/ccmd_data/casualty_recording_organizations.csv'
    chmr_dmp_users_path = cwd+'/redis_code/ccmd_data/chmr_dmp_users.csv'
    chmr_test_data_path = cwd+'/redis_code/ccmd_data/chmr_test_data.csv'

    df_submissions = pd.read_csv(submissions_path)
    df_incidents = pd.read_csv(incidents_path)
    df_investigations = pd.read_csv(investigations_path)

# TRANSFORM TO PROPER FORMAT
#print("Redis DataFrame:")
#print(df_submissions)
#print(df_incidents)
#print(df_investigations)

# CONCATENATE HERE IF NEEDED
'''
data_connection_submissions = pd.concat([], ignore_index=True)
data_connection_incidents = pd.concat([], ignore_index=True)
data_connection_investigations = pd.concat([], ignore_index=True)
'''


# IF SINGLE COMBATANT COMMAND...
# CONNECT TO INDIVIDUAL CCMDs DATABASE
# EXTRACT DATA
#dir_path = "ccmd_data/"
#filename_submissions = "submissions_data.csv"
#filename_incidents = "incidents_data.csv"
#filename_investigations = "investigations_data.csv"
#data_connection_submissions = pd.read_csv(dir_path + filename_submissions)
#data_connection_incidents = pd.read_csv(dir_path + filename_incidents)
#data_connection_investigations = pd.read_csv(dir_path + filename_investigations)

# CREATE DATAFRAMES FROM THE CONNECTIONS
# TRANSFORM TO PROPER FORMAT
#df_submissions = data_connection_submissions
#df_incidents = data_connection_incidents
#df_investigations = data_connection_investigations




