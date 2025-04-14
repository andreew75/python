# Костромин Андрей Львович


class Human():
    def __init__(self, name, surname, age, score):
        self.name = name
        self.surname = surname
        self.age = age
        self.score = score

    def person_info(self):
        return f"{self.surname} {self.name}, {self.age} лет"


class Student(Human):
    def __init__(self, name, surname, age, group, score):
        super().__init__(name, surname, age, score)
        self.group = group

    def __str__(self):
        return f"Студент: {self.person_info()}, группа: {self.group}, {self.score} баллов"


class Teacher(Human):
    def __init__(self, name, surname, age, subject, score):
        super().__init__(name, surname, age, score)
        self.subject = subject

    def __str__(self):
        return f"Преподаватель: {self.person_info()}, предмет: {self.subject}, {self.score} часов "


class Graduate(Student):
    def __init__(self, name, surname, age, group, score, diploma):
        super().__init__(name, surname, age, group, score)
        self.diploma = diploma

    def __str__(self):
        return f"Дипломник: {self.person_info()}, группа: {self.group}, тема: {self.diploma}, {self.score} баллов"


humans = [
    Student("Даши", "Батодалаев", 16, "ГК Web_011", 5),
    Student("Линар", "Загидуллин", 32, "РПО PD_011", 9),
    Graduate("Сергей", "Шугани", 15, "РПО PD_011", 5, "Защита данных"),
    Teacher("Андрей", "Даньшин", 38, "Астрофизика", 100),
    Student("Даниил", "Маркин", 17, "ГК Python_011", 5),
    Teacher("Алексей", "Башкиров", 45, "Разработка приложений", 20)
]

for human in humans:
    print(human)
