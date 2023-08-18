# We use one file as RAW file called main-raw.csv

# Running cluster-creating.py for create new cluster, the clustered_data.csv will be created
python cluster-creating.py

# Make new file for merging raw.csv with clustered_data.csv into file called merged-data.csv, the merge change GRS if ADA is 1, if TIDAK ADA is 0
python merge.py

# Create Clustering with K-Means Algorithm
python main.py