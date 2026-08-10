from sklearn.metrics import confusion_matrix
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# ---------- Confusion Matrix ----------
cm = confusion_matrix(y_test, y_pred)
fig_cm, ax = plt.subplots(figsize=(5, 4.5), dpi=150)
im = ax.imshow(cm, cmap="Blues")
for (i, j), v in np.ndenumerate(cm):
    ax.text(j, i, str(v), ha="center", va="center",
             color="white" if v > cm.max() / 2 else "black", fontsize=12)
ax.set_xticks([0, 1]); ax.set_xticklabels(["Profitable", "Loss"])
ax.set_yticks([0, 1]); ax.set_yticklabels(["Profitable", "Loss"])
ax.set_xlabel("Predicted"); ax.set_ylabel("Actual")
ax.set_title(f"Order Loss-Risk Model — Confusion Matrix\nAUC = {auc:.3f}")
plt.tight_layout()
plt.close("all")

# ---------- Feature Importance ----------
ohe_cols = clf.named_steps["prep"].named_transformers_["cat"].get_feature_names_out(cat_features)
all_cols = list(ohe_cols) + num_features
importances = clf.named_steps["model"].feature_importances_

imp_df = pd.DataFrame({"feature": all_cols, "importance": importances}) \
    .sort_values("importance", ascending=False).head(12)

fig_imp, ax = plt.subplots(figsize=(9, 6), dpi=150)
ax.barh(imp_df["feature"][::-1], imp_df["importance"][::-1], color="#4C78A8")
ax.set_title("Top Drivers of Order-Loss Risk (Random Forest Feature Importance)")
ax.set_xlabel("Importance")
plt.tight_layout()
plt.close("all")
