# Костромин Андрей Львович

from math import pi, sqrt


def triangle(a, b, c):
    s = (a + b + c) / 2
    return round(sqrt(s * (s - a) * (s - b) * (s - c)), 2)


def rectangle(a, b):
    return round(a * b, 2)


def circle(r):
    return round(pi * r**2, 2)


def get_correct(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Ошибка ввода! Значения должны быть больше нуля")
        except ValueError:
            print("Введите корректное значение.")


print("----- Вычисление площади фигур -----")
while True:
    try:
        choice = int(input("Выберите фигуру: \n1 - Треугольник\n2 - Прямоугольник\n3 - Круг\n: "))
        if choice in [1, 2, 3]:
            break
        else:
            print("Ошибка ввода! Введите значение от 1 до 3")
    except ValueError:
        print("Введите корректное значение")

if choice == 1:
    while True:
        side_a = get_correct("Введите сторону А: ")
        side_b = get_correct("Введите сторону В: ")
        side_c = get_correct("Введите сторону С: ")
        # Проверка на неравенство треугольника
        if side_a + side_b > side_c and side_a + side_c > side_b and side_b + side_c > side_a:
            break
        else:
            print("Стороны не могут составить треугольник. Введите другие значения.")
    print("Площадь треугольника равна:", triangle(side_a, side_b, side_c))

elif choice == 2:
    side_a = get_correct("Введите сторону А: ")
    side_b = get_correct("Введите сторону В: ")
    print("Площадь прямоугольника равна: ", rectangle(side_a, side_b))

elif choice == 3:
    radius = get_correct("Введите радиус окружности: ")
    print("Площадь круга равна:", circle(radius))
