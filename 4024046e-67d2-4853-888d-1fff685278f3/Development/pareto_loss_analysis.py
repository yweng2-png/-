import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.patches as mpatches

# Step 1: compute real dollar loss per sub-category directly from order-level data
loss_by_subcat = (
    clean_order[clean_order["Profit"] < 0]
    .groupby("Sub_Category")["Profit"]
    .sum()
    .abs()
    .rename("loss_magnitude")
)

pareto_df = subcategory_diagnosis.merge(loss_by_subcat, on="Sub_Category", how="left")
pareto_df["loss_magnitude"] = pareto_df["loss_magnitude"].fillna(0)
pareto_df = pareto_df.sort_values("loss_magnitude", ascending=False).reset_index(drop=True)
pareto_df["cum_pct"] = pareto_df["loss_magnitude"].cumsum() / pareto_df["loss_magnitude"].sum()

# sanity check before plotting
print(pareto_df[["Sub_Category", "avg_margin_rate", "loss_magnitude", "cum_pct"]])

fig, ax1 = plt.subplots(figsize=(11, 6), dpi=150)
bar_colors = ["#d64550" if m < 0.08 else "#4C78A8" for m in pareto_df["avg_margin_rate"]]
ax1.bar(pareto_df["Sub_Category"], pareto_df["loss_magnitude"], color=bar_colors)
ax1.set_ylabel("Total Dollar Loss from Loss-Making Orders ($)")
ax1.set_xlabel("Sub-Category")
plt.setp(ax1.get_xticklabels(), rotation=45, ha="right")

ax2 = ax1.twinx()
ax2.plot(pareto_df["Sub_Category"], pareto_df["cum_pct"], color="black", marker="o", markersize=4, linewidth=1.5)
ax2.yaxis.set_major_formatter(mticker.PercentFormatter(1.0))
ax2.set_ylabel("Cumulative % of Total Dollar Loss")
ax2.axhline(0.8, color="gray", linestyle="--", linewidth=1)
ax2.text(len(pareto_df)-1, 0.82, "80% threshold", ha="right", fontsize=8, color="gray")

red_patch = mpatches.Patch(color="#d64550", label="Margin rate < 8% (discount-vulnerable)")
blue_patch = mpatches.Patch(color="#4C78A8", label="Margin rate ≥ 8%")
ax1.legend(handles=[red_patch, blue_patch], loc="upper left", fontsize=8)
ax1.set_title("Pareto Analysis: Which Sub-Categories Drive Actual Dollar Losses")
plt.tight_layout()
plt.show()
