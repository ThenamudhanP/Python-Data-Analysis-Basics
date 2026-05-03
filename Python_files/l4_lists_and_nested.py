import random

# ==========================================
# 1. CREATING AND ACCESSING LISTS
# ==========================================
# Lists store multiple related pieces of data in a specific order.
states_of_india = ["Tamil Nadu", "Kerala", "Indore", "Karnataka", "Gujarat", "Assam", "Rajasthan", "Telangana"]

# Always remember: In programming, counting (indexing) starts at 0, not 1!
print(f"The first state in the list is: {states_of_india[0]}")

# You can fetch the very last item easily by using -1
print(f"The last state in the list is: {states_of_india[-1]}")

# ==========================================
# 2. MODIFYING LISTS
# ==========================================
# "Indore" is a city, not a state! Let's update that specific item using its index (2).
states_of_india[2] = "Madhya Pradesh"
print("\nUpdated list after fixing index 2:")
print(states_of_india)

# append() adds a SINGLE item to the very end of the list
states_of_india.append("Haryana")

# extend() adds MULTIPLE items (an entire list) to the end of an existing list
states_of_india.extend(["Uttar Pradesh", "Andhra Pradesh", "Uttarakhand", "Nagaland"])

print("\nList after appending and extending:")
print(states_of_india)

# ==========================================
# 3. LIST LENGTH & DYNAMIC ACCESS
# ==========================================
# len() fetches the total number of items in a list
length_of_list = len(states_of_india)
print(f"\nTotal number of states in our list: {length_of_list}")

# Because len() counts normally (starting at 1) but lists start at 0,
# the last item's index is ALWAYS (length - 1).
last_item = states_of_india[length_of_list - 1]
print(f"Fetching the last item using length - 1: {last_item}")

# ==========================================
# 4. NESTED LISTS (LISTS INSIDE LISTS)
# ==========================================
print("\n--- Nested Lists ---")
fruits = ["Strawberry", "Mango", "Apple", "Lemon", "Guava", "Orange"]
veggies = ["Carrot", "Beetroot", "Spinach", "Onions", "Tomato"]

# We can put lists inside a master list (often called a 2D list or matrix)
grocery_list = [fruits, veggies]

print("Full Grocery List:")
print(grocery_list)

# To access an item, use two brackets: [Which List?][Which Item?]
# [0] grabs the fruits list. [1] grabs "Mango" from that fruits list.
print(f"Fetching index [0][1]: {grocery_list[0][1]}")

# ==========================================
# 5. MINI-PROJECT: ROCK, PAPER, SCISSORS
# ==========================================
print("\n--- FINAL MINI-PROJECT ---")
print("🎮 Welcome to Rock, Paper, Scissors!")

# ASCII Art Variables
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

# Store our images in a list so we can access them via index (0, 1, 2)
game_images = [rock, scissors, paper]

# Get user input
user_move = int(input("Please enter 0 for Rock, 1 for Scissors, or 2 for Paper: "))

# IMPORTANT: We must check if the user typed a valid number BEFORE checking the list.
# If they typed 5, game_images[5] will crash the program (IndexError).
if user_move >= 3 or user_move < 0:
    print("❌ Invalid input! You typed a number outside the range. You lose!")
else:
    # If the input is valid, proceed with the game
    computer_move = random.randint(0, 2)

    print("\nYou chose:")
    print(game_images[user_move])

    print("Computer chose:")
    print(game_images[computer_move])

    # Game Logic
    # 0 (Rock) beats 1 (Scissors)
    # 1 (Scissors) beats 2 (Paper)
    # 2 (Paper) beats 0 (Rock)

    if user_move == computer_move:
        print("🤝 It's a draw!")
    elif (user_move == 0 and computer_move == 1) or \
            (user_move == 1 and computer_move == 2) or \
            (user_move == 2 and computer_move == 0):
        print("🏆 You win!")
    else:
        print("💀 You lose!")