# try:
#     n = int(input("Напишите тексте количество чисел: "))
#     numbers = [int(input("-> ")) for _ in range(n)]
# except ValueError:
#     print("Ошибка: необходимо вводить целые числа!")
#     exit()
#
# negative_sum = sum(x for x in numbers if x < 0)
#
# if negative_sum < 0:
#     print("Сумма отрицательных чисел:", negative_sum)
# else:
#     print("Вы не ввели ни одного отрицательного числа")


# summa = 0
# while True:
#     try:
#         number_of_days = int(input("Напишите тексте количество дней для учета расходов на обеды: "))
#         if number_of_days >= 0:
#             break
#         else:
#             print("Количество дней не может быть отрицательным. Попробуйте снова.")
#     except ValueError:
#         print("Пожалуйста, Напишите тексте число.")
#
# for i in range(1, number_of_days + 1):
#     while True:
#         try:
#             expense = float(input(f"Напишите тексте расходы на обед за день {i}: "))
#             if expense >= 0:
#                 break
#             else:
#                 print("Расходы не могут быть отрицательными. Пожалуйста, Напишите тексте положительное значение.")
#         except ValueError:
#             print("Неверный ввод! Пожалуйста, Напишите тексте числовое значение расходов.")
#     print(f"За день {i} зарегистрированы расходы на обед в размере {expense} рублей.")
#     summa += expense
# print("\nВсе расходы на обеды успешно зарегистрированы. Потрачено на обеды: ", summa)

# numbers = [10, 20, 30, 40, 50]
# slice_of_numbers = numbers[2:4]  # Элементы с индексами 1, 2, 3
# print(slice_of_numbers)  # Вывод: [20, 30, 40]

# n = [1, 4, 5, 8]
# print(len(n))
# n[2:2] = [20]
# print(n[1:3])

# purchase = int(input("Напишите тексте сумму покупки: "))
# age = int(input("Напишите тексте Ваш возраст: "))
# if purchase > 100 and age > 65:
#     print("Вам предоставляется скидка 15%")
# elif purchase > 100:
#     print("Вам предоставляется скидка 10%")
# else:
#     print("Спасибо за покупку!")

# name = str(input("Напишите тексте слово: "))
# reversed_name = name[::-1]
# print(reversed_name)


# def get_sum(a, b):
#     print(a + b)
#
#
# x = 4
# y = 6
# get_sum(x, y)
#
# q = 8
# w = 12
# get_sum(q, w)

# def result(a, b):
#     if a > b:
#         return a - b
#     else:
#         return a + b
# 
# 
# number_1 = int(input("Напишите тексте число: "))
# number_2 = int(input("Напишите тексте число: "))
# 
# print(result(number_1, number_2))


# text_1 = input("Напишите текст: ")
# text_2 = input("Напишите текст: ")
#
# set_text_1 = set(text_1.split())
# set_text_2 = set(text_2.split())
#
# both_texts = set_text_1 & set_text_2
# only_1 = set_text_1 - set_text_2
# only_2 = set_text_2 - set_text_1
#
# print(both_texts)
# print(only_1)
# print(only_2)


# discount = 20.5
# total_amount = 150.75
# formatted_string = f"Ваша скидка составила: ${discount:.2f}. Итоговая сумма: ${total_amount:.2f}."
# print(formatted_string)

# """
# так можно оставлять
# длинные комментарии
# и пайтон их игнорирует
#
# """
# from itertools import count
# from operator import index


# name = input("Введите строку: ")
# print(name[::-1])


# vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
# consonants = "бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ"
#
# # Запрашиваем ввод у пользователя
# paragraph = input("Введите абзац текста: ")
#
# # Подсчитываем гласные и согласные
# vowel_count = sum(1 for char in paragraph if char in vowels)
# consonant_count = sum(1 for char in paragraph if char in consonants)
#
# # Выводим результат
# print(f"Гласных: {vowel_count}")
# print(f"Согласных: {consonant_count}")


# def minimum(arr):
#     return min(arr)
#
#
# def maximum(arr):
#     return max(arr)
#
#
# minimum([4, 6, 2, 1, 9, 63, -134, 566])
# maximum([4, 6, 2, 1, 9, 63, -134, 566])

#
# def reverse_seq(n):
#     return range(n, 0, -1)
#
#
# print(reverse_seq(8))

