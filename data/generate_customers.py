from faker import Faker
import pandas as pd
import random

fake = Faker()

customers = []

for i in range(5000):
    customers.append({
        "customer_name": fake.name(),
        "city": fake.city(),
        "state": fake.state(),
        "segment": random.choice(
            ["Consumer", "Corporate", "Small Business"]
        )
    })

df = pd.DataFrame(customers)

df.to_csv("customers.csv", index=False)

print(df.head())
print("Customers generated successfully.")
