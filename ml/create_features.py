import pandas as pd

# load transactional data
df = pd.read_csv("../finance_transactions.csv")

# create business features
df["budget_variance"] = df["amount"] - df["budget"]
df["forecast_variance"] = df["amount"] - df["forecast"]

# time-based feature
df["month"] = pd.to_datetime(df["transaction_date"]).dt.month

# select final feature set
features = df[
    [
        "amount",
        "budget",
        "forecast",
        "budget_variance",
        "forecast_variance",
        "month"
    ]
]

# save features
features.to_csv("finance_features.csv", index=False)

print("Feature engineering complete")
