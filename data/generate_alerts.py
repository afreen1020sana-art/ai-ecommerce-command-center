import pandas as pd
from datetime import datetime
import uuid

# Read datasets
orders = pd.read_csv("data/orders.csv")
returns = pd.read_csv("data/returns.csv")
shipments = pd.read_csv("data/shipments.csv")
products = pd.read_csv("data/products.csv")

alerts = []

# Delivery Delay Alert
delay_rate = (
    len(shipments[shipments["delay_days"] > 0])
    / len(shipments)
)

if delay_rate > 0.20:
    alerts.append({
        "alert_id": str(uuid.uuid4())[:8],
        "alert_date": datetime.now().strftime("%Y-%m-%d"),
        "alert_type": "Delivery Delays",
        "severity": "High",
        "message": f"Delay rate is {delay_rate:.2%}",
        "recommended_action": "Review logistics operations"
    })

# Low Inventory Alert
low_stock = products[products["stock"] < 20]

if len(low_stock) > 0:
    alerts.append({
        "alert_id": str(uuid.uuid4())[:8],
        "alert_date": datetime.now().strftime("%Y-%m-%d"),
        "alert_type": "Low Inventory",
        "severity": "Medium",
        "message": f"{len(low_stock)} products have low inventory",
        "recommended_action": "Replenish stock"
    })

# Create alerts dataframe
df = pd.DataFrame(alerts)

# Save alerts file
df.to_csv("alerts.csv", index=False)

# Print output
print(df)
print("Alerts generated successfully.")