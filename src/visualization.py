import matplotlib.pyplot as plt

def plot_monthly_spend(monthly_spend):
    plt.figure()
    plt.plot(monthly_spend["month"].astype(str), monthly_spend["amount"])
    plt.xlabel("Month")
    plt.ylabel("Total Spend")
    plt.title("Monthly Transaction Spend Trend")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("../outputs/monthly_spend.png")
    plt.show()


def plot_category_spend(category_spend):
    plt.figure()
    plt.bar(category_spend["merchant_category"], category_spend["amount"])
    plt.xlabel("Category")
    plt.ylabel("Total Spend")
    plt.title("Spend by Merchant Category")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("../outputs/category_spend.png")
    plt.show()

