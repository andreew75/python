# Костромин Андрей Львович

res = 0
while True:
    try:
        a = [int(input('- > ')) for _ in range(int(input("Введите количество чисел: ")))]
        break
    except ValueError:
        print("Ошибка: необходимо вводить целые числа цифрами!")

for i in a:
    if i < 0:
        res += i

if res < 0:
    print("Сумма отрицательных чисел: ", res)
else:
    print("Вы не ввели ни одного отрицательного числа!")
