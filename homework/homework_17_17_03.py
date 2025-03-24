# Костромин Андрей Львович


def negative_numbers(lst):
    if not lst:
        return 0
    return 1 + negative_numbers(lst[1:]) if lst[0] < 0 else negative_numbers(lst[1:])


print(negative_numbers([-2, 3, 8, -11, -4, 61]))
