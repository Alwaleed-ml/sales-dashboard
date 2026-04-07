import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Title
st.title("📊 Sales Data Dashboard")

# Load data
df = pd.read_csv("pro_sales_dataset.csv")

# Convert date
df["Order Date"] = pd.to_datetime(df["Order Date"])

# Show data
st.subheader("📄 Dataset Preview")
st.dataframe(df.head())

# =========================

st.subheader("Top Insights")

top_products = df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(3)
st.write("Top 3 Products:")
st.write(top_products)

avg_region = df.groupby("Region")["Sales"].mean()
st.write("Average Sales per Region:")
st.write(avg_region)

# =========================

st.subheader("📈 Sales Over Time")

sales_over_time = df.groupby("Order Date")["Sales"].sum()

fig1, ax1 = plt.subplots()
sales_over_time.plot(ax=ax1)
st.pyplot(fig1)


st.subheader("🌍 Region Performance")

sales_region = df.groupby("Region")["Sales"].sum()

best_region = sales_region.idxmax()
worst_region = sales_region.idxmin()

st.write("Best Region:", best_region)
st.write("Worst Region:", worst_region)

# =========================
st.subheader("📊 Sales by Category")

category_sales = df.groupby("Category")["Sales"].sum()

fig2, ax2 = plt.subplots()
category_sales.plot(kind="pie", autopct='%1.1f%%', ax=ax2)
st.pyplot(fig2)
