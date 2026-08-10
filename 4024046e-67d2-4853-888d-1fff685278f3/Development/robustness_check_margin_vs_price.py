import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import roc_auc_score
from sklearn.impute import SimpleImputer

# Robustness check: does the model rely on raw price fields, or can it learn
# the same signal from the business-interpretable Margin_Rate + category structure?

model_df2 = clean_order.copy()
model_df2["is_loss"] = (model_df2["Profit"] < 0).astype(int)

cat_features2 = ["Category", "Sub_Category", "Segment", "Ship_Mode"]
num_features2 = ["Discount_Percent", "Quantity", "Margin_Rate"]  # swap raw price for Margin_Rate

X2 = model_df2[cat_features2 + num_features2]
y2 = model_df2["is_loss"]

X2_train, X2_test, y2_train, y2_test = train_test_split(
    X2, y2, test_size=0.25, random_state=42, stratify=y2
)

preprocess2 = ColumnTransformer([
    ("cat", OneHotEncoder(handle_unknown="ignore"), cat_features2),
    ("num", Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler()),
    ]), num_features2),
])
clf2 = Pipeline([
    ("prep", preprocess2),
    ("model", RandomForestClassifier(n_estimators=300, max_depth=8, random_state=42, class_weight="balanced")),
])
clf2.fit(X2_train, y2_train)
auc2 = roc_auc_score(y2_test, clf2.predict_proba(X2_test)[:, 1])

print(f"Original model AUC (raw List_Price/cost_price): {auc:.3f}")
print(f"Interpretable model AUC (Margin_Rate instead):   {auc2:.3f}")

ohe_cols2 = clf2.named_steps["prep"].named_transformers_["cat"].get_feature_names_out(cat_features2)
imp2 = pd.DataFrame({
    "feature": list(ohe_cols2) + num_features2,
    "importance": clf2.named_steps["model"].feature_importances_
}).sort_values("importance", ascending=False).head(10)
print(imp2)