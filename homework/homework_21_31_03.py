# Костромин Андрей Львович


class Cars:
    name = ""
    year = ""
    brand = ""
    power = ""
    color = ""
    price = ""

    def print_info(self):
        print(" Данные автомобиля ".center(40, "*"))
        print(f"Название модели: {self.name}\n"
              f"Год выпуска: {self.year}\n"
              f"Производитель: {self.brand}\n"
              f"Мощность двигателя: {self.power}\n"
              f"Цвет машины: {self.color}\n"
              f"Цена: {self.price}\n")
        print("=" * 40, "\n")

    def __init__(self, name, year, brand, power, color, price):
        self.name = name
        self.year = year
        self.brand = brand
        self.power = power
        self.color = color
        self.price = price

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_year(self, year):
        self.year = year

    def get_year(self):
        return self.year

    def set_brand(self, brand):
        self.brand = brand

    def get_brand(self):
        return self.brand

    def set_power(self, power):
        self.power = power

    def get_power(self):
        return self.power

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_price(self, price):
        self.price = price

    def get_price(self):
        return self.price


car_1 = Cars("X7 M50i", "2021", "BMW", "530 л.с.", "White", "10 790 000 руб.")
car_1.print_info()
car_1.set_price("9 840 000 руб.")
car_1.print_info()
print(car_1.get_brand())
print()
car_2 = Cars("Model S", "2024", "Tesla", "670 л.с.", "Red", "12 840 000 руб.")
car_2.print_info()
