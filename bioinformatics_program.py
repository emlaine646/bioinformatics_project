import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
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

# Step 5: Handle missing values
missing_counts = data.isnull().sum()
print("\n=== Missing Values per Column ===")
print(missing_counts[missing_counts > 0])

# Step 6: Detect age column and plot histogram
age_col_candidates = [col for col in data.columns if "age" in col.lower()]

if age_col_candidates:
    age_col = age_col_candidates[0]
    print(f"\nPlotting histogram for column: {age_col}")
    plt.figure(figsize=(8,5))
    plt.hist(data[age_col].dropna(), bins=20, color='skyblue', edgecolor='black')
    plt.title(f"{age_col} Distribution")
    plt.xlabel(age_col)
    plt.ylabel("Count")
    plt.show()
else:
    print("\nNo age-related column found to plot.")

# Step 7: Additional histograms for key features
numeric_features = ["BMI", "CA125", "TumorSize", "ProgressionProbability"]
for feature in numeric_features:
    if feature in data.columns:
        plt.figure(figsize=(8,5))
        plt.hist(data[feature].dropna(), bins=20, color='lightgreen', edgecolor='black')
        plt.title(f"{feature} Distribution")
        plt.xlabel(feature)
        plt.ylabel("Count")
        plt.show()
    else:
        print(f"{feature} column not found.")

# Step 8: Correlation heatmap (numeric columns)
numeric_cols = data.select_dtypes(include='number').columns
if len(numeric_cols) > 1:
    plt.figure(figsize=(12,10))
    corr = data[numeric_cols].corr()
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm")
    plt.title("Correlation Heatmap of Numeric Features")
    plt.show()
else:
    print("Not enough numeric columns to compute correlation heatmap.")

# -----------------------------
# Step 9: Ovarian Cancer Risk Summary by CancerStage
# -----------------------------
if "CancerStage" in data.columns and "ProgressionProbability" in data.columns:
    risk_summary = data.groupby("CancerStage")["ProgressionProbability"].mean()
    print("\n=== Average ProgressionProbability by CancerStage ===")
    print(risk_summary)

    plt.figure(figsize=(8,5))
    sns.barplot(x=risk_summary.index, y=risk_summary.values, palette="Reds")
    plt.title("Average ProgressionProbability by CancerStage")
    plt.xlabel("CancerStage")
    plt.ylabel("Average ProgressionProbability")
    plt.show()
else:
    print("\nCannot generate risk summary plot: required columns missing.")
