# bioinformatics_program.py

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# ------------------------------
# Load CSV files
# ------------------------------
csv_files = ["data_part1.csv", "data_part2.csv", "data_part3.csv"]

df_list = []
for file in csv_files:
    df_list.append(pd.read_csv(file))

df = pd.concat(df_list, ignore_index=True)

# ------------------------------
# Prepare plots folder
# ------------------------------
plot_dir = "plots"
if not os.path.exists(plot_dir):
    os.makedirs(plot_dir)

# ------------------------------
# Summary of dataset
# ------------------------------
print("=== Dataset Info ===")
print(df.info())
print("\n=== First 5 Rows ===")
print(df.head())
print("\n=== Summary Statistics ===")
print(df.describe())
print("\n=== Missing Values per Column ===")
print(df.isnull().sum())

# ------------------------------
# Histograms for selected columns
# ------------------------------
hist_cols = ['Age', 'BMI', 'CA125', 'TumorSize', 'ProgressionProbability']

for col in hist_cols:
    plt.figure(figsize=(8,6))
    sns.histplot(df[col], bins=30, kde=True, color='skyblue')
    plt.title(f"Histogram of {col}")
    plt.xlabel(col)
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig(os.path.join(plot_dir, f"{col}_histogram.png"))
    plt.show()

# ------------------------------
# Correlation heatmap
# ------------------------------
continuous_cols = [
    'Age', 'BMI', 'CA125', 'GeneExpression', 'DNAMethylation', 'miRNA',
    'TumorSize', 'EnhancementPattern', 'RadiomicTexture', 'RadiomicIntensity',
    'RadiomicShape', 'DopplerVelocity', 'ProgressionProbability'
]

# Ensure numeric
for col in continuous_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Remove zero variance columns
continuous_cols = [col for col in continuous_cols if df[col].var() > 0]

corr_matrix = df[continuous_cols].corr()
mask = np.eye(len(corr_matrix), dtype=bool)

plt.figure(figsize=(12,10))
sns.set(font_scale=1)
sns.heatmap(corr_matrix, annot=True, fmt=".3f", cmap="coolwarm", center=0, mask=mask,
            linewidths=0.5, linecolor='gray')
plt.title("Correlation Heatmap of Continuous Numeric Features", fontsize=16)
plt.tight_layout()
plt.savefig(os.path.join(plot_dir, "correlation_heatmap.png"))
plt.show()

# ------------------------------
# Average Progression Probability by CancerStage (enhanced)
# ------------------------------
df['CancerStage'] = pd.to_numeric(df['CancerStage'], errors='coerce')
df['ProgressionProbability'] = pd.to_numeric(df['ProgressionProbability'], errors='coerce')

stage_means = df.groupby('CancerStage')['ProgressionProbability'].mean()

plt.figure(figsize=(8,6))
sns.barplot(x=stage_means.index, y=stage_means.values, palette="Blues_d")

plt.title("Average Progression Probability by Cancer Stage")
plt.ylabel("Avg Progression Probability")
plt.xlabel("Cancer Stage")

# Set y-axis limits to zoom in around the data
plt.ylim(stage_means.min() - 0.01, stage_means.max() + 0.01)

# Annotate each bar with the numeric value
for i, val in enumerate(stage_means.values):
    plt.text(i, val + 0.002, f"{val:.3f}", ha='center', va='bottom')

plt.tight_layout()
plt.savefig(os.path.join(plot_dir, "progression_by_stage.png"))
plt.show()
