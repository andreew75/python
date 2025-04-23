# Костромин Андрей Львович

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def square(self):
        pass

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def info(self):
        pass


class Square(Shape, ABC):
    def __init__(self, a, name, color):
        self.a = a
        self.name = name
        self.color = color

    def perimeter(self):
        return self.a * 4

    def square(self):
        return self.a * 2

    def draw(self):
        return '\n'.join(['*' * self.a for _ in range(self.a)])

    def info(self):
        return (
            f"***{self.name: ^15}***\n"
            f"Сторона: {self.a}\n"
            f"Цвет: {self.color}\n"
            f"Площадь: {self.square()}\n"
            f"Периметр: {self.perimeter()}\n"
            f"{self.draw()}"
        )


class Rectangle(Shape, ABC):
    def __init__(self, a, b, name, color):
        self.a = a
        self.b = b
        self.name = name
        self.color = color

    def perimeter(self):
        return (self.a + self.b) * 2

    def square(self):
        return self.a * self.b

    def draw(self):
        return '\n'.join(['*' * self.a for _ in range(self.b)])

    def info(self):
        return (
            f"***{self.name: ^15}***\n"
            f"Ширина: {self.a}\n"
            f"Высота: {self.b}\n"
            f"Цвет: {self.color}\n"
            f"Площадь: {self.square()}\n"
            f"Периметр: {self.perimeter()}\n"
            f"{self.draw()}"
        )


class Triangle(Shape, ABC):
    def __init__(self, a, b, c, name, color):
        self.a = a
        self.b = b
        self.c = c
        self.name = name
        self.color = color
        self.max_side = max(a, b, c)
        self.draw_height = max(3, math.ceil(self.max_side / 2))

    def perimeter(self):
        return self.a + self.b + self.c

    def square(self):
        p = self.perimeter() / 2
        return round(math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c)), 2)

    def draw(self):
        lines = []
        for i in range(self.draw_height):
            stars = '*' * (2 * i + 1)
            lines.append(stars.center(2 * self.draw_height - 1))
        return '\n'.join(lines)

    def info(self):
        return (
            f"***{self.name: ^15}***\n"
            f"Сторона А: {self.a}\n"
            f"Сторона В: {self.b}\n"
            f"Сторона С: {self.c}\n"
            f"Цвет: {self.color}\n"
            f"Площадь: {self.square()}\n"
            f"Периметр: {self.perimeter()}\n"
            f"{self.draw()}"
        )


s1 = Square(3, "Квадрат", "Красный")
r1 = Rectangle(7, 3, "Прямоугольник", "Зеленый")
t1 = Triangle(11, 6, 6, "Треугольник", "Желтый")

figures = [s1, r1, t1]

for f in figures:
    print(f.info(), "\n")
