from bs4 import BeautifulSoup
import requests
import csv


def get_html(url):
    r = requests.get(url)
    r.encoding = 'utf-8'
    return r.text


def write_csv(data):
    with open('books.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow((data['name'], data['price'], data['stock']))


def get_book(html):
    soup = BeautifulSoup(html, 'lxml')
    books = soup.find_all('article', class_="product_pod")
    for book in books:
        try:
            name = book.find('h3').find('a').get('title')
        except AttributeError:
            name = ''
        try:
            price = book.find('p', class_='price_color').text
        except AttributeError:
            price = ''
        try:
            stock = book.find('p', class_='instock availability').text.strip()
        except AttributeError:
            stock = ''
        # print(f'Title: {name}, Price: {price}, Availability: {stock}')
        data = {'name': name, 'price': price, 'stock': stock}
        write_csv(data)


def main():
    url = 'http://books.toscrape.com/'
    get_book(get_html(url))


if __name__ == '__main__':
    main()