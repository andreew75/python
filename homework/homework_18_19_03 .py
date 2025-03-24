# Костромин Андрей Львович


file = 'text_str.txt'
text = "-> Купить горный велосипед;\n-> Прочитать умную книгу;\n-> Поздравить любимую тещу;\n"

with open(file, 'w+') as f:
    f.write(text)

with open(file, 'r') as f:
    data = f.readlines()

while True:
    try:
        choose_1 = int(input(f"Поменяйте местами любые две строки (1-3):\n{text}\nВведите первое значение:\n")) - 1
        choose_2 = int(input("Введите второе значение:\n")) - 1
        if 0 <= choose_1 < len(data) and 0 <= choose_2 < len(data):
            break
        else:
            print("Введите значение от 1 до 3")
    except ValueError:
        print("Ошибка ввода данных")

with open(file, 'w+') as f:
    data[choose_1], data[choose_2] = data[choose_2], data[choose_1]
    f.writelines(data)
with open(file, 'r') as f:
    print("Изменения внесены успешно!")
    print(f.read())
