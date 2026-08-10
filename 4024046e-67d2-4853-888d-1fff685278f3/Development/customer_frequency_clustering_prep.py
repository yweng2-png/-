freq_map = {
    "Weekly": 52, "Bi-Weekly": 26, "Fortnightly": 26, "Monthly": 12,
    "Every 3 Months": 4, "Quarterly": 4, "Annually": 1
}

seg_df = clean_customer_filled.copy()
seg_df["Freq_Score"] = seg_df["Frequency_of_Purchases"].map(freq_map)
seg_df["Freq_Score"] = seg_df["Freq_Score"].fillna(seg_df["Freq_Score"].median())

cluster_features = ["Age", "Purchase_Amount", "Previous_Purchases", "Review_Rating", "Freq_Score"]

# Check scale differences — this determines whether StandardScaler is necessary
print(seg_df[cluster_features].describe().T[["mean", "std", "min", "max"]])