# Костромин Андрей Львович


class Pair:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def multiply(self):
        return self.a * self.b


class RightTriangle(Pair):
    def __init__(self, a, b):
        super().__init__(a, b)

    def hypotenuse(self):
        return round((self.a ** 2 + self.b ** 2) ** 0.5, 2)

    def square(self):
        return self.multiply() / 2

    def print_info(self):
        print(f"Прямоугольный треугольник АВС ({self.a}, {self.b}, {self.hypotenuse()})")
        print(f"Катеты: {self.a}, {self.b}")
        print(f"Гипотенуза: {self.hypotenuse()}")
        print(f"Площадь треугольника: {self.square()}")
        print(f"Сумма катетов: {self.add()}")
        print(f"Произведение катетов: {self.multiply()}")


triangle = RightTriangle(5, 8)
triangle.print_info()

