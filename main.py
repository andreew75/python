# # name = "admin"
# #
# # print("Hello", name)
# #
# # age = 20.2
# # print(age)
# #
# # print(type(name))
# # print(type(age))
# #
# # print(id(name))
# # print(id(age))
#
# # a = b = c = 1
#
# # a, b, c = 5, "Mor", 5.6
# #
# # print(a)
# # print(b)
# # print(c)
#
# # first_name = "admin"
# # print(first_name)
#
# # import keyword
# # print(keyword.kwlist)
#
#
# # a = 5
# # print(a)
# #
# # a = "Andrew"
# # print(a)
#
# # print("dok")
# # print('dok')
# #
# # print("\tdor\nwent")
#
#
#
# # УРОК 2
#
# # print("Document \"file.txt\" path to: D:\\folder\\file.txt")
#
# # s1 = "hello,"
# # s2 = "Python!"
# # s3 = s1 + " " + s2 "?\t"
# # print(s3)
# #
# # s4 = s3 * 3
# # print(s4)
#
#
# # number = 6 + 4 * 5 ** 3 + 7
# # print(number)
# #
# # a = 5
# #
# # # a = a + 3
# #
# # a += 3
# #
# # print(a)
# #
# # a -= 3
# # print(a)
#
# # num = 4562
# #
# # print("Исходное число:", num)
# #
# # a = num % 10
# # print(a)
# # num = num // 10
# # print(num)
# # b = num % 10
# # print(b)
# # num = num // 10
# # c = num % 10
# # print(c)
# # num = num // 10
# # d = num % 10
# # print(d)
# # print(a *1000 + b * 100 + c * 10 + d)
#
# # num1 = "2"
# # num2 = 3
# # res = num1 + "\t " + str(num2)
# # print(res)
# #
# # print(int(5.345))
# # print(round(3.453))
# # print(round(3.453, 2))
#
# # num1 = "2.4"
# # num2 = 10
# # res = float(num1) + num2
# # print(res)
#
# # name = "Andrew."
# # age = 50
# # print("My name is ", name, " Age ", age, sep='', end = "\n\n")
# # print("Hello Lobby")
#
# # name = input("Your Name: ")
# # print("hello", name)
#
# # num = int(input("Введите число: "))
# # power = int(input("Введите степень: "))
# # # num = int(num)
# # # power = int(power)
# # res = num ** power
# # print("Число", num, "в степени", power, "равно: ", res)
#
# # num1 = int(input('1: '))
# # num2 = int(input('2: '))
# # num3 = int(input('3: '))
# # num4 = int(input('4: '))
# #
# # res1 = num1 + num2
# # res2 = num3 + num4
# # res3= res1 / res2
# #
# # print(round(res3, 2))
#
#
# # b1 = True
# # b2 = False
# #
# # print(5 == 4)
#
# # print(bool("Hello"))
# # print(bool(4))
# # print(bool(0))
# # print(bool(None))
#
#
# test = None
#
# # Урок 3
#
# # print(5 - 3 == 2 and 1 + 3 == 4)
# # print(5 - 3 == 2 and 1 + 3 == 4)
# #
# # print(5 - 3 == 2 or 1 + 3 < 4)
# #
# # print(not 9 - 5)     # not True => False
#
# a = 15
# # b = 25
# if a > b:
#     print(a, ">", b)
# elif b == a:
#     print(b, "==", a)
# else:
#     print(b, ">", a)
# from itertools import count
# from nis import match
# from os.path import split
# from zoneinfo import reset_tzpath

# cnt = 5
# if cnt < 10:
#     cnt = cnt + 1
# else:
#     cnt = cnt - 1
# print(cnt)

# age = int(input("Введите свой возраст: "))
# if age >= 18:
#     print("Доступ разрешен")
# else:
#     print("Доступ запрещен")


# age = int(input("Введите свой возраст: "))
# a = 'Мужчина'
# b = 'Женщина'
# if age >= 18:
#     if a == (input("Введите свой пол: ")):
#         print("Доступ разрешен")
#     else:
#         print("Доступ запрещен")
# else:
#     print("Доступ запрещен")

#
# day = int(input("Введите день недели цифрой: "))
# if 1 <= day <= 5:  # (day >= 1) and (day <= 5):
#     print("Рабочий день - ", end="")
#     if day == 1:
#         print("Понедельник")
#     if day == 2:
#         print("Вторник")
#     if day == 3:
#         print("Среда")
#     if day == 4:
#         print("Четверг")
#     if day == 5:
#         print("Пятница")
# elif day == 6 or day == 7:
#     print("Выходной день - ", end="")
#     if day == 6:
#         print("Суббота")
#     if day == 7:
#         print("Воскресенье")
# else:
#     print("Такого дня недели не существует")

# month = int(input("Введите номер месяца: "))
# if 1 <= month <= 12:
#     print("Время года - ", end="")
#     if month == 12 or 1 <= month <= 2:
#         print("Зима")
#     if month == 3 or month == 4 or month == 5:
#         print("Весна")
# else:
#     print("Ошибка ввода данных")

# day = 'Суббота'
# time = 14
#
# match day:
#     case 'Понедельник' | 'Вторник' | 'Среда' | 'Четверг' | 'Пятница':
#         print('Рабочий день')
#     case 'Суббота' | 'Воскресенье' if 9 <= time <= 15 or 12 <= time <= 13:
#         print('Выходной день')
#     case _:
#         print('Ошибка ввода данных')

# a, b = 30, 20
#
# print(a if a < b else b)


# УРОК 4

# try:
#     a = int(input("Введите число"))
#     print(a)
# except ValueError:
#     print("Ошибка")
#

# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
#
# except (ValueError, ZeroDivisionError):
#     print("Нельзя вводить строки или Нельзя делить на 0")
#
# else:
#     print("Все хорошо, поздравляем вас!")
#
# finally:
#     print("Конец программы")


# a = input("введите первое число: ")
# b = input("введите второе число: ")
#
# try:
#     a = int(a)
#     b = int(b)
# except ValueError:
#     a = str(a)
# finally:
#     print(a + b)

# Циклы

# a = 0   # счетчик
# while a < 5:    # условие
#     print("i = ", a)
#     a += 1  # изменение счетчика

# итерация - один шаг цикла

# a = 0   # счетчик
# while a < 100:    # условие
#     print("i = ", a)
#     a += 10  # изменение счетчика

# a = 2
# while a <= 20:
#     print("i = ", a)
#     a += 2  # изменение счетчика

