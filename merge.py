import pandas as pd

# Read the Excel file
data = pd.read_excel('source/main-raw.csv')
data_clustered = pd.read_csv('result/clustered_data.csv')

# Extract column values into separate arrays
harga = data['HARGA']
lt = data['LT']
lb = data['LB']
jkt = data['JKT']
jkm = data['JKM']
grs = data['GRS']
kota = data['KOTA']

cluster = data_clustered['Cluster']

# Convert 'GRS' values based on 'ADA' column
grs = [1 if value == 'ADA' else 0 for value in grs]

# Create a new DataFrame from the extracted arrays
new_data = pd.DataFrame({
    'HARGA': harga,
    'LT': lt,
    'LB': lb,
    'JKT': jkt,
    'JKM': jkm,
    'GRS': grs,
    'KOTA': kota,
    'CLUSTER': cluster
})

# Save the new DataFrame to a CSV file
new_data.to_csv('result/merged_data.csv', index=False)