import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Read the CSV file
data = pd.read_csv('result/merged_data.csv')

# Extract features
features = data[['HARGA', 'LT', 'LB', 'JKT', 'JKM', 'GRS']]

# Number of runs to perform
n_runs = 10

# Create a list to store the comparison results
comparison_results = []

for i in range(n_runs):
    # Create the KMeans model
    kmeans = KMeans(n_clusters=3, random_state=i)
    
    # Fit the model to the data
    kmeans.fit(features)
    
    # Add the 'RECENT_CLUSTER' column to the DataFrame
    data['RECENT_CLUSTER'] = kmeans.labels_
    
    # Compare 'CLUSTER' from merged_data.csv with 'RECENT_CLUSTER'
    data['COMPARISON'] = 'Same'
    data.loc[data['CLUSTER'] != data['RECENT_CLUSTER'], 'COMPARISON'] = 'Different'
    
    # Calculate the total number of 'Same' and 'Different' comparisons
    total_same = (data['COMPARISON'] == 'Same').sum()
    total_different = (data['COMPARISON'] == 'Different').sum()
    total_comparisons = total_same + total_different
    
    # Calculate the percentages
    percentage_same = (total_same / total_comparisons) * 100
    percentage_different = (total_different / total_comparisons) * 100
    
    # Append the results to the comparison_results list
    comparison_results.append((total_same, total_different, percentage_same, percentage_different))

# Print the comparison results for each run
for i, (total_same, total_different, percentage_same, percentage_different) in enumerate(comparison_results):
    print(f"Run {i + 1} - Total Same: {total_same}, Total Different: {total_different}")
    print(f"     Percentage Same: {percentage_same:.2f}%, Percentage Different: {percentage_different:.2f}%")

# Plot the data points and the cluster centroids for the last run
plt.scatter(data['HARGA'], data['LT'], c=data['RECENT_CLUSTER'], s=50)
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c='red', s=100)
plt.xlabel('HARGA')
plt.ylabel('LT')
plt.title('KMeans Clustering')
plt.show()