# def sum_array(arr):
#     return sum(arr)  # Проверяем, пустой ли массив
#
#
# print(sum_array([2, 4, 8, -9]))

# def summation(num):
#     total = 0
#     for i in range(1, num + 1):
#         total += i
#     return total

# def summation(num):
#     return sum(range(1, num+1))
#
#
# print(summation(9))

# def rental_car_cost(d):
#     rent = 40
#     if d >= 7:
#         return rent * d - 50
#     elif 3 <= d < 7:
#         return rent * d - 20
#     return rent * d
#
#
# print(rental_car_cost(2))

# def basic_op(operator, value1, value2):
#     if operator == '+':
#         return value1 + value2
#     elif operator == '-':
#         return value1 - value2
#     elif operator == '*':
#         return value1 * value2
#     elif operator == '/':
#         return (value1 / value2)
#
#
# print(basic_op('/', 10, 5))

# def square_digits(num):
#     return int(''.join(str(int(i) ** 2) for i in str(num)))
#
#
# print(square_digits(1991))


# import math
#
#
# def is_square(n):
#     return n > -1 and math.sqrt(n) % 1 == 0
#
#
# print(is_square(36))

# def high_and_low(numbers):
#     numbers = [int(i) for i in numbers.split()]
#     return f"{max(numbers)} {min(numbers)}"
#
#
# print(high_and_low("1 2 3 4 5"))

######

# def lovefunc(flower1, flower2):
#     if flower1 % 2 == 1 and flower2 % 2 == 0 or flower2 % 2 == 1 and flower1 % 2 == 0:
#         return True
#     else:
#         return False

# def lovefunc(flower1, flower2):
#     return (flower1 + flower2) % 2 == 1
#
#
# print(lovefunc(6, 8))
#
# #######

# def remove_char(s):
#     return s[1:-1]
#
#
# print(remove_char('Hello World'))

# import math
#
#
# def grow(arr):
#     return math.prod(arr)
#
#
# print(grow([8, 2, 3, 4]))


# from math import floor
#
#
# def litres(time):
#     return floor(0.5 * time)
#
#
# print(litres(9.3))


# def abbrev_name(name):
#     first, last = name.split()  # Разбиваем строку на два слова
#     return f"{first[0].upper()}.{last[0].upper()}"
#
#
# print(abbrev_name('Sam Harris'))

# def count_sheep(n):
#     return ''.join(f"{i} sheep..." for i in range(1, n + 1))
#
#
# print(count_sheep(2))

# def xo(s):
#     return s.lower().count('x') == s.lower().count('o')
#
#
# print(xo('ooxoxoxxxoqw'))

#
# def get_grade(s1, s2, s3):
#     score = (s1 + s2 + s3) / 3
#     if 90 <= score <= 100:
#         return "A"
#     if 80 <= score < 90:
#         return "B"
#     if 70 <= score < 80:
#         return "C"
#     if 60 <= score < 70:
#         return "D"
#     if 0 <= score < 60:
#         return "F"
#
#
# print(get_grade(92, 88, 95))

# def string_to_array(s):
#     return s.split() if s else [""]
#
#
# print(string_to_array("Robin Singh"))

# def digitize(n):
#     return [int(i) for i in str(n)][::-1]
#
#
# print(digitize(479164332))


# def opposite(number):
#     return -number
#
#
# print(opposite(1425.2222))

# def odd_or_even(arr):
#     if sum(arr) % 2 == 0:
#         return "even"
#     elif sum(arr) % 2 == 1:
#         return "odd"
#     else:
#         return "even"
#
#
#     return 'even' if sum(arr) % 2 == 0 else 'odd'
#
#
# print(odd_or_even([0]))

#
# def reverse_words(text):
#     return ' '.join(s[::-1] for s in text.split(' '))
#
#
# print(reverse_words('My code is fine'))


# def maximum(a, b=22):
#     return a if a > b else b
#
#
# print(maximum(19))

# def are_you_playing_banjo(name):
#     return name + ' plays banjo' if name[0] == 'r' or name[0] == 'R' else name + ' does not play banjo'
#
#
# print(are_you_playing_banjo('Sonin'))

# def make_negative(number):
#     return number if number < 0 - number else - number
#
#
# print(make_negative(0))

# def filter_list(l):
#     return [x for x in l if not isinstance(x, str)]

