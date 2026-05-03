# ==========================================
# FINAL PROJECT: WEATHER DATA ANALYSIS
# ==========================================
import requests
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import os

print("🌍 Fetching weather data...")

# ==========================================
# STEP 1: CALCULATE DATES
# ==========================================
# Get today's date and the date exactly 7 days ago
today = datetime.now()
week_ago = today - timedelta(days=7)

# Format dates for the API (YYYY-MM-DD)
start_date = week_ago.strftime("%Y-%m-%d")
end_date = today.strftime("%Y-%m-%d")

# ==========================================
# STEP 2: FETCH DATA FROM API
# ==========================================
# We are using Paris coordinates (48.85, 2.35) just like the tutorial.
# The URL asks for the max and min temperatures for our specific date range.
url = f"https://api.open-meteo.com/v1/forecast?latitude=48.85&longitude=2.35&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min&timezone=auto"

response = requests.get(url)
data = response.json()

# ==========================================
# STEP 3: CLEAN DATA WITH PANDAS
# ==========================================
print("📊 Processing data with Pandas...")

# Extract just the 'daily' portion of the JSON data
daily_data = data['daily']

# Create a Pandas DataFrame (a structured table, like Excel)
df = pd.DataFrame({
    'date': daily_data['time'],
    'max_temp': daily_data['temperature_2m_max'],
    'min_temp': daily_data['temperature_2m_min']
})

# Convert the raw date strings into actual datetime objects so Matplotlib can read them properly
df['date'] = pd.to_datetime(df['date'])

# Print the table to the console so we can verify it looks correct
print("\n--- Processed DataFrame ---")
print(df)

# ==========================================
# STEP 4: VISUALIZE WITH MATPLOTLIB
# ==========================================
print("\n📈 Generating weather chart...")

# Create the plot canvas (10 inches wide, 6 inches tall)
plt.figure(figsize=(10, 6))

# Plot the Max and Min temperatures on the graph
# marker='o' puts a little dot on each specific day
plt.plot(df['date'], df['max_temp'], marker='o', label='Max Temp')
plt.plot(df['date'], df['min_temp'], marker='o', label='Min Temp')

# Add labels and a title to make it professional
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.title('Paris Weather - Past 7 Days')
plt.legend() # Shows the key (which line is Max and which is Min)

# Rotate the x-axis date labels by 45 degrees so they don't overlap
plt.xticks(rotation=45)
plt.tight_layout() # Ensures everything fits perfectly inside the image frame

# Save the plot as an image file in your folder, then display it on screen
plt.savefig('weather_chart.png')
print("✅ Chart saved as 'weather_chart.png'. Close the image window to finish the program.")
plt.show()

# ==========================================
# STEP 5: SAVE DATA TO CSV
# ==========================================
# Create 'data' folder if it doesn't exist
if not os.path.exists('data'):
    os.makedirs('data')

# Save the Pandas DataFrame to a CSV file
# index=False prevents pandas from writing row numbers into the file
df.to_csv('data/paris_weather.csv', index=False)
print("✅ Data saved to data/paris_weather.csv")