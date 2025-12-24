# bioinformatics_project
# Ovarian Cancer Bioinformatics Project

This project analyzes ovarian cancer patient data using Python. The dataset is split into three CSV files (`data_part1.csv`, `data_part2.csv`, `data_part3.csv`) due to size constraints. The project provides basic exploratory data analysis (EDA), visualizations, and a summary of ovarian cancer progression probability.

---

## Project Features

- Load and combine large CSV datasets.
- Print dataset info, first rows, summary statistics, and missing values.
- Generate histograms for key features:
  - Age
  - BMI
  - CA125
  - Tumor Size
  - Progression Probability
- Correlation heatmap for all numeric features.
- Bar plot showing average ovarian cancer progression probability by CancerStage.
- Automatically saves all plots to a `plots` folder in the project directory.

---

## Requirements

Install the required Python packages:

```bash
pip install -r requirements.txt
