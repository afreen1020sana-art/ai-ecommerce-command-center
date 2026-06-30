import pandas as pd
import random
from datetime import timedelta

orders = pd.read_csv("orders.csv")

shipments = []

for i, row in orders.iterrows():
    delivery_days = random.randint(1, 10)

    shipments.append({
        "order_id": i + 1,
        "delivery_date":
            pd.to_datetime(row["order_date"])
            + timedelta(days=delivery_days),
        "delay_days": max(delivery_days - 5, 0)
    })

df = pd.DataFrame(shipments)

df.to_csv("shipments.csv", index=False)

print("Shipments generated successfully.")