import os
from flask import Flask, request, redirect
from webhook_parser import *

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
print(os.environ['APP_SETTINGS'])

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        test = webhook_item(request.json)
        return (str(test.save_to_db()), 200)
    else:
        abort(400)

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/<name>')
def hello_name(name):
    return 'Hello %s'%name


if __name__ == '__main__':
    app.run()

# client = TrelloClient(
#     api_key = APP_KEY,
#     api_secret = TOKEN
# )
