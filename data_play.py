import sys
import pandas as pd

# Load the data
data = pd.read_csv(r"D:\Project\Data_science_project\data\retail_sales (1).csv")  # or use pd.DataFrame({...}) for mock

# # print("Data Shape: ",data.shape)
# print("Data Info: ",data.info())
# print("Data Description: "data.describe())
data['Quantity'].fillna('4.0', inplace=True)   #Fill missing values in 'Quantity' with '4.0'
data_clean = data.dropna() # Drop rows with any missing values

apparel_sales = data[data['Category'] == 'Apparel']  #ignoregropuing by 'Category' and filtering for 'Apparel' 
print(apparel_sales)

sales_by_country = data.groupby('Country')['Total_Sales'].sum().reset_index()  # Grouping by 'Country' and summing 'Sales'
print("Sales by Country: ", sales_by_country)

vag_price_by_category = data.groupby('Category')['Unit_Price'].mean().reset_index()  # Grouping by 'Category' and calculating mean 'Unit_Price'
print("Average Price by Category: ", vag_price_by_category)

data['Profit'] = data['Total_Sales'] * 0.30  # Assuming Profit is 30% of Total_Sales
data['Order_ID'] = data.index + 1  # Creating a new column 'Order
print(data[['Order_ID', 'Profit']])

top_sales = data.sort_values(by='Total_Sales', ascending=False).head(3)
print("top sales: ", top_sales)

# Convert to datetime
data['Date'] = pd.to_datetime(data['Date'])

# Filter data for January 2023 only
jan_sales = data[data['Date'].dt.month == 1]
print(jan_sales)
# Sales per Category by Country
pivot_table = pd.pivot_table(data, values='Total_Sales', index='Country', columns='Category', aggfunc='sum', fill_value=0)
print(pivot_table)
# Save modified data
data.to_csv('retail_sales_cleaned.csv', index=False)



print("Data Hade: ",data.head()) 
print("Missing Data",data.isnull().sum()) 

