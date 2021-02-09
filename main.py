from utils.news import News
from utils.decorator import send_email
from dotenv import load_dotenv
import os

load_dotenv()


email = os.getenv('EMAIL')
password = os.getenv('PASSWORD')

news = News()


@send_email(email, password, 'sulav291@gmail.com')
def mail():
    return news.get_news()


mail()
