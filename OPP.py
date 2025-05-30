# Объектно-ориентированное программирование
import json
import pickle

from car.electro_car import ElectroCar

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


# class Vector(list):
#     def __str__(self):
#         return " ".join(map(str, self))
#
#
# v = Vector([1, 2, 3])
# print(v)


# Абстрактные методы

# Вложенные классы

# class MyOuter:
#     age = 18
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     @staticmethod
#     def outer_static_method():
#         print("Метод внешнего класса")
#
#     def outer_obj_method(self):
#         print("Метод внешнего экземпляра класса", self.name)
#
#     class MyInner:
#         def __init__(self, inner_name, obj):
#             self.inner_name = inner_name
#             self.obj = obj
#
#         def inner_method(self):
#             print("Метод вложенного класса", MyOuter.age, self.obj.name, self.obj.surname)
#             MyOuter.outer_static_method()
#             self.obj.outer_obj_method()
#
#
# out = MyOuter('внешний', 'второй параметр')
# out.outer_obj_method()
# inner = out.MyInner('внутренний', out)
# print(out.name)
# print(inner.inner_name)
# inner.inner_method()


# class Color:
#     def __init__(self):
#         self.name = "Green"
#         self.lg = self.LightGreen()
#
#     def show(self):
#         print("Name:", self.name)
#
#     class LightGreen:
#         def __init__(self):
#             self.name = "Light Green"
#
#         def display(self):
#             print("Name:", self.name)
#
#
# outer = Color()
# outer.show()
# print(outer.name)
# # print(outer.lg.name)
# # outer.lg.display()
# g = outer.lg
# g.display()

# class Intern:
#     def __init__(self):
#         self.name = "Дмитрий"
#
#     def display(self):
#         print("Name:", self.name)
#
#
# class Employee:
#     def __init__(self):
#         self.name = "Employee"
#         self.intern = Intern()
#         # self.head = self.Head()
#
#     def show(self):
#         print("Name:", self.name)
#
#     class Head:
#         def __init__(self):
#             self.name = "Александр"
#
#         def display(self):
#             print("Name:", self.name)
#
#
# outer = Employee()
# outer.show()
#
# d1 = outer.intern
# # d2 = outer.head
#
# d2 = Employee().Head()
# d1.display()
# d2.display()

# class Outer:
#     def __init__(self):
#         self.inner = self.Inner()
#
#     def show(self):
#         print("Наружный класс")
#
#     class Inner:
#         def __init__(self):
#             self.inner_inner = self.InnerClass()
#
#         def show(self):
#             print("Промежуточный класс")
#
#         class InnerClass:
#
#             def show(self):
#                 print("Вложенный класс")
#
#
# outer = Outer()
# outer.show()
#
# inner1 = outer.inner
# inner1.show()
#
# inner2 = outer.inner.inner_inner
# inner2.show()

# class Computer:
#     def __init__(self):
#         self.name = "PC001"
#         self.os = self.OS()
#         self.cpu = self.CPU()
#
#     class OS:
#         def system(self):
#             return "Windows 10"
#
#     class CPU:
#         def make(self):
#             return "Intel"
#
#         def model(self):
#             return "Core-i9"
#
#
# comp = Computer()
# my_os = comp.os
# my_cpu = comp.cpu
# print(comp.name)
# print(my_os.system())
# print(my_cpu.make())
# print(my_cpu.model())

# class Base:
#     def __init__(self):
#         self.db = self.Inner()
#
#     def display(self):
#         print("In Base Class")
#
#     class Inner:
#         def display1(self):
#             print("Inner Of Base Class")
#
#
# class SubClass(Base):
#     def __init__(self):
#         print("In Subclass")
#         super().__init__()
#
#     class Inner(Base.Inner):
#         def display2(self):
#             print("Inner Of Subclass")
#
#
# a = SubClass()
# # a.display()
# b = a.db
# # b = SubClass.Inner()
# b.display1()
# b.display2()

# class Creature:
#     def __init__(self, name):
#         self.name = name
#
#
# class Animal(Creature):
#     def sleep(self):
#         print(self.name + " is sleeping")
#
#
# class Pet(Creature):
#     def play(self):
#         print(self.name + " is playing")
#
#
# class Dog(Animal, Pet):
#     def bark(self):
#         print(self.name + " is barking")
#
#
# dog = Dog("Buddy")
# dog.sleep()
# dog.play()
# dog.bark()


