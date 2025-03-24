# Костромин Андрей Львович

# Вариант с глобальной переменной:

s = None


def rect_parallel(a, b, c):
    global s
    s = 2 * (a * b + a * c + b * c)


rect_parallel(2, 4, 6)
print(s)
rect_parallel(5, 8, 2)
print(s)
rect_parallel(1, 6, 8)
print(s)


# Вариант с нелокальной переменной:

def rect_parallel(a, b, c):
    s = None

    def inner():
        nonlocal s
        s = 2 * (a * b + a * c + b * c)

    inner()
    return s


print(rect_parallel(2, 4, 6))
print(rect_parallel(5, 8, 2))
print(rect_parallel(1, 6, 8))