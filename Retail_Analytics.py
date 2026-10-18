import pyodbc
import pandas as pd
conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=.\\SQLEXPRESS;"
    "DATABASE=RETAIL_ANALYTICS;"
    "Trusted_Connection=yes;"
)
query = """
SELECT
    O.ORDER_ID,
    O.ORDER_DATE,
    C.CUSTOMER_NAME,
    C.CITY,
    P.PRODUCT_NAME,
    P.CATEGORY,
    OI.QUANTITY,
    OI.UNIT_PRICE,
    OI.QUANTITY * OI.UNIT_PRICE AS TOTAL_SALES,
    O.ORDER_STATUS
FROM ORDERS O
JOIN CUSTOMERS C
    ON O.CUSTOMER_ID = C.CUSTOMER_ID
JOIN ORDER_ITEMS OI
    ON O.ORDER_ID = OI.ORDER_ID
JOIN PRODUCTS P
    ON OI.PRODUCT_ID = P.PRODUCT_ID
ORDER BY O.ORDER_DATE;
"""
df = pd.read_sql(query, conn)
print(df.head())
print(df.info())

print(df)
total_sales = df["TOTAL_SALES"].sum()

print("Total Sales:", total_sales)
total_quantity = df["QUANTITY"].sum()

print("Total Quantity:", total_quantity)
total_orders = df["ORDER_ID"].nunique()

print("Total Orders:", total_orders)
aov = total_sales / total_orders

print("Average Order Value:", aov)
category_sales = df.groupby("CATEGORY")["TOTAL_SALES"].sum()

print("\nSales by Category:")
print(category_sales)
city_sales = df.groupby("CITY")["TOTAL_SALES"].sum()

print("\nSales by City:")
print(city_sales.sort_values(ascending=False))
product_sales = df.groupby("PRODUCT_NAME")["TOTAL_SALES"].sum()

print("\nSales by Product:")
print(product_sales.sort_values(ascending=False))
df["ORDER_DATE"] = pd.to_datetime(df["ORDER_DATE"])

monthly_sales = df.groupby(
    df["ORDER_DATE"].dt.to_period("M")
)["TOTAL_SALES"].sum()

print("\nMonthly Sales:")
print(monthly_sales)
import matplotlib.pyplot as plt

monthly_sales.plot(kind="bar", title="Monthly Sales")

plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()
customer_sales = df.groupby("CUSTOMER_NAME")["TOTAL_SALES"].sum().sort_values(ascending=False)

print("\nSales by Customer:")
print(customer_sales)
status_count = df.groupby("ORDER_STATUS")["ORDER_ID"].nunique()

print("\nOrders by Status:")
print(status_count)
quantity_by_product = df.groupby("PRODUCT_NAME")["QUANTITY"].sum().sort_values(ascending=False)

print("\nQuantity by Product:")
print(quantity_by_product)
top_5_products = df.groupby("PRODUCT_NAME")["TOTAL_SALES"].sum().sort_values(ascending=False).head(5)

print("\nTop 5 Products by Sales:")
print(top_5_products)
summary = pd.DataFrame({
    "Metric": ["Total Sales", "Total Orders", "Total Quantity", "Average Order Value"],
    "Value": [total_sales, total_orders, total_quantity, aov]
})

print("\nBusiness Summary:")
print(summary)