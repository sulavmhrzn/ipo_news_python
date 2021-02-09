try:
    import requests
    from bs4 import BeautifulSoup
    from dotenv import load_dotenv
    import yagmail
    import os
    from datetime import datetime
except ModuleNotFoundError:
    print('Required modules were not found.')
    exit()


class News:
    def __init__(self):
        self.news = list()
        # self.links = list()
        # self.cache = list()
        self.url = 'https://www.sharesansar.com/category/ipo-fpo-news'
        try:
            self.response = requests.get(self.url)
            self.soup = BeautifulSoup(self.response.text, 'html.parser')
        except Exception as e:
            print('Something went wrong:', e)
            exit()

    # TODO Memoize news
    def get_news(self):
        contents = ''
        if self.response.status_code == 200:
            headlines = self.soup.select('.newslist h4')
            for i in headlines:
                self.news.append(i.text)
            for index, news in enumerate(self.news):
                contents += f'{index+1}. {news}\n'
            return contents
            # return self.news
        return self.response.status_code

    # use this method or decorator
    def send_email(self, your_email, your_password, recepient_email):
        contents = ''
        current_date = datetime.now().strftime('%Y-%m-%d')
        subject = f"Share Market News: {current_date}"
        for index, news in enumerate(self.get_news()):
            contents += f'{index+1}. {news}\n'
        try:
            yag = yagmail.SMTP(your_email, your_password)
            yag.send(recepient_email, subject, contents)
            return "Emails were successfully sent."
        except Exception as e:
            return('Something went wrong:', e)
