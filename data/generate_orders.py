import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()

orders = []

regions = [
    "North",
    "South",
    "East",
    "West"
]

statuses = [
    "Delivered",
    "Pending",
    "Cancelled"
]

start_date = datetime(2025, 1, 1)

for i in range(1, 100001):

    order_date = start_date + timedelta(
        days=random.randint(0, 364)
    )

    quantity = random.randint(1, 5)

    revenue = round(
        quantity * random.uniform(100, 5000),
        2
    )

    orders.append({
        "order_date": order_date.date(),
        "customer_id": random.randint(1, 5000),
        "product_id": random.randint(1, 500),
        "quantity": quantity,
        "revenue": revenue,
        "region": random.choice(regions),
        "order_status": random.choice(statuses)
    })

df = pd.DataFrame(orders)

df.to_csv("orders.csv", index=False)

print(df.head())
print("Orders generated successfully.")