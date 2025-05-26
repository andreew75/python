# guest = ['Anton', 'Robert', 'Ivan']
# print(guest)
#
# print("I invite you to the party,", guest[0])
# print("I invite you to the party,", guest[1])
# print("I invite you to the party,", guest[2])
#
# guest[0] = 'Boris'
# print(guest)
# print()
# print('I bought a big table')
#
# guest.insert(0, 'Karl')
# guest.insert(2, 'Victor')
# guest.append('Alex')
#
# print(guest)
#
# guest.pop()
# guest.pop()
# guest.pop()
# guest.pop()
#
# print(guest)
#
# guest.clear()
# print(guest)
from OPP import users
# guests = ['Anton', 'Robert', 'Ivan', 'Petr']
# for guest in guests:
#     print(f"Hi, {guest}!")

# fruits = ['apple', 'banana', 'mango', 'cherry']
# for fruit in fruits:
#     print(fruit)

# numbers = [i ** 3 for i in range(1, 11)]
#
# print(numbers)


# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# players_2 = players[:]
# players_2.append('kay')
# print(players_2)

# my_foods = ['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']
# # print('Первые три пункта в списке — это: ', my_foods[:3])
# # print('Средние три пункта в списке — это: ', my_foods[1:4])
# # print('Последние три пункта в списке — это: ', my_foods[-3:])
# # for food in my_foods:
# #     print(food)
# my_foods.insert(1, 'apple')
# print(my_foods)
# my_foods.append('apple')
# print(my_foods)
# for food in my_foods:
#     my_foods.remove('apple')
#     print(my_foods)

# users = ['red', 'green', 'Admin', 'black', 'white']
# for name in users:
#     if users:
#         print('Нам нужно добавить несколько пользователей')
#     if name.lower() == 'admin':
#         print('Здравствуйте, admin, хотите просмотреть отчет о состоянии дел?')
#     elif name.lower() != 'admin':
#         print(f'Привет,{name}! Спасибо, что авторизовался в системе')
#     else:
#         print('Нам нужно добавить несколько пользователей')


# def goals(*args):
#     return sum(args)
#
#
# print(goals(5, 10, 2))


# def sum_mix(arr):
#     return sum(map(int, arr))
#
#
# print(sum_mix(['5', '0', 9, 3, 2, 1, '9', 6, 7]))

# def get_age(age):
#     parts = age.split()
#     return int(parts[0]) if parts and parts[0].isdigit() else None
#
#
# print(get_age(9))
#
#
# # s = 7
# # # s.split()
# # print(s, "years old")


# def number_to_string(num):
#     return str(num)
#
#
# print(number_to_string(12))

# list_0 = {}
#
# list_0["green"] = 88
# list_0["green"] = 12
#
# del list_0["green"]
#
#
# list_0 = {
#     'lord': 'python',
#     'mary': 'c++',
#     'dora': 'java',
#     'moris': 'java',
#
# }
#
# for lang in set(list_0.values()):
#     print(f"{lang}")
#
# list_1 = []
#
# for lst in range(10):
#     new_list = {'red': 12, 'blue': 133}
#     list_1.append(new_list)
# print(list_1[:3])

# prompt = "If you share your name, we can personalize the messages you see."
# prompt += "\nWhat is your first name? "
# name = input(prompt)
# print(f"\nHello, {name}!")

# current_number = 1
# while current_number <= 5:
#     print(current_number)
#     current_number += 1

# responses = {}
# polling_active = True
# while polling_active:
#     name = input("\nWhat is your name? ")
#     response = input("Which mountain would you like to climb someday? ")
#     repeat = input("Would you like to let another person respond? (yes/ no) ")
#     if repeat == 'no':
#         polling_active = False
#         print("\n--- Poll Results ---")
#     for name, response in responses.items():
#         print(f"{name} would like to climb {response}.")


# class Rectangle:
#     def __init__(self, width, height):
#         """Инициализирует прямоугольник с заданной шириной и высотой."""
#         self.width = width
#         self.height = height
#
#     def area(self) -> float:
#         return self.width * self.height
#
#     def perimeter(self):
#         return 2 * (self.width + self.height)
#
#     def is_square(self) -> bool:
#         return self.width == self.height
#
#     def print_info(self):
#         return (
#             f"Площадь прямоугольника: {self.area()} \n"
#             f"Периметр прямоугольника: {self.perimeter()}\n"
#             f"Это квадрат? {self.is_square()}\n"
#         )
#
#
# rectangle1 = Rectangle(5, 10)
# print(rectangle1.print_info())

