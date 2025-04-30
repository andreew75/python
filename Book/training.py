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


import re

# Корректные строки
file = ["Много солнца\n", "Много воды\n", "Воды нет\n", "Солнце светит!\n", "Ночь длинная\n", "\n"]

with open("text_words.txt", "w") as f:
    f.writelines(file)

# Читаем и считаем слова
word_count = {}

with open("text_words.txt", "r") as f:
    for line in f:
        words = re.findall(r'\b\w+\b', line.lower())  # Приводим к нижнему регистру
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1

# Сохраняем результат
with open("word_count.txt", "w") as f:
    for word, count in word_count.items():
        f.write(f"{word}: {count}\n")




