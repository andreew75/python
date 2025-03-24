# Костромин Андрей Львович

from math import pi, sqrt

print("Вычисление площади фигур")
while True:
    try:
        choice = int(input("""Выберите фигуру: 
1 - Треугольник
2 - Прямоугольник
3 - Круг """))
        if choice in [1, 2, 3]:
            break
        else:
            print("Ошибка ввода! Введите значение от 1 до 3")
    except ValueError:
        print("Введите корректное значение")

if choice == 1:
    while True:
        try:
            side_a = int(input("Введите сторону А: "))
            side_b = int(input("Введите сторону В: "))
            side_c = int(input("Введите сторону С: "))
            if side_a > 0 and side_b > 0 and side_c > 0:
                # Проверка на неравенство треугольника
                if side_a + side_b > side_c and side_a + side_c > side_b and side_b + side_c > side_a:
                    break
                else:
                    print("Стороны не могут составить треугольник. Введите другие значения.")
            else:
                print("Ошибка ввода! Стороны должны быть больше нуля")
        except ValueError:
            print("Введите корректное значение.")

    s = (side_a + side_b + side_c) / 2
    area = sqrt(s * (s - side_a) * (s - side_b) * (s - side_c))
    print("Площадь треугольника равна:", round(area, 2))

if choice == 2:
    while True:
        try:
            side_a = int(input("Введите сторону А: "))
            side_b = int(input("Введите сторону В: "))
            if side_a > 0 and side_b > 0:
                break
            else:
                print("Ошибка ввода! Стороны должны быть больше нуля")
        except ValueError:
            print("Введите корректное значение.")

    print("Площадь прямоугольника равна:", round(side_a * side_b, 2))

if choice == 3:
    while True:
        try:
            r = int(input("Введите радиус окружности: "))
            if r > 0:
                break
            else:
                print("Ошибка ввода! Радиус должен быть больше нуля")
        except ValueError:
            print("Введите корректное значение")

    print("Площадь круга равна:", round(pi * r**2, 2))
