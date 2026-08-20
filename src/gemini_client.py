from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

from tools import (
    get_shipment_status,
    get_top_profitable_shipments_tool,
    get_profit_by_region_tool,
    get_cancelled_shipments_tool
)


load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)


shipment_tool = types.Tool(
    function_declarations=[
        types.FunctionDeclaration(
            name="get_shipment_status",
            description="Get the delivery status and basic details of a shipment using its shipment ID.",
            parameters=types.Schema(
                type=types.Type.OBJECT,
                properties={
                    "shipment_id": types.Schema(
                        type=types.Type.STRING,
                        description="The unique shipment ID, for example S00000004."
                    )
                },
                required=["shipment_id"]
            )
        ),

        types.FunctionDeclaration(
            name="get_top_profitable_shipments_tool",
            description="Get the shipments with the highest profit.",
            parameters=types.Schema(
                type=types.Type.OBJECT,
                properties={
                    "limit": types.Schema(
                        type=types.Type.INTEGER,
                        description="The number of top profitable shipments to return."
                    )
                },
                required=["limit"]
            )
        ),

        types.FunctionDeclaration(
            name="get_profit_by_region_tool",
            description="Get the total profit for each region.",
            parameters=types.Schema(
                type=types.Type.OBJECT,
                properties={}
            )
        ),

        types.FunctionDeclaration(
            name="get_cancelled_shipments_tool",
            description="Get cancelled shipments. Returns the total number of cancelled shipments and a limited list of shipment records.",
            parameters=types.Schema(
                type=types.Type.OBJECT,
                properties={
                    "limit": types.Schema(
                        type=types.Type.INTEGER,
                        description="Maximum number of cancelled shipment records to return. Must be between 1 and 20."
                    )
                }
            )
        )
    ]
)    



chat = client.chats.create(
    model="gemini-2.5-flash",
    config=types.GenerateContentConfig(
        tools=[shipment_tool
            ]
    )
)

user_message = input("Ask about a shipment: ")

response = chat.send_message(
    user_message
)

for part in response.candidates[0].content.parts:

    if part.function_call:

        function_call = part.function_call

        print("Function requested:", function_call.name)
        print("Arguments:", function_call.args)

        try:

            if function_call.name == "get_shipment_status":

                result = get_shipment_status(
                    function_call.args["shipment_id"]
                )

            elif function_call.name == "get_top_profitable_shipments_tool":

                result = get_top_profitable_shipments_tool(
                    function_call.args["limit"]
                )

            elif function_call.name == "get_profit_by_region_tool":

                result = get_profit_by_region_tool()

            elif function_call.name == "get_cancelled_shipments_tool":

                result = get_cancelled_shipments_tool(
                    function_call.args.get("limit", 10)
                )

            else:

                result = {
                    "success": False,
                    "error": f"Unknown function: {function_call.name}"
                }

        except Exception as e:

            result = {
                "success": False,
                "error": "An unexpected error occurred while executing the tool."
            }

            print("Tool error:", e)
            
            # Send the function result back to Gemini
        response = chat.send_message(
            types.Part(
                function_response=types.FunctionResponse(
                    name=function_call.name,
                    response=result
                )
            )
        )

        print("\nGemini:", response.text)