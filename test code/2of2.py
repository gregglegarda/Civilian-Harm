import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import Normalize
from matplotlib.cm import ScalarMappable


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

# Plotting the observations and missions
fig = plt.figure(figsize=(20, 10))  # Make the plot twice as big
ax = fig.add_subplot(111, projection='3d')

# Normalize confidence for color mapping in observations
norm_confidence = observations_df["Confidence"] / 100

# Scatter plot for observations with color based on confidence
sc_obs = ax.scatter(observations_df["Latitude"], observations_df["Longitude"],
                    observations_df["Start Time"].apply(lambda x: x.timestamp()),
                    c=observations_df["Confidence"], cmap='Reds', alpha=0.6)

# Scatter plot for missions with different markers based on mission type
markers = {'Dynamic Targeting': 'o', 'Deliberate Targeting': '^', 'Drone Strike': 's', 'Rotary': 'P', 'LRPF': '*',
           'Artillery': 'X', 'Infantry Operation': 'D'}
for mission_type in mission_types:
    subset = missions_df[missions_df["Mission Type"] == mission_type]
    ax.scatter(subset["Latitude"], subset["Longitude"], subset["Time/Date"].apply(lambda x: x.timestamp()),
               c='green', marker=markers[mission_type], label=mission_type)

# Add labels and legend
ax.set_xlabel('Latitude')
ax.set_ylabel('Longitude')
ax.set_zlabel('Time (timestamp)')
plt.title('Observations and Missions')

# Create a colorbar legend for observations with light red to dark red color mapping
norm = Normalize(vmin=0, vmax=100)
sm = ScalarMappable(cmap='Reds', norm=norm)
sm.set_array([])
cbar = plt.colorbar(sm)
cbar.set_label('Confidence')

# Add legend for mission types in the same box as the colorbar legend and move it to the left twice as far
handles, labels = ax.get_legend_handles_labels()
legend1 = ax.legend(handles=handles[:len(mission_types)], labels=labels[:len(mission_types)], loc='upper left',
                    bbox_to_anchor=(2.1, 1))
ax.add_artist(legend1)

plt.show()

# Print the first few rows of the DataFrames to verify the data
print("Observations DataFrame:")
print(observations_df.head())
print("\nMissions DataFrame:")
print(missions_df.head())