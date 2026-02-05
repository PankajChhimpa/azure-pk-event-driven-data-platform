import pandas as pd
import joblib
import os

# ADLS path (processed zone)
DATA_PATH = "/mnt/azureml/finance_features.csv"  # placeholder

# If using datastore mount, Azure ML will mount it here
df = pd.read_csv(DATA_PATH)

X = df.drop("target", axis=1)
y = df["target"]

from sklearn.linear_model import LogisticRegression
model = LogisticRegression(max_iter=1000)
model.fit(X, y)

os.makedirs("outputs", exist_ok=True)
joblib.dump(model, "outputs/model.pkl")

print("Model training complete")
int(f"MODEL_ACCURACY: {accuracy}")