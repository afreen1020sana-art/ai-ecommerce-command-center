import pandas as pd
import random

orders = pd.read_csv("orders.csv")

return_reasons = [
    "Damaged",
    "Wrong Item",
    "Not Needed",
    "Late Delivery"
]

returns = []

sample = orders.sample(n=10000)

for i, row in sample.iterrows():
    returns.append({
        "order_id": i + 1,
        "return_reason":
            random.choice(return_reasons),
        "return_date":
            row["order_date"]
    })

df = pd.DataFrame(returns)

df.to_csv("returns.csv", index=False)

print("Returns generated successfully.")