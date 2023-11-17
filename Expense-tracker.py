import os
from datetime import datetime

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.categories = set()
        self.filename = "expenses.txt"
        self.load_data()

    def load_data(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                lines = file.readlines()
                for line in lines:
                    expense_info = line.strip().split(",")
                    date_str, amount, category, description = map(str.strip, expense_info)
                    date = datetime.strptime(date_str, "%Y-%m-%d")
                    expense = {"date": date, "amount": float(amount), "category": category, "description": description}
                    self.expenses.append(expense)
                    self.categories.add(category)

    def save_data(self):
        with open(self.filename, "w") as file:
            for expense in self.expenses:
                date_str = expense['date'].strftime("%Y-%m-%d")
                file.write(f"{date_str},{expense['amount']},{expense['category']},{expense['description']}\n")

    def display_expenses(self):
        if not self.expenses:
            print("No expenses found.")
            return

        print("Date       | Amount  | Category      | Description")
        print("-------------------------------------------------")
        for expense in self.expenses:
            date_str = expense['date'].strftime("%Y-%m-%d")
            print(f"{date_str} | {expense['amount']:.2f}  | {expense['category'][:12]:12} | {expense['description'][:30]}")

    def add_expense(self, amount, category, description):
        date = datetime.now()
        expense = {"date": date, "amount": float(amount), "category": category, "description": description}
        self.expenses.append(expense)
        self.categories.add(category)
        print("Expense added.")

    def calculate_total_expenses(self, time_frame):
        total_expenses = sum(expense['amount'] for expense in self.expenses if self.is_within_time_frame(expense['date'], time_frame))
        print(f"Total expenses for {time_frame}: ${total_expenses:.2f}")

    def generate_monthly_report(self):
        if not self.expenses:
            print("No expenses found.")
            return

        print("Monthly Report:")
        for category in self.categories:
            category_total = sum(expense['amount'] for expense in self.expenses if expense['category'] == category)
            print(f"{category}: ${category_total:.2f}")

    def is_within_time_frame(self, expense_date, time_frame):
        now = datetime.now()
        if time_frame == 'daily':
            return now.day == expense_date.day and now.month == expense_date.month and now.year == expense_date.year
        elif time_frame == 'weekly':
            return now.isocalendar()[1] == expense_date.isocalendar()[1] and now.year == expense_date.year
        elif time_frame == 'monthly':
            return now.month == expense_date.month and now.year == expense_date.year

    def menu(self):
        while True:
            print("\n===== Expense Tracker =====")
            print("1. Add Expense")
            print("2. List Expenses")
            print("3. Calculate Total Expenses")
            print("4. Generate Monthly Report")
            print("5. Save and Exit")

            choice = input("Enter your choice (1-5): ")
            if choice == '1':
                amount = input("Enter expense amount: ")
                category = input("Enter expense category: ")
                description = input("Enter expense description: ")
                self.add_expense(amount, category, description)
            elif choice == '2':
                self.display_expenses()
            elif choice == '3':
                time_frame = input("Enter time frame (daily, weekly, monthly): ")
                self.calculate_total_expenses(time_frame)
            elif choice == '4':
                self.generate_monthly_report()
            elif choice == '5':
                self.save_data()
                print("Data saved. Exiting.")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    expense_tracker = ExpenseTracker()
    expense_tracker.menu()
