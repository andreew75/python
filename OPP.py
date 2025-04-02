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


def inc(x):
    return x + 1


def dec(x):
    return x - 1


print(inc(10), dec(5))


class Change:
    @staticmethod
    def inc(x):
        return x + 1

    @staticmethod
    def dec(x):
        return x - 1


print(Change.inc(10), Change.dec(5))