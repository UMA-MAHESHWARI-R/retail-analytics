-- =========================================
-- RETAIL ANALYTICS PROJECT
-- SQL Analysis using SQL Server
-- =========================================
SELECT *
FROM Orders;
-- 1. Sales by Product
SELECT
    PRODUCT_NAME,
    SUM(QUANTITY * UNIT_PRICE) AS Total_Sales
FROM Orders
GROUP BY PRODUCT_NAME
ORDER BY Total_Sales DESC;
-- 2. Sales by City
SELECT
    CITY,
    SUM(QUANTITY * UNIT_PRICE) AS Total_Sales
FROM Orders
GROUP BY CITY
ORDER BY Total_Sales DESC;
-- 3. Order Status Analysis
SELECT
    ORDER_STATUS,
    COUNT(*) AS Total_Orders
FROM Orders
GROUP BY ORDER_STATUS
ORDER BY Total_Orders DESC;
-- 4. Total Quantity Sold by Product
SELECT
    PRODUCT_NAME,
    SUM(QUANTITY) AS Total_Quantity
FROM Orders
GROUP BY PRODUCT_NAME
ORDER BY Total_Quantity DESC;
-- 5. Monthly Sales Analysis
SELECT
    YEAR(ORDER_DATE) AS Sales_Year,
    MONTH(ORDER_DATE) AS Sales_Month,
    SUM(QUANTITY * UNIT_PRICE) AS Total_Sales
FROM Orders
GROUP BY
    YEAR(ORDER_DATE),
    MONTH(ORDER_DATE)
ORDER BY
    Sales_Year,
    Sales_Month;