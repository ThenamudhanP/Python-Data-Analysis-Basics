# ==========================================
# 1. IMPORTING BUILT-IN MODULES
# ==========================================
# These modules come pre-installed with Python.

import math
# The math module gives us access to mathematical functions
print("--- Math Module ---")
print(math.sqrt(16))  # Outputs: 4.0

import datetime
# The datetime module lets us work with dates and times
print("\n--- Datetime Module ---")
today = datetime.date.today()
print(f"Today's date is: {today}")

import os
# The os module allows Python to interact with your operating system (like your files and folders)
print("\n--- OS Module ---")
current_dir = os.getcwd() # Gets the Current Working Directory
print(f"My current folder path is: {current_dir}")

import json
# The json module is used to read and write JSON data (very common in web development and APIs)
print("\n--- JSON Module ---")
data = {"name": "Alice", "age": 30}
json_string = json.dumps(data) # Converts a Python dictionary into a JSON formatted string
print(f"JSON String: {json_string}")


# ==========================================
# 2. DIFFERENT WAYS TO IMPORT
# ==========================================
print("\n--- Import Patterns ---")

# Pattern 1: Import specific items only (saves memory)
from math import sqrt, pi
print(f"Using specific import: Pi is {pi} and square root of 25 is {sqrt(25)}")

# Pattern 2: Import with an alias (nickname)
# This is heavily used in Data Science to save typing time.
import pandas as pd
# Now instead of typing pandas.DataFrame(), we just type pd.DataFrame()

# Pattern 3: Import EVERYTHING (The Asterisk)
# from math import *
# Note: This is generally frowned upon by professional developers because it
# clutters your program and you might accidentally overwrite an existing variable.


# ==========================================
# 3. EXTERNAL PACKAGES & PIP
# ==========================================
"""
While Python has many built-in modules, the community has built thousands of external packages.
To use these, you must install them using your terminal/command prompt using 'pip'.

Command example: pip install requests

WHAT IS 'REQUESTS'?
The 'requests' package is used to fetch data from the internet. 
If you want to pull data from a weather API, or download a webpage's HTML, 
you use requests.get("https://website.com"). It is the bridge between Python and the web.
"""

# ==========================================
# 4. WHAT IS REQUIREMENTS.TXT?
# ==========================================
"""
Imagine you build a massive Python project using 10 different external packages (Pandas, Requests, etc.).
If you send that code to a friend, it will crash on their computer because they don't have those packages installed.

By running this command in your terminal:
> pip freeze > requirements.txt

Python automatically creates a text file listing every package you used and its exact version:
certifi==2024.2.2
charset-normalizer==3.3.2
idna==3.6
requests==2.31.0
urllib3==2.2.0

Now, your friend just runs 'pip install -r requirements.txt', and Python instantly 
downloads the exact same setup you had. It guarantees the code works identically everywhere!
"""