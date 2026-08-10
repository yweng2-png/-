import sqlite3
import pandas as pd

conn = sqlite3.connect(":memory:")
customer_raw.to_sql("raw_customer", conn, index=False, if_exists="replace")
order_raw.to_sql("raw_order", conn, index=False, if_exists="replace")

fill_purchase_amount = customer_raw["Purchase_Amount"].median()
fill_review_rating = customer_raw["Review_Rating"].median()
fill_previous_purchases = customer_raw["Previous_Purchases"].mean()

sql_script = f"""
CREATE TABLE clean_customer AS
SELECT DISTINCT * FROM raw_customer;

CREATE TABLE clean_customer_filled AS
SELECT
    Customer_ID, Age, Gender,
    COALESCE(Purchase_Amount, {fill_purchase_amount}) AS Purchase_Amount,
    Location,
    COALESCE(Size, 'Unknown') AS Size,
    Color, Season,
    COALESCE(Review_Rating, {fill_review_rating}) AS Review_Rating,
    Subscription_Status,
    COALESCE(Discount_Applied, 'No') AS Discount_Applied,
    COALESCE(Previous_Purchases, {fill_previous_purchases}) AS Previous_Purchases,
    Payment_Method, Frequency_of_Purchases
FROM clean_customer;

CREATE TABLE clean_order AS
SELECT
    Order_Id, Order_Date,
    CASE WHEN Ship_Mode IS NULL OR Ship_Mode IN ('Not Available','unknown') THEN 'Unknown' ELSE Ship_Mode END AS Ship_Mode,
    Segment, Category, Sub_Category, Product_Id, cost_price, List_Price, Quantity, Discount_Percent, Customer_ID,
    ROUND(List_Price * (1 - Discount_Percent/100.0), 2)                          AS Net_Price,
    ROUND(List_Price * (1 - Discount_Percent/100.0) * Quantity, 2)               AS Revenue,
    ROUND((List_Price * (1 - Discount_Percent/100.0) - cost_price) * Quantity,2) AS Profit,
    ROUND((List_Price - cost_price)*1.0 / NULLIF(List_Price,0), 4)               AS Margin_Rate,
    ROUND(List_Price * (Discount_Percent/100.0) * Quantity, 2)                   AS Discount_Amount
FROM raw_order;
"""

conn.executescript(sql_script)

clean_customer_filled = pd.read_sql("SELECT * FROM clean_customer_filled", conn)
clean_order = pd.read_sql("SELECT * FROM clean_order", conn)

print(clean_customer_filled.shape, clean_order.shape)