# class Contact:
#     def __init__(self, first_name, last_name, phone, email):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.phone = phone
#         self.email = email
#
#     def get_full_name(self):
#         return f"{self.first_name} {self.last_name}"
#
#     def __str__(self):
#         return f"Имя: {self.first_name}, Фамилия: {self.last_name}, Телефон: {self.phone}, Email: {self.email}"
#
#
# class ContactList:
#     def __init__(self):
#         self.contacts = []
#
#     def add_contact(self, contact):
#         self.contacts.append(contact)
#
#     def remove_contact(self, phone_number):
#         for contact in self.contacts:
#             if contact.phone == phone_number:
#                 self.contacts.remove(contact)
#                 return
#         raise ValueError()
#
#     def search_contact(self, search_term):
#         results = []
#         for contact in self.contacts:
#             if (search_term.lower() in contact.first_name.lower() or
#                     search_term.lower() in contact.last_name.lower() or
#                     search_term in contact.phone or
#                     search_term.lower() in contact.email.lower()):
#                 results.append(contact)
#         return results
#
#     def display_contacts(self):
#         for contact in self.contacts:
#             print(contact)
#
#
# c1 = Contact("Зайцев", "Владимир", 9215110012, "asbest@gamil.com")
# c2 = Contact("Волков", "Сергей", 9515113011, "asbest2@gamil.com")
#
#
# contact_list = ContactList()
# contact_list.add_contact(c1)
# contact_list.add_contact(c2)
#
# print("Все контакты:")
# contact_list.display_contacts()


# class Book:
#     def __init__(self, book_id, title, author, isbn, publication_year):
#         self.book_id = book_id
#         self.title = title
#         self.author = author
#         self.isbn = isbn
#         self.publication_year = publication_year
#
#     def __str__(self):
#         return (
#             f"ID: {self.book_id}\n"
#             f"Название: {self.title}\n"
#             f"Автор: {self.author}\n"
#             f"ISBN: {self.isbn}\n"
#             f"Год издания: {self.publication_year}"
#         )
#
#
# class Library:
#     def __init__(self):
#         self.books = {}
#
#     def add_book(self, book: Book) -> None:
#         """Добавляем книги в библиотеку"""
#         self.books[book.book_id] = book
#
#     def remove_book(self, book_id):
#         """Удаляем книги из библиотеки"""
#         if book_id in self.books:
#             del self.books[book_id]
#         else:
#             raise ValueError("Такой книги нет в списке")
#
#     def search_book(self, search_term) -> list:
#         """Ищем книги в библиотеке"""
#         results = []
#         for book_id in self.books:
#             book = self.books[book_id]
#             if (search_term.lower() in book.title.lower() or
#                     search_term.lower() in book.author.lower() or
#                     search_term in book.isbn):
#                 results.append(book)
#         return results
#
#     def display_books(self):
#         """Выводим информацию обо всех книгах в библиотеке"""
#         if not self.books:
#             print("В библиотеке нет книг.")
#             return
#         for book_id in self.books:
#             book = self.books[book_id]
#             print(book)
#             print("+" * 20)
#
#
# b1 = Book(3452, "Камера Обскура", "Владимир Набоков", "5", 1995)
# b2 = Book(1275, "Белая гвардия", "Михаил Булгаков", "5", 2021)
#
# library = Library()
# library.add_book(b1)
# library.add_book(b2)
#
#
# library.remove_book(1275)
# library.display_books()

