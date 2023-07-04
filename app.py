from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)


ALLOW_HOST = {
    'https://d937-2401-e180-8851-bb27-5d53-bc26-204c-9c84.ngrok-free.app'
}

# Channel Access Token
line_bot_api = LineBotApi('0pJNfFni77KaR1UFW39QD71g7Vk0IqUY6t5lSwTgDjEN1B+U38qz+hhOTBrOjjV+aolJMzDr2LETjGUtuRfiUM7+2vclI+F9ncWFPopH5YrxXUTAfKWHD3oks5/3PWHe8IGH6Sd4VC8ZP4x2BEKvgAdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('7ff547e35ea053e575357a78319cd9c6')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if event.message.text == "hello":
        message = TextSendMessage(text='hello')
        line_bot_api.reply_message(event.reply_token, message)
    else:
        message = TextSendMessage(text='hello')
        line_bot_api.reply_message(event.reply_token, message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
