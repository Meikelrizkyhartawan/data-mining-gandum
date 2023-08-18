import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import pandas as pd

# Read the data from the Excel file
df = pd.read_excel('main-raw.csv')
data = df[['HARGA']]

# Create the KMeans model with a fixed random state
kmeans = KMeans(n_clusters=3, random_state=42)  # You can adjust the random_state value

# Fit the model to the data
kmeans.fit(data)

# Predict the cluster labels for each data point
labels = kmeans.predict(data)

# Add the cluster labels to the DataFrame
data['Cluster'] = labels

# Save the DataFrame to a new CSV file
data.to_csv('clustered_data.csv', index=False)

# Print the cluster labels
print(labels)

# Get the index values as x values
x_values = data.index

# Plot the data points and the cluster centroids
plt.scatter(x_values, data['HARGA'], c=labels, s=50)
plt.scatter(kmeans.cluster_centers_, kmeans.cluster_centers_, c='red', s=100)

# Calculate the total count of data points in each cluster
cluster_counts = np.bincount(labels)

# Swap the counts for Cluster 2 and Cluster 3
temp = cluster_counts[2]
cluster_counts[2] = cluster_counts[1]
cluster_counts[1] = temp

for cluster_num, count in enumerate(cluster_counts):
    print(f"Cluster {cluster_num + 1}: {count} data points")

plt.show()