# a = int(input("Количество символов: "))
# # print("*" * a)
# b = 0
# while b < a:
#     print("*", end="")
#     b += 1

# a = int(input("Количество символов: "))
# # print("*" * a)
# b = 0
# while b < a:
#     if b % 2 == 0:
#         print("+", end="")
#     else:
#         print("-", end="")
#     b += 1


# УРОК 5

# i = 0
# while i < 10:
#     if i == 5:
#         break
#     print(i)
#     i += 1
# else:
#     print("Цикл окончен, i = ", 1)

# i = 1
# while i < 5:
#     print("Внешний Цикл, i = ", i)
#     h = 1
#     while h < 4:
#         print("Внутреннмй Цикл, h = ", h)
#         h += 1
#     i += 1

# i = 1
# while i < 10:
#     h = 1
#     while h < 10:
#         print(i, "*", h, "=", i * h, end="\t")
#         h += 1
#     print()
#     i += 1

# i = 0
# while i < 3:
#     h = 0
#     while h < 6:
#         print("$", end="\t")
#         h += 1
#         continue
#     print()
#     i += 1

# i = 0
# while i < 5:
#     h = 0
#     while h < 16:
#         if h % 2 == 0:
#             print("+", end="\t")
#         else:
#             print("-", end="\t")
#         h += 1
#     print()
#     i += 1

# for i in "Hello", 5:
#     print(i)


# # range (start = 0, stop, step = 1)  по умолчанию
# a = 10
# for i in range(2, a + 1, 1):
#     print(i, end="\t")
#
# print()
#
# i = 0
# while i < 8:
#     print(i, end='\t')
#     i += 1
# print()
#
# a = int(input("Введите число: "))
#
# for i in range(1, a + 1):
#     if a % i == 0:
#         print(i, end='\t')
#

# for i in range(11, 100, 11):
#     if i % 11 == 0:
#         print(i, end=" ")
#
# print()
#

# for i in range(11, 100):
#     if i % 10 == i // 10:
#         print(i, end=" ")
#
# for i in range(3):
#     print(i)
#     if i == 2
#         break
# else:
#     print("Цикл закончен")


# for i in range(3):
#     print("+++")
#     for h in range(2):
#         print("-----")

# w, h = 12, 4
#
# for i in range(h):
#     for g in range(w):
#         print("*", end=" ")
#     print()
#
# print()
#
# w = int(input("Ширина: "))
# h = int(input("Высота: "))
#
# for i in range(h):
#     for g in range(w):
#         if i == 0 or i == h - 1 or g == 0 or g == w - 1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# Список (List)
# num = [0, 2, 3, 4, 10]
# print(num)
# print(num[1])
# print(num[-1])
#
# num[1] = 256
# num[3] += 12
# print(num)
# print("Кол-во элементов в списке: ", len(num))


# num = [input("Введите: ")]


# s = []
# print(s)
#
# t = list("Hello")
# print(t)
#
# print(range( 0, 8, 2))
# print(list(range( 0, 18, 2)))

# a = [10, 12, 14, 16]
# b = [2, 4, 6, 8]
# print(a + b)
# print(a * 3)

# a = [10, 12, 14, 16]
#
# for i in a:
#     print(i)

# a = [0 for _ in range(5)]
# print(a)
#
# a = [i for i in range(5)]
# print(a)
#
# n = 5
# a = [i ** 2 for i in range(2, n)]
# print(a)

# a = [0] * int(input("Введите кол-во элементов списка: "))
# # print(a)
# for i in range(len(a)):
#     a[i] = int(input("> "))
# print(a)

# a = [int(input('> '))for _ in range(int(input("Введите кол-во элементов списка: ")))]
# print(a)

# lst = [10, 12, 14, 16]
# for i in range(len(lst)):
#     print(lst[i], end=" ")
#
# print()
#
# for x in lst:
#     print(x, end=" ")

# 6 Lesson

# n = list(range(21, 41))
# print(n)
#
# count = sum_ = 0
# for i in range(len(n)):
#     if n[i] % 2 == 0:
#         count += 1
#     else:
#         sum_ += n[i]
#
# print("Четные: ",  count)
# print("Нечетные: ",  sum_)

# a = [int(input('> '))for _ in range(int(input("n =: ")))]
# print(a)
# for i in range(len(a)):
#     if a[i] % 2 == 0:
#         print(a[i], end=" ")
# print()
#
# a = [int(input('> '))for _ in range(int(input("n =: ")))]
# print(a)
# for i in range(0, len(a), 2):
#     print(a[i], end=" ")

# a = [int(input('> '))for _ in range(int(input("n =: ")))]
# print(a)
# for i in range(1, len(a)):
#     if a[i] > a[ - 1]:
#         print(a[i], end="")

# a = [int(input('> '))for _ in range(int(input("n =: ")))]
# print(a)
# for i in a:
#     if i > i - 1:
#         print(a[i], end="")

# a = [3, 4, 5, 2]
# a[0], a[1] = a[1], a[0]
# print(a)

# Срез
# [start:stop:step]
# a = [3, 4, 5, 2, 3, 8]
# print(a)
# print(a[1:4])
# print(a[:])
# print(a[2:])
# print(a[2:5:2])
# print(a[::-1])
# print(a[4:2:-2])

# list_ = list(range(1, 8))
# print(list_)
# print(list_[::-1])

# a = [3, 4, 5, 2, 3, 8]
# print(a)
# a[1:2] = [0, 0, 0, 0]
# print(a)
# a[1:2] = [34]
# print(a)


# ['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
# a = [3, 4, 5, 2, 3, 8]
# print(a)
# a.append(99)
# print(a)

# a = []
# b = int(input("Кол-во элемттов списка: "))
# for num in range(b):
#     x = int(input("введи число: "))
#     a.append(x)
# print(a)
#
# a = [3, 4, 8, 2, 9, 2]
# b = [8, 2, 9, 1, 7, 10]
# c = []
#
# for i in a:
#     for j in b:
#         if i in c:
#             continue
#         if i == j:
#             c.append(i)
#             break
# print(c)

# a = [3, 4, 8, 2, 9, 2]
# b = [8, 2, 9, 1, 7, 10]
# c = []
#
# for i in a:
#     if i in b and i not in c:
#         c.append(i)
# print(c)
#
# a = [1, 2, 3,  5, 3]
# b = [11, 22, 22]
# c = []
#
# if len(b) > len(a):
#     for i in range(len(a)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(a)), (len(b)):
#         c.append(b[i])
# else:
#     for i in range(len(b)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(b)), (len(a)):
#         c.append(b[i])
#
# print(c)

