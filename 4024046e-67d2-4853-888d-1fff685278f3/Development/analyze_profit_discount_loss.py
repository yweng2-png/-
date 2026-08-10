import sqlite3
import pandas as pd

# Recreate the in-memory SQLite connection (conn is an sqlite3.Connection
# which cannot be serialized across blocks; we rebuild it from the DataFrames
# that ARE serializable: clean_order from the upstream block)
_conn = sqlite3.connect(":memory:")
clean_order.to_sql("clean_order", _conn, index=False, if_exists="replace")

diag_sql = """
DROP TABLE IF EXISTS v_subcategory_diagnosis;
DROP TABLE IF EXISTS v_discount_recovery_estimate;

CREATE TABLE v_subcategory_diagnosis AS
SELECT
    Category, Sub_Category,
    COUNT(*) AS order_cnt,
    ROUND(AVG(Margin_Rate),4) AS avg_margin_rate,
    ROUND(AVG(Discount_Percent),2) AS avg_discount_pct,
    ROUND(SUM(CASE WHEN Profit<0 THEN 1.0 ELSE 0 END)/COUNT(*),4) AS loss_rate,
    ROUND(SUM(Profit),2) AS total_profit,
    ROUND(SUM(Discount_Amount),2) AS total_discount_given
FROM clean_order
GROUP BY Category, Sub_Category
ORDER BY loss_rate DESC;

CREATE TABLE v_discount_recovery_estimate AS
WITH low_margin AS (
    SELECT Sub_Category FROM v_subcategory_diagnosis WHERE avg_margin_rate < 0.08
)
SELECT
    (SELECT COUNT(*) FROM clean_order WHERE Sub_Category IN (SELECT Sub_Category FROM low_margin)) AS affected_orders,
    (SELECT ROUND(SUM(Discount_Amount),2) FROM clean_order WHERE Sub_Category IN (SELECT Sub_Category FROM low_margin)) AS recoverable_profit,
    (SELECT ROUND(SUM(Profit),2) FROM clean_order) AS company_total_profit,
    ROUND(
        (SELECT SUM(Discount_Amount) FROM clean_order WHERE Sub_Category IN (SELECT Sub_Category FROM low_margin))
        * 100.0 /
        (SELECT SUM(Profit) FROM clean_order)
    , 2) AS recovery_pct_of_total_profit;
"""

_conn.executescript(diag_sql)

subcategory_diagnosis = pd.read_sql("SELECT * FROM v_subcategory_diagnosis", _conn)
discount_recovery = pd.read_sql("SELECT * FROM v_discount_recovery_estimate", _conn)

print(subcategory_diagnosis)
print(discount_recovery)
