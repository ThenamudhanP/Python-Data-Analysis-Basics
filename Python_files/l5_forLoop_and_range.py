import random

# ==========================================
# 1. THE 'FOR' LOOP (Iterating over Lists)
# ==========================================

print("--- For Loop Basics ---")
fruits = ["Mango", "Apple", "Orange"]

for fruit in fruits:
    print(fruit)
    # You can also manipulate the item inside the loop
    print(fruit + " juice\n")


# ==========================================
# 2. THE RANGE() FUNCTION
# ==========================================
print("--- The range() Function ---")
# range() cannot work alone to output numbers; it is usually combined with a for loop.
# Remember: The range function DOES NOT include the final number.
# range(1, 101) goes from 1 up to 100.

# The Carl Gauss Problem:
# When mathematician Carl Gauss was 10 years old, his teacher asked the class to add
# numbers from 1 to 100. He quickly realized that pairing them (1+100, 2+99) created
# 50 pairs of 101, instantly getting 5050. Let's do this with a Python loop!

total = 0
for number in range(1, 101):
    total += number

print(f"The sum of numbers from 1 to 100 is: {total}")

# --- Using 'Step' in Range ---
# range(start, stop, step)
# Here, (1, 10, 4) starts at 1, goes up to (but not including) 10, and skips by 4 digits.
print("\nCounting with a step of 4:")
for digit in range(1, 10, 4):
    print(digit) # Output: 1, 5, 9


# ==========================================
# 3. MINI-PROJECT 1: FIZZBUZZ
# ==========================================
# A classic programming interview question!
print("\n--- Project 1: FizzBuzz ---")

for num in range(1, 101):
    # Check the most strict condition first (divisible by BOTH 3 and 5)
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)


# ==========================================
# 4. MINI-PROJECT 2: PASSWORD GENERATOR
# ==========================================
print("\n--- Project 2: Password Generator ---")

letters = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
    "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F",
    "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
    "W", "X", "Y", "Z"
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = [
    "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+",
    "[", "]", "{", "}", "|", ";", ":", "'", ",", ".", "<", ">", "/", "?", "~", "`"
]

print("Welcome to the PyPassword Generator!")

no_of_letters = int(input("How many letters would you like in your password? "))
no_of_numbers = int(input("How many numbers would you like? "))
no_of_symbols = int(input("How many symbols would you like? "))

# IMPORTANT: We use a List instead of a String here.
# Why? Because you cannot use random.shuffle() on a string. Strings are immutable!
password_list = []

# Fetch random letters
for _ in range(no_of_letters):
    password_list.append(random.choice(letters))

# Fetch random numbers
for _ in range(no_of_numbers):
    password_list.append(random.choice(numbers))

# Fetch random symbols
for _ in range(no_of_symbols):
    password_list.append(random.choice(symbols))

# Right now, the password is in order: letters -> numbers -> symbols.
# Let's shuffle the list so it is completely randomized.
random.shuffle(password_list)

# Now, convert the list back into a single string using the .join() method.
final_password = "".join(password_list)

print(f"\n🔐 Your secure generated password is: {final_password}")