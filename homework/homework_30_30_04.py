# Костромин Андрей Львович

import json


def users_input() -> int:
    while True:
        try:
            user_input = int(input("""
Выбор действия:
    1 - добавление данных
    2 - удаление данных
    3 - поиск данных
    4 - редактирование данных
    5 - просмотр данных
    6 - завершение работы
Введите значение: """))

            if 0 < user_input < 7:
                return user_input
            else:
                print("Ошибка ввода! Введите значение от 1 до 6")
        except ValueError:
            print("Введите корректное значение")


class Countries:

    regions = {}
    filename = 'countries.json'

    @staticmethod
    def load_data():
        try:
            with open(Countries.filename, 'r') as f:
                Countries.regions = json.load(f)
        except FileNotFoundError:
            print("Файл создан.")
        except json.JSONDecodeError:
            print("Ошибка чтения файла.")

    @staticmethod
    def save_data():
        with open(Countries.filename, 'w') as f:
            json.dump(Countries.regions, f, indent=2)

    @staticmethod
    def add_data():
        try:
            country = input("Введите название страны: ").strip().capitalize()
            capital = input("Введите название столицы: ").strip().capitalize()
            if not country or not capital:
                print("Название страны не может быть пустым")
                return

            if country in Countries.regions:
                print("Такая страна уже существует")
                return

            Countries.regions[country] = capital
            Countries.save_data()
            print("Данные успешно сохранены")

        except Exception as e:
            print(f"Произошла ошибка при добавлении данных: {e}")

    @staticmethod
    def delete_data():
        country = input("Введите страну для удаления: ").strip().capitalize()
        if country in Countries.regions:
            del Countries.regions[country]
            Countries.save_data()
            print("Данные удалены!")
        else:
            print("Страна не найдена!")

    @staticmethod
    def search_data():
        search = input("Введите страну или столицу для поиска: ").strip().lower()
        results = []

        for country, capital in Countries.regions.items():
            if (search in country.lower() or
                    search in capital.lower()):
                results.append((country, capital))

        if not results:
            print("\nНичего не найдено.")
            return

        print(f"\nНайдено совпадений: {len(results)}")
        for i, (country, capital) in enumerate(results, 1):
            print(f"{i}. {country} - {capital}")

    @staticmethod
    def edit_data():
        country = input("Введите страну для редактирования: ").strip().capitalize()

        if not country:
            print("Название страны не может быть пустым!")
            return

        if country not in Countries.regions:
            print("Такая страна не найдена!")
            return

        print(f"\nТекущие данные: {country} - {Countries.regions[country]}")

        while True:
            new_capital = input("Введите новую столицу: ").strip().capitalize()
            if not new_capital:
                print("Редактирование отменено")
                return

            if new_capital == Countries.regions[country]:
                print("Новая столица совпадает с текущей!")
                continue

            Countries.regions[country] = new_capital
            Countries.save_data()
            print("Данные успешно обновлены!")
            break

    @staticmethod
    def view_data():
        with open(Countries.filename, 'r') as f:
            Countries.regions = json.load(f)
            print(Countries.regions)


if __name__ == "__main__":
    Countries.load_data()

    while True:
        user_choice = users_input()  # Получаем выбор

        if user_choice == 1:
            Countries.add_data()

        elif user_choice == 2:
            Countries.delete_data()

        elif user_choice == 3:
            Countries.search_data()

        elif user_choice == 4:
            Countries.edit_data()

        elif user_choice == 5:
            Countries.view_data()

        elif user_choice == 6:
            print("Работа завершена.")
            break