# a = [3, 4, 8, 2, 9, 2]
# print(a)
# a.remove(3)
# print(a)
#
# last = a.pop()
# print(last)
# print(a)
#
# try:
# # item = 1
# # if item in a:
#     second = a.pop(10)
# except IndexError:
#     second = "Такого индекса нет"
#     print(second)
# print(a)

# a = [3, 4, 8, 2, 9, 2]
# print(a)
#
# a[3:] = []
# print(a)
#
# del a[1:3]
# print(a)

# УРОК 7

# a = [1, 2, 3]
# b = a.copy()
# # b.append(10)
# print(b, id(b))
# print(a, id(a))

# m = [1, 9, 6, 2, 8]
# print(m)
# # m.reverse()
# # print(m)
# m.sort(reverse=True)
# print(m)

# s = ['Tornado', 'Lob', 'Prosecutor']
# s.sort(key=len, reverse=True)
# print(s)

# m = [1, 9, 6, 2, 8]
# s = sorted(m, reverse=True)
# print(m)
# print(s)


# print(random.random())
# print(random.randint(1, 11))
# print(random.randrange(1, 11, 2))
# print(round(random.uniform(10.4, 18.3)))

# city_list = ['Moskva', 'Novosibirsk', 'Vologda', 'Kirov']
# s = [1,2, 5, 3, 8, 9, 2]
#
# # print(random.choice(city_list))
# # print(random.choice(s))
# # print(random.choices(city_list, k=3))
# # print(random.choices(s, k=5))
# random.shuffle(city_list)
# print(city_list)

# mas = [random.randint(15, 100) for i in range(10)]
# print(mas)
# print(len(mas))
# print(max(mas))
# print(min(mas))
# print(sum(mas))

# mas = [random.randint(15, 100) for i in range(10)]
# print(mas)
# min_ = min(mas)
# print(min_)
#
# ind = mas.index(min_)
# print(ind)
# del mas[:ind]
# print(mas)


# m = [
#     [1, 2, 3],
#     [5, 5, 7, 8],
#     [10, 12, 13]
# ]
# print(m)
# print(m[0][2])
# print(m[1][3])
# print(m[2][1])

# m = [
#     [1, 2, 3],
#     [5, 5, 7, 8],
#     [10, 12, 13]
# ]
# print(m)
#
# for row in range(len(m)):
#     for col in range(len(m[row])):
#         print(m[row][col], end="\t")
#     print()
#
# print()
#
# for row in m:
#     for x in row:
#         print(x, end="\t")
#     print()

# m = ['hello', 'World']
# print(m)
# print(m[1][2])

# import math
#
# print(math.sqrt(4))
# print(math.ceil(3.2))
# print(math.floor(3.9))

# import math as m
#
# print(m.sqrt(4))
# print(m.ceil(3.2))
# print(m.floor(3.9))

# from math import *
#
# print(sqrt(4))
# print(ceil(3.2))
# print(floor(3.9))

# from math import sqrt, ceil, floor  # Предпочтительный вариант (загружает только нужные модули)
#
# print(sqrt(4))
# print(ceil(3.2))
# print(floor(3.9))

# from math import pi
#
# radius = int(input("Веедите радиус окружности: "))
# print("Длина окружности: ", round(radius * 2 * pi, 2))


# import time
# import locale
#
# # print(time.ctime(182873788))
#
# # res = time.localtime()
# # print(res)
# # print(res.tm_mday, res.tm_mon, res.tm_year)
# # print(time.strftime("Today is %B %d, %Y"))
# # print(time.strftime("Today is %m/%Y, %H:%M:%S"))
# # locale.setlocale(locale.LC_TIME, "ru")
# # print(time.strftime("Сегодня %B %d, %Y"))
#
#
# start = time.time()
# print("Запуск программы")
# time.sleep(5)
# res = time.time() - start
# print("Программа выполнилась за", round(res, 4), "сек")

# УРОК 8 (ФУНКЦИИ)

# print()
#
#
# def hello(name, age):
#     print('My name is', name, 'My age is', age)
#
#
# hello('Andrey.', 28)
# hello('Kostromin', 50)

# def get_sum(a, b):
#     print(a + b)
#
#
# x = 2
# y = 5
# get_sum(x, y)
# get_sum('abc', 'dce')


# def symbol(count, a, b):
#     for i in range(count):
#         if i % 2 == 0:
#             print(a, end="")
#         else:
#             print(b, end="")
#     print()
#
#
# symbol(9, '+', '-')
# symbol(9, 'X', '0')


# def get_sum(a, b):
#     return a + b
#
#
# x = 2
# y = 5
# res = get_sum(x, y)
# print(res)

# def maximum(one, two):
#     if one > two:
#         return one
#     else:
#         return two
#
#
# print(maximum(9, 5))
# print(maximum(5, 15))


# def cube(a):
#     return a * a * a
#
#
# for i in range(1, 11):
#     print(i, 'в кубе = ', cube(i))

#
# def change(lst):
#     lst.reverse()
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(['c', 'a', "d", 'g']))
#
#
# def change(lst):
#     lst[0], lst[-1] = lst[-1], lst[0]
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(['c', 'a', "d", 'g']))

# def one_big(x, y):
#     if x > y:
#         return True
#     else:
#         return False
#
#
# a = int(input('a: '))
# b = int(input('b: '))
# if one_big(a, b):
#     print('Первое больше второго')
# else:
#     print('Второе больше второго')
#
# print(one_big(10, 2))
# print(one_big(10, 20))

# def check_password(password):
#     has_upper = False
#     has_lower = False
#     has_num = False
#     for i in password:
#         if "A" <= i <= "Z":
#             has_upper = True
#         if "a" <= i <= "b":
#             has_lower = True
#         if '0' <= i <= '9':
#             has_num = True
#     if len(password) >= 8 and has_upper and has_lower and has_num:
#         return True
#     return False
#
#
# p = input("Введите пароль: ")
# if check_password(p):
#     print("Надежный пароль")
# else:
#     print("Ненадежный пароль")
#
# def get_sum(a, b, c=0, d=0, e, g):
#     return a + b + c + d +e + g
#
#
# print(get_sum(1, 5, 2, 7))
# print(get_sum(1, 5, 2))
# print(get_sum(1, 5))
# print(get_sum(1, 5, d=3))
# print(get_sum('K', 'O', 'W', 'B', 'O', 'Y'))


