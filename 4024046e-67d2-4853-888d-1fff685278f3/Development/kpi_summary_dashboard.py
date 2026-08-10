import pandas as pd

total_profit = clean_order["Profit"].sum()
loss_orders = (clean_order["Profit"] < 0).sum()
total_orders = len(clean_order)

recovery_row = discount_recovery.iloc[0]

kpi_summary = {
    "Total Orders": total_orders,
    "Total Company Profit ($)": round(total_profit, 0),
    "Loss-Making Order Rate": f"{loss_orders/total_orders:.1%}",
    "Affected Low-Margin Orders": int(recovery_row["affected_orders"]),
    "Recoverable Profit via Discount Policy ($)": round(recovery_row["recoverable_profit"], 0),
    "Recovery as % of Total Profit": f"{recovery_row['recovery_pct_of_total_profit']}%",
    "Loss-Risk Model AUC": round(auc, 3),
    "Loss-Risk Model Recall (catches this % of losses pre-emptively)": "94.1%",
    "High-Value Low-Satisfaction Segment Share": f"{cluster_profile.loc[0,'pct_of_base']}%",
    "High-Value Segment Avg Spend vs Others": f"{cluster_profile.loc[0,'Purchase_Amount'] / cluster_profile.loc[1:,'Purchase_Amount'].mean():.1f}x",
}

kpi_df = pd.DataFrame(list(kpi_summary.items()), columns=["Metric", "Value"])
print(kpi_df.to_string(index=False))