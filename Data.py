import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Page config
st.set_page_config(page_title="Sales Dashboard", layout="wide")

# Title
st.title("📊 Sales Dashboard")

# Load data
df = pd.read_csv("pro_sales_dataset.csv")
df["Order Date"] = pd.to_datetime(df["Order Date"])

# =========================
# =========================
total_sales = df["Sales"].sum()
total_orders = len(df)
best_product = df.groupby("Product Name")["Sales"].sum().idxmax()

col1, col2, col3 = st.columns(3)

col1.metric("💰 Total Sales", f"${total_sales:,.0f}")
col2.metric("📦 Total Orders", total_orders)
col3.metric("🏆 Best Product", best_product)

st.divider()

# =========================
# =========================
region = st.selectbox("Select Region", df["Region"].unique())

filtered_df = df[df["Region"] == region]

# =========================
# =========================
st.subheader("📈 Sales Over Time")

sales_over_time = filtered_df.groupby("Order Date")["Sales"].sum()

fig1, ax1 = plt.subplots()
sales_over_time.plot(ax=ax1)
st.pyplot(fig1)

# =========================
# =========================
st.subheader("🔥 Top Products")

top_products = filtered_df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(5)

st.bar_chart(top_products)

# =========================
# =========================
st.subheader("📊 Category Distribution")

category_sales = filtered_df.groupby("Category")["Sales"].sum()

fig2, ax2 = plt.subplots()
category_sales.plot(kind="pie", autopct='%1.1f%%', ax=ax2)
st.pyplot(fig2)
