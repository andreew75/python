# Костромин Андрей Львович


class Student:
    def __init__(self, name, model="HP", cpu="Intel Core-i7", ram=16):
        self.name = name
        self.notebook = self.Notebook(model, cpu, ram)

    def display(self):
        print(f"{self.name} {self.notebook.display()}")

    class Notebook:
        def __init__(self, model: str, cpu: str, ram: int):
            self.model = model
            self.cpu = cpu
            self.ram = ram

        def display(self):
            return f"=> {self.model}, {self.cpu}, {self.ram} Гб"


student_1 = Student("Роман")
student_2 = Student("Владимир")
student_3 = Student("Ольга", "Acer", "AMD", 32)
student_1.display()
student_2.display()
student_3.display()
