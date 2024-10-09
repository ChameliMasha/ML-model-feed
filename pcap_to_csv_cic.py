import pandas as pd
from pyflowmeter import FeatureExtractor

# Path to the PCAP file and the output CSV file
pcap_file = "example.pcap"
csv_output = "network_traffic_features.csv"

# Initialize the feature extractor
extractor = FeatureExtractor()

# Extract flow features
features = extractor.extract(pcap_file)

# Convert the list of flow features to a DataFrame
df = pd.DataFrame(features)

# Save the DataFrame to a CSV file
df.to_csv(csv_output, index=False)

print(f"Flow features saved to {csv_output}")
