def monthly_spend_analysis(transactions):
    monthly_spend = (
        transactions
        .groupby("month")["amount"]
        .sum()
        .reset_index()
    )
    return monthly_spend


def category_spend_analysis(transactions):
    category_spend = (
        transactions
        .groupby("merchant_category")["amount"]
        .sum()
        .reset_index()
        .sort_values(by="amount", ascending=False)
    )
    return category_spend

