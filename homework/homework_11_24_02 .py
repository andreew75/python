# Костромин Андрей Львович

# Вариант без проверки исключений:

students = {
    input('Имя студента: '): int(input('Балл: ')) for _ in range(int(input("Количество студентов в группе: ")))
            }

average_score = sum(students.values()) / len(students)
print("Средний балл: ", average_score)

print("Студенты с баллом выше среднего: ")
for x, y in students.items():
    if y > average_score:
        print(x)


# Вариант c проверкой исключений:

# def valid_input():
#     while True:
#         try:
#             score = int(input('Балл (0-12): '))
#             if 0 <= score <= 12:
#                 return score
#             else:
#                 print("Ошибка! Введите количество баллов в указанном диапазоне.")
#         except ValueError:
#             print("Ошибка! Введите целое число от 0 до 12.")
#
#
# while True:
#     try:
#         num_students = int(input("Количество студентов в группе: "))
#         if num_students > 0:
#             break
#         else:
#             print("Ошибка! Должен быть хотя бы один студент.")
#     except ValueError:
#         print("Ошибка! Введите целое число.")
#
#
# students = {
#     input('Имя студента: '): valid_input() for _ in range(num_students)
# }
#
# average_score = sum(students.values()) / len(students)
# print("Средний балл: ", average_score)
#
# print("Студенты с баллом выше среднего: ")
# best_students = [x for x, y in students.items() if y > average_score]
# print(best_students)
