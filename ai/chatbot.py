import pandas as pd

alerts = pd.read_csv("alerts.csv")

question = input("Ask a business question: ").lower()

if "delay" in question:
    print("""
Delivery delays are currently high (49.88%).

Possible reasons:
- Logistics issues
- Warehouse bottlenecks
- Increased order volume

Recommended actions:
- Review shipping partners
- Monitor delayed regions
""")

elif "inventory" in question:
    print("""
12 products have low inventory.

Recommended actions:
- Replenish stock
- Prioritize high-demand products
- Improve forecasting
""")

else:
    print("Sorry, I don't know the answer yet.")