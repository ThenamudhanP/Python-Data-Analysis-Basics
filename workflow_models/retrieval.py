import json
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load the secret variables from the .env file
load_dotenv()

# 1. Point the client to Groq
client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)


# ---------------------------------------------------------
# Phase 1: Define the Tool (Local Function & AI Blueprint)
# ---------------------------------------------------------
def search_kb(question: str):
    """Load the whole knowledge base from the JSON file."""
    with open("kb.json", "r") as f:
        return json.load(f)


tools = [
    {
        "type": "function",
        "function": {
            "name": "search_kb",
            "description": "Get the answer to the user's question from the knowledge base",
            "parameters": {
                "type": "object",
                "properties": {
                    "question": {"type": "string"},
                },
                "required": ["question"],
                "additionalProperties": False,
            },
            "strict": True,
        }
    }
]

# ---------------------------------------------------------
# Phase 2: First AI Call - Asking a relevant question
# ---------------------------------------------------------
system_prompt = "You are a helpful assistant that answers questions based on the provided knowledge base."

messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": "What and all services does the infoziant company offers"},
]

completion = client.chat.completions.create(
    model="llama-3.3-70b-versatile",  # 2. Use Groq's model
    messages=messages,
    tools=tools,
)


# ---------------------------------------------------------
# Phase 3: Execute the function locally
# ---------------------------------------------------------
def call_function(name, args):
    if name == "search_kb":
        return search_kb(**args)


for tool_call in completion.choices[0].message.tool_calls:
    name = tool_call.function.name
    args = json.loads(tool_call.function.arguments)

    # Save the AI's tool request to history
    messages.append(completion.choices[0].message)

    # Run the Python function to read kb.json
    result = call_function(name, args)

    # Give the file contents back to the AI
    messages.append(
        {"role": "tool", "tool_call_id": tool_call.id, "content": json.dumps(result)}
    )

# ---------------------------------------------------------
# Phase 4: Second AI Call - Getting a structured answer (Groq Version)
# ---------------------------------------------------------
# 3. Manually ask for JSON format instead of using Pydantic
messages.append({
    "role": "system",
    "content": "Provide your final answer in JSON format with exactly two keys: 'answer' (a string) and 'source_id' (an integer representing the record ID of the answer)."
})

completion_2 = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=messages,
    response_format={"type": "json_object"}  # Force JSON mode
)

final_text = completion_2.choices[0].message.content
final_data = json.loads(final_text)

print(f"Answer: {final_data.get('answer')}")
print(f"Source ID: {final_data.get('source_id')}")

# ---------------------------------------------------------
# Phase 5: Question that doesn't trigger the tool
# ---------------------------------------------------------
print("\n--- Testing unrelated question ---")
messages_unrelated = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": "What is the weather in Tokyo?"},
]

completion_3 = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=messages_unrelated
)

print(completion_3.choices[0].message.content)