import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
import joblib

# load features
X = pd.read_csv("finance_features.csv")

# scale data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# train model
model = IsolationForest(
    n_estimators=200,
    contamination=0.02,
    random_state=42
)
model.fit(X_scaled)

# save model + scaler
joblib.dump(model, "anomaly_model.pkl")
joblib.dump(scaler, "scaler.pkl")

print("Model trained and saved")
