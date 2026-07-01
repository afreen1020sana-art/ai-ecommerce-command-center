import pandas as pd

alerts = pd.read_csv("alerts.csv")

for _, row in alerts.iterrows():
    print("\n" + "=" * 60)
    print(f"ALERT: {row['alert_type']}")
    print(f"SEVERITY: {row['severity']}")
    print(f"MESSAGE: {row['message']}")

    if row["alert_type"] == "Delivery Delays":
        explanation = """
Business Impact:
- Orders may arrive late.
- Customer satisfaction may decrease.
- Returns and cancellations could increase.

Recommended Action:
- Review logistics performance.
- Investigate warehouse bottlenecks.
- Monitor delayed regions.
"""
    elif row["alert_type"] == "Low Inventory":
        explanation = """
Business Impact:
- Products may go out of stock.
- Revenue opportunities could be lost.

Recommended Action:
- Replenish inventory.
- Review demand forecasting.
- Prioritize high-selling products.
"""
    else:
        explanation = "No explanation available."

    print(explanation)