# class Task:
#     def __init__(self, task_id, description, due_date, priority, completed):
#         self.task_id = task_id
#         self.description = description
#         self.due_date = due_date
#         self.priority = priority
#         self.completed = completed
#
#     def mark_completed(self):
#         self.completed = True
#
#     def __str__(self):
#         return (
#             f"ID: {self.task_id}\n"
#             f"Описание: {self.description}\n"
#             f"Срок: {self.due_date}\n"
#             f"Приоритет: {self.priority}\n"
#         )
#
#
# class TaskList:
#     def __init__(self):
#         self.tasks = []
#
#     def add_task(self, task) -> None:
#         self.tasks.append(task)
#
#     def remove_task(self, task_id):
#         for task in self.tasks:
#             if task.task_id == task_id:
#                 self.tasks.remove(task)
#                 return
#         raise ValueError("Такой задачи нет")
#
#     def mark_task_completed(self, task_id):
#         for task in self.tasks:
#             if task.task_id == task_id:
#                 task.mark_completed()
#                 return
#         raise ValueError("Такой задачи нет")
#
#     def get_pending_tasks(self):
#         results_false = []
#         for task in self.tasks:
#             if not task.completed:
#                 results_false.append(task)
#         return results_false
#
#     def get_completed_tasks(self):
#         results_true = []
#         for task in self.tasks:
#             if task.completed:
#                 results_true.append(task)
#         return results_true
#
#     def get_tasks_by_priority(self, priority):
#         results = []
#         for task in self.tasks:
#             if task.priority == priority:
#                 results.append(task)
#         return results
#
#     def display_tasks(self):
#         for task in self.tasks:
#             print(task)
#
#
# t1 = Task(4328, "Включить чайник", "10-11-2024",
#           "Medium", True)
# t2 = Task(9865, "Забрать книгу", "11-11-2024",
#           "High", False)
#
# task_list = TaskList()
# task_list.add_task(t1)
# task_list.add_task(t2)
#
# task_list.mark_task_completed(4328)
# task_list.display_tasks()
# task_list.remove_task(3)


# def check_prices(prices):
#     correct_prices = []
#     # user_input = input("Введите цены через запятую: ")
#     items = prices.split(',')
#     for item in items:
#         item = item.strip()
#         try:
#             price = float(item)
#             if price < 0:
#                 raise ValueError(f"Цена не может быть отрицательной: {price}")
#         except (ValueError, TypeError) as e:
#             print(f"Ошибка: {e}")
#         else:
#             correct_prices.append(item)
#             print(f"Добавлена цена: {item}")
#
#     print(correct_prices)
#
#
# check_prices(input("Введите цены через запятую: "))


# def check_prices():
#     while True:
#         prices = input("Введите цены через запятую: ")
#         valid_prices = []
#         errors = []
#         items = prices.split(',')
#         for item in items:
#             item = item.strip()
#             try:
#                 price = float(item)
#                 if price < 0:
#                     raise ValueError(f"Цена не может быть отрицательной: {price}")
#             except (ValueError, TypeError) as e:
#                 errors.append(str(e))
#             else:
#                 valid_prices.append(price)
#
#         if errors:
#             for error in errors:
#                 print(f"Ошибка: {error}")
#             print("Попробуйте снова.\n")
#             continue
#         else:
#             print("Все цены корректны.")
#             print(f"Список: {valid_prices}")
#             break
#
#
# check_prices()


# file = ["1\n", "2\n", "3\n"]
#
# with open("input.txt", "w") as f:
#     f.writelines(file)
#
# with open("input.txt", "r") as f:
#     lines = f.readlines()
#     numbers = [int(line.strip()) for line in lines]
#
# result = sum(numbers)
#
# with open("output.txt", "w") as f:
#     f.write(str(result))

# file = ["1\n", "word\n", "2\n", " \n", "3\n", "\n"]
#
# with open("mixed_input.txt", "w") as f:
#     f.writelines(file)
#
# with open("mixed_input.txt", "r") as f:
#     lines = f.readlines()
#     result = []
#     for line in lines:
#         try:
#             number = int(line.strip())
#             result.append(number)
#         except ValueError:
#             pass
#
# with open("result.txt", "w") as f:
#     f.write(str(sum(result)))

#
# import re
#
# # Корректные строки
# file = ["Много солнца\n", "Много воды\n", "Воды нет\n", "Солнце светит!\n", "Ночь длинная\n", "\n"]
#
# with open("text_words.txt", "w") as f:
#     f.writelines(file)
#
# # Читаем и считаем слова
# word_count = {}
#
# with open("text_words.txt", "r") as f:
#     for line in f:
#         words = re.findall(r'\b\w+\b', line.lower())  # Приводим к нижнему регистру
#         for word in words:
#             word_count[word] = word_count.get(word, 0) + 1
#
# # Сохраняем результат
# with open("word_count.txt", "w") as f:
#     for word, count in word_count.items():
#         f.write(f"{word}: {count}\n")


