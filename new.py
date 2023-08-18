import pandas as pd

# Read the data from 'main-raw.csv'
data = pd.read_csv('main-raw.csv', sep='\t')

# Create a new DataFrame with the same data
new_data = pd.DataFrame(data)

# Save the new DataFrame to 'new-raw.csv'
new_data.to_csv('new-raw.csv', sep='\t', index=False)
