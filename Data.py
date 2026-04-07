import pandas as pd
import matplotlib.pyplot as plt

# Load
df = pd.read_csv("pro_sales_dataset.csv")

# Convert date
df["Order Date"] = pd.to_datetime(df["Order Date"])


top_products = df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(3)
print("\nTop 3 Products:")
print(top_products)

avg_region = df.groupby("Region")["Sales"].mean()
print("\nAverage Sales per Region:")
print(avg_region)

sales_over_time = df.groupby("Order Date")["Sales"].sum()

sales_over_time.plot(figsize=(10,5))
plt.title("Sales Over Time")
plt.show()


sales_region = df.groupby("Region")["Sales"].sum()

print("\nBest Region:", sales_region.idxmax())
print("Worst Region:", sales_region.idxmin())

category_sales = df.groupby("Category")["Sales"].sum()

category_sales.plot(kind="pie", autopct='%1.1f%%')
plt.title("Sales by Category")
plt.show()

profit_analysis = df.groupby("Category")["Profit"].sum()
print("\nProfit by Category:")
print(profit_analysis)