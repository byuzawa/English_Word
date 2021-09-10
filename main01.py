import pandas as pd
import json
import random
from linebot import LineBotApi
from linebot.models import TextSendMessage

#json読み込み
file=open('info.json','r')
info=json.load(file)

#パス指定
CHANNEL_ACCESS_TOKEN=info['CHANNEL_ACCESS_TOKEN']
line_bot_api=LineBotApi(CHANNEL_ACCESS_TOKEN)

#単語帳の読み込み
df=pd.read_csv('単語帳.csv')

#ランダムで番号を取得する
num=random.randint(0,126)

def main(count):
    USER_ID="tomomisato0614"
    messages=TextSendMessage(text=df['単語'][count]+' : '+df['意味'][count])
    line_bot_api.push_message(USER_ID,messages=messages)
    
if __name__=="__main__":
    main(num)
