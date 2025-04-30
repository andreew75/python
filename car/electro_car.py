
from car import car_class


class ElectroCar(car_class.CarClass):
    def __init__(self, brand, model, year, run, battery):
        super().__init__(brand, model, year, run)
        self.battery = battery

    def description_power(self):
        print(f"Этот автомобиль имеет мощность {self.battery} %")

