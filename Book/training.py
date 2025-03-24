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
from ctypes import pythonapi
from os.path import split

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

list_1 = []

for lst in range(10):
    new_list = {'red': 12, 'blue': 133}
    list_1.append(new_list)
print(list_1[:3])
