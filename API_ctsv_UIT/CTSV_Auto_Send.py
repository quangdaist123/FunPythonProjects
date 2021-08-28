# Avoid import error when running the the terminal
# Add module paths outside of the current folder
import sys
sys.path.append(r"C:\\Users\quang\PycharmProjects\pythonProject3")
from emailsender import EmailSender
from API_ctsv_UIT.ctsv_api import CTSV_API
from datetime import datetime
import time

bot = CTSV_API()

if bot.hasNewArticle():
    new_articles = bot.getLatestArticle()
    EmailSender().make_message(subject="[CSTV] Thông báo mới", plain_text=new_articles).send_message()
