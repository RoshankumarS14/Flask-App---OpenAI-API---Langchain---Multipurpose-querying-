from flask import Flask, request
import os
from flask_cors import CORS
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
import json
from airtable import Airtable

app = Flask(__name__)
CORS(app)
API_KEY = os.getenv("OPENAI_API_KEY")

chat = ChatOpenAI(model="gpt-4-0125-preview", temperature=0.2, openai_api_key=API_KEY)

base_key = 'appDeLA2xgfphKya3'
table_name = 'Prompts'
airtable_api_key = os.getenv("AIRTABLE_API_KEY")
airtable1 = Airtable(base_key, table_name, airtable_api_key)

prompts_data = {i["fields"]["Title"]:i["fields"]["Prompt Instructions"] for i in airtable1.get_all()}

@app.route('/gpt', methods=['GET'])
def get_response():
    parameters = {
        'prompt': request.args.get('prompt'),
        'category': request.args.get('category')
    }
    response = chat.invoke(
    [
        HumanMessage(
            content=prompts_data[parameters["category"]]+parameters["prompt"]
        )
    ]
    )
    response = json.loads(response.json())
    return {"response":response["content"]}

if __name__ == '__main__':
    app.run(debug=True)
