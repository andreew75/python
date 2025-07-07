from homework_0707 import Books


def main():
    for i in range(1, 43):
        pars = Books(f'https://book24.ru/novie-knigi/page-{i}', 'books.csv')
        pars.run()
        pars.res = []


if __name__ == '__main__':
    main()