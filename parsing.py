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

def get_html(url):
    r = requests.get(url)
    return r.text


def refine(st):
    return re.sub(r'\D', '', st)


def write_csv(data):
    with open('plugins.csv', 'a') as f:
        writer = csv.writer(f, lineterminator="\n")
        writer.writerow([data['name'], data['url'], data['rating']])


def get_jobs(html):
    soup = BeautifulSoup(html, 'lxml')
    p1 = soup.find_all('section', class_="plugin-section")[2]
    plg = p1.find_all('li')
    for i in plg:
        try:
            name = i.find('h3').text
        except AttributeError:
            name = ''
        url = i.find('h3').find('a').get('href')
        rating = i.find('span', class_='rating-count').text
        replace = refine(rating)

        data = {'name': name, 'url': url, 'rating': replace}
        write_csv(data)


def main():
    url = 'https://ru.wordpress.org/plugins/'
    (get_jobs(get_html(url)))


if __name__ == '__main__':
    main()
