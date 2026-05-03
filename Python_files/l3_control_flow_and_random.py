import random

# You have to import external modules before using them.
# You can also create your own modules (other .py files), import them,
# and use their functions by typing module_name.function_name()

# ==========================================
# 1. THE RANDOM MODULE
# ==========================================
print("--- Exploring Random Numbers ---")

# randint(): Generates a random integer between two numbers (inclusive of both)
random_integer = random.randint(1, 10)
print(f"Random Integer (1 to 10): {random_integer}")

# random(): Generates a random float between 0.0 and 1.0 (includes 0.0, but not 1.0)
random_float_0to1 = random.random()
print(f"Random Float (0 to 1): {random_float_0to1}")

# By multiplying by 10, we expand the range to 0.0 up to 9.999...
print(f"Random Float (0 to 9.99): {random_float_0to1 * 10}")

# uniform(): Generates a random float between two specific numbers (inclusive)
random_float = random.uniform(1, 10)
print(f"Random Float (1.0 to 10.0): {random_float}")

# ==========================================
# 2. IF / ELSE STATEMENTS (CONTROL FLOW)
# ==========================================
# An if/else statement allows your program to make decisions based on conditions.
# It works like a fork in the road:
# IF the condition is True, do Action A.
# ELSE (if it is False), do Action B.


print("\n--- Basic If/Else Example ---")
weather = "raining"

if weather == "raining":
    print("Take an umbrella!")
else:
    print("Enjoy the sunshine!")

# ==========================================
# 3. MINI-PROJECT 1: VIRTUAL COIN TOSS
# ==========================================
print("\n--- Project 1: Coin Toss ---")
# We use randint(0, 1) to simulate a 50/50 chance.
coin_toss = random.randint(0, 1)

if coin_toss == 0:
    print("Result: Heads")
else:
    print("Result: Tails")

# ==========================================
# 4. MINI-PROJECT 2: ROLLER COASTER TICKETING
# ==========================================
print("\n--- Project 2: Roller Coaster Ride ---")
print("🎢 Welcome to the Roller Coaster Ride!")

bill = 0

# Ask for height and convert to integer
height = int(input("What is your height in cm? "))

# First check: Are they tall enough to ride at all?
if height >= 120:
    print("You can ride the roller coaster!")

    # Nested check: Determine ticket price based on age
    age = int(input("What is your age? "))

    if age <= 12:
        print("Child ticket is ₹5.")
        bill = 5
    elif age <= 18:
        print("Teen ticket is ₹9.")
        bill = 9
    elif age >= 45 and age <= 55:
        print("Midlife crisis special: Enjoy the ride, the ticket is on us!")
        bill = 0
    else:
        print("Adult ticket is ₹15.")
        bill = 15

    # Check for photo addition
    photo = input("If you want a picture taken, type 'y' or type 'n': ")

    if photo == "y":
        bill = bill + 4  # Can also be written as: bill += 4

    print(f"💵 The total bill for your ticket is ₹{bill}")

else:
    # If the very first height check fails, it skips to here
    print("Sorry, you have to grow taller before you can ride.")