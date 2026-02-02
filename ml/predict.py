import pandas as pd
import joblib

# load artifacts
X = pd.read_csv("finance_features.csv")
model = joblib.load("anomaly_model.pkl")
scaler = joblib.load("scaler.pkl")

# scale features
X_scaled = scaler.transform(X)

# predict anomalies
preds = model.predict(X_scaled)

# convert to business-friendly format
results = X.copy()
results["anomaly"] = [1 if p == -1 else 0 for p in preds]

# save predictions
results.to_csv("predictions.csv", index=False)

print("Predictions generated")
