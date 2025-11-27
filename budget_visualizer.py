# BUDGET VISUALIZATION - TEXT BASED
def visualize_budget_text(income, expenses_dict, money_left, savings_goal):
    total_expenses = sum(expenses_dict.values())
    
    print("\n" + "="*50)
    print("📊 BUDGET VISUALIZATION")
    print("="*50)
    
    # Income bar
    income_bar = "█" * int(income / 100)
    print(f"INCOME: ${income}")
    print(f"│{income_bar}│")
    
    # Expenses breakdown
    print("\nEXPENSES BREAKDOWN:")
    for category, amount in expenses_dict.items():
        bar = "█" * int(amount / 50)  # Scale for visibility
        percentage = (amount / total_expenses) * 100
        print(f"  {category:15} ${amount:6.0f} {bar:20} ({percentage:.1f}%)")
    
    # Money left vs savings goal
    print(f"\nMONEY LEFT: ${money_left}")
    if money_left >= savings_goal:
        status = "✅ GOAL ACHIEVED!"
    elif money_left > 0:
        status = "⚠️  CLOSE TO GOAL"
    else:
        status = "❌ OVERSPENT!"
    
    print(f"SAVINGS GOAL: ${savings_goal}")
    print(f"STATUS: {status}")

# Test with your data
income = 3000
expenses = {
    'Rent': 1200,
    'Groceries': 400,
    'Transportation': 300,
    'Entertainment': 200
}
money_left = 900
savings_goal = 500

visualize_budget_text(income, expenses, money_left, savings_goal)

# Test with different scenario
print("\n" + "="*50)
print("TESTING DIFFERENT SCENARIO: OVERS PENT")
print("="*50)

expenses_overspent = {
    'Rent': 1500,
    'Groceries': 500,
    'Transportation': 400,
    'Entertainment': 300
}
money_left_overspent = 300
visualize_budget_text(income, expenses_overspent, money_left_overspent, savings_goal)
