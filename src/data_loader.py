import pandas as pd

def load_data():
    transactions = pd.read_csv("../data/transactions.csv", parse_dates=["transaction_date"])
    customers = pd.read_csv("../data/customers.csv")
    return transactions, customers

