def add_title(title):
    def wrapper(func):
        def wrap(*args, **kwargs):
            print(f" {title} ".center(50, "-"))
            output = func(*args, **kwargs)
            print("*" * 50)
            return output

        return wrap

    return wrapper


class UserInterface:
    @add_title(" Редактирование данных каталога фильмов ")
    def wait_user_answer(self):
        print("Действия с фильмами: ")
        print("1 - добавление фильма"
              "\n2 - каталог фильмов"
              "\n3 - поиск фильма по названию"
              "\n4 - удаление фильма"
              "\nq - выход из программы")
        user_answer = input("Выберите вариант действия: ")
        return user_answer

    @add_title(" Редактирование данных каталога фильмов ")
    def show_message(self, message):
        print(message)

    @add_title(" Редактирование данных каталога фильмов ")
    def ask_continue(self):
        choice = input("Хотите добавить еще фильм? (Да/Нет): ").strip().lower()
        return choice

    @add_title(" Добавление фильма в каталог ")
    def add_user_movie(self):
        dic_movie = {
            "название": None,
            "жанр": None,
            "режиссера": None,
            "год выхода": None,
            "продолжительность": None
        }
        for key in dic_movie:
            dic_movie[key] = input(f"Введите {key} фильма: ").strip().lower()
        return dic_movie

    @add_title(" Каталог фильмов ")
    def show_all_movies(self, movies):
        if not movies:
            print("В каталоге пока нет фильмов.")
            return
        for index, movie in enumerate(movies, 1):
            print(f"{index}. {movie}".title())

    @add_title(" Ввод названия фильма ")
    def get_user_movie(self):
        user_movie = input("Введите название фильма: ").strip().lower()
        return user_movie

    @add_title(" Сведения о фильме ")
    def show_single_movie(self, movie):
        for key in movie:
            print(f"{key.capitalize()}: {movie[key]}")

    @add_title(" Сообщение об ошибке ")
    def show_incorrect_title_error(self, user_title):
        print(f"Фильм с названием \"{user_title.title()}\" не найден.")

    @add_title(" Удаление фильма ")
    def remove_single_movie(self, title):
        print(f"Этот фильм удален: {title}")

    @add_title(" Сообщение об ошибке ")
    def show_incorrect_answer_error(self, answer):
        print(f"Варианта выбора {answer} не существует.")
