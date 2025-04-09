# Объектно-ориентированное программирование

# class Point:
#     x = 1
#     y = 2


# p1 = Point()
# print(p1.x)
# p1.x = 100
# print(p1.x)
# print(p1.__dict__)

# class Point:
#     x = 1
#     y = 2
#
#     def set_coords(self):
#         print(self.__dict__)
#
#
# p1 = Point()
# p1.x = 10
# p1.y = 50
# p1.set_coords()
# Point.set_coords(p1)
#
# p2 = Point()
# p2.set_coords()


# class Point:
#     x = 1
#     y = 2
#
#     def set_coords(self, x1, y1):
#         self.x = x1
#         self.y = y1
#
#
# p1 = Point()
# p1.set_coords(5, 10)
# print(p1.__dict__)
#
# p2 = Point()
# p2.set_coords(51, 101)
# print(p2.__dict__)
#

# class Human:
#     name = "name"
#     date = "date"
#     phone = "0000000"
#     country = "country"
#     city = "city"
#     address = "street"
#
#     def print_info(self):
#         print(" Персональные данные ".center(40, '*'))
#         print(f"Имя: {self.name}\n"
#               f"Дата рождения: {self.date}\n"
#               f"Номер телефона: {self.phone}\n"
#               f"Страна: {self.country}\n"
#               f"Город: {self.city}\n"
#               f"Адрес: {self.address}\n")
#         print("=" * 40)
#
#     def input_info(self, first_name, date, phone, country, city, address):
#         self.name = first_name
#         self.date = date
#         self.phone = phone
#         self.country = country
#         self.city = city
#         self.address = address
#
#     def set_name(self, name):
#         self.name = name
#
#     def get_name(self):
#         return self.name
#
#
# h1 = Human()
# h1.print_info()
# h1.input_info("Юля", "23.05.1977", "72-30-09", "Россия", "Москва", "ул Ленина, 12")
# h1.print_info()
# h1.set_name("Юлия")
# h1.print_info()
# print(h1.get_name())


# class Person:
#     skill = 10
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     def print_info(self):
#         print('Данные сотрудника: ', self.name, self.surname)
#
#     def add_skill(self, k):
#         self.skill += k
#         print('Квалификация сотрудника: ', self.skill, "\n")
#
#
# p1 = Person("Виктор", "Довгань")
# p1.print_info()
# p1.add_skill(3)
#
# p2 = Person("Виктор", "Довгань")
# p2.print_info()
# p2.add_skill(2)


# class Person:
#     count = 0
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#         Person.count += 1
#
#     def print_info(self):
#         print('Данные сотрудника: ', self.name, self.surname)
#
#
# p1 = Person("Виктор", "Довгань")
# p1.print_info()
#
# p2 = Person("Виктор", "Довгань")
# p2.print_info()
#
# print(p1.count)
# print(Person.count)


# class Point:
#
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __check_value(x):
#         return isinstance(x, int) or isinstance(x, float)
#
#     def set_coord(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def get_coord(self, x, y):
#         return self.__x, self.__y
#
#
# p1 = Point(5, 10)
# p1.set_coord(33, 44)
# p1.z = 200
#
# print(p1.__dict__)

# class Point:
#     __slots__ = ("x", "y")
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# p1 = Point(5, 10)
# # p1.z = 20
# print(p1.x, p1.y)

# class Point:
#
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     @property
#     def x(self):
#         return self.__x
#
#     @x.setter
#     def x(self, x):
#         self.__x = x
#
#     @x.deleter
#     def x(self):
#         del self.__x
#
#
#
#
# p1 = Point(5, 12)
# p1.coord_x = 100
# del p1.coord_x


# class Person:
#
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, name):
#         self.__name = name
#
#     @name.deleter
#     def name(self):
#         del self.__name
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, age):
#         self.__age = age
#
#     @age.deleter
#     def age(self):
#         del self.__age
#
#
# p1 = Person("Irina", 26)
# print(p1.__dict__)
# p1.name = "Ivan"
# p1.age = 50
# print(p1.__dict__)
# print()
# del p1.name
# print(p1.__dict__)


# def inc(x):
#     return x + 1
#
#
# def dec(x):
#     return x - 1
#
#
# print(inc(10), dec(5))
#
#
# class Change:
#     @staticmethod
#     def inc(x):
#         return x + 1
#
#     @staticmethod
#     def dec(x):
#         return x - 1
#
#
# print(Change.inc(10), Change.dec(5))