# class A:
#     def __init__(self):
#         print("Инициализатор класса A")
#
#
# class AA:
#     def __init__(self):
#         print("Инициализатор класса AA")
#
#
# class B(A):
#     def __init__(self):
#         print("Инициализатор класса B")
#
#
# class C(AA):
#     def __init__(self):
#         print("Инициализатор класса C")
#
#
# class D(B, C):
#     def __init__(self):
#         print("Инициализатор класса D")

#
# d = D()
# print(D.mro())
# print(D.__mro__)


# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#
# class Styles:
#     def __init__(self, color="red", width=1):
#         print("Инициализатор Styles")
#         self.color = color
#         self.width = width
#
#
# class Pos:
#     def __init__(self, sp: Point, ep: Point, *args):
#         print("Инициализатор Pos")
#         self.sp = sp
#         self.ep = ep
#         # Styles.__init__(self, *args)
#         super().__init__(*args)
#
#
# class Line(Pos, Styles):
#     def draw(self):
#         print(f"Рисование линии: {self.sp}, {self.ep}, {self.color}, {self.width}")
#
#
# l1 = Line(Point(10, 10), Point(100, 100), "green", 5)
# l1.draw()


# Миксины

# class Displayer:
#     @staticmethod
#     def display(message):
#         print(message)
#
#
# class LoggerMixin:
#     def log(self, message, filename="log_file.txt"):
#         with open(filename, "a") as fh:
#             fh.write(message)
#
#     def display(self, message):
#         Displayer.display(message)
#         self.log(message)
#
#
# class MySubClass(LoggerMixin, Displayer):
#     def log(self, message, filename=""):
#         super().log(message, filename="log.txt")
#
#
# subclass = MySubClass()
# subclass.display("Эта строка будет печататься и записываться в файл")


# class Goods:
#     def __init__(self, name, weight, price):
#         super().__init__()
#         print("Init Goods")
#         self.name = name
#         self.weight = weight
#         self.price = price
#
#     def print_info(self):
#         print(f"{self.name}, {self.weight}, {self.price}")
#
#
# class MixinLog:
#     ID = 0
#
#     def __init__(self):
#         print("Init MixinLog")
#         MixinLog.ID += 1
#         self.id = MixinLog.ID
#
#     def save_sell_log(self):
#         print(f"{self.id}: товар был продан в 15:20")
#
#
# class Notebook(Goods, MixinLog):
#     ...
#
#
# n = Notebook("HP", 1.5, 35000)
# n.print_info()
# n.save_sell_log()

# class Student:
#     def __init__(self, name, *marks):
#         self.name = name
#         self.marks = list(marks)
#
#     def __getitem__(self, item):
#         if 0 <= item < len(self.marks):
#             return self.marks[item]
#         else:
#             raise IndexError("Неверный индекс")
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, int) or key < 0:
#             raise TypeError("Индекс должен быть целым числом")
#
#         if key >= len(self.marks):
#             off = key + 1 - len(self.marks)
#             self.marks.extend([None] * off)
#
#         self.marks[key] = value
#
#     def __delitem__(self, key):
#         if not isinstance(key, int) or key < 0:
#             raise TypeError("Индекс должен быть целым числом")
#         del self.marks[key]
#
#
# s1 = Student("Anton", 5, 4, 5, 3, 5)
# print(s1[2])
# s1[10] = 4
# del s1[2]
# print(s1.marks)


# class Point:
#     def __init__(self, x):
#         self.x = x
#
#     # def __str__(self):
#     #     return f"{self.x}"
#
#     def __repr__(self):
#         return f"{self.__class__}: {self.x}"
#
#
# p1 = Point(5)
# print(p1)

# from random import choice, randint
#
#
# class Cat:
#     def __init__(self, name, age, pol):
#         self.name = name
#         self.age = age
#         self.pol = pol
#
#     def __str__(self):
#         if self.pol == "M":
#             return f"{self.name} is good boy!"
#         elif self.pol == "F":
#             return f"{self.name} is good girl!"
#         else:
#             return f"{self.name} is good Kitty!"
#
#     def __repr__(self):
#         return f"Cat(name='{self.name}', age={self.age}, pol='{self.pol}')"
#
#     def __add__(self, other):
#         if self.pol != other.pol:
#             return [Cat("No name", 0, choice(["M", "F"])) for _ in range(1, randint(2, 5))]
#         raise TypeError("Types not supported")
#
#
# cat1 = Cat("Tom", 4, "M")
# cat2 = Cat("Elsa", 5, "F")
# print(cat1)
# print(cat2)
# print(cat1 + cat2)

# class Numbers:
#
#     def __init__(self,value):
#         self.value = value
#
#     def total(self, a):
#         return self.value + int(a)
#
#
# class Text:
#
#     def __init__(self, value):
#         self.value = value
#
#     def total(self, a):
#         return len(self.value + str(a))