# def show_kwargs(**kwargs):
#     print(kwargs)
#
#
# show_kwargs(name="Андрей", age=25, gentre="male")
#
#
# def example(*args, **kwargs):
#     print("ARGS:", args)
#     print("KWARGS:", kwargs)
#
#
# example(1, 2, name="Alex", active=True)


# # Задача 1
# def sum_all(*args):
#     return sum(args)
#
#
# print(sum_all(1, 2, 3))
# print(sum_all(10, -5, 4, 11))


# # Задача 2
# def describe_person(**kwargs):
#     print(f"name: {kwargs['name']}\nage: {kwargs['age']}\ncity: {kwargs['city']}")


# вариант 2

# def describe_person(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
#
#
# describe_person(name="Анна", age=30, city="Москва")


# def custom_print(*args, **kwargs):
#     print(*args, **kwargs)
#
#
# custom_print(1, 2, 3, sep=' - ', end='!')


# def avg(*args):
#     if not args:
#         return None
#     return sum(args) / len(args)
#
#
# print(avg(20, 30, 40))
# print(avg(10, 20, 30, 40))
# print(avg(10, 20, 30, 40, 50))
# print(avg())


# def show_profile(*hobbies, **info):
#     for key, value in info.items():
#         print(f"{key}: {value}")
#
#     if hobbies:
#         print("Хобби:", ", ".join(hobbies))
#
#
# show_profile('чтение', 'плавание', name='Андрей', age=25, city='Тверь')


# def filter_settings(**kwargs):
#     result = filter(lambda x: x[1], kwargs.items())
#     print(dict(result))


# def filter_settings(**kwargs):
#     return {k: v for k, v in kwargs.items() if v}
#
#
# print(filter_settings(dark_mode=True, autosave=False, sync=True, beta=False))


# def build_query(table_name, *fields, **filters):
#     lines = []
#
#     if fields:
#         lines.append(f"Выбираем: {', '.join(fields)}")
#
#     lines.append(f"Из категории: {table_name}")
#
#     if filters:
#         filter_parts = [f"{k}='{v}'" for k, v in filters.items()]
#         lines.append("Фильтры: " + " и ".join(filter_parts))
#
#     return "\n".join(lines)
#
#
# print(build_query("users", "name", "age",  city='Moscow', active=True))


# def log_action(*args, **kwargs):
#     lines = []
#     if args:
#         action = ", ".join(args)
#         lines.append(f"Действие: {action}")
#     if kwargs:
#         details = [f"{k}='{v}'" for k, v in kwargs.items()]
#         lines.append("Детали: " + " и ".join(details))
#     return "\n".join(lines)
#
#
# print(log_action("вход", "поиск", пользователь="Андрей", время="22:00"))


# def check_sign(num):
#     return "Положительное" if num > 0 else ("Отрицательное" if num < 0 else "Ноль")
#
#
# print(check_sign(0))


# def max_of_two(a, b):
#     return "Первое больше" if a > b else ("Второе больше" if a < b else "Равны")
#
#
# print(max_of_two(3, 2))


# def even_or_odd_list(*args):
#     return ["Четное" if arg % 2 == 0 else "Нечетное" for arg in args]
#
#
# print(even_or_odd_list(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

# def greet(name, is_morning=True):
#     return f"Доброе утро, {name}!" if is_morning else f"Добрый вечер, {name}!"
#
#
# print(greet("Андрей"))
# print(greet("Мария", is_morning=False))

# def user_summary(*hobbies, **info):
#     user = []
#
#     name = info.get("name")
#     if name:
#         user.append(f"Имя: {name}")
#
#     age = info.get("age")
#     if age:
#         user.append(f"Возраст: {age}")
#
#     if hobbies:
#         hobbie = ", ".join(hobbies)
#         user.append(f"Хобби: {hobbie}")
#
#     return "\n".join(user)
#
#
# print(user_summary("программирование", "гитара", name="Андрей", age=25))

#
# def get_number():
#     while True:
#         try:
#             num = int(input("Введите число: "))
#             return num
#         except ValueError:
#             print("Вы ввели не число")
#
#
# get_number()


# list_1 = [1, 2, 3, 4, 5]
# result = [x + 10 for x in list_1]
# print(result)


# person = ("Андрей", 25, "Тверь")
# name, age, city = person
# print(f"Имя: {name}\nВозраст: {age}\nГород: {city}")


