from bs4 import BeautifulSoup
import requests
import csv


class Books:
    html = ''
    res = []

    def __init__(self, url, path):
        self.url = url
        self.path = path

    def get_html(self):
        r = requests.get(self.url).text
        self.html = BeautifulSoup(r, 'lxml')

    def get_books(self):
        books = self.html.find_all('div', class_="product-card__content")
        for book in books:
            try:
                name = book.find('a', class_='product-card__name').text.strip()
            except AttributeError:
                name = ''
            try:
                author = book.find('a', class_='author-list__item smartLink').text.strip()
            except AttributeError:
                author = ''
            try:
                href = book.find('div', class_='product-card__content').find('a')['href']
            except AttributeError:
                href = ''

            self.res.append({
                'name': name,
                'author': author,
                'href': href,
            })

    def write_csv(self):
        with open(self.path, 'a', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            for i in self.res:
                writer.writerow([f'Название: {i["name"]}', f'Автор: {i["author"]}', f'Ссылка: {i["href"]}'])

    def run(self):
        self.get_html()
        self.get_books()
        self.write_csv()