# filter_list = [1, 2, 'aasf', '1', '123', 123]
# lst2 = list(filter(lambda s: not isinstance(s, str), filter_list))
# print(lst2)
# # print([1, 2, 'aasf', '1', '123', 123])

# def better_than_average(class_points, your_points):
#     return your_points > sum(class_points) / len(class_points)
#
#
# print(better_than_average([100, 40, 34, 57, 29, 72, 57, 88], 22))


# def make_upper_case(s):
#     return s.upper()

# def fake_bin(x):
#     return ''.join(map(lambda c: '0' if int(c) < 5 else '1', x))
#
#
# print(fake_bin("800857237867"))


# def tower_builder(n_floors):
#     result = []
#     for i in range(n_floors):
#         spaces = ' ' * (n_floors - i - 1)
#         stars = '*' * (2 * i + 1)
#         result.append(spaces + stars + spaces)
#     return result

# def invert(lst):
#     return [-i for i in lst]
#
#
# print(invert([1, -2, 3, 4, 5]))


# def sort_array(source_array):
#     odd_sorted = iter(sorted(num for num in source_array if num % 2 != 0))
#     return [next(odd_sorted) if num % 2 != 0 else num for num in source_array]
#
#
# print(sort_array([5, 8, 6, 3, 4]))


# def array_diff(a, b):
#     return [x for x in a if x not in b]
#
#
# print(array_diff([1, 2, 2, 2, 3], [2]))

#
# def check(seq, elem):
#     return elem in seq
#
#     # for x in seq:
#     #     if x == elem:
#     #         return True
#     #
#     # return False
#
#
# print(check([66, "codewars", 11, "alex loves pushups"], "alex loves pushups"))


# def double_char(s):
#     return ''.join([i * 2 for i in s])
#
#
# print(double_char('String'))

# n = (lambda a: lambda b: lambda c: a + b + c)(1)(2)(3)
#
# print(n)

# def find_uniq(arr):
#     return [n for n in set(arr) if arr.count(n) == 1][0]
#
#
# print(find_uniq([1, 1, 1, 2, 1, 1]))


# favorite_language = ' python '
# favorite_language = favorite_language.strip()
# print(favorite_language)

# def positive_sum(arr):
#     # a = []
#     # for i in arr:
#     #     if i > 0:
#     #         a.append(i)
#     # return sum(a)
#     return sum(x for x in arr if x > 0)
#
#
# print(positive_sum([1, -4, 7, 12]))


# def remove_every_other(my_list):
#     return my_list[1::2]
#
#
# print(remove_every_other(["Keep", "Remove", "Keep", "Remove"]))


# lts = [1, 2, 3, 4, 3, 3]
# for i in lts:
#     lts.remove(3)
# print(lts)
#
# lts.insert(0, 6)
# print(lts)


# cars = ['bmw', 'audi', 'toyota', 'subaru']
# print(cars)
# print(sorted(cars))
#
# cars.sort(reverse=True)
# print(cars)
# print(sorted(cars))


# players = [
#     {'name': "Антон", 'last name': 'Яблоков', 'rating': 9},
#     {'name': "Алексей", 'last name': 'Роднин', 'rating': 10},
#     {'name': "Федор", 'last name': 'Сидоров', 'pating': 4},
#     {'name': "Михаил", 'last name': 'Ежкин', 'rating': 6}
# ]
#
# res1 = sorted(players, key=lambda last_name: last_name["last name"])
# print(res1)


# lst = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
# lst2 = (list(filter(lambda s: s > 75, lst)))
# print(lst2)

#
# def binary_array_to_number(arr):
#     return int(''.join(map(str, arr)), 2)
#
#     # a = ''.join(map(str, arr))
#     # return int(a, 2)
#
#
# print(binary_array_to_number([1, 1, 1, 1]))

# def two_sum(numbers, target):
#     for i in range(len(numbers)):
#         for j in range(i + 1, len(numbers)):
#             if numbers[i] + numbers[j] == target:
#                 return i, j
#
#
# print(two_sum([7, 2, 4], 9))


# def validate_pin(pin):
#     return len(pin) in (4, 6) and pin.isdigit()
#
#
# print(validate_pin('123473'))

# def quarter_of(month):
#     if 1 <= month <= 3:
#         return 1
#     if 4 <= month <= 6:
#         return 2
#     if 7 <= month <= 9:
#         return 3
#     else:
#         return 4

