# PERSONAL BUDGET TRACKER - COMPLETE VERSION

print("=== PERSONAL BUDGET TRACKER ===")

# TASK 1 & 3: Get user information
def get_user_info():
    name = input("Enter your name: ")
    formatted_name = name.strip().title()
    
    monthly_income = float(input("Enter your monthly income: $"))
    savings_goal = float(input("Enter your savings goal: $"))
    
    print(f"\nHello, {formatted_name}! Now enter your actual expenses:")
    rent = float(input("Rent: $"))
    groceries = float(input("Groceries: $"))
    transportation = float(input("Transportation: $"))
    entertainment = float(input("Entertainment: $"))
    
    return formatted_name, monthly_income, savings_goal, rent, groceries, transportation, entertainment

# TASK 2: Calculation functions
def calculate_total_expenses(rent, groceries, transportation, entertainment):
    return rent + groceries + transportation + entertainment

def calculate_money_left(income, total_expenses):
    return income - total_expenses

# TASK 4: Budget analysis - FIXED INDENTATION
def analyze_budget(money_left, savings_goal):
    if money_left < 0:
        overspent = abs(money_left)
        return f"Warning: You overspent by ${overspent} this month! 💸"
    elif money_left >= savings_goal:
        return "Great job! You met your savings goal! 🎉"
    elif money_left > 0:
        short_amount = savings_goal - money_left
        return f"You saved ${money_left} but were ${short_amount} from your goal."
    else:
        return "You broke even this month."

# TASK 5: Generate report - FIXED STRING FORMATTING
def generate_budget_report(name, income, savings_goal, rent, groceries, transportation, entertainment):
    total_expenses = calculate_total_expenses(rent, groceries, transportation, entertainment)
    money_left = calculate_money_left(income, total_expenses)
    status = analyze_budget(money_left, savings_goal)
    
    report = f"""
=== MONTHLY BUDGET REPORT FOR {name.upper()} ===
INCOME: ${income}
EXPENSES: ${total_expenses}
  - Rent: ${rent}
  - Groceries: ${groceries}
  - Transportation: ${transportation}
  - Entertainment: ${entertainment}
MONEY LEFT: ${money_left}
SAVINGS GOAL: ${savings_goal}
STATUS: {status}
"""
    return report

# MAIN PROGRAM - FIXED EXTRA CHARACTERS
def main():
    name, income, savings_goal, rent, groceries, transport, entertainment = get_user_info()
    report = generate_budget_report(name, income, savings_goal, rent, groceries, transport, entertainment)
    print(report)

# Run the program
if __name__ == "__main__":
    main()
