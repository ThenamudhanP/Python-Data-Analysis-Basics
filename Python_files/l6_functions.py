# ==========================================
# 1. DEFINING AND CALLING A FUNCTION
# ==========================================
# Defining a function
def my_function():
    print("I created this function")
    print("Good morning")


# Calling the function
my_function()


# Another basic function example
def greet():
    print("\nHello world!")
    print("Ore wa Monkey D. Luffy!")
    print("Kaizoku ou ni ore wa naru!")  # I am going to be the pirate king!


greet()


# ==========================================
# 2. PARAMETERS AND ARGUMENTS
# ==========================================
# We can define functions with variables too, and then do things with the variable inside the function.
def greet_name(name):
    print(f"\nHello {name}")
    print(f"Nice to meet you {name}, I am Monkey D. Luffy")


greet_name("Tom")


# Important distinction:
# In here, the variable "name" (in the definition) is referred to as the PARAMETER.
# The actual data passed inside ("Tom") is called the ARGUMENT.


# ==========================================
# 3. MULTIPLE INPUTS & KEYWORD ARGUMENTS
# ==========================================
# Taking multiple inputs in the function
def greet_name_place(name, location):
    print(f"\nOre wa {name}")
    print(f"I am from {location}")


# Positional arguments (matches the exact order of the parameters)
greet_name_place("Sanji", "All Blue")

# Keyword arguments: When calling the function, you mention what argument to assign to what parameter.
# Even though you change the place/order, if you define it explicitly, it will work perfectly.
greet_name_place(location="Baratie", name="Cook")

# ==========================================
# 4. MINI-PROJECT: LOVE CALCULATOR
# ==========================================
print("\n--- FINAL MINI-PROJECT ---")


def calculate_love_score(name1, name2):
    score1 = 0
    score2 = 0

    # Combine both names and convert to lowercase so capital letters don't mess up the count
    combined_names = (name1 + name2).lower()

    # Check for letters in "true"
    for letter in combined_names:
        if letter in "true":
            score1 += 1

    # Check for letters in "love"
    for letter in combined_names:
        if letter in "love":
            score2 += 1

    # Print the individual scores (optional, good for debugging)
    print(f"T, R, U, E occurs: {score1} times")
    print(f"L, O, V, E occurs: {score2} times")

    # Combine the numbers as a string, then print the final score
    print(f"Your overall Love Score is: {score1}{score2}")


# Calling our project function with our arguments
calculate_love_score("Angela Yu", "Thenamudhan")