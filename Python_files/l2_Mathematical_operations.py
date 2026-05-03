# ==========================================
# 1. CHECKING DATA TYPES
# ==========================================
# Use the type() function to see what kind of data you are working with
print(type("1234555"))  # <class 'str'> (String)
print(type(12333))      # <class 'int'> (Integer)
print(type(3.141592))   # <class 'float'> (Floating point number / Decimal)
print(type(3 < 2))      # <class 'bool'> (Boolean - True or False)

# ==========================================
# 2. BASIC MATHEMATICAL OPERATIONS
# ==========================================
print(1 + 1)  # Addition
print(4 - 2)  # Subtraction
print(5 * 5)  # Multiplication
print(6 / 2)  # Division (Always returns a float in Python, e.g., 3.0)

# Special Mathematical Operators
print(2 ** 4)   # Exponent (2 to the power of 4)
print(78 // 9)  # Floor division (Divides and drops the decimal, returning an integer)
print(80000 % 2) # Modulo / Remainder (Returns the remainder of a division. Great for checking even/odd numbers)

# ==========================================
# 3. ORDER OF OPERATIONS (PEMDAS)
# ==========================================
# Python follows PEMDAS: Parentheses (), Exponents **, Multiplication * / Division /, Addition + / Subtraction -
# Here are two examples showing how parentheses change the final result:

# Example 1: Left to right following standard PEMDAS (Multiplication and Division happen first)
print(3 * 3 + 3 / 3 - 3)
# Steps: (3 * 3) + (3 / 3) - 3  =>  9 + 1.0 - 3  =>  7.0

# Example 2: Using parentheses to force addition to happen first
print(3 * (3 + 3) / 3 - 3)
# Steps: 3 * (6) / 3 - 3  =>  18 / 3 - 3  =>  6.0 - 3  =>  3.0

# ==========================================
# 4. TYPE CONVERSION (CASTING) & CONCATENATION
# ==========================================
# Strings vs Integers
print("123" + "456")  # String concatenation (combines text: "123456")
print(int("123") + int("45"))  # Converting strings to integers to do math (123 + 45 = 168)
print(str(12) + str(32)) # Converting integers to strings to concatenate ("1232")

# Getting input, converting it, and doing math
number1 = int(input("Give me first number: "))
number2 = int(input("Give me second number: "))
print("The sum is:", number1 + number2)

# ==========================================
# 5. THE LEN() CONVERSION RULE
# ==========================================
user_name = input("What is your name? ")
length = len(user_name)

# CRITICAL RULE: The len() function outputs an Integer.
# You CANNOT concatenate a string and an integer using the '+' symbol.
# You MUST convert the integer into a string first using str().
print("Number of characters in your name is " + str(length))

# ==========================================
# 6. NUMBER MANIPULATION & ASSIGNMENT
# ==========================================
# Rounding numbers
print(round(78 / 9))        # Rounds to the nearest whole number (9)
print(round(3.14159, 2))    # Rounds to exactly 2 decimal places (3.14)

# Assignment Operators (Shortcut for updating a variable)
score = 10
score /= 5  # This is the same as writing: score = score / 5
print(score)

# ==========================================
# 7. MINI-PROJECT: TIP CALCULATOR
# ==========================================
print("\n--- FINAL MINI-PROJECT ---")
print("🔷 Initializing... [MAGI-CORE 9000 Activated]")
print("💡 Hello, I am your AI dining assistant. Let's split your bill with precision and elegance.\n")

# Get inputs from the user and immediately cast them to the correct data types
bill = float(input("Enter the total bill amount (e.g., 987.65): ₹ "))
tip_percent = int(input("How much tip would you like to give? (10, 12, 15): "))
people = int(input("How many people are splitting the bill? "))

print("\n🔍 Calculating optimal split... Please wait...")
print("✅ Tip calculated. Bill adjusted. Distribution protocol engaged.\n")

# Magic calculation
tip_amount = (tip_percent / 100) * bill
total_amount = tip_amount + bill
split_amount = total_amount / people

# Show result rounded to 2 decimal places using f-strings
print(f"🧮 Total bill with tip: ₹{round(total_amount, 2)}")
print(f"🪄 Each person should pay: ₹{round(split_amount, 2)}")
print(f"\n🔷 Thank you for using MAGI-CORE 9000. 🍽️🛸")

# ==========================================
# 8. COMPARISON OPERATORS
# ==========================================
# Comparison operators compare two values and always return a Boolean (True or False).

x = 10
y = 5

print(x > y)   # Greater than (Output: True)
print(x < y)   # Less than (Output: False)

# CRITICAL RULE:
# A single '=' assigns a value to a variable (e.g., x = 10).
# A double '==' compares two values to see if they are the same.
print(x == y)  # Equal to (Output: False)
print(x != y)  # Not equal to (Output: True)

print(x >= 10) # Greater than or equal to (Output: True)
print(y <= 5)  # Less than or equal to (Output: True)

# --- Quick Practical Example ---
# Checking if someone meets an age requirement
print("\n--- Age Check ---")
user_age = int(input("How old are you? "))
is_adult = user_age >= 18

print(f"Are you 18 or older? {is_adult}")