# def set_param(count=20, symbol=" "):
#     print(symbol * count)
#
#
# set_param(10, "+")
# set_param(5, "*")
# set_param(15, "#")
# set_param(7)
# set_param()


# def display_info(name, age):
#     print('Name', name,'\nAge', age)
#
#
# def display_info("hello", name):
#
#
# display_info('Andrey', 50)
# # display_info(age=50, name='Andrey')

# lt1 = 'Hello'
# lt2 = 'Hello'
# print(lt1 is lt2)
# print(lt1, id(lt2))
#
# lst1 = [1, 2, 3]
# lst2 = [1, 2, 3]
# print(lst1 is lst2)
# print(lst1 == lst2)

# lst1 = [1, 2, 3]
# print(lst1, id(lst1))
# lst1.append(4)
# lst1.pop(0)
# print(lst1, id(lst1))

# lt1 = 'Hello'
# print(lt1, id(lt1))
# lt1 = lt1 + '!'
# print(lt1, id(lt1))


# a = 5
# print(a, id(a))
# a = 7
# print(a, id(a))

# УРОК 9

# lst = [10, 20, 30]  # список
# lpt = (10, 20, 30)  # кортеж
#
# print(lst)
# print(lpt)

# a = ()
# print(type(a))
# b = tuple()
# print(type(b))

# a = 1, 2, 3, 4, 5, 6
# print(a, type(a))
#
# b = tuple('Hello')
# print(b, type(b))

# b = tuple('Hello')
# print(b[0:-1:2])


# sa = tuple(input("- > ") for i in range(5))
# print(sa)

# from random import randint
#
# sa = tuple((randint(33, 78)) for i in range(10))
# print(sa)

# t1 = tuple('hello')
# t2 = tuple('World')
# # print(t1)
# # print(t2)
# t3 = t1 + t2
# # print(t3 * 3)
# print(t3.count('l'))
# print(t3.index('l', 3, -1))
#
# v = "g"
# if v in t3:
#     t3.index(v)
# else:
#     print("Такого символа нет")

# def slicer(tpl, el):
#     if el in tpl:
#         if tpl.count(el) == 1:
#             return tpl[tpl.index(el):]
#         else:
#             first = tpl.index(el)
#             second = tpl.index(el, first + 1) + 1
#             return tpl[first:second]
#     else:
#         return ()
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9 ,2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))

# t = (10, True, [1, 2, 3], ['hello', 'world'])
# print(t, id(t))
# t[4][0] = 'new'
# print(t, id(t))


# def get_user():
#     name = 'Tom'
#     age = 50
#     is_married = False
#     return name, age, is_married
#
#
# first_name, my_age, married = get_user()
# print(first_name, my_age, married)

# lst = [1, 2, 3, 4, 5, 6]
# print(lst)
#
# tpl = tuple(lst)
# print(tpl)
# lst2 = list(tpl)
# print(lst2)


# countries = (
#     ('Italy', 80.2, ('Milan', 5.5)),
#     ('France', 78)
# )
# print(countries, end="\n\n")
#
# for city in countries:
#     country_name, country_pop, cities = city
#     print('Страна:', country_name, 'Население:', country_pop, cities)

# tpl = tuple(input("Введи строку: "))
# lst = []
# for i in range(len(tpl)):
#     if tpl[i] not in lst:
#         lst.append(tpl[i])
#
# for i in range(len(lst)):
#     print('Кол-во', lst[i], '=', tpl.count(lst[i]))

# print(tpl)
# print(lst)

# s = {'red', 'blue', 'green'}    # Множество (set)
# s1 = {'red', 'blue', 'green', 'blue', 'green'}
# print(s)
# print(s1)

# a = set("hello")
# print(a)


# s = {i for i in range(10)}
# print(s)

# lst = [1, 2, 2, 2, 2, 4, 4, 4, 4]
# num = set(lst)
# print(num)
# lst2 = list(num)
# print(lst2)

# t = {'red', 'blue', 'green'}
# print('red' in t)
# print('yellow' in t)
# for i in t:
#     print(i)

# lst = ['ab_1', 'ac_1', 'bc_1', 'bc_2']
# print([i for i in lst if 'a' in i])
# print(['A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in lst])
# print(['A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in lst if i[1] == 'c'])        # Список
# print({'A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in lst if i[1] == 'c'})        # Множество
# print(tuple('A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in lst if i[1] == 'c'))   # Кортеж

# a = {'red', 'blue', 'green'}
# print(a)
# a.add('white')
# print(a)
# # a.remove('red')
# color = 'black'
# # if color in a:
# #     a.remove('black')
# # a.discard('black')
# # a.pop()
# a.clear()
# print(a)

# a = {0, 1, 2, 3}
# b = {4, 3, 2, 8}
# # c = a | b
# # print(c)
# # a |= b
# # print(a)
# #
# # c = a & b
# # print(c)
# # a &= b
# # print(a)
#
# # c = a - b
# # print(c)
#
# c = a ^ b
# print(c)
# a ^= b
# print(a)

# a = {1, 2, 6, 0}
# b = {3, 1, 4, 7, 2}
# c = {6, 0, 5, 2}
# # d = b ^ c ^ a
# d = b ^ c ^ a
# print(d)

# a = {1, 2}
# b = {3}
# c = {4, 5}
# d = {3, 2, 6}
# e = {6}
# f = {7, 8}
# g = {9, 8}
#
# all = a.union(b, c, d, e, f, g)
# print(all)
# print("Количество элементов: ", len(all))
# print(min(all))
# print(max(all))

# str_1 = input("1 строка: ")
# str_2 = input("2 строка: ")
# a = set(str_1) & set(str_2)
# # print(a)
# for i in a:
#     print(i, end="")

# s = frozenset([1, 2, 3, 4, 5, 6])
# print(s)
#
# s_1 = frozenset("hello")
# print(s_1)

# Словари

# lst = ["one", "two"]
# d = {"first": "one", "second": "two"}
# print(lst)
# print(lst[1])
#
# print(d)
# print(d["second"])

# d = {0: "text", (1, 2): "Кортеж", "lst": [1, 2, 3]}
# print(d)
# print(d[0])
#
# d = {"first": "one", "second": "two"}       # Словарь
# d1 = dict(first="one", second="two")        # Словарь (ключи только строки)

# lst = [
#     ["one", 1],
#     ["two", 2],
#     ["three", 3]
# ]
# print(lst)
# d = dict(lst)
# print(d)

