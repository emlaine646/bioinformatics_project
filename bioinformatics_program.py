# bioinformatics_program.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ------------------------------
# Load CSV files
# ------------------------------
csv_files = ["data_part1.csv", "data_part2.csv", "data_part3.csv"]
df_list = [pd.read_csv(f) for f in csv_files]
df = pd.concat(df_list, ignore_index=True)

# ------------------------------
# Display basic dataset info
# ------------------------------
print("\n=== Dataset Info ===")
print(df.info())

print("\n=== First 5 Rows ===")
print(df.head())

print("\n=== Summary Statistics ===")
print(df.describe())

print("\n=== Missing Values per Column ===")
print(df.isnull().sum())

# ------------------------------
# Create folder for saved plots
# ------------------------------
plot_dir = "plots"
os.makedirs(plot_dir, exist_ok=True)

# ------------------------------
# Plot histograms for key columns
# ------------------------------
columns_to_plot = ["Age", "BMI", "CA125", "TumorSize", "ProgressionProbability"]

for col in columns_to_plot:
    if col in df.columns:
        plt.figure(figsize=(8,5))
        plt.hist(df[col], bins=30, color='skyblue', edgecolor='black')
        plt.title(f'Histogram of {col}')
        plt.xlabel(col)
        plt.ylabel('Frequency')
        plt.tight_layout()
        # Save plot
        plt.savefig(os.path.join(plot_dir, f"{col}_histogram.png"))
        plt.show()
    else:
        print(f"Column {col} not found in the dataset.")

# ------------------------------
# Correlation heatmap for numeric columns
# ------------------------------
numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
plt.figure(figsize=(12,10))
sns.heatmap(df[numeric_cols].corr(), annot=True, fmt=".2f", cmap="coolwarm")
plt.title("Correlation Heatmap of Numeric Features")
plt.tight_layout()
plt.savefig(os.path.join(plot_dir, "correlation_heatmap.png"))
plt.show()

# ------------------------------
# Average ProgressionProbability by CancerStage
# ------------------------------
if "CancerStage" in df.columns and "ProgressionProbability" in df.columns:
    stage_avg = df.groupby("CancerStage")["ProgressionProbability"].mean()
    plt.figure(figsize=(8,5))
    stage_avg.plot(kind='bar', color='salmon', edgecolor='black')
    plt.title("Average Progression Probability by CancerStage")
    plt.xlabel("Cancer Stage")
    plt.ylabel("Average Progression Probability")
    plt.tight_layout()
    plt.savefig(os.path.join(plot_dir, "progression_by_stage.png"))
    plt.show()
else:
    print("Columns 'CancerStage' or 'ProgressionProbability' not found in dataset.")