# line = [1, 2, 2, 3, 3, 3]
# result = set(line)
# print(result)

#
# dic = {
#     "Имя": "Андрей",
#     "Возраст": 25,
#     "Город": "Тверь"
# }
#
# dic.update({"Профессия": "Программист"})
# dic.pop("Возраст")
# dic.update({"Город": "Москва"})
# print(dic)

# def create_profile(name, age, city, *hobbies):
#     profile = {
#         "Имя": name,
#         "Возраст": age,
#         "Город": city,
#         "Хобби": set(hobbies)
#     }
#     if age < 0:
#         del profile["Возраст"]
#
#     return profile, len(set(hobbies))
#
#
# print(create_profile("Андрей", 25, "Тверь", "гитара", "чтение", "гитара"))


# def create_book_record(title, author, year, *genres):
#     book_record = {
#         "название": title,
#         "автор": author,
#         "год": year,
#         "жанры": set(genres)
#     }
#     if year < 1900:
#         book_record.pop("год")
#
#     return book_record, len(set(genres))
#
#
# print(create_book_record("Преступление и наказание", "Достоевский",1866,
#     "роман", "драма", "роман"))


# def safe_divide():
#     while True:
#         try:
#             x = int(input("Введите первое число: "))
#             y = int(input("Введите второе число: "))
#             return x / y
#         except ValueError:
#             print("Ошибка. Нужно вводить числа")
#         except ZeroDivisionError:
#             print("Ошибка. Нельзя делить на ноль")
#         except Exception as e:
#             print("Ошибка", e)
#
#
# print(safe_divide())

# def input_and_log():
#     while True:
#         try:
#             num = int(input("Введите число: "))
#         except ValueError:
#             print("Ошибка ввода")
#         else:
#             print("Число введено успешно: ", num)
#             break
#         finally:
#             print("Завершено")
#
#
# input_and_log()

# def validate_age():
#     try:
#         age = int(input("Введите свой возраст: "))
#         if age < 0:
#             raise ValueError("Возраст не может быть отрицательным числом")
#         print(f"Возраст принят: {age}")
#     except ValueError as e:
#         print("Ошибка:", e)
#     finally:
#         print("Завершено.")
#
#
# validate_age()

# if __name__ == "__main__":
#
#     def validate_login():
#         while True:
#             try:
#                 login = input("Введите логин: ")
#                 if len(login) < 5:
#                     raise ValueError("Логин слишком короткий")
#                 if not login.isalnum():
#                     raise ValueError("Логин должен содержать только буквы и цифры")
#             except ValueError as e:
#                 print("Ошибка ввода", e)
#                 continue
#             else:
#                 print(f"Возраст принят: {login}")
#                 break
#             finally:
#                 print("Проверка завершена")
#
#
#     validate_login()

# def validate_password():
#     while True:
#         try:
#             password = input("Введите пароль: ")
#             if len(password) < 8:
#                 raise ValueError("Пароль слишком короткий")
#             if " " in password:
#                 raise ValueError("Пароль не должен содержать пробелы")
#             if not any(char.isdigit() for char in password):
#                 raise ValueError("Пароль должен содержать хотя бы одну цифру")
#             if not any(letter.isupper() for letter in password):
#                 raise ValueError("Пароль должен содержать заглавную букву")
#         except ValueError as e:
#             print("Ошибка ввода", e)
#             continue
#         else:
#             print("Пароль принят")
#             break
#         finally:
#             print("Проверка завершена")
#
#
# validate_password()

# import random as rnd
#
# print(rnd.randint(1, 10))

# from my_utils import is_prime, digit_sum, reverse_number, is_palindrome, word_count, shorten
#
#
# def analyze_input(data):
#     try:
#         if isinstance(data, int):
#             return {
#                 "число": data,
#                 "простое": is_prime(data),
#                 "сумма_цифр": digit_sum(data),
#                 "обратное": reverse_number(data)
#             }
#
#         if isinstance(data, str):
#             return {
#                 "строка": data,
#                 "палиндром": is_palindrome(data),
#                 "слов": word_count(data),
#                 "сокращено": shorten(data, 10)
#             }
#
#         else:
#             raise TypeError("Неверный тип данных.")
#
#     except TypeError as e:
#         print("Ошибка.", e)
#         return None
#     finally:
#         print("Анализ завершен!")
#
#
# print(analyze_input(12345))

