import pickle
import os.path


class Movie:
    def __init__(self, title, genre, director, release, duration):
        self.title = title
        self.genre = genre
        self.director = director
        self.release = release
        self.duration = duration

    def __str__(self):
        return f"\"{self.title.title()}\" ({self.release})"


class MovieModel:
    def __init__(self):
        self.db_name = "catalog.txt"
        self.movies = self.load_data()

    def add_movie(self, dic_movie):
        movie = Movie(*dic_movie.values())
        self.movies[movie.title] = movie

    def get_all_movie(self):
        return self.movies.values()

    def get_single_movie(self, user_title):
        movie = self.movies[user_title]
        dic_movie = {
            "название": movie.title.title(),
            "жанр": movie.genre.title(),
            "режиссер": movie.director.title(),
            "год выхода": movie.release,
            "продолжительность": movie.duration
        }
        return dic_movie

    def remove_movie(self, user_title):
        return self.movies.pop(user_title)

    def save_data(self):
        with open(self.db_name, "wb") as f:
            pickle.dump(self.movies, f)

    def load_data(self):
        if os.path.exists(self.db_name):
            with open(self.db_name, "rb") as f:
                return pickle.load(f)
        else:
            return {}