# class Numbers:
#     @staticmethod
#     def max(*args):
#         for i in args:
#             return max(args)
#
#
# print(Numbers.max(3, 5, 6, 9))


# class Account:
#
#     rate_usd = 0.013
#     rate_eur = 0.011
#     suffix = "RUB"
#     suffix_usd = "USD"
#     suffix_eur = "EUR"
#
#     def __init__(self, num, surname, percent, value):
#         self.num = num
#         self.surname = surname
#         self.percent = percent
#         self.value = value
#         print(f"Счет #{self.num} принадлежащий {self.surname} был открыт.")
#         print("*" * 43)
#
#     def __del__(self):
#         print("*" * 43)
#         print(f"Счет #{self.num} принадлежащий {self.surname} был закрыт.")
#
#     @classmethod
#     def set_eur_rate(cls, rate):
#         cls.rate_eur = rate
#
#     @classmethod
#     def set_usd_rate(cls, rate):
#         cls.rate_usd = rate
#
#     def print_balance(self):
#         print(f"Текущий баланс: {self.value} {Account.suffix}")
#
#     def print_info(self):
#         print("Информация о счете: ")
#         print("-" * 20)
#         print(f"{self.num}")
#         print(f"Владелец: {self.surname}")
#         self.print_balance()
#         print(f"Проценты: {self.percent:.0%}")
#         print("-" * 20)
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     def convert_to_usd(self):
#         usd_val = Account.convert(self.value, Account.rate_usd)
#         print(f"Состояние счета: {usd_val} {Account.suffix_usd}")
#
#     def edit_owner(self, surname):
#         self.surname = surname
#
#     def add_persons(self):
#         self.value += self.value * self.percent
#         print("Проценты были начислены: ")
#         self.print_balance()
#
#
# account = Account("12345", "Бояров", 0.03, 1000)
# account.print_info()
# account.convert_to_usd()
# Account.set_eur_rate(2)
# Account.edit_owner("Портной")
# account.add_persons()
# print()

# import re
#
#
# class UserData:
#     def __init__(self, fio, old, ps, weight):
#         self.verify_fio(fio)
#         self.verify_old(old)
#         self.verify_weight(weight)
#
#         self.__fio = fio
#         self.__old = old
#         self.__password = ps
#         self.__weight = weight
#
#     @staticmethod
#     def verify_fio(fio):
#         if not isinstance(fio, str):
#             raise TypeError("ФИО должно быть строкой")
#         f = fio.split()  # ['Волков2', 'Иго@@@рь', 'Николаевич!']
#         if len(f) != 3:
#             raise TypeError("Неверный формат ФИО")
#         letter = "".join(re.findall(r"[a-zа-яё-]", fio, flags=re.IGNORECASE))  # ВолковИгорьНиколаевич
#         for s in f:
#             # print(s.strip(letter))
#             if len(s.strip(letter)) != 0:
#                 raise TypeError("В ФИО можно использовать только буквы и дефис")
#
#     @staticmethod
#     def verify_old(old):
#         if not isinstance(old, int) or not 14 < old < 100:  # old < 14 or old > 100
#             raise TypeError("Возраст должен быть числом в диапазоне от 14 до 100 лет")
#
#     @staticmethod
#     def verify_weight(w):
#         if not isinstance(w, float) or w < 30:  # old < 14 or old > 100
#             raise TypeError("Вес должен быть числом и более 30 кг")
#
#
# p1 = UserData("Волков Игорь Николаевич", 26, "1234 4567890", 80.8)


# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#
# class Parent:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1) -> None:
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#
# class Line(Parent):
#
#     def __init__(self, *args):
#         # Parent.__init__(self, *args)
#         super().__init__(*args)
#
#     def draw_line(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# class Rect(Parent):
#     def draw_rect(self):
#         print(f"Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# line = Line(Point(1, 3), Point(11, 22))
# line.draw_line()
# rect = Rect(Point(45, 78), Point(70, 80))
# rect.draw_rect()

# class Figure:
#     def __init__(self, color):
#         self.__color = color
#
#     @property
#     def color(self):
#         return self.__color
#
#     @color.setter
#     def color(self, c):
#         self.__color = c



