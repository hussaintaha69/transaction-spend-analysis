import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

np.random.seed(42)

# -------------------
# Customers
# -------------------
num_customers = 20

customer_ids = [f"C{str(i).zfill(3)}" for i in range(1, num_customers + 1)]
cities = ["New York", "Chicago", "San Francisco", "Boston", "Seattle"]
card_types = ["Silver", "Gold", "Platinum"]

customers = pd.DataFrame({
    "customer_id": customer_ids,
    "age": np.random.randint(22, 60, size=num_customers),
    "city": np.random.choice(cities, size=num_customers),
    "card_type": np.random.choice(card_types, size=num_customers)
})

customers.to_csv("../data/customers.csv", index=False)

# -------------------
# Transactions
# -------------------
num_transactions = 250
merchant_categories = [
    "Groceries", "Food", "Fuel", "Travel",
    "Electronics", "Entertainment"
]

start_date = datetime(2024, 1, 1)

transactions = []

for i in range(num_transactions):
    transaction = {
        "transaction_id": f"T{str(i+1).zfill(4)}",
        "customer_id": random.choice(customer_ids),
        "transaction_date": start_date + timedelta(days=random.randint(0, 180)),
        "amount": round(np.random.uniform(10, 600), 2),
        "merchant_category": random.choice(merchant_categories)
    }
    transactions.append(transaction)

transactions_df = pd.DataFrame(transactions)
transactions_df.to_csv("../data/transactions.csv", index=False)

print("Data generation completed:")
print(" - customers.csv")
print(" - transactions.csv")

