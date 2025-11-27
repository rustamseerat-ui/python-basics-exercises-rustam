from flask import Flask, render_template_string, request

app = Flask(__name__)

# HTML template for our web app
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>💰 Web Budget Tracker</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }
        .container { background: #f5f5f5; padding: 20px; border-radius: 10px; }
        input, button { padding: 10px; margin: 5px; width: 100%; }
        .result { background: white; padding: 15px; margin: 10px 0; border-radius: 5px; }
        .success { color: green; }
        .warning { color: orange; }
        .danger { color: red; }
    </style>
</head>
<body>
    <div class="container">
        <h1>💰 Web Budget Tracker</h1>
        
        <form method="POST">
            <h3>Enter Your Budget Information:</h3>
            <input type="text" name="name" placeholder="Your Name" required>
            <input type="number" name="income" placeholder="Monthly Income ($)" required>
            <input type="number" name="savings_goal" placeholder="Savings Goal ($)" required>
            
            <h4>Expenses:</h4>
            <input type="number" name="rent" placeholder="Rent ($)" required>
            <input type="number" name="groceries" placeholder="Groceries ($)" required>
            <input type="number" name="transportation" placeholder="Transportation ($)" required>
            <input type="number" name="entertainment" placeholder="Entertainment ($)" required>
            
            <button type="submit">Calculate Budget</button>
        </form>

        {% if result %}
        <div class="result">
            <h2>📊 Budget Report for {{ name }}</h2>
            <p><strong>Income:</strong> ${{ income }}</p>
            <p><strong>Total Expenses:</strong> ${{ total_expenses }}</p>
            <p><strong>Money Left:</strong> ${{ money_left }}</p>
            <p><strong>Savings Goal:</strong> ${{ savings_goal }}</p>
            <p class="{% if status == 'GOAL_ACHIEVED' %}success{% elif status == 'CLOSE' %}warning{% else %}danger{% endif %}">
                <strong>Status:</strong> {{ status_text }}
            </p>
            
            <h3>Expenses Breakdown:</h3>
            <ul>
            {% for category, amount in expenses.items() %}
                <li>{{ category }}: ${{ amount }} ({{ (amount/total_expenses*100)|round(1) }}%)</li>
            {% endfor %}
            </ul>
        </div>
        {% endif %}
    </div>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def budget_tracker():
    if request.method == 'POST':
        # Get form data
        name = request.form['name']
        income = float(request.form['income'])
        savings_goal = float(request.form['savings_goal'])
        
        expenses = {
            'Rent': float(request.form['rent']),
            'Groceries': float(request.form['groceries']),
            'Transportation': float(request.form['transportation']),
            'Entertainment': float(request.form['entertainment'])
        }
        
        # Calculate budget (using your existing logic)
        total_expenses = sum(expenses.values())
        money_left = income - total_expenses
        
        # Determine status
        if money_left >= savings_goal:
            status = 'GOAL_ACHIEVED'
            status_text = '✅ Great job! You met your savings goal!'
        elif money_left > 0:
            status = 'CLOSE'
            status_text = f'⚠️ Close! You saved ${money_left} but need ${savings_goal - money_left} more'
        else:
            status = 'OVERSPENT'
            status_text = f'❌ Overspent by ${abs(money_left)}!'
        
        return render_template_string(HTML_TEMPLATE, 
            result=True, name=name, income=income, savings_goal=savings_goal,
            total_expenses=total_expenses, money_left=money_left,
            expenses=expenses, status=status, status_text=status_text)
    
    return render_template_string(HTML_TEMPLATE, result=False)

if __name__ == '__main__':
    print("🌐 Starting Web Budget Tracker...")
    print("📱 Open your browser and go to: http://localhost:5000")
    print("🛑 Press Ctrl+C to stop the server")
    app.run(debug=True)
