import matplotlib.pyplot as plt
import seaborn as sns

fig, axes = plt.subplots(1, 3, figsize=(15, 4))
for ax, col in zip(axes, fields_to_check):
    sns.boxplot(y=customer_raw[col].dropna(), ax=ax, color="#4C78A8")
    q1, q3 = customer_raw[col].quantile([0.25, 0.75])
    iqr = q3 - q1
    outliers = customer_raw[col][(customer_raw[col] < q1 - 1.5*iqr) | (customer_raw[col] > q3 + 1.5*iqr)]
    ax.set_title(f"{col}\n(outliers: {outliers.count()}, {outliers.count()/len(customer_raw)*100:.1f}%)")
plt.tight_layout()
plt.show()
