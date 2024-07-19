import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = r"C:\Users\Harsh_ehn0ysj\Downloads\Amazon Sales data.csv"
df = pd.read_csv(file_path)

# Checking for missing values
missing_values = df.isnull().sum()
print("Missing values:\n", missing_values)

# Convert 'Order Date' to datetime format
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Derive new features: year, month, and year_month
df['year'] = df['Order Date'].dt.year
df['month'] = df['Order Date'].dt.month
df['year_month'] = df['Order Date'].dt.to_period('M')

# Display the transformed data
print("Transformed Data:\n", df.head())

# Month-wise Sales Trend
monthly_sales = df.groupby(['year', 'month']).agg({'Total Revenue': 'sum'}).reset_index()
monthly_sales_pivot = monthly_sales.pivot(index='month', columns='year', values='Total Revenue')

plt.figure(figsize=(12, 8))
monthly_sales_pivot.plot(kind='bar')
plt.title('Month-wise Sales Trend')
plt.xlabel('Month')
plt.ylabel('Total Revenue')
plt.legend(title='Year')
plt.xticks(rotation=0)
plt.show()

# Year-wise Sales Trend
yearly_sales = df.groupby('year').agg({'Total Revenue': 'sum'}).reset_index()

plt.figure(figsize=(12, 8))
plt.bar(yearly_sales['year'], yearly_sales['Total Revenue'])
plt.title('Year-wise Sales Trend')
plt.xlabel('Year')
plt.ylabel('Total Revenue')
plt.xticks(yearly_sales['year'])
plt.show()

# Yearly Month-wise Sales Trend
yearly_monthly_sales = df.groupby('year_month').agg({'Total Revenue': 'sum'}).reset_index()
yearly_monthly_sales['year_month'] = yearly_monthly_sales['year_month'].astype(str)

plt.figure(figsize=(12, 8))
plt.plot(yearly_monthly_sales['year_month'], yearly_monthly_sales['Total Revenue'])
plt.title('Yearly Month-wise Sales Trend')
plt.xlabel('Year-Month')
plt.ylabel('Total Revenue')
plt.xticks(rotation=90)
plt.show()

# Total Sales by Product
product_sales = df.groupby('Item Type').agg({'Total Revenue': 'sum'}).reset_index()
top_products = product_sales.sort_values(by='Total Revenue', ascending=False).head(10)

plt.figure(figsize=(12, 8))
plt.bar(top_products['Item Type'], top_products['Total Revenue'])
plt.title('Top 10 Products by Total Revenue')
plt.xlabel('Item Type')
plt.ylabel('Total Revenue')
plt.xticks(rotation=45)
plt.show()

# Pie Chart for Product Sales
plt.figure(figsize=(12, 8))
plt.pie(top_products['Total Revenue'], labels=top_products['Item Type'], autopct='%1.1f%%', startangle=140)
plt.title('Top 10 Products by Total Revenue')
plt.axis('equal')
plt.show()

# Total Sales by Customer
customer_sales = df.groupby('Order ID').agg({'Total Revenue': 'sum'}).reset_index()
top_customers = customer_sales.sort_values(by='Total Revenue', ascending=False).head(10)

plt.figure(figsize=(12, 8))
plt.bar(top_customers['Order ID'], top_customers['Total Revenue'])
plt.title('Top 10 Customers by Total Revenue')
plt.xlabel('Order ID')
plt.ylabel('Total Revenue')
plt.xticks(rotation=45)
plt.show()

# Correlation between Units Sold and Total Revenue
correlation = df[['Units Sold', 'Total Revenue']].corr()
print("Correlation between Units Sold and Total Revenue:\n", correlation)

# Scatter Plot for Units Sold vs. Total Revenue
plt.figure(figsize=(12, 8))
plt.scatter(df['Units Sold'], df['Total Revenue'])
plt.title('Units Sold vs. Total Revenue')
plt.xlabel('Units Sold')
plt.ylabel('Total Revenue')
plt.show()

# Sales Distribution Over Time
sales_distribution = df.groupby('Order Date').agg({'Total Revenue': 'sum'}).reset_index()

plt.figure(figsize=(12, 8))
plt.plot(sales_distribution['Order Date'], sales_distribution['Total Revenue'])
plt.title('Sales Distribution Over Time')
plt.xlabel('Order Date')
plt.ylabel('Total Revenue')
plt.show()

# Pie Chart for Monthly Sales
monthly_sales_pie = df.groupby('month').agg({'Total Revenue': 'sum'}).reset_index()

plt.figure(figsize=(12, 8))
plt.pie(monthly_sales_pie['Total Revenue'], labels=monthly_sales_pie['month'], autopct='%1.1f%%', startangle=140)
plt.title('Monthly Sales Distribution')
plt.axis('equal')
plt.show()

# Histogram of Total Revenue
plt.figure(figsize=(12, 8))
plt.hist(df['Total Revenue'], bins=30)
plt.title('Distribution of Total Revenue')
plt.xlabel('Total Revenue')
plt.ylabel('Frequency')
plt.show()
