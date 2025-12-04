import pandas as pd

# Load the dataset
df = pd.read_csv("../data/sales_data.csv")

# Print the first rows
print("Preview of the dataset:")
print(df.head())

# Basic summary
print("\nDataset summary:")
print(df.describe())

# Total revenue calculation
df["Revenue"] = df["Units_Sold"] * df["Unit_Price"]

print("\nTotal revenue by product:")
print(df.groupby("Product")["Revenue"].sum())

print("\nTotal revenue by region:")
print(df.groupby("Region")["Revenue"].sum())

print("\nDone!")

pip install pandas