from io_utils import save_to_file, append_to_file, read_file

# def notebook():
#     while True:
#         try:
#             choice_user = int(input("""
# Выберите действие:
#     1 - Создать заметку
#     2 - Добавить к заметке
#     3 - Прочитать заметку
#     4 - Выход
#     Ввод: """))
#         except ValueError:
#             print("Ошибка. Введите число.")
#             continue
#
#         else:
#             if choice_user == 1:
#                 filename = input("Введите название заметки: ")
#                 data = input("Введите текст заметки: ")
#                 save_to_file(filename, data)
#                 print("Заметка сохранена!")
#
#             elif choice_user == 2:
#                 filename = input("Введите название заметки: ")
#                 data = input("Введите текст заметки: ")
#                 append_to_file(filename, data)
#                 print("Заметка сохранена!")
#
#             elif choice_user == 3:
#                 filename = input("Введите название заметки: ")
#                 print("Содержимое файла: ")
#                 print(read_file(filename))
#
#             elif choice_user == 4:
#                 print("Программа завершена!")
#                 break
#
#             else:
#                 print("Выберите действие от 1 до 4.")
#
#
# notebook()
# save_to_file("test.txt", "Hello world!")
# append_to_file("test.txt", "Hello again!")
# print(read_file("test.txt"))


# def merge_notes(file1, file2, result_file):
#
#     with open(file1, "w") as f1:
#         f1.write("Содержимое note1...")
#
#     with open(file2, "w") as f2:
#         f2.write("Содержимое note2...")
#     try:
#         with open(file1, "r") as f1, open(file2, "r") as f2:
#             result = f1.read() + "\n---\n" + f2.read()
#
#         with open(result_file, "w+") as f3:
#             f3.write(result)
#     except FileNotFoundError:
#         print("Файл не существует.")
#         return ""
#
#     return result, len(result)
#
#
# print(merge_notes("file1.txt", "file2.txt", "result.txt"))


# Методы строк и словарей

# def analyze_text(text):
#     text = text.strip()
#     return {
#         "Длина": len(text),
#         "Заглавных букв": sum(1 for t in text if t.isupper()),
#         "Цифр": sum(1 for t in text if t.isdigit()),
#         "Слова": len(text.split())
#     }
#
#
# print(analyze_text("  Привет, Андрей! 123 Год 2025  "))

# def update_scores(scores, name, new_score):
#
#     if name in scores.keys():
#         scores[name] += new_score
#     else:
#         scores[name] = new_score
#     return scores
#
#
# print(update_scores({"Андрей": 10, "Мария": 15}, "Андрей", 20))

# def get_top_player(scores):
#     return max(scores.items(), key=lambda x: x[1])
#
#
# print(get_top_player({
#     "Андрей": 10,
#     "Мария": 25,
#     "Олег": 17
# }))

# import re
#
#
# def word_stats(text):
#     text = text.lower().strip()
#     text = re.split(r'[-,.! ]+', text)
#     res = {}
#     for word in text:
#         res[word] = res.get(word, 0) + 1
#     return res
#
#
# print(word_stats("Привет, Андрей! Привет-привет тебе Андрей."))

