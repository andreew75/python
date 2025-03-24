# Костромин Андрей Львович


sales = {
    "John": {'N': 3056, 'S': 8463, 'E': 8441, 'W': 2694},
    "Tom": {'N': 4832, 'S': 6786, 'E': 4737, 'W': 3612},
    "Anna": {'N': 5239, 'S': 4802, 'E': 5820, 'W': 1859},
    "Fiona": {'N': 3904, 'S': 3645, 'E': 8821, 'W': 2451},
}

while True:
    name = input("Введите имя продавца (John, Tom, Anna, Fiona): ")
    if name in sales:
        break
    else:
        print("Введите имя из списка!")
while True:
    region = input("Введите регион (N, S, E, W): ")
    if region in sales[name]:
        break
    else:
        print("Регион не найден!")

print(sales[name][region])

try:
    new_value = int(input("Введите новое значение: "))
    sales[name][region] += new_value
    print("Успешно! Обновленное значение: ", sales[name][region])
    print("Обновленные данные: ", sales[name])
except ValueError:
    print("Ошибка! Введите целое число.")
