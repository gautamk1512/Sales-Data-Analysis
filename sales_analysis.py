import pandas as pd
import matplotlib.pyplot as plt
import os

# Step 1: Read the data
try:
    df = pd.read_csv('sales_data.csv')
    print("Data loaded successfully.")
except FileNotFoundError:
    print("Error: sales_data.csv not found.")
    exit()

# Step 2: Calculate Total Sales for each row
df['Total_Sales'] = df['Quantity_Sold'] * df['Price_per_Unit']

# Step 3: Analysis
total_sales = df['Total_Sales'].sum()
best_selling_product = df.groupby('Product')['Total_Sales'].sum().idxmax()
average_daily_sales = df.groupby('Date')['Total_Sales'].sum().mean()

print("-" * 30)
print("ANALYSIS RESULTS")
print("-" * 30)
print(f"Total Revenue: {total_sales}")
print(f"Best Selling Product (by Revenue): {best_selling_product}")
print(f"Average Daily Sales: {average_daily_sales:.2f}")
print("-" * 30)

# Step 4: Visualization

# Create a directory for plots if it doesn't exist
if not os.path.exists('plots'):
    os.makedirs('plots')

# Product-wise sales
plt.figure(figsize=(10, 6))
product_sales = df.groupby('Product')['Total_Sales'].sum()
product_sales.plot(kind='bar', color='skyblue')
plt.title('Product-wise Total Sales')
plt.xlabel('Product')
plt.ylabel('Total Sales (Currency)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('plots/product_sales.png')
print("Saved plot: plots/product_sales.png")

# Daily sales trend
plt.figure(figsize=(10, 6))
daily_sales = df.groupby('Date')['Total_Sales'].sum()
daily_sales.plot(kind='line', marker='o', color='green')
plt.title('Daily Sales Trend')
plt.xlabel('Date')
plt.ylabel('Total Sales (Currency)')
plt.grid(True)
plt.tight_layout()
plt.savefig('plots/daily_sales_trend.png')
print("Saved plot: plots/daily_sales_trend.png")

print("Analysis complete.")
