from bs4 import BeautifulSoup
import requests
import re
import csv

# def get_copywriter(tag):
#     whois = tag.find('div', class_='whois').text
#     if whois == "Copywriter":
#         return tag
#     return None
# def get_salary(st):
#     pattern = r'\d+'
#     res = re.findall(pattern, st)[0]
#     print(res)


# f = open("index.html").read()
# soup = BeautifulSoup(f, 'html.parser')
# row = soup.find_all('div', class_='row')[2].find('div', class_='name').text
# print(row)
# row = soup.find('div', string="Alena").parent
# row = soup.find('div', string="Alena").find_parent('div', class_='row')
# row = soup.find('div', id="whois3").find_next_sibling()
# print(row)
# copywriter = []
# row = soup.find_all('div', class_='row')
# for i in row:
#     cw = get_copywriter(i)
#     if cw:
#         copywriter.append(cw)
# print(copywriter)

# salary = soup.find_all('div', {'data-set': 'salary'})
#
# for i in salary:
#     get_salary(i.text)

# r = requests.get('https://ru.wordpress.org/')
# # print(r.content)
# print(r.text)

# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# def get_jobs(html):
#     soup = BeautifulSoup(html, 'lxml')
#     p1 = soup.find('h1').text
#     return p1
#
#
# def main():
#     url = 'https://ru.wordpress.org/'
#     print(get_jobs(get_html(url)))
#
#
# if __name__ == '__main__':
#     main()

# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# def write_csv(data):
#     with open('popular.csv', 'a') as f:
#         writer = csv.writer(f, lineterminator='\n')
#         writer.writerow((data['name'], data['url'], data['active'], data['test']))
#
#
# def refine_html(st):
#     return st.split()[-1]
#
#
# def get_jobs(html):
#     soup = BeautifulSoup(html, 'lxml')
#     p1 = soup.find_all('li', class_="wp-block-post")
#     for el in p1:
#         name = el.find('h3', class_="entry-title").text
#         url = el.find('h3', class_="entry-title").find('a')['href']
#         active = el.find('span', class_="active-installs").text.strip()
#         try:
#             tested = el.find('span', class_="tested-with").text.strip()
#             test = refine_html(tested)
#         except AttributeError:
#             test = ''
#         data = {
#             'name': name,
#             'url': url,
#             'active': active,
#             'test': test
#         }
#         write_csv(data)
#
#
# def main():
#     for i in range(2, 50):
#         url = 'https://ru.wordpress.org/plugins/browse/popular/page/' + str(i) + '/'
#         (get_jobs(get_html(url)))
#
#
# if __name__ == '__main__':
#     main()

from parsers import Parser


def main():
    pars = Parser('https://www.ixbt.com/live/index/news/', 'news.txt')
    pars.run()


if __name__ == '__main__':
    main()