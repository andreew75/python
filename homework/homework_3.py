# Костромин Андрей Львович

money = int(input("Введите число от 1 до 99: "))
if 1 <= money <= 99:
    if 11 <= money % 100 <= 19:     # Числа от 11 до 19
        print("копеек")
    elif money % 10 == 1:           # Числа, оканчивающиеся на 1
        print("копейка")
    elif 2 <= money % 10 <= 4:      # Числа, оканчивающиеся на 2, 3 или 4
        print("копейки")
    else:                           # Все остальные числа
        print("копеек")
else:
    print("Ошибка. Вы ввели число вне диапазона от 1 до 99")
