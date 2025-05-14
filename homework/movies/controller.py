from view import UserInterface
from model import MovieModel


class Controller:
    def __init__(self):
        self.movie_model = MovieModel()
        self.user_interface = UserInterface()

    def run(self):
        answer = None
        while answer != "q":
            answer = self.user_interface.wait_user_answer()
            self.check_user_answer(answer)

    def check_user_answer(self, answer):
        if answer == "1":
            while True:
                movie = self.user_interface.add_user_movie()
                added = self.movie_model.add_movie(movie)
                if added:
                    self.user_interface.show_message("Фильм успешно добавлен в каталог!")
                choice = self.user_interface.ask_continue()
                if choice == "нет":
                    return False
                elif choice != "да":
                    self.user_interface.show_message("Некорректный ввод!")
                # return None
        elif answer == "2":
            movies = self.movie_model.get_all_movie()
            self.user_interface.show_all_movies(movies)
            return None
        elif answer == "3":
            movie_title = self.user_interface.get_user_movie()
            try:
                movie = self.movie_model.get_single_movie(movie_title)
            except KeyError:
                self.user_interface.show_incorrect_title_error(movie_title)
                return None
            else:
                self.user_interface.show_single_movie(movie)
        elif answer == "4":
            movie_title = self.user_interface.get_user_movie()
            try:
                title = self.movie_model.remove_movie(movie_title)
            except KeyError:
                self.user_interface.show_incorrect_title_error(movie_title)
                return None
            else:
                self.user_interface.remove_single_movie(title)
        elif answer == "q":
            self.movie_model.save_data()
            print("До свидания!")
            return None
        else:
            self.user_interface.show_incorrect_answer_error(answer)
            return None
