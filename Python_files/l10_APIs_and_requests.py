import requests

# ==========================================
# 1. WHAT IS AN API?
# ==========================================
"""
API stands for Application Programming Interface. 
Think of an API like a waiter at a restaurant:
1. You look at the menu and tell the waiter what you want (Sending a Request).
2. The waiter takes your order to the kitchen (The API processes the request).
3. The kitchen prepares the food, and the waiter brings it back to you (Receiving JSON Data).

How it works in code:
1. Connect to an API's URL with parameters (like coordinates).
2. Send the request.
3. Get JSON data back.
4. Extract the specific parts you need to use in your code.
"""

# ==========================================
# 2. YOUR FIRST API CALL (Erode Weather)
# ==========================================
print("--- Fetching Weather for Erode ---")

# We need coordinates to get weather data. Here are the coordinates for Erode:
latitude = 11.3410
longitude = 77.7172

# Build the API URL with our parameters using an f-string
# (Note: We add '&current=temperature_2m' to tell the API exactly what data we want)
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"

# Make the request to the server
response = requests.get(url)

# Convert the response into a JSON dictionary so Python can read it
data = response.json()

# As requested, extracting the exact temperature from the JSON and storing it in a variable
temperature = data['current']['temperature_2m']

print(f"The current temperature in Erode is: {temperature}°C\n")

# ==========================================
# 3. CREATING A REUSABLE API FUNCTION
# ==========================================
print("--- Using a Function for Multiple Cities ---")


# Instead of rewriting the URL every time, we put it inside a function!
def get_weather(lat, lon):
    # Notice we use the parameters 'lat' and 'lon' inside the f-string now
    api_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m"
    res = requests.get(api_url)
    weather_data = res.json()

    # Return JUST the temperature value back to the user
    return weather_data['current']['temperature_2m']


# Get temperature for different cities worldwide using our new function
paris_temp = get_weather(48.85, 2.35)
london_temp = get_weather(51.50, -0.12)
tokyo_temp = get_weather(35.68, 139.69)
erode_temp = get_weather(11.3410, 77.7172)  # Added your hometown to the list!

# Print the final results
print(f"Paris: {paris_temp}°C")
print(f"London: {london_temp}°C")
print(f"Tokyo: {tokyo_temp}°C")
print(f"Erode: {erode_temp}°C")