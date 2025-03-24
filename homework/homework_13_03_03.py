# Костромин Андрей Львович

from math import pi

square = {
    'circle': lambda r: pi * r ** 2,
    'rectangle': lambda x, y: x * y,
    'trapezoid': lambda a, b, c: (a + b) / 2 * c,
}

print("Площадь круга: ", square['circle'](2))
print("Площадь прямоугольника: ", square['rectangle'](10, 15))
print("Площадь трапеции: ", square['trapezoid'](7, 5, 3))
