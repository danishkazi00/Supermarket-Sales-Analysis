import pandas as pd


# ==========================================
# 1. LOAD DATASET
# ==========================================

df = pd.read_csv("data/supermarket_sales.csv")

# Display first 5 rows
print("\nFirst 5 Rows:")
print(df.head())

# Display last 5 rows
print("\nLast 5 Rows:")
print(df.tail())

# Number of rows and columns
print("\nDataset Shape:")
print(df.shape)

# Column names
print("\nColumn Names:")
print(df.columns.tolist())

# Dataset information
print("\nDataset Information:")
df.info()

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Duplicate rows
print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Statistical summary
print("\nStatistical Summary:")
print(df.describe())


# ==========================================
# PRODUCT REVENUE ANALYSIS
# ==========================================

# Calculate total revenue for each product line
product_revenue = df.groupby("Product line")["Total"].sum()

# Sort from highest to lowest revenue
product_revenue = product_revenue.sort_values(ascending=False)

print("\nRevenue by Product Line:")
print(product_revenue)

# Display the highest revenue product
highest_product = product_revenue.idxmax()
highest_revenue = product_revenue.max()

print("\nHighest Revenue Product Line:")
print(highest_product)

print("\nRevenue:")
print(highest_revenue)