# import json
#
# with open("users.txt", "w") as f:
#     f.writelines("Андрей,25,Тверь\nМария,30,Москва")
#
#
# def load_users(filename):
#     users = []
#
#     with open(filename, "r") as f:
#         for line in f:
#             user_data = line.strip().split(",")
#             user = {
#                 "name": user_data[0],
#                 "age": int(user_data[1]),
#                 "city": user_data[2]
#             }
#             users.append(user)
#     return users
#
#
# def add_user(filename, name, age, city):
#     with open(filename, "a") as f:
#         f.write(f"{name},{age},{city}\n")
#
#
# def find_user(filename, name):
#     with open(filename, "r") as f:
#         for line in f:
#             user_data = line.strip().split(",")
#             if user_data[0] == name:
#                 return {
#                     "name": user_data[0],
#                     "age": int(user_data[1]),
#                     "city": user_data[2]
#                 }
#     return None
#
#
# def save_users_json(filename, users):
#     with open(filename, "w") as f:
#         json.dump(users, f, ensure_ascii=False, indent=2)
#
#
# def load_users_json(filename):
#     try:
#         with open(filename, "r") as f:
#             return json.load(f)
#     except FileNotFoundError:
#         print("Файл не существует.")
#         return []
#
#
# def save_users_txt(filename, users):
#     with open(filename, "w") as f:
#         for user in users:
#             line = f"{user['name']},{user['age']},{user['city']}\n"
#             f.write(line)
#
#
# def delete_user(filename, name):
#     users = load_users(filename)  # Загружаем всех пользователей
#     updated_users = [u for u in users if u["name"] != name]  # Удаляем по имени
#
#     if len(users) == len(updated_users):
#         print("Пользователь не найден.")
#         return
#
#     save_users_txt(filename, updated_users)  # Сохраняем обратно
#     print(f"Пользователь {name} удалён.")
#
#
# def user_manager():
#     while True:
#         try:
#             choice_user = int(input("""
# Выберите действие:
# 1 – Показать всех пользователей
# 2 – Добавить пользователя
# 3 – Найти пользователя
# 4 - Сохранить всех пользователей в JSON
# 5 - Загрузить пользователей из JSON
# 6 - Сохранить пользователей в TXT и JSON
# 7 - Удалить пользователя
# 8 – Выход
# Ввод: """))
#             filename = "users.txt"
#             if not 1 <= choice_user <= 8:
#                 print("Ошибка. Введите число от 1 до 8")
#         except ValueError:
#             print("Введите число от 1 до 8.")
#         else:
#             if choice_user == 1:
#                 users = load_users("users.txt")
#                 print(users)
#             elif choice_user == 2:
#                 name = input("Введите имя: ")
#                 age = int(input("Введите возраст: "))
#                 city = input("Введите город: ")
#                 add_user(filename, name, age, city)
#                 print("Пользователь добавлен!")
#             elif choice_user == 3:
#                 name = input("Введите имя: ")
#                 result = find_user("users.txt", name)
#                 if result:
#                     print("Найден:", result)
#                 else:
#                     print("Пользователь не найден.")
#             elif choice_user == 4:
#                 users = load_users("users.txt")
#                 save_users_json("users.json", users)
#                 print("Пользователи сохранены в users.json")
#             elif choice_user == 5:
#                 users = load_users_json("users.json")
#                 if users:
#                     print("Пользователи из JSON:")
#                     for user in users:
#                         print(f"{user['name']} — {user['age']} лет, {user['city']}")
#                 else:
#                     print("JSON-файл пуст или не найден.")
#             elif choice_user == 6:
#                 users = load_users("users.txt")
#                 save_users_txt("users.txt", users)
#                 save_users_json("users.json", users)
#                 print("Пользователи сохранены в TXT и JSON.")
#             elif choice_user == 7:
#                 name = input("Введите имя пользователя для удаления: ")
#                 delete_user("users.txt", name)
#             elif choice_user == 8:
#                 break
#
#
# user_manager()

import json


class User:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def show_info(self):
        return f"{self.name} - {self.age} лет, город {self.city}"

    def to_dict(self):
        return {"name": self.name, "age": self.age, "city": self.city}
#
#
# user = User("Андрей", 25, "Тверь")
# print(user.show_info())


class UserManager:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def show_all_users(self):
        for user in self.users:
            print(user.show_info())

    def find_user(self, name):
        for user in self.users:
            if user.name == name:
                return user
        return None

    def remove_user(self, name):
        for user in self.users:
            if user.name == name:
                self.users.remove(user)
                return True
        return False

    def update_user(self, name, new_age=None, new_city=None):
        for user in self.users:
            if user.name == name:
                if new_age is not None:
                    user.age = new_age
                if new_city is not None:
                    user.city = new_city

    def save_to_json(self, filename):
        users = [user.to_dict() for user in self.users]
        with open(filename, "w") as f:
            json.dump(users, f, ensure_ascii=False, indent=2)

    def load_from_json(self, filename):
        with open(filename, "r") as f:
            users = json.load(f)
            for user_data in users:
                user = User(user_data["name"], user_data["age"], user_data["city"])
                self.add_user(user)


manager = UserManager()
manager.add_user(User("Андрей", 25, "Тверь"))
manager.add_user(User("Мария", 30, "Москва"))
manager.show_all_users()
manager.save_to_json(users)

result = manager.find_user("Мария")
if result:
    print(result.show_info())
else:
    print("Пользователь не найден.")