# d = {i: i ** 2 for i in range(1, 7)}
# print(d)
#
# for i in d:
#     print("key =", i, "value =", d[i])

# d = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
# res = 1
# for key in d:
#     res *= d[key]
# print(res)

# d = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
# del d['x2']
# print(d)

# d = dict()
# d[1] = input('> ')
# d[2] = input('> ')
# d[3] = input('> ')
# d[4] = input('> ')
# print(d)

# d = {i: input('> ') for i in range(1, 5)}
# print(d)
#
# dislike = int(input("Какой элемент исключить? "))
# del d[dislike]
# print(d)

# items = {
#     '1': ['Core-i3 4333', 45000, 9],
#     '2': ['Core-i5 5300', 48000, 3],
#     '3': ['Core-i7 74333', 39000, 6],
#     '4': ['Core-i9 5340', 45000, 4],
#     '5': ['Core-i9 7333', 45000, 1]
# }
#
# for i in items:
#     print(i, ") ", items[i][0], " - ", items[i][1], " руб. ", items[i][2], " шт", sep="")
#
# while True:
#     n = input("№ ")
#     if n == "0":
#         break
#     else:
#         if n in items:
#             while True:
#                 try:
#                     count = int(input("Количество: "))
#                     items[n][2] += count
#                 except ValueError:
#                     print("Некорректное значение")
#         else:
#             print("Такого номера нет")
# for i in items:
#     print(i, ") ", items[i][0], " - ", items[i][1], " руб. ", items[i][2], " шт", sep="")

# d = {0: "text", (1, 2): "Кортеж", "lst": [1, 2, 3]}
# print(d.keys())
# print(d.values())
# print(d.items())

# for i, k in d.items():
#     print(i, ":", k)

# d = {0: "text", (1, 2): "Кортеж", "lst": [1, 2, 3]}
# d1 = d.copy()
# print(d)
# print(d1)

# d = {0: "text0", 1: "text1", 2: "text3"}
# value = d.get(6, 'Такого ключа не существует')
# print(value)

# d.clear()

# item = d.pop(1)
# print(item)

# # item = d.pop(2, None)   # Добавить None чтобы не было ошибки, если ключ не существует
# item = d.popitem()   # Добавить None чтобы не было ошибки, если ключ не существует
#
# print(item)

# d = {0: "text0", 1: "text1", 2: "text3"}
# # item = d.setdefault(4, "four")
# # print(item)
# d_2 = [(10, 'A'), (20, 'B'), (2, 'C')]
# # c = d | d_2
# d.update(d_2)
# print(d)

# d = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
# new_d = dict()
# new_d['name'] = d.pop('name')
# new_d['salary'] = d.pop('salary')
#
# print(d)
# print(new_d)


# d = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
# d['location'] = d.pop('city')
#
# print(d)

# sales = {
#     "John": {'N': 3056, 'S': 8463, 'E': 8441, 'W': 2694},
#     "Tom": {'N': 4832, 'S': 6786, 'E': 4737, 'W': 3612},
#     "Anna": {'N': 5239, 'S': 4802, 'E': 5820, 'W': 1859},
#     "Fiona": {'N': 3904, 'S': 3645, 'E': 8821, 'W': 2451},
# }
#
# for x, y in sales.items():
#     print(x)
#     for i, j in sales[x].items():
#         print("\t", i, ":", j)

# d = {'One': 2, 'Two': 2, 'Three': 3, 'Four': 4}
# new_d = {value: key for key, value in d.items()}
# print(d)
# print(new_d)

# d = {'One': 2, 'Two': 2, 'Three': 3, 'Four': 4}
# new_d = {key: value for key, value in d.items() if value <= 2}
# print(d)

# d = {i: i * 5 for i in [10, 20, 30, 40]}
# print(d)
#
# s = "Hello"
# d1 = {key: key * 3 for key in s}
# print(d1)

# d = {'One': 2, 'Two': 2, 'Three': 3, 'Four': 4}
# print(list(d.items()))
# print(list(d.keys()))
# print(list(d.values()))

# a = ["one", 1, 2, 3, "two", 10, 29, "three", 15, 36, 60, "four", -20]
# d = {}
# s = None
# for i in a:
#     if type(i) is str:
#         d[i] = []
#         s = i
#     else:
#         d[s].append(i)
# print(d)

# zip

# d = dict(zip([1, 2, 3], ['one', 'two', 'three']))
# d1 = list(zip([1, 2, 3], ['one', 'two', 'three']))
# print(d)
# print(d1)

# a = [1, 2, 3]
# b = ['one', 'two', 'three']
# d = {k: v for k, v in zip(a, b)}
# print(d)

# a = {1, 2, 3}
# b = {'one', 'two', 'three'}
# d = {k: v for k, v in zip(a, b)}
# print(d)

# one = {'name': 'Ivan', 'surname': 'Ivanov', 'job': 'director'}
# two = {'name': 'Andrey', 'surname': 'Petrov', 'job': 'Lover'}
# for (k1, v1),( k2, v2) in zip(one.items(), two.items()):
#     print(k1, '->', v1)
#     print(k2, '->', v2)

# s = [(1, 'a'), (2, 'b'), (3, 'c')]
# a, b = zip(*s)
#
# print(a)
# print(b)

# letters = ['b', 'd', 'a', 'c']
# numbers = [4, 2, 1, 5]
# d = dict(zip(letters, numbers))
# print(d)
#
# data1 = list(zip(letters, numbers))
# print(data1)
# data1.sort()
# print(data1)
#
# d2 = dict(data1)
# print(d2)
#
# data2 = list(zip(numbers, letters))
# data2.sort()
# print(data2)
#
# d3 = {v: k for k, v in data2}
# print(d3)


# letters = ['b', 'd', 'a', 'c']
# numbers = [4, 2, 1, 5]
# data = sorted(zip(letters, numbers))
# print(dict(data))

# one_d = {'One': 2, 'Two': 2}
# two_d = {'Three': 3, 'Four': 4}
#
# print({**one_d, **two_d})
# print(one_d | two_d)
#
# for k, v in {**one_d, **two_d}.items():
#     print(k, v)

# lst = ['red', 'yellow', 'blue']
# ind = 1
# for color in lst:
#     print(str(ind) + " " + color)
#     ind += 1
#
# print()
#
# for index, color in enumerate(lst, 1):
#     print(str(index) + " " + color)


