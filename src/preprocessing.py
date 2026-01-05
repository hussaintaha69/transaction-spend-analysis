def preprocess(transactions):
    transactions["month"] = transactions["transaction_date"].dt.to_period("M")
    return transactions

