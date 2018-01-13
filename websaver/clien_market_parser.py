
import requests
from bs4 import BeautifulSoup
import os
import time
import telegram

bot = telegram.Bot(token='539796424:AAF3eiM8S5J2t-5QHRUk1ffZV8EIIlWMTqU')

chat_id = bot.getUpdates()[-1].message.chat.id

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

while True:
    req = requests.get('https://clien.net/service/board/sold')
    req.encoding = 'utf-8'

    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    posts = soup.select('a.list_subject')
    latest = posts[3].text

    with open(os.path.join(BASE_DIR, 'latest.txt'), 'r+') as f_read:
        before = f_read.readline()
        if before != latest:
            bot.sendMessage(chat_id=chat_id, text='New Post !! ')
        else:
            bot.sendMessage(chat_id=chat_id, text='No Post!! ')
        f_read.close()

    with open(os.path.join(BASE_DIR, 'latest.txt'), 'w+') as f_write:
        f_write.write(latest)
        f_write.close()

    time.sleep(60)
