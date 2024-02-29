# --------------------------------------------------------------
# Import Modules
# --------------------------------------------------------------

import os
import json
import openai
from datetime import datetime, timedelta
# from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, AIMessage, ChatMessage


# --------------------------------------------------------------
# Load OpenAI API Token From the .env File
# --------------------------------------------------------------

openai.api_key = "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"


# --------------------------------------------------------------
# Ask ChatGPT a Question
# --------------------------------------------------------------

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo-0613",
    messages=[
        {
            "role": "user",
            "content": "When's the next flight from Amsterdam to New York?",
        },
    ],
)

output = completion.choices[0].message.content
print(output)

# --------------------------------------------------------------
# Use OpenAI’s Function Calling Feature
# --------------------------------------------------------------

function_descriptions = [
    {
        "name": "get_flight_info",
        "description": "Get flight information between two locations",
        "parameters": {
            "type": "object",
            "properties": {
                "loc_origin": {
                    "type": "string",
                    "description": "The departure airport, e.g. DUS",
                },
                "loc_destination": {
                    "type": "string",
                    "description": "The destination airport, e.g. HAM",
                },
            },
            "required": ["loc_origin", "loc_destination"],
        },
    }
]

user_prompt = "Find flight amsertdam to newyork"

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo-0613",
    messages=[{"role": "user", "content": user_prompt}],
    # Add function calling
    functions=function_descriptions,
    function_call="auto",  # specify the function call
)

# It automatically fills the arguments with correct info based on the prompt
# Note: the function does not exist yet

output = completion.choices[0].message
print(output)

# --------------------------------------------------------------
# Add a Function
# --------------------------------------------------------------


def get_flight_info(loc_origin, loc_destination):
    """Get flight information between two locations."""

    print('HAHA HAHA HAHA HAHA HAHAHAHAHAHAHAHAHHA')
    # Example output returned from an API or database
    flight_info = {
        "loc_origin": loc_origin,
        "loc_destination": loc_destination,
        "datetime": str(datetime.now() + timedelta(hours=2)),
        "airline": "KLM",
        "flight": "KL643",
    }

    return json.dumps(flight_info)


# Use the LLM output to manually call the function
# The json.loads function converts the string to a Python object

origin = json.loads(output.function_call.arguments).get("loc_origin")
destination = json.loads(output.function_call.arguments).get("loc_destination")
params = json.loads(output.function_call.arguments)
type(params)

print(origin)
print(destination)
print(params)

# Call the function with arguments

chosen_function = eval(output.function_call.name)
flight = chosen_function(**params)

print('-------> ' +
      flight)
