import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

fields_to_check = ["Purchase_Amount", "Review_Rating", "Previous_Purchases"]

diagnosis_rows = []
for col in fields_to_check:
    series = customer_raw[col].dropna()
    diagnosis_rows.append({
        "field": col,
        "missing_count": customer_raw[col].isna().sum(),
        "missing_pct": round(customer_raw[col].isna().mean() * 100, 2),
        "mean": round(series.mean(), 2),
        "median": round(series.median(), 2),
        "std": round(series.std(), 2),
        "cv": round(series.std() / series.mean(), 3),          
        "skewness": round(stats.skew(series), 3),
        "q1": round(series.quantile(0.25), 2),
        "q3": round(series.quantile(0.75), 2),
        "iqr": round(series.quantile(0.75) - series.quantile(0.25), 2),
    })

diagnosis_df = pd.DataFrame(diagnosis_rows)
print(diagnosis_df.to_string(index=False))

# Visual check: distribution shape for each field
fig, axes = plt.subplots(1, 3, figsize=(15, 4))
for ax, col in zip(axes, fields_to_check):
    ax.hist(customer_raw[col].dropna(), bins=30, color="#4C78A8", alpha=0.8)
    ax.axvline(customer_raw[col].mean(), color="red", linestyle="--", label="mean")
    ax.axvline(customer_raw[col].median(), color="green", linestyle="--", label="median")
    ax.set_title(col)
    ax.legend()
plt.tight_layout()
plt.show()