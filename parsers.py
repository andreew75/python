from bs4 import BeautifulSoup
import requests


class Parser:
    html = ''
    res = []

    def __init__(self, url, path):
        self.url = url
        self.path = path

    def get_html(self):
        req = requests.get(self.url).text
        self.html = BeautifulSoup(req, 'lxml')

    def parsing(self):
        news = self.html.find_all('div', class_='caption')
        for i in news:
            title = i.find('h3', class_='topic-title').text
            href = i.find('h3', class_='topic-title').find('a')['href']
            author = i.find('a', class_='topic-info-author-link').text.strip()
            self.res.append({
                'title': title,
                'href': href,
                'author': author
            })
        # print(self.res)

    def save(self):
        with open(self.path, 'w') as file:
            i = 1
        for i in self.res:
            file.write(f'Новость:{i}\nНазвание: {i["title"]}\nСсылка: {i["href"]}\n')
            i += 1

    def run(self):
        self.get_html()
        self.parsing()
        self.save()