# d = {'One': 2, 'Two': 2, 'Three': 3, 'Four': 4}
#
# for i, (k, v) in enumerate(d.items(), 1):
#     print(i, ")", k, v)

# a = [1, 2, 3]
# b = [*a, 4, 5, 6]
# print(b)

# def func(*args):
#     return args
#
#
# print(func(5))
# print(func(1, 2, 3, 'abc'))


# def summa(*params):
#     res = 0
#     for n in params:
#         res += n
#     return res
#
#
# print(summa(1, 2, 3, 4, 6))
# print(summa(7, 2, 12))

# def to_dict(*args):
#     return {i: i for i in args}
#
#
# print(to_dict(1, 2, 3, 4))
# print(to_dict('grey', (2, 17), 3.11, -4))

# def average(*args):
#     a = sum(args) / len(args)
#     res = []
#     for num in args:
#         if num < a:
#             res.append(num)
#     return res
#
#
# print(average(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(average(3, 6, 1, 8, 5))

# def func(a, b,  *arg):
#     return a, b, arg
#
#
# print(func(5, 22, 3, 4, 5))

# def func(**kwargs):
#     return kwargs
#
#
# print(func(a=1, b=2, c=3))
# print(func(name='Andrey'))


# def data(**info):
#     for k, v in info.items():
#         print(k, ':', v)
#     print()
#
#
# data(name='Andrey', surname='Lev', age=50)
# data(name='Ivan', phone=9217222295)

# def db(**kwargs):
#     my_dict.update(kwargs)
#
#
# my_dict = {"one": "first"}
# db(k1=22, k2=22, k3=11, k4=91)
# db(name='bob', age=32, weight=71)
#
# print(my_dict)

# def func(a, *args, **kwargs):
#     return a, args, kwargs
#
# print(func(1, 234, 34, 7, c=44, d=12)

# def func1(*args):
#     print(args[0])
#
#
# def func2(**kwargs):
#     print(kwargs['one'])
#
#
# func1(1, 2, 3, 4, 5)
# func2(one=123, two=456)


# Области видимости (scope)

# name = "Tom"    # Глобальная область видимости
#
#
# def hi():
#     global name
#     name = "Halk"
#     surname = "Love"    # Локальная область видимости
#     print("Hello", name, surname)
#
#
# def by():
#     print("Good bye", name)
#
#
# hi()
# by()

# i = 5
#
# def func(arg=1):
#     print(arg)
#
# i = 6
# func()
# print(i)


# def add_two(a):
#     x = 2
#
#     def add_one():
#         print(x)
#         return a + x
#
#     return add_one()
#
#
# print(add_two(3))

# Вложенные функции

# def outer(a):
#     def inner():
#         print('Hello', a)
#
#     inner()
#
#
# outer('World')

# def outer():
#     a = 6
#
#     def inner(b):
#         a = 4
#         print('Сумма: ', a + b)
#     print(a)
#     inner(5)
#
#
# outer()

# x = 25
#
#
# def fn():
#     global t
#     a = 30
#
#     def inner():
#         nonlocal a
#         a = 35
#         print(a)
#
#     inner()
#     t = a
#
#
# fn()
# c = x + t
# print(c)


# def rect_paral(a, b, c):
#     def inner(i, j):
#         return i * j
#
#     s = 2 * (inner(a, b) + inner(a, c) + inner(b, c))
#     return s
#
#
# print(rect_paral(2, 4, 6))
# print(rect_paral(5, 8, 2))
# print(rect_paral(1, 6, 8))

# Замыкание функций

# def out(n):
#     def inner(x):
#         return n + x
#
#     return inner
#
#
# a = out(5)
# print(a(10))
#
# b = out(6)
# print(b(10))

# def func(city):
#     s = 0
#
#     def inner():
#         nonlocal s
#         s += 1
#         print(city, s)
#
#     return inner
#
#
# res1 = func('Moscow')
# res1()
# res1()
# res2 = func('Sochi')
# res2()
# res2()
# res1()

# Анонимные функции (lambda)

# print((lambda x, y: x + y)(1, 2))
# print((lambda x, y: x + y)('A', 'B'))
#
# func1 = lambda x, y: x + y
#
# print((lambda a, b, c: a + b + c)(10, 20, 30))
# print((lambda a, b, c=6: a + b + c)(10, 20, 30))
#
# print((lambda **kwargs: kwargs)(1, 2, 3))

# c = (
#     lambda x: x * 2,
#     lambda x: x * 3,
#     lambda x: x * 4,
# )
#
# for i in c:
#     print(i('ABC_'))

# def outer(n):
#     return lambda x: x + n
#
#
# f = outer(43)
# print(f(3))


# outer = (lambda n: lambda x: x + n)
# f = outer(43)
# print(f(3))
#
#
# print((lambda n: lambda x: x + n)(33)(14))
#
# res = (lambda n: lambda x: x + n)(23)(14)
# print(res)

# res = ((lambda a: lambda b: lambda c: a + b + c)(10)(20)(300))


# d = {'a': 10, 'c': 12, 'b': 7}
# lst = list(d.items())
#
# lst.sort(key=lambda i: i[1])
# print(lst)
#
# d2 = dict(lst)
# print(d2)

# players = [
#     {'name': "Антон", 'last name': 'Бирюков', 'rating': 9},
#     {'name': "Алексей", 'last name': 'Бондаренко', 'rating': 10},
#     {'name': "Федор", 'last name': 'Сидоров', 'rating': 4},
#     {'name': "Михаил", 'last name': 'Семенов', 'rating': 6},
# ]
#
# res_1 = sorted(players, key=lambda i: i['last name'])
# res_2 = sorted(players, key=lambda i: i['rating'])
# res_3 = sorted(players, key=lambda i: i['rating'], reverse=True)
#
# print(res_1)


# lst = [lambda x, y: x + y, lambda x, y: x - y, lambda x, y: x * y, lambda x, y: x // y,]
#
# print(lst[0](12, 6))
# print(lst[1](12, 6))
# print(lst[2](12, 6))
# print(lst[3](12, 6))

# d = {
#     1: lambda: print('Январь'),
#     2: lambda: print('Февраль'),
#     3: lambda: print('Март'),
#     4: lambda: print('Апрель'),
#     5: lambda: print('Май'),
#     6: lambda: print('Июнь'),
# }
#
# d[3]()

