from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score

model_df = clean_order.copy()
model_df["is_loss"] = (model_df["Profit"] < 0).astype(int)

# Sanity check: class balance before modeling
print("Class balance (is_loss):")
print(model_df["is_loss"].value_counts(normalize=True))

cat_features = ["Category", "Sub_Category", "Segment", "Ship_Mode"]
num_features = ["Discount_Percent", "Quantity", "List_Price", "cost_price"]

X = model_df[cat_features + num_features]
y = model_df["is_loss"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)

preprocess = ColumnTransformer([
    ("cat", OneHotEncoder(handle_unknown="ignore"), cat_features),
    ("num", StandardScaler(), num_features),
])

clf = Pipeline([
    ("prep", preprocess),
    ("model", RandomForestClassifier(
        n_estimators=300, max_depth=8, random_state=42, class_weight="balanced"
    )),
])

clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
y_proba = clf.predict_proba(X_test)[:, 1]
auc = roc_auc_score(y_test, y_proba)

print(f"\nTest set size: {len(X_test)}")
print(f"ROC-AUC: {auc:.3f}")
print(classification_report(y_test, y_pred, digits=3))