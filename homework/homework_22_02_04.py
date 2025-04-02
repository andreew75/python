# Костромин Андрей Львович


class Weight:
    __slots__ = "__x",

    def __init__(self, x=0):
        self.__x = x

    @staticmethod
    def __check_value(x):
        return isinstance(x, (int, float))

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if Weight.__check_value(x):
            self.__x = x
        else:
            print("Значение должно быть числом! Попробуйте снова")

    @staticmethod
    def conversion(x):
        return f"{x * 2.205} фунтов"


w1 = Weight()
w1.x = 41
print(Weight.conversion(w1.x))

