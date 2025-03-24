# Костромин Андрей Львович


def mean(fn):
    def wrapper(*args):
        return round(fn(*args) / len(args), 2)

    return wrapper


@mean
def addition(*args):
    return sum(args)


print(addition(10, 3, 4, 8, 11, 63))
