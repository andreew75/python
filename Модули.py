# Создание модулей

from geometry import rect, sqr, trian

r1 = rect.Rect.Rect(1, 2)
r2 = rect.Rect.Rect(3, 4)

s1 = rect.Rect.Sqr(10)
s2 = rect.Rect.Sqr(20)

t1 = rect.Rect.Triangle(1, 2, 3)
t2 = rect.Rect.Triangle(4, 5, 6)

shape = [r1, r2, s1, s2, t1, t2]

for i in shape:
    print(i.get_perimetr())