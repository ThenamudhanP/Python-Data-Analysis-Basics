# ==========================================
# 1. PRINT STATEMENTS AND DATA TYPES
# ==========================================
print("Hello, World!")

# Printing an integer
print(123)

# Using special characters (\n creates a new line)
print("Monday \nTuesday \nWednesday")

# String concatenation (combining strings with the + )
# Notice the space added after "Hi " so the words don't squish together
print("Hi " + "how are you?")

# ==========================================
# 2. VARIABLES AND INPUT
# ==========================================
# Taking basic input from the user in the console
# input("What is your name? ")

# Storing that input in a variable
username = input("What is your name? ")
print(username)

# ==========================================
# 3. STRING CONCATENATION & F-STRINGS
# ==========================================
user_lastname = input("What is your second name? ")

# The older way using string concatenation
print("Hello " + user_lastname + ", nice to meet you!")

# The modern, preferred way using f-strings
print(f"Hello {user_lastname}, nice to meet you!")

# ==========================================
# 4. THE LEN() FUNCTION & COMMON ERRORS
# ==========================================
my_friend = "Raja"
# This works perfectly because len() counts the characters in a string
print(len(my_friend))

# INTENTIONAL ERROR DEMONSTRATION:
# The len() function cannot be used directly on numbers/integers.
# my_friend_number = 28378274388373847384
# print(len(my_friend_number))  # Uncommenting this line will cause a TypeError!

# To find the length of a number, you must convert it to a string first:
# print(len(str(my_friend_name)))

# ==========================================
# 5. VARIABLE SWAPPING
# ==========================================
jar1 = "sugar"
jar2 = "salt"

# Python allows you to swap values in a single line
jar1, jar2 = jar2, jar1

print(f"Jar 1 now contains: {jar1}")
print(f"Jar 2 now contains: {jar2}")

# ==========================================
# 6. VARIABLE NAMING RULES & COMMENTS
# ==========================================
# Rules for naming variables:
# 1. Cannot start with numbers (e.g., 1username is invalid)
# 2. Cannot use hyphens (e.g., user-name is invalid)
# 3. snake_case (small letters with underscores) is preferred in Python (e.g., user_name)
# 4. camelCase is another acceptable style (e.g., firstName)

"""
This is a multi-line string, often used as a multi-line comment.
Shortcut: You can comment multiple lines by highlighting them and pressing Ctrl + /
"""

# ==========================================
# 7. MINI-PROJECT: MAGIC INTRODUCTION
# ==========================================
print("\n--- FINAL MINI-PROJECT ---")
print("🧙‍♂️ Welcome to the Magic Introduction Generator!")

name = input("What is your name, traveler? ")
origin = input("Where do you hail from? 🔮 ")
power = input("🪄 What magical power do you possess? Fire 🔥, lightning ⚡, or anything special! ")

print("\n✨ Behold! ✨")
print(f"{name} of {origin}, master of {power}, your destiny awaits...")