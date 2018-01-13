import requests
from bs4 import BeautifulSoup
import os

import telegram

bot = telegram.Bot(token='539796424:AAF3eiM8S5J2t-5QHRUk1ffZV8EIIlWMTqU')
chat_id=bot.getUpdates()[-1].message.chat.id


# 파일의 위치
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

req = requests.get('https://www.clien.net/service/board/sold')
req.encoding = 'utf-8' 

html = req.text
soup = BeautifulSoup(html, 'html.parser')
posts = soup.select('div_content > div:nth-child(10) > div.list_title > a')
latest = posts[1].text # 0번은 회원중고장터 규칙입니다.

with open(os.path.join(BASE_DIR, 'latest.txt'),'r+') as f_read:
    before = f_read.readline()
    if before != latest:
        bot.sendMessage(chat_id=chat_id, text='New posts!!')
    else:
        bot.sendMessage(chat_id=chat_id, text='No new post')

    f_read.close()

with open(os.path.join(BASE_DIR, 'latest.txt'), 'w+') as f_write:
        f_write.write(latest)
        f_write.close()
