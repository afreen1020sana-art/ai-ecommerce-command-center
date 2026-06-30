import pandas as pd
import random

categories = [
    "Electronics",
    "Fashion",
    "Home",
    "Beauty",
    "Sports"
]

products = []

for i in range(1, 501):
    category = random.choice(categories)

    products.append({
        "product_name": f"{category} Product {i}",
        "category": category,
        "price": round(random.uniform(100, 5000), 2),
        "stock": random.randint(10, 500)
    })

df = pd.DataFrame(products)

df.to_csv("products.csv", index=False)

print(df.head())
<<<<<<< HEAD
print("Products generated successfully.")
=======
print("Products generated successfully.")
>>>>>>> 4f4d27a (Day 1 - Generated ecommerce datasets)
