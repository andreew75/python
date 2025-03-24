# Костромин Андрей Львович

res, number = 1, False

while True:
    try:
        d = int(input("Введите любое целое число цифрами (0 завершит ввод): "))
        if d == 0 and not number:
            print("Сначала введите число кроме 0.")
            continue
        elif d == 0:
            break
        res *= d
        number = True
    except ValueError:
        print("Недопустимое значение! Введите целое число цифрами.")

print("Общее произведение чисел:", res, "\nРабота программы завершена!")


