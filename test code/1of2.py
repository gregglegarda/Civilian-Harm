import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import Normalize
from matplotlib.cm import ScalarMappable
from sklearn.cluster import KMeans


# Function to generate random latitude and longitude
def generate_lat_lon():
    lat = random.uniform(-80, 84)  # Latitude range for MGRS
    lon = random.uniform(-180, 180)
    return lat, lon


# Function to generate random datetime within a range
def generate_random_datetime(start, end):
    return start + timedelta(seconds=random.randint(0, int((end - start).total_seconds())))


# Generate random observations for Observations table
num_observations = 500
observations = []

start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31)

for _ in range(num_observations):
    start_time = generate_random_datetime(start_date, end_date)
    end_time = start_time + timedelta(hours=random.randint(1, 24))
    lat, lon = generate_lat_lon()
    grid_location = f"{lat:.5f}, {lon:.5f}"
    observation = f"Observation {_}"
    confidence = random.uniform(0, 100)

    observations.append([start_time, end_time, grid_location, observation, confidence, lat, lon])

# Create DataFrame for Observations table
observations_df = pd.DataFrame(observations,
                               columns=["Start Time", "End Time", "Grid Location", "Observation", "Confidence",
                                        "Latitude", "Longitude"])

# Add a column to the observation table called Action and populate it with Infantry, Drone, Bomb, Artillery
actions = ["Infantry", "Drone", "Bomb", "Artillery"]
observations_df["Action"] = [random.choice(actions) for _ in range(len(observations_df))]

# Generate random observations for MissionData table
num_missions = 100
missions = []

mission_types = ["Dynamic Targeting", "Deliberate Targeting", "Drone Strike", "Rotary", "LRPF", "Artillery",
                 "Infantry Operation"]

for _ in range(num_missions):
    time_date = generate_random_datetime(start_date, end_date)
    lat, lon = generate_lat_lon()
    mission_info = f"Mission {_}"
    mission_type = random.choice(mission_types)

    missions.append([lat, lon, time_date, mission_info, mission_type])

# Create DataFrame for MissionData table
missions_df = pd.DataFrame(missions,
                           columns=["Latitude", "Longitude", "Time/Date", "Mission Information", "Mission Type"])


# Function to perform k-means clustering and find the closest mission data points to a specified observation
def find_closest_missions(observation_index, n_clusters=5, n_nearest=1):
    # Combine location and time fields for clustering
    observation_data = observations_df[["Latitude", "Longitude", "Start Time"]].copy()
    observation_data["Time"] = observation_data["Start Time"].apply(lambda x: x.timestamp())
    mission_data = missions_df[["Latitude", "Longitude", "Time/Date"]].copy()
    mission_data["Time"] = mission_data["Time/Date"].apply(lambda x: x.timestamp())

    # Combine both datasets for clustering
    combined_data = pd.concat([observation_data, mission_data], ignore_index=True)

    # Perform k-means clustering
    kmeans = KMeans(n_clusters=n_clusters)
    combined_data["Cluster"] = kmeans.fit_predict(combined_data[["Latitude", "Longitude", "Time"]])

    # Find the cluster of the specified observation
    observation_cluster = combined_data.loc[observation_index, "Cluster"]

    # Find all mission data points in the same cluster
    mission_indices = combined_data[
        (combined_data["Cluster"] == observation_cluster) & (combined_data.index >= len(observation_data))].index

    # Calculate distances to the specified observation
    distances = []
    for idx in mission_indices:
        distance = np.linalg.norm(
            combined_data.loc[observation_index, ["Latitude", "Longitude", "Time"]] - combined_data.loc[
                idx, ["Latitude", "Longitude", "Time"]])
        distances.append((idx - len(observation_data), distance))

    # Sort by distance and get the nearest mission data points
    nearest_missions = sorted(distances, key=lambda x: x[1])[:n_nearest]

    return missions_df.iloc[[idx for idx, _ in nearest_missions]]


# User input for observation number, number of nearest mission data points, and k-means parameters
observation_number = int(input("Enter the observation number: "))
num_nearest_missions = int(input("Enter the number of nearest mission data points to report: "))
num_clusters = int(input("Enter the number of clusters for k-means: "))

# Find and print the nearest mission data points
nearest_missions = find_closest_missions(observation_number, n_clusters=num_clusters, n_nearest=num_nearest_missions)
print(f"Nearest {num_nearest_missions} Mission Data Points to Observation {observation_number}:")
print(nearest_missions)

# Print the data for the specified observation
print(f"\nData for Observation {observation_number}:")
print(observations_df.iloc[observation_number])

# Print the first few rows of the updated Observations DataFrame to verify the Action column
print("\nUpdated Observations DataFrame:")
# print(observations_df.head())