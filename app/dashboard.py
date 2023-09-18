from flask import Flask, request, Response ,jsonify
from app import app
import requests
from dotenv import load_dotenv
from os import environ

load_dotenv
bot_token = environ.get("bot_token")

@app.route('/', methods=['GET'])
def index():
    if request.method == 'GET':
        return "<h1>Welcome your server is running!</h1>"
    
@app.route('/', methods=['POST'])
def post_example():
    if request.method == 'POST':
        # Access POST data from the request
        msg = request.get_json()  
        print("Message: ",msg)

        # Trying to parse message
        try:
            print("There is a text")
            chat_id = msg['message']['chat']['id']
            text = msg['message']['text'] # This gets the text from the msg

            print(chat_id)
            print(text)

            if text == "are you alive?":
                print('yes i am')
            
                url = f'https://api.telegram.org/bot{bot_token}/sendMessage' # Calling the telegram API to reply the message
                
                payload = {
                    'chat_id': chat_id,
                    'text': "yes, I am alive"
                }

                r = requests.post(url, json=payload)

                if r.status_code == 200:
                    return Response('ok', status=200)
                else: 
                    return Response('Failed to send message to Telegram', status=500)
        except:
            print("No text found")

        return Response('ok', status=200)
 
if __name__ == '__main__':
   app.run(debug=True)