# def maul(y):
#     return y * 2
#
#
# lst = [1, 3, 7, 12]
#
# print(tuple(map(maul, lst)))
# print(list(map(maul, lst)))
#
# print(list(map(lambda t: t * 2, lst)))
# print(list(map(lambda t: t * 2, [1, 3, 7, 12])))
#
# print(dict(map(lambda t, v: (t, v), [1, 3, 7, 12], [33, 9, 7, 11])))

# t = (2.33, - 4.23, 110.23)
#
# print(tuple(map(lambda x: int(x), t)))
# print(tuple(map(int, t)))

# areas = [3.45682, 5.8773562, 99.409734245]
# print(list(map(round, areas, range(1, 4))))

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
#
# print(list(map(lambda x, y: x + y, l1, l2)))

# t = ('abcde', 'qe', 'ret', 'four')
#
# print(tuple(filter(lambda s: len(s) > 3, t)))

# lst = [44, 21, 66, 73, 89, 100]
# lst2 = list(filter(lambda s: s > 75, lst))
# print(lst2)
#
# import random

# lst = [random.randint(0, 40) for i in range(10)]
# print(lst)
# print(list(filter(lambda s: 10 <= s <= 20, lst)))

# numbers = [45, 55, 60, 37, 100, 105, 220]
#
# print(list(filter(lambda x: x % 15 == 0, numbers)))
# print(list(filter(lambda x: not x % 15, numbers)))

# print(list(map(lambda x: x ** 2, filter(lambda x: x % 2, range(10)))))
# print([x ** 2 for x in range(10) if x % 2])

# Декораторы


# def hello():
#     return 'Hi, friend'
#
#
# def func(a):
#     print('Good')
#     print(a())
#
#
# func(hello)

# def hello():
#     return 'Hi, friend'
#
#
# text = hello
# print(text())


# def my_decorator(one):  # Декорирующая функция
#     def inner():
#         print("-" * 30)
#         one()
#         print("=" * 30)
#     return inner
#
#
# @my_decorator   # Декоратор
# def func_test():    # Декорируемая функция
#     print('Hi, friend')
#
#
# func_test()


# def circle(fn):
#     def wrap():
#         return "(" + fn() + ")"
#
#     return wrap
#
#
# def angle(fn):
#     def wrap():
#         return "<" + fn() + ">"
#
#     return wrap
#
#
# @angle
# @circle
# def expression():
#     return '5 + 2'
#
#
# print(expression())


# def cnt(fn):
#     count = 0
#
#     def wrap():
#         nonlocal count
#         count = count + 1
#         fn()
#         print("Вызов функции: ", count)
#
#     return wrap
#
#
# @cnt
# def hello():
#     print("Hello")
#
#
# hello()
# hello()
# hello()


# def decor(arg_1, arg_2):
#     def args_dec(fn):
#         def wrap(x, y):
#             print(arg_1, x, arg_2, y, "=", end=" ")
#             fn(x, y)
#
#         return wrap
#     return args_dec
#
#
# @decor("Сумма: ", "+")
# def summa(a, b):
#     print(a + b)
#
#
# summa(5, 2)
#

# def multyply(arg):
#     def my_decor(func):
#         def wrap(*args, **kwargs):
#             return arg * func(*args, **kwargs)
#
#         return wrap
#     return my_decor
#
#
# @multyply(3)
# def return_num(num):
#     return num
#
#
#
# print(return_num(5))


# def typed(*args, **kwargs):
#     def wrapper(fn):
#         def wrap(*f_args, **f_kwargs):
#             for i in range(len(args)):
#                 if type(f_args[i]) is not args[i]:
#                     raise TypeError("Неверный тип данных")
#             for k in kwargs:
#                 if type(f_kwargs[k]) is not kwargs[k]:
#                     raise TypeError("Неверный тип данных")
#
#             return fn(*f_args, **f_kwargs)
#
#         return wrap
#
#     return wrapper
#
#
# @typed(int, int, int)
# def type_fn(x, y, z):
#     return x * y * z
#
#
# @typed(str, str, str)
# def type_fn_2(x, y, z):
#     return x + y + z
#
#
# # print(type_fn(3, 4, 5))
# # print(type_fn(3, 4, 'Hello '))
# print(type_fn_2('Hi ', 'Your ', 'Love'))


# СТРОКИ

# print(bin(18))  # Двоичная система исчисления
# print(oct(18))  # Восьмеричная система
# print(hex(18))  # Шестнадцатеричная система
# print()
# print(0b10010)
# print(0b10010 + 0x12 + 18)


# q = "Hi "
# w = 'World '
# e = q + w
# print(e * 3)
# print('o' in e)

# def change(s, old, new):
#     s2 = ''
#     i = 0
#     while i < len(s):
#         if s[i] == old:
#             s2 += new
#         else:
#             s2 += s[i]
#         i += 1
#
#     return s2
#
#
# str1 = 'I know Nython'
# str2 = change(str1, 'N', 'P')
# print(str1)
# print(str2)

# def square(n):
#     """
#     Принимает число n, возвращает квадрат числа n.
#     :param n: Положительное число
#     :return: Квадрат числа
#     """
#     return n ** 2
#
#
# print(square(3))
# print(square.__doc__)

# while True:
#     n = input("> ")
#     if n != "-1":
#         print(ord(n))
#     else:
#         break

# st = 'Test string for me'
# arr = [ord(x) for x in st]
# print(f"Коды: {arr}")
# arr = [int(sum(arr) / len(arr))] + arr
# print(f"Среднее арифметическое: {arr}")
# arr += [ord(x) for x in input('> ')[:3] if ord(x) not in arr]
# print(arr)
# print(arr.count(arr[-1] - 1))
# arr.sort(reverse=True)
# print(arr)

# print(chr(1078))

# a = 122
# b = 97
#
# for i in range(b, a + 1):
#     print(chr(i), end=" ")

# from random import randint
#
# MIN_ASCII = 33
# MAX_ASCII = 126
# SHORT = 6
# LONG = 16
#
#
# def random_password():
#     rand_len = randint(SHORT, LONG)
#     result = ""
#     for i in range(rand_len):
#         result += chr(randint(MIN_ASCII, MAX_ASCII))
#     return result
#
#
# print('Случайный пароль: ', random_password())


# s = "one two"
# one = s[:s.find(" ")]
# two = s[s.find(" ") + 1:]
# print(two + " " + one)

# st = 'I am learning Python. hello, WORLD!'
# print(st[:st.find('h')] + st[st.rfind('h') + 1:])


# str1 = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования"
# print(str1.replace("Nython", "Python", 2))


