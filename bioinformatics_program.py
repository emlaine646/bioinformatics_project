import pandas as pd
import matplotlib.pyplot as plt
import os

# -----------------------------
# Step 1: CSV file paths
# -----------------------------
csv_files = [
    "data_part1.csv",
    "data_part2.csv",
    "data_part3.csv"
]

# Step 2: Check files exist
for file in csv_files:
    if not os.path.exists(file):
        raise FileNotFoundError(f"Missing file: {file}")

# Step 3: Load and combine CSVs
dataframes = [pd.read_csv(file) for file in csv_files]
data = pd.concat(dataframes, ignore_index=True)

# Step 4: Dataset info
print("\n=== Dataset Info ===")
print(data.info())

print("\n=== First 5 Rows ===")
print(data.head())

print("\n=== Summary Statistics ===")
print(data.describe())

# Step 5: Example visualization
if 'age' in data.columns:
    plt.hist(data['age'], bins=20)
    plt.title("Age Distribution")
    plt.xlabel("Age")
    plt.ylabel("Count")
    plt.show()
else:
    print("\nNo 'age' column found.")