# class Animals:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# class Cat(Animals):
#     def info(self):
#         print(f"Я кот. Меня зовут {self.name}. Мой возраст {self.age}")
#
#     def make_sound(self):
#         print(f"{self.name} мяукает.")
#
#
# class Dog(Animals):
#     def info(self):
#         print(f"Я собака. Меня зовут {self.name}. Мой возраст {self.age}")
#
#     def make_sound(self):
#         print(f"{self.name} гавкает.")
#
#
# cat = Cat("Пушок", 3)
# dog = Dog("Мухтар", 6)
#
# for animal in cat, dog:
#     animal.info()
#     animal.make_sound()


# def string_strip(chars):
#     def wrap(string):
#         if not isinstance(string, str):
#             raise ValueError("")
#
#         return string.strip(chars)
#     return wrap
#
#
# s1 = string_strip("&#?.! ")
# print(s1("    Hello!    "))
#
#
# class StringStrip:
#     def __init__(self, chars):
#         self.chars = chars
#
#     def __call__(self, *args, **kwargs):
#         if not isinstance(args[0], str):
#             raise ValueError("")
#
#         return args[0].strip(self.chars)
#
#
# s2 = string_strip("&#?.! ")
# print(s1("    Hello!    "))

# class MyDecorator:
#     def __init__(self, fn):
#         self.func = fn
#
#     def __call__(self, *args):
#         print("До вызова")
#         print(self.func(*args))
#         print("После вызова")
#
#
# @MyDecorator
# def func(a, b):
#     return a * b
#
#
# func(2, 5)

# from car.electro_car import ElectroCar
#
# if __name__ == '__main__':
#     e_car = ElectroCar("Tesla", "T", 2018, 99000, 100)
#     e_car.show_car()
#     e_car.description_power()
#

# +++++++++++++++

# Упаковка данных (Сериализация) и распаковка данных (Десериализация)

# dump() - Сохраняет данные в открытый файл
# load() - Считывает данные из открытого файла
# dumps() - сохраняет данные в строку
# loads( ) - считывает данные из строки

# import pickle
#
# filename = "basket.txt"
#
# shop = {
#     "fruits": ["apple", "orange"],
#     "veget": ("tomato", "redis"),
#     "1000": 1000
# }
#
# with open(filename, "wb") as fn:
#     pickle.dump(shop, fn)
#
# with open(filename, "rb") as fn:
#     shop_list = pickle.load(fn)
#
# print(shop_list)

#
# class Test:
#     num = 25
#     string = "Privet"
#     lst = [1, 2, 3]
#     dictionary = {"first": 1, "second": 2}
#
#     def __str__(self):
#         return f"Число: {Test.num}\nСтрока: {Test.string}\n "
#
#
# obj = Test()
# print(obj)
#
# obj1 = pickle.dumps(obj)
# print(obj1)
#
# obj2 = pickle.loads(obj1)
# print(obj2)


# import json
# from random import choice
#
#
# def gen_person():
#     name = ''
#     tel = ''
#
#     letters = ['a', 'b', 'd', 'e', 'f', 'p']
#     num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
#
#     while len(name) != 6:
#         name += choice(letters)
#
#     while len(tel) < 7:
#         tel += choice(num)
#
#     person = {
#         'name': name,
#         'tel': tel,
#     }
#
#     return person
#
#
# print(gen_person())

# data = {
#     'name': 'Olga',
#     'age': 35,
#     20: None,
#     True: False,
#     'hobbies': ('run', 'sing')
# }
#
# with open('data_file.json', 'w') as fw:
#     json.dump(data, fw, indent=4)
#
#
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#
#     def __str__(self):
#         st = ", ".join(map(str, self.marks))
#         return f"Student {self.name}: {st}"
#
#     def add_marks(self, mark):
#         self.marks.append(mark)
#
#     def delete_mark(self, index):
#         self.marks.pop(index)
#
#     def edit_marks(self, index, new_mark):
#         self.marks[index] = new_mark
#
#     def average_mark(self):
#         return sum(self.marks) / len(self.marks)
#
#     def _dump_to_json(self):
#         data = {"name:": self.name, "marks:": self.marks}
#         with open(self.get_file_name(), "w") as f:
#             json.dump(data, f)
#
#     def get_file_name(self):
#         return self.name + ".json"
#
#
# st1 = Student("Anton", [5, 3, 5, 4])
# st2 = Student("Egor", [2, 3, 5, 3])
# st3 = Student("Misha", [4, 5, 3, 4])
#
#
# # print(st1)
# # st1.add_marks(2)
# # print(st1)
# # st1.delete_mark(1)
# # print(st1)
# # st1.edit_marks(3, 5)
# # print(st1)
#
#
# class Group:
#     def __init__(self, students, group):
#         self.students = students
#         self.group = group
#
#     def __str__(self):
#         st = "\n".join(map(str, self.students))
#         return f"Group: {self.group}\n{st}"
#
#     def _get_file_name(self):
#         return self.group.lower().replace(" ", "_") + ".json"
#
#     def dump_to_json(self):
#         date = [{'name': student.name, 'marks': student.marks} for student in self.students]
#         with open(self._get_file_name(), "w") as f:
#             json.dump(date, f, indent=2)
#
#
# sts1 = [st1, st2]
# gr1 = Group(sts1, "Python")
# print(gr1)
# gr1.dump_to_json()


