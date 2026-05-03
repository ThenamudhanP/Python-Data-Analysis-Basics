# ==========================================
# 1. LOCAL VS GLOBAL VARIABLES (SCOPE)
# ==========================================
# Global variables are defined OUTSIDE any function and can be used anywhere in the file.
global_tax_rate = 0.08


def calculate_total(price):
    # Local variables are defined INSIDE a function.
    # They CANNOT be used outside of this specific function.
    local_discount = 10

    tax = price * global_tax_rate
    final_price = price + tax - local_discount
    print(f"Total: ${final_price}")


# Calling the function works perfectly
calculate_total(price=100)


# INTENTIONAL ERROR DEMONSTRATION:
# If you try to print(local_discount) out here, Python will throw a NameError!
# This is because 'local_discount' only exists inside the calculate_total function.
# print(local_discount)  # Uncommenting this line will crash the program


# ==========================================
# 2. PRINT VS RETURN IN FUNCTIONS
# ==========================================
# Print just shows the value on the screen, but the program forgets it immediately.
def add_print(a, b):
    print(f"Printing inside function: {a + b}")


# You see the answer, but you can't save it to a variable.
add_print(a=5, b=10)


# Return actually gives the value back to the program so you can store it and use it later.
# This is highly preferred when building real applications!
def add_return(a, b):
    return a + b


# Now we can save the output into a new variable!
result = add_return(a=5, b=10)
print(f"The saved result from our return function is: {result}")

# ==========================================
# 3. TUPLES (Immutable Lists)
# ==========================================
# A Tuple is very similar to a list, but it is IMMUTABLE (it cannot be changed).
# You use parentheses () instead of square brackets [].
my_tuple = ("Apple", "Banana", "Cherry")

print("\n--- Tuple Example ---")
print(my_tuple[1])  # You can still read items from it using an index (Outputs: Banana)

# my_tuple[1] = "Mango"
# ^ ERROR: You cannot change, add, or remove items in a tuple once it is created!


# ==========================================
# 4. SETS (Unique Collections)
# ==========================================
# A Set is an unordered, unindexed collection of UNIQUE items. No duplicates allowed!
# You use curly braces {}, just like a dictionary, but without the Key:Value pairs.
my_set = {"Apple", "Banana", "Apple", "Cherry", "Banana"}

print("\n--- Set Example ---")
# Notice how "Apple" and "Banana" only print ONCE. Sets automatically delete any duplicates.
print(my_set)