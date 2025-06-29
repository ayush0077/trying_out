
class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({
            "amount": amount,
            "description": description
        })

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({
                "amount": -amount,
                "description": description
            })
            return True
        return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = self.name.center(30, "*")
        output = title + "\n"

        for item in self.ledger:
            description = item["description"][:23]
            amount = f"{item['amount']:.2f}"
            output += f"{description:<23}{amount:>7}\n"

        output += f"Total: {self.get_balance():.2f}"
        return output


def create_spend_chart(categories):
    title = "Percentage spent by category\n"

    # Calculate total spent per category (withdrawals only)
    spent = []
    for category in categories:
        total = 0
        for item in category.ledger:
            if item["amount"] < 0:
                total += -item["amount"]
        spent.append(total)

    total_spent = sum(spent)

    # Calculate percentages rounded down to nearest 10
    percentages = [(int((s / total_spent) * 100) // 10) * 10 for s in spent]

    # Build chart
    chart = ""
    for level in range(100, -1, -10):
        chart += f"{level:>3}| "
        for percent in percentages:
            chart += "o  " if percent >= level else "   "
        chart += "\n"

    # Horizontal line
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # Vertical category names
    max_length = max(len(category.name) for category in categories)
    for i in range(max_length):
        chart += "     "
        for category in categories:
            if i < len(category.name):
                chart += category.name[i] + "  "
            else:
                chart += "   "
        if i < max_length - 1:
            chart += "\n"

    return title + chart



