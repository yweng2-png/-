import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

# Sort by total_discount_given (the recoverable-profit driver) descending — Pareto logic
pareto_df = subcategory_diagnosis.sort_values("total_discount_given", ascending=False).reset_index(drop=True)
pareto_df["cum_pct"] = pareto_df["total_discount_given"].cumsum() / pareto_df["total_discount_given"].sum()

fig, ax1 = plt.subplots(figsize=(11, 6), dpi=150)

bar_colors = ["#d64550" if m < 0.08 else "#4C78A8" for m in pareto_df["avg_margin_rate"]]
ax1.bar(pareto_df["Sub_Category"], pareto_df["total_discount_given"], color=bar_colors)
ax1.set_ylabel("Discount Amount Given ($)")
ax1.set_xlabel("Sub-Category")
plt.setp(ax1.get_xticklabels(), rotation=45, ha="right")

ax2 = ax1.twinx()
ax2.plot(pareto_df["Sub_Category"], pareto_df["cum_pct"], color="black", marker="o", markersize=4, linewidth=1.5)
ax2.yaxis.set_major_formatter(mticker.PercentFormatter(1.0))
ax2.set_ylabel("Cumulative % of Total Discount Exposure")
ax2.axhline(0.8, color="gray", linestyle="--", linewidth=1)
ax2.text(len(pareto_df)-1, 0.82, "80% threshold", ha="right", fontsize=8, color="gray")

import matplotlib.patches as mpatches
red_patch = mpatches.Patch(color="#d64550", label="Margin rate < 8% (discount-vulnerable)")
blue_patch = mpatches.Patch(color="#4C78A8", label="Margin rate ≥ 8%")
ax1.legend(handles=[red_patch, blue_patch], loc="upper left", fontsize=8)

ax1.set_title("Pareto Analysis: Which Sub-Categories Drive Discount-Related Profit Exposure")
plt.tight_layout()
plt.show()

n_to_80pct = (pareto_df["cum_pct"] <= 0.8).sum() + 1
print(f"Top {n_to_80pct} sub-categories account for 80% of total discount exposure (${pareto_df['total_discount_given'].sum():,.0f})")