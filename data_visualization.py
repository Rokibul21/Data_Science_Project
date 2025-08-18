import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
data = pd.read_csv(r"D:\Project\Data_science_project\data\retail_sales (1).csv")

# Bar plot for Total Sales by Category
plt.figure(figsize=(6,4))
sns.barplot(x="Category", y="Total_Sales", data=data, estimator=sum, ci=None)
plt.title("Total Sales by Category")
plt.show()

# scatter plot for Quantity vs Total Sales
plt.figure(figsize=(6,4))
sns.scatterplot(x="Quantity", y="Total_Sales", hue="Category", data=data, s=100)
plt.title("Quantity vs Total Sales")
plt.show()


# line plot for Sales Trend Over Time
data["Date"] = pd.to_datetime(data["Date"])
sales_over_time = data.groupby("Date")["Total_Sales"].sum().reset_index()

plt.figure(figsize=(8,4))
sns.lineplot(x="Date", y="Total_Sales", data=sales_over_time, marker="o")
plt.title("Sales Trend Over Time")
plt.show()

print("data_head: ", data.head())