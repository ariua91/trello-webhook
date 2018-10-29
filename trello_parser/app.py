# from trello import TrelloClient
# import json
from flask import Flask, request, redirect
from webhook_parser import *

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        test = webhook_item(request.json)
        return (str(test.save_to_db()), 200)
    else:
        abort(400)


if __name__ == '__main__':
    app.run()

# client = TrelloClient(
#     api_key = APP_KEY,
#     api_secret = TOKEN
# )