# def quarter_of(month):
#     return (month + 2) // 3
#
#
# print(quarter_of(2))

# def maps(a):
#     return list(map(lambda s: s * 2, a))
#
#
# print(maps([1, 2, 3]))


# def enough(cap, on, wait):
#     # return 0 if wait < cap - on else wait - (cap - on)
#     return max(0, wait - (cap - on))
#
#
# print(enough(10, 5, 5))

# def to_jaden_case(string):
#     return ' '.join(word.capitalize() for word in string.split())
#
#
# print(to_jaden_case("How can mirrors be real if our eyes aren't real"))


# def is_even(n):
#     return n % 2 == 0
#
#
# print(is_even(5))

#
# def find_smallest_int(arr):
#     return min(arr)
#
#
# print(find_smallest_int([34, 15, 88, 2]))


# def remove_exclamation_marks(s):
#     return s.replace("!", "")
#
#
# print(remove_exclamation_marks("hello! World!"))

# def divisors(n):
#     return len([x for x in range(1, n + 1) if n % x == 0])
#
#
# print(divisors(12))


# def get_sum(a, b):
#     # if a == b:
#     #     return a
#     # if a > b:
#     #     return sum([x for x in range(b, a) if b < a]) + a
#     # else:
#     #     return sum([x for x in range(a, b) if a < b]) + b
#
#     return sum(range(min(a, b), max(a, b) + 1))
#
#
# print(get_sum(-3, 10))

# def str_count(string, letter):
#     return string.count(letter)
#
#
# print(str_count("Helllo", 'l'))

# def descending_order(num):
#     return int("".join(sorted(([x for x in str(num)[::-1]]), reverse=True)))
#
#
# print(descending_order(145263))

# def count_by(x, n):
#     return [x * i for i in range(1, n + 1)]
#
#
# print(count_by(2, 5))


# def boolean_to_string(b):
#     return str(b)
#
#
# print(boolean_to_string(False))

# def check_for_factor(base, factor):
#     return base % factor == 0
#
#
# print(check_for_factor(9, 2))

# def is_uppercase(inp):
#     return inp.upper() == inp
#
#
# print(is_uppercase("D"))


# def square_sum(numbers):
#     return sum(i ** 2 for i in numbers)
#
#
# print(square_sum([1, 2, 2]))
#
# def between(a, b):
#     return list(range(a, b + 1))
#
#
# print(between(1, 4))

# import re
#
#
# def solution(s):
#     pattern = r"([A-Z])"
#     return re.sub(pattern, r' \1', s)
#
#
# print(solution("camelCasing"))

# def bmi(weight, height):
#     if weight / height ** 2 <= 18.5:
#         return "Underweight"
#     elif weight / height ** 2 <= 25.0:
#         return "Normal"
#     elif weight / height ** 2 <= 30.0:
#         return "Overweight"
#     else:
#         return "Obese"
#
#
# print(bmi(72, 1.75))

# def find_short(s):
#     return min(len(i) for i in s.split())
#
#
# print(find_short("bitcoin take over the world maybe who knows perhaps"))

# def sequence_sum(begin_number, end_number, step):
#     return sum(range(begin_number, end_number + 1, step))
#
#
# print(sequence_sum(2, 6, 2))

# def cockroach_speed(s):
#     return int(s * 27.777778)
#
#
# print(cockroach_speed(1.08))

# import math
#
#
# def find_next_square(sq):
#     if int(math.sqrt(sq)) ** 2 == sq:
#         return int(math.sqrt(sq) + 1) ** 2
#     else:
#         return -1
#
#
# print(find_next_square(121))
#
# def switch_it_up(number):
#     # numbers =
#     # {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five',
#     # 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 0: 'Zero'}
#     # for i in numbers:
#     #     if i == number:
#     #         return numbers[i]
#     return ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine'][number]
#
#
# print(switch_it_up(6))

# import re
#
# s = "Я ищу совпадения в 2025 году. И я их найду в 2 счёта. 6789. [Hel-lo] Wor_ld 2000000000000000000"
# reg = r"\d+\s\w+"
#
# print(re.findall(reg, s))

# def is_triangle(a, b, c):
#     return a + b > c and b + c > a and c + a > b
#
#
# print(is_triangle(1, 2, 2))


def to_alternating_case(string):
    return string.swapcase()


print(to_alternating_case("hello world"))
