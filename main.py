from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

import json

app = Flask(__name__)




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
    #change
    # event.message.text : user input
                    #event.message.text == "1" or "1.food" or "food" :
                #message = TextSendMessage(text='hello')
                #line_bot_api.reply_message(event.reply_token, message)
    #event.message.text =="hello" or event.message.text == "hello " or event.message.text =="Hello" :
    #message = TextSendMessage(text='Hello,what can I help you? \n Please enter the number of the list below \n 1.food \n 2.transportation \n 3.cloth \n 4.living \n 5.exit \n ')
    #line_bot_api.reply_message(event.reply_token, message)

    k =1
    while k !=0:
        message = eval (TextSendMessage(text='Hello,what can I help you? \n Please enter the number of the list below \n 1.food \n 2.transportation \n 3.cloth \n 4.living \n 5.exit \n '))
        line_bot_api.reply_message(event.reply_token, message)
        k == message 
        if k==1 :
#food
            message = TextSendMessage(text='we are in 1')
            line_bot_api.reply_message(event.reply_token, message)
        if k==2 :
#transportation
            message = TextSendMessage(text='we are in 2')
            line_bot_api.reply_message(event.reply_token, message)
        elif k==3 :
#cloth
            message = TextSendMessage(text='we are in 3')
            line_bot_api.reply_message(event.reply_token, message)
        elif k==4 :
#living
            message = TextSendMessage(text='we are in 4')
            line_bot_api.reply_message(event.reply_token, message)
        elif k==5 :
#log out
            message = TextSendMessage(text='Thanks, see you next time~')
            line_bot_api.reply_message(event.reply_token, message)
        else:
            message = TextSendMessage(text='error, please try again')
            line_bot_api.reply_message(event.reply_token, message)
                

    else:
        message = TextSendMessage(text='you are so ugly')
        line_bot_api.reply_message(event.reply_token, message)
                
        #card = json.load(open('card.json','r',encoding='utf-8'))
        #message = FlexSendMessage('profile',card)
        #line_bot_api.reply_message(event.reply_token, message)
#

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
