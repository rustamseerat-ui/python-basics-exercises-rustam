# DAY 4 - Math Operators

# TASK 18
print("=== TASK 18 ===")
x = 15
y = 4

print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)
print("Modulus:", x % y)

# TASK 19
print("\n=== TASK 19 ===")
counter = 0
print("Initial counter:", counter)

# Increment 3 times
counter += 1
counter += 1
counter += 1
print("After 3 increments:", counter)

# Decrement 2 times
counter -= 1
counter -= 1
print("After 2 decrements:", counter)

# TASK 20 - FREE EXERCISE
print("\n=== TASK 20 ===")
def calculate_bmi(weight, height):
    """Calculate BMI using weight (kg) and height (m)"""
    return weight / (height ** 2)

def categorize_bmi(bmi):
    """Categorize BMI into health categories"""
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def health_report(name, weight, height):
    """Generate a health report"""
    bmi = calculate_bmi(weight, height)
    category = categorize_bmi(bmi)
    
    report = f"""
    HEALTH REPORT FOR {name.upper()}
    =============================
    Weight: {weight} kg
    Height: {height} m
    BMI: {bmi:.2f}
    Category: {category}
    =============================
    """
    return report

# Main program
person_name = "Alice"
person_weight = 68
person_height = 1.75

print(health_report(person_name, person_weight, person_height))

# Additional example
print(health_report("Bob", 80, 1.80))
