# ==========================================
# 1. CREATING AND ACCESSING DICTIONARIES
# ==========================================
# Dictionaries store data in Key-Value pairs.
my_dictionary = {
    "wanderlust": "A deep, uncontrollable desire to travel and explore the world.",
    "serendipity": "The unexpected discovery of something wonderful purely by chance.",
    "mindstorm": "A rapid and intense burst of creative ideas or problem-solving thoughts."
}

# You can retrieve things from your dictionary using the Key
print("--- Accessing Values ---")
print(f"Wanderlust means: {my_dictionary['wanderlust']}")


# ==========================================
# 2. MODIFYING DICTIONARIES
# ==========================================
print("\n--- Modifying Dictionaries ---")

# Adding a new item to your dictionary
my_dictionary["explorer"] = "Someone who explores everywhere without the fear of new places."
print("Added 'explorer':", my_dictionary)

# Editing a value of an existing key (Done the exact same way as adding)
my_dictionary["wanderlust"] = "Wandering fearlessly."
print("Edited 'wanderlust':", my_dictionary)

# You can start with an empty dictionary if you want
empty_dictionary = {}

# You can wipe an existing dictionary by reassigning it to empty brackets
# Note: Thenamudhan, if nothing is working below this line, check if you
# accidentally wiped the dictionary! I have commented it out to be safe.
# my_dictionary = {}
# print(my_dictionary)


# ==========================================
# 3. LOOPING THROUGH A DICTIONARY
# ==========================================
print("\n--- Looping Through Dictionaries ---")
# When you loop through a dictionary, the 'for' loop iterates through the KEYS, not the values.
for key in my_dictionary:
    print(f"Key: {key}")
    print(f"Value: {my_dictionary[key]}\n")


# ==========================================
# 4. NESTED DICTIONARIES AND LISTS
# ==========================================
print("--- Nested Structures ---")
indian_states = {
    "Tamil Nadu": "Southern part of India",
    "Andhra Pradesh": "Also southern part of India"
}

# We can put lists inside a dictionary, or even dictionaries inside dictionaries!
indian_states_language = {
    "South Indian States": ["Tamil Nadu", "Kerala", "Karnataka", "Andhra Pradesh"],
    "South Indian Languages": {"Tamil Nadu": "Tamil", "Kerala": "Malayalam", "Karnataka": "Kannada"}
}

# This is how you get items from a nested list inside a dictionary
print("Fetching from nested list:")
print(indian_states_language["South Indian States"][1]) # Outputs: Kerala

# Reminder on nested lists (Lists inside Lists)
india = [["Tamil Nadu", "Telangana"], ["Gujarat", "Assam"]]
# Fetching item from a nested list
print("Fetching from nested list directly:")
print(india[1][1]) # Outputs: Assam


# ==========================================
# 5. MINI-PROJECT: TRAVEL LOG
# ==========================================
print("\n--- FINAL MINI-PROJECT: TRAVEL LOG ---")

# A highly nested dictionary containing integers, lists, and other dictionaries
travel_log = {
    "Japan": {
        "no_of_times_visited": 3,
        "cities_visited": ["Tokyo", "Kyoto"],
        "favorite_food": ["Ramen", "Sushi"]
    },
    "United_States": {
        "no_of_times_visited": 8,
        "cities_visited": ["NYC", "Los Angeles", "Texas"],
        "favorite_food": ["Hamburger", "Hot dog"]
    }
}

# Retrieving a specific item from deep inside the nest
japan_food = travel_log["Japan"]["favorite_food"][1]
print(f"My second favorite food in Japan is: {japan_food}")