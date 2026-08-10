from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt

X_scaled = StandardScaler().fit_transform(seg_df[cluster_features])

inertias = []
silhouettes = []
k_range = range(2, 8)
for k in k_range:
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    labels = km.fit_predict(X_scaled)
    inertias.append(km.inertia_)
    silhouettes.append(silhouette_score(X_scaled, labels))

fig, axes = plt.subplots(1, 2, figsize=(12, 4.5), dpi=150)
axes[0].plot(list(k_range), inertias, marker="o")
axes[0].set_xlabel("Number of Clusters (k)")
axes[0].set_ylabel("Inertia (Elbow Method)")
axes[0].set_title("Elbow Method")

axes[1].plot(list(k_range), silhouettes, marker="o", color="#F58518")
axes[1].set_xlabel("Number of Clusters (k)")
axes[1].set_ylabel("Silhouette Score")
axes[1].set_title("Silhouette Score by k")
plt.tight_layout()
plt.show()

print("Silhouette scores:", dict(zip(k_range, [round(s,3) for s in silhouettes])))