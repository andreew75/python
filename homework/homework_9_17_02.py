# Костромин Андрей Львович

from random import randint

# Вариант 1:


def random_tpl():
    tpl_1 = tuple((randint(0, 5)) for _ in range(10))
    tpl_2 = tuple((randint(-5, 0)) for _ in range(10))
    tpl_3 = tpl_2 + tpl_1
    print(tpl_1)
    print(tpl_2)
    print(tpl_3)
    print("0 =", tpl_3.count(0))


random_tpl()


# Вариант 2:


# def generate_tuple(start, end, length=10):
#     return tuple(randint(start, end) for _ in range(length))
#
#
# tpl_1 = generate_tuple(0, 5)
# tpl_2 = generate_tuple(-5, 0)
# tpl_3 = tpl_1 + tpl_2
#
# print(tpl_1)
# print(tpl_2)
# print(tpl_3)
# print("0 =", tpl_3.count(0))
