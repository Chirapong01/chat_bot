import requests
import openai
import os

from flask import Flask, request
from dotenv import load_dotenv,find_dotenv

load_dotenv(find_dotenv())

app = Flask(__name__)

openai.api_key = os.getenv('OPENAI_API_KEY')
# openai.api_key = "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"
token = "EAANtA2sHmvQBO1ntRBwOuaxTalnwYtyxTuj18E52zmCyQtjjgSudwpHhqElU1bNRBVu3GeTuT9p3Ty1SKL9ss89DiZBeNZCETT4Ti3N5ZBZArV60xCDfNG8jykeMj4uSu21jq3zUiCUFpqZCBiBEtrA59j2eEANVtpg8UCwjMtHmwtlZAtC4z6IojBFKuIvlK2AcUZD"
API = "https://graph.facebook.com/v17.0/me/messages?access_token=" + token
VERIFY_TOKEN = "pass1234"

# @app.route("/", methods=["GET"])
# def fbverify():
#     if not request.args.get("hub.verify_token") == VERIFY_TOKEN:
#         return "Verification token missmatch"
#     return request.args["hub.challenge"]




# @app.route("/", methods=['POST'])
# def fbwebhook():
#     data = request.get_json()
#     print(data)
#     try:
#         if data['entry'][0]['messaging'][0]['sender']['id']:
#             message = data['entry'][0]['messaging'][0]['message']
#             sender_id = data['entry'][0]['messaging'][0]['sender']['id']
#             chat_gpt_input=message['text']
#             print(chat_gpt_input)
#             completion = openai.ChatCompletion.create(
#                             max_tokens = 1024,
#                             model="gpt-3.5-turbo",
#                             messages=[{"role": "user", "content": chat_gpt_input}]) 
#             response_msg = completion['choices'][0]['message']['content']    
#             request_body = {
#                 "recipient": {
#                     "id": sender_id
#                 },
#                 "message": {
#                     "text": response_msg
#                 }
#             }
#             print('messenger: ',response_msg)     
#             headers = {"Content-Type": "application/json"}
#             response = requests.post(API, json=request_body,headers=headers).json()
#             return response
#     except Exception as e:
#         print(e)
#     return '200 OK HTTPS.'

@app.route("/", methods=['POST'])
def fbwebhook():
    print(request)
    data = request.get_json()
    print('data is: ',data)
    try:
        # Read messages from facebook messanger.
        message = data['entry'][0]['messaging'][0]['message']
        sender_id = data['entry'][0]['messaging'][0]['sender']['id']
        if message['text'] == "hi":
            print()
            request_body = {
                "recipient": {
                    "id": sender_id
                },
                "message": {
                    "text": "hello, world!"
                }
            }
            headers = {"Content-Type": "application/json"}
            print('body is: ' ,request_body)
            response = requests.post(API, json=request_body,headers=headers).json()
            print('respond is:' , response)
            return response
    except Exception as e:
        print(e)
    return '200 OK HTTPS.'

if __name__ == "__main__":
    app.run(port=5500)
