# def say_hello(name):
#     return f"Hello, {name}"
# print(say_hello("Mr. Spock"))

# dict= {"London": "Temza", "Russia": "Volga", "Ukraine": "Dnepr"}

# for k, v in dict.items():
#     print(f"{v} течет в {k}")

# for k in dict:
#     print(k)

# for v in dict.values():
#     print(v)

# import string
# from collections import Counter

# def word_frequency(text):
#     # Удаляем пунктуацию и приводим к нижнему регистру
#     translator = str.maketrans('', '', string.punctuation)
#     cleaned_text = text.translate(translator).lower()

#     # Разбиваем на слова и считаем частоту
#     words = cleaned_text.split()
#     word_counts = Counter(words)

#     # Сортируем словарь по убыванию частоты
#     sorted_words = sorted(word_counts.items(), key=lambda item: (-item[1], item[0]))

#     # Формируем итоговый словарь (если нужен именно dict)
#     result_dict = dict(sorted_words)

#     # Выводим топ-3 слов
#     top_3 = [word for word, count in sorted_words[:3]]
#     print("Топ-3 слов:", top_3)

#     return result_dict

# print(word_frequency("Привет, привет, как дела? Как твои дела, друг?"))

# num1 = int(input("Введите число: "))
# num2 = int(input("Введите число: "))
# print("Сумма:", num1 + num2)

# radius = int(input("Введите радиус круна: "))
# square = 3.14 * radius ** 2
# print(square)

# word = "Annas"
# if word.lower() == word[::-1].lower():
#     print(True) 
# else:
#     print(False)

# age = int(input("Введите возраст: "))
# if age >= 18:
#     print("Доступ разрешен!")
# else:
#     print("Доступ запрещен!")

# import re

# def is_palidrome(text):
#     # cleaned_text = text.replace(" ", "").lower()
#     cleaned_text = re.sub(r'[^a-zа-яË]', "", text.lower())
#     return cleaned_text == cleaned_text[::-1]


# print(is_palidrome("Кит на море романтик"))

# lst = ["Мама", "мыла", "раму"]
# print(" ".join(lst))

# def has_duplicates(text):
#     for i in range(1, len(text)):
#         if text[i] == text[i - 1]:
#             return True
#         return False


# print(has_duplicates('world'))


# def bool_to_word(b):
#     return 'Yes' if b == True else 'No'


# print(bool_to_word(False))

# def count_letter(text):
#     glas = "aeiouаеёиоуыэюя"
#     soglas = "bcdfghjklmnpqrstvwxyzбвгджзйклмнпрстфхцчшщ"
#     count = {'гласные': 0, 'согласные': 0}
#     for char in text.lower():
#         if char in glas:
#             count['гласные'] += 1
#         else:
#             if char in soglas:
#                 count['согласные'] += 1
#     return count

# print(count_letter('ждем всех домой'))


# def reverse_words(text):
#     lst_words = text.split()

#     return lst_words

# print(reverse_words('hello, world!'))

# import random
#
# secret_number = random.randint(1, 100)
# attempt = 0
#
# while True:
#     try:
#         guess = int(input("Угадай число от 1 до 100: "))
#         if guess < 0 or guess > 100:
#             print("Введите число от 1 до 100")
#         else:
#             while True:
#                 attempt += 1
#                 if guess > secret_number:
#                     print("Меньше!")
#                 elif guess < secret_number:
#                     print("Больше!")
#                 else:
#                     print(f"Угадано! Число {secret_number} c {attempt} попытки")
#                 break
#     except ValueError:
#         print("Введите число от 1 до 100")

# numbers = [3, 1, 4, 1, 5, 9, 2]
# # sort_numbers = []
# # for num in numbers:
# #     if num not in sort_numbers:
# #         sort_numbers.append(num)
# numbers = [3, 1, 4, 1, 5, 9, 2]
# unique_numbers = set(numbers)
# list_numbers = list(unique_numbers)
# print(list_numbers)

# def sum_list(numbers):
#     total = []
#     for num in numbers:
#         if isinstance(num, (int, float)):
#             total.append(num)
#     return sum(total)

# print(sum_list([1, 2, "3", "a", 4]))

# from collections import Counter

# def find_unique(numbers):
#     count = Counter(numbers)
#     return [num for num in numbers if count[num] == 1]

# print(find_unique([1, 2, 2, 3, 4, 4, 5]))

# def sort_by_length(words):
#     return sorted(words, key=lambda x: len(x))

# print(sort_by_length(["яблоко", "груша", "а", "арбуз"]))
import re

st = "+7 499 456-45-78, +74994564578, +7 (499) 456 45 78, 74994564578"

reg = r"\+?\d{11}"

print(re.findall(reg, st))