# import requests
# import json
#
#
# response = requests.get("https://jsonplaceholder.typicode.com/todos")
# todos = json.loads(response.text)
# # print(todos)
#
# todos_by_user = {}
#
# for todo in todos:
#     if todo['completed']:
#         try:
#             todos_by_user[todo["userId"]] += 1
#         except KeyError:
#             todos_by_user[todo["userId"]] = 1
#
# # print(todos_by_user)
#
# top_user = sorted(todos_by_user.items(), key=lambda x: x[1], reverse=True)[0]
# print(top_user)
#
# users = []
# for user, num_complete in top_user:
#     if num_complete < top_user:
#         break
#     users.append(user)
#
#
# print(users)

import csv

# with open('data.csv', 'r') as f:
#     file_reader = csv.reader(f)
#     count = 0
#     for row in file_reader:
#         if count == 0:
#             print(f"Файл содержит столбцы: {', '.join(row)}")
#         else:
#             print(f"\t{row[0]} - {row[1]}. Родился в {row[2]} году.")
#         count += 1

# with open('data.csv', 'r') as f:
#     fields = ["Имя", "Профессия", "Год рождения"]
#     file_reader = csv.DictReader(f, fieldnames=fields)
#     count = 0
#     for row in file_reader:
#         if count == 0:
#             print(f"Файл содержит столбцы: {', '.join(row)}")
#         print(f"\t{row["Имя"]} - {row["Профессия"]}. Родился в {row["Год рождения"]} году.")
#         count += 1

# with open('students.csv', 'w') as f:
#     writer = csv.writer(f, lineterminator='\r')
#     writer.writerow(["Имя", "Класс", "Возраст"])
#     writer.writerow(["Маша", "10", "15"])
#     writer.writerow(["Люда", "11", "17"])


# data = [['hostname', 'vendor', 'model', 'location'],
#         ['sw1', 'Cisco', '3750', 'London, Best str'],
#         ['sw2', 'Cisco', '3850', 'Liverpool, Better str'],
#         ['sw3', 'Cisco', '3650', 'Liverpool, Better str'],
#         ['sw4', 'Cisco', '3650', 'London, Best str']]
#
# with open('switches.csv', 'w') as f:
#     writer = csv.writer(f, lineterminator='\r')
#     writer.writerows(data)
#
# with open('switches.csv', 'r') as f:
#     print(f.read())

# with open('sw_dict.csv', 'w') as f:
#     writer = csv.DictWriter(f, fieldnames=["hostname", "vendor", "model", "location"], lineterminator='\r')
#     writer.writeheader()
#     writer.writerow({"hostname": "sw1", "vendor": "Cisco", "model": "3750", "location": "London, Best str"})
#     writer.writerow({"hostname": "sw2", "vendor": "Cisco", "model": "3850", "location": "Liverpool, Better str"})
#     writer.writerow({"hostname": "sw3", "vendor": "Cisco", "model": "3650", "location": "Liverpool, Better str"})


data = [{
    'hostname': 'sw1',
    'location': 'London',
    'model': '3750',
    'vendor': 'Cisco'
}, {
    'hostname': 'sw2',
    'location': 'Liverpool',
    'model': '3850',
    'vendor': 'Cisco'
}, {
    'hostname': 'sw3',
    'location': 'Liverpool',
    'model': '3650',
    'vendor': 'Cisco'
}, {
    'hostname': 'sw4',
    'location': 'London',
    'model': '3650',
    'vendor': 'Cisco'
}]

with open('sw_dict_2.csv', 'w') as f:
    writer = csv.DictWriter(f, fieldnames=data[0].keys(), lineterminator='\r')
    writer.writeheader()
    for row in data:
        writer.writerow(row)