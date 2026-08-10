from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
seg_df["Cluster"] = kmeans.fit_predict(X_scaled)

cluster_profile = seg_df.groupby("Cluster")[cluster_features].mean().round(1)
cluster_profile["customers"] = seg_df["Cluster"].value_counts().sort_index()
cluster_profile["pct_of_base"] = (cluster_profile["customers"] / len(seg_df) * 100).round(1)

print(cluster_profile)
