import json
import os
import requests
from openai import OpenAI
from dotenv import load_dotenv # <-- Add this

# Load the secret variables from the .env file
load_dotenv() # <-- Add this

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

# ---------------------------------------------------------
# Phase 1: Define the actual Python function
# ---------------------------------------------------------
def get_weather(latitude, longitude):
    """This is a publically available API that returns the weather for a given location."""
    response = requests.get(
        f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m&hourly=temperature_2m"
    )
    data = response.json()
    return data["current"]


# ---------------------------------------------------------
# Phase 2: Define the "Tool" blueprint for the AI
# ---------------------------------------------------------
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get current temperature for provided coordinates",
            "parameters": {
                "type": "object",
                "properties": {
                    "latitude": {"type": "number"},
                    "longitude": {"type": "number"},
                },
                "required": ["latitude", "longitude"],
                "additionalProperties": False,
            },
            "strict": True,
        }
    }
]

system_prompt = "You are a helpful weather assistant."
messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": "What's the weather like in tamil nadu today?"}
]

# ---------------------------------------------------------
# Phase 3: First AI Call - The AI asks for data
# ---------------------------------------------------------
completion = client.chat.completions.create(
    model="llama-3.3-70b-versatile", # A free model great at using tools
    messages=messages,
    tools=tools,
)


# ---------------------------------------------------------
# Phase 4: Execute the function locally and send data back
# ---------------------------------------------------------
def call_function(name, args):
    if name == "get_weather":
        return get_weather(**args)


for tool_call in completion.choices[0].message.tool_calls:
    name = tool_call.function.name
    args = json.loads(tool_call.function.arguments)

    # Save the AI's request to use the tool in our message history
    messages.append(completion.choices[0].message)

    # Actually run our Python code
    result = call_function(name, args)

    # Append the raw weather data back to the conversation
    messages.append(
        {"role": "tool", "tool_call_id": tool_call.id, "content": json.dumps(result)}
    )


# ---------------------------------------------------------
# Phase 5: Final AI Call - Getting the structured answer (Groq Version)
# ---------------------------------------------------------

# 1. We manually tell the AI we want JSON
messages.append({
    "role": "system",
    "content": "Provide your final answer in JSON format with exactly two keys: 'temperature' (a float) and 'response' (a string)."
})

# 2. We use standard .create() and simple json_object mode
completion_2 = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=messages,
    response_format={"type": "json_object"},
)

# 3. We use Python's built-in json library to read the answer
final_text = completion_2.choices[0].message.content
final_data = json.loads(final_text)

print(final_data["temperature"])
print(final_data["response"])