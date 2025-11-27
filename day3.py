# DAY 3 - Methods & String Manipulation

# TASK 11 - METHODS 1
print("=== TASK 11 ===")
def square_number(num):
    return num ** 2

print("Square of 5:", square_number(5))
print("Square of 8:", square_number(8))

# TASK 12 - METHODS 2
print("\n=== TASK 12 ===")
def print_name_age(name, age):
    print(f"{name} is {age} years old.")

print_name_age("Alice", 30)
print_name_age("Bob", 25)

# TASK 13 - METHODS 3
print("\n=== TASK 13 ===")
def multiply_numbers(a, b):
    return a * b

print("Multiplication result (4 × 7):", multiply_numbers(4, 7))
print("Multiplication result (3 × 9):", multiply_numbers(3, 9))

# TASK 14 - METHODS 4
print("\n=== TASK 14 ===")
def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

print("10 is:", check_even_odd(10))
print("7 is:", check_even_odd(7))
print("15 is:", check_even_odd(15))

# TASK 15 - METHODS 5
print("\n=== TASK 15 ===")
def find_largest(a, b, c):
    return max(a, b, c)

print("Largest of 3, 7, 2:", find_largest(3, 7, 2))
print("Largest of 10, 5, 8:", find_largest(10, 5, 8))

# TASK 16 - STRING MANIPULATION
print("\n=== TASK 16 ===")
text = " Python programming is awesome! "

# strip spaces
stripped_text = text.strip()
print("Stripped:", stripped_text)

# length
print("Length:", len(stripped_text))

# uppercase
print("Uppercase:", stripped_text.upper())

# replace "awesome" with "powerful"
replaced_text = stripped_text.replace("awesome", "powerful")
print("Replaced:", replaced_text)

# TASK 17 - ADVANCED STRING MANIPULATION
print("\n=== TASK 17 ===")
email = "john.doe@example.com"

# extract username (before @)
username = email.split('@')[0]
print("Username:", username)

# extract domain
domain = email.split('@')[1]
print("Domain:", domain)

# print formatted result
print(f"Username: {username}, Domain: {domain}")
