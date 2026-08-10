import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

pca = PCA(n_components=2, random_state=42)
coords = pca.fit_transform(X_scaled)

fig, ax = plt.subplots(figsize=(8, 6), dpi=150)
scatter = ax.scatter(coords[:, 0], coords[:, 1], c=seg_df["Cluster"], cmap="tab10", s=10, alpha=0.6)
ax.set_title("Customer Segments (KMeans, k=4) — PCA Projection")
ax.set_xlabel(f"PC1 ({pca.explained_variance_ratio_[0]:.1%} variance)")
ax.set_ylabel(f"PC2 ({pca.explained_variance_ratio_[1]:.1%} variance)")
legend1 = ax.legend(*scatter.legend_elements(), title="Cluster", loc="best")
ax.add_artist(legend1)
plt.tight_layout()
plt.close('all')