# st = input("введите ФИО: ").split()
# print(f'{st[0]} {st[1][0]}. {st[2][0]}.')

# ********

# Регулярные выражения

# ********

# import re
# from itertools import count
# from os import close
# from tkinter.font import names

# s = 'Я ищу совпадени_я в 2025 году. И я их найду в 2 счёта.'
# # reg = '[2025]'
# # # reg = '[0-3]'
# # reg = '[0-9]' * 4
# # reg = '[0-9]...'
# # reg = r'\d'   # выводит цифры
# # reg = r'\D'   # выводит все кроме цифр
# # reg = r'\s'   # выводит все пробелы
# # reg = r'\S'     # выводит все кроме пробелов
# reg = r'\w+'     # выводит все строки, цифры и нижние пробелы
#
#
# # # reg = '[А-яËё]'     # русский алфавит
# # reg = '[A-Za-z]'     # латинский алфавит
# #
# #
# # # print(re.findall(reg, s.lower()))  # находит все совпадения
# # # print(re.search(reg, s))  # расположение первого совпадения
# # # print(re.split(reg, s))     # разбивает строку по символу
# # # print(re.sub(reg, '!', s))
# #
# print(re.findall(reg, s))
#
# # st = 'Час в 24-часовом формате от 00 до 23. 2021-06-15121:45. Минуты, в диапазоне от 00 до 59. 2021-06-15Т01Ж09'
# # reg = '[0-2][0-9]:[0-5][0-9]'
# # print(re.findall(reg, st))

# st = 'author=Пушкин А.С; title = Евгений Онегин; price =200; year= 1883'
# # reg = r"\w+\s*=\s*\w+\s*\w+\.?\w?\.?"
# reg = r"\w+\s*=[^;]+"
# print(re.findall(reg, st))


# def validate_login(login):
#     return re.findall(r"^[A-Za-z0-9_-]{3,16}$", login)
#
#
# print(validate_login('Python_master'))
# print(validate_login('P!!yt!!!!'))
# print(validate_login('P123yt54'))


# text = "<body>Пример жадного совпадения соотвествия выражений</body>"
# print(re.findall("<.*?>", text))
# # ? - добавление знака вопроса - по минимальному значению

# st = 'Jack = 4, Marie = 7.6, Bob = 2.0F'
# reg = r"\w+\s*=\s*\d[.\w+]*"
# print(re.findall(reg, st))


# st = 'Jack, Marie, Bob'
# reg = r"Jack|Marie|Bob|Vera"

# print(re.findall(reg,st))

# +++++++++
# РЕКУРСИЯ
# +++++++++

# def elevator(n):
#     if n == 0:
#         print("How are you?")
#         return
#     print("->>", n)
#     elevator(n - 1)
#     print(n, end=" ")
#
#
# n1 = int(input("Get: "))
# elevator(n1)


# def sum_list(lst):
#     # res = 0
#     # for i in lst:
#     #     res += i
#     # return res
#     if len(lst) == 1:
#         return lst[0]
#     else:
#         return lst[0] + sum_list(lst[1:])
#
#
# print(sum_list([1, 2, 2, 3, 5]))

# def to_str(n, base):
#     convert = "0123456789ABCDEF"
#     if n < base:
#         return convert[n]
#     else:
#         return to_str(n // base, base) + convert[n % base]
#
#
# print(to_str(254, 16))


# names = ["Adam", ["Bob", ["Chet", "Cat"], "Barb", "Berb"], "Alex", ["Bea", "Bill"], "Ann"]
# print(len(names))
# # print(names[0])
# print(isinstance(names[1][1], list))


# def count_items(item_list):
#     count = 0
#     for item in item_list:
#         if isinstance(item, list):
#             count += count_items(item)
#         else:
#             count += 1
#
#     return count
#
#
# print(count_items(names))

# ФАЙЛЫ

# f = open(r"/Volumes/Work/Python522/text.txt", 'r')
# print(*f)
# # f.close()
# # print(f.closed)
# # print(f.name)

# f = open("text2.txt")
# # print(f.read())
#
# # print(f.readline(12))
#
# print(f.readlines())
# f.close()

# count = 0
# f = open("text2.txt")
# for line in f:
#     print(line)
#     count += 1
# f.close()
# print(count)

# f = open("text_3.txt", "w")
# f.write("How are you?")
# f.close()

# lines = ['This is line 1', 'This is line 1', 'This is line 1']
#
# f = open("text_3.txt", "a")
# f.writelines(lines)
# f.close()

# file = 'note.txt'
# f = open(file, "w")
# f.write("Замена строки в текстовом файле;\n"
#         "Изменить строку в списке;\n"
#         "Записать список в файле;")
# f.close()
#
# f = open(file)
# data = f.readlines()
# print(data)
# data[1] = "Hello World;\n"
# print(data)
# f.close()
#
# f = open(file, "w")
# f.writelines(data)
# f.close()

# f = open("text_3.txt", "w")
# lst = [i for i in range(1, 100, 4)]
# print(lst)
# for index in lst:
#     f.write(str(index + "\t"))
# f.close()

# f = open("text.txt", "w+")
# print(f.write("How are you?"))
# print(f.seek(3))
# print(f.write(" - new string - "))
# print(f.tell())
# f.close()

# with open("text.txt", "w") as f:
#     print(f.write('122334556'))
# print(f.closed)
#
# with open("text.txt") as f:
#     print(f.read())

# file_name = "long.txt"
# with open(file_name, "w+") as f:
#     f.write("Файл — именованная область данных на носителе информации, используемая как базовый объект "
#             "взаимодействия с данными в операционных системах.")
#
#
# def longest_word(file):
#     with open(file) as text:
#         lst = text.read().split()
#         max_len = len(max(lst, key=len))
#         res = [word for word in lst if len(word) == max_len]
#         return res[0] if len(res) == 1 else res
#
#
# print(longest_word(file_name))


# text = "Строка № 1\nСтрока № 2\nСтрока № 3\nСтрока № 4\nСтрока № 5\nСтрока № 6\nСтрока № 7\n"
# with open('one.txt', 'w+') as f:
#     f.write(text)
#
# with open('one.txt', 'r') as fr, open('two.txt', 'w') as fw:
#     for line in fr:
#         line = line.replace("Строка", "Линия")
#         fw.write(line)


# МОДУЛИ OS и OS.PATH

import os

# os.rmdir('folder')
# os.makedirs('1/2/3')
# os.remove('two.txt')
os.rename('one.txt', 'one_1.txt')


