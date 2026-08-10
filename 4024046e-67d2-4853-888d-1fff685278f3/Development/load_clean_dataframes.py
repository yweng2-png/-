import pandas as pd

customer_raw = pd.read_csv("customer_data.csv")
order_raw = pd.read_csv("order_data.csv")

customer_raw.columns = [c.strip().replace(" ", "_").replace("(USD)", "").strip("_") for c in customer_raw.columns]
order_raw.columns = [c.strip().replace(" ", "_") for c in order_raw.columns]

print(customer_raw.shape, order_raw.shape)
