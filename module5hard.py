import time


class User:
    """
    Класс пользователя, содержащий атрибуты: имя_пользователя, пароль и возраст.
    """

    def __init__(self, nickname, password, age):  # определяем метод __init__
        self.nickname = nickname
        self.password = hash(password)
        self.age = age
        UrTube.users.append(self)


class Video:
    """
    Класс видео, содержащий атрибуты: заголовок, продолжительность, секунда остановки, ограничение по возрасту.
    """

    def __init__(self, title, duration, time_now=0, adult_mode=False):  # определяем метод __init__
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube:
    """
    Класс видеохостинг, содержащий атрибуты: пользователи, видео, текущий пользователь.
    """
    users = []
    videos = []

    def __init__(self):  # определяем метод __init__
        self.users = UrTube.users
        self.videos = UrTube.videos
        self.current_user = None

    def register(self, nickname, password, age):  # определяем метод, который регистрирует новых пользователей
        users_list = []
        for i in UrTube.users:
            users_list.append(i.nickname)
        if nickname not in users_list:
            User(nickname, password, age)
            self.log_in(nickname, password)
        elif nickname in users_list:
            print(f'Пользователь {nickname} уже существует')

    def log_in(self, nickname, password):  # определяем метод для входа в систему и проверки правильности пароля
        for i in UrTube.users:
            if nickname == i.nickname and hash(password) == i.password:
                self.current_user = nickname

    def log_out(self, *args):  # определяем метод для выхода из системы
        self.current_user = None

    def add(self, *args):
        UrTube.videos.extend(args)  # определяем метод для добавления видео

    def get_videos(self, check):  # определяем метод для поиска видео
        check_list = []
        for search in UrTube.videos:
            if check.upper() in search.title.upper():
                check_list.append(search.title)
        if len(check_list) > 0:
            return check_list
        print('Совпадений не найдено - ', end='')

    def watch_video(self, movie):  # определяем метод для воспроизведения видео
        if self.current_user is None:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return
        for search_movie in UrTube.videos:
            if movie == search_movie.title and search_movie.adult_mode is True:
                for i in UrTube.users:
                    if i.nickname == self.current_user:
                        if i.age < 18:
                            print('Вам нет 18 лет, пожалуйста, покиньте страницу')
                        else:
                            self.time_goes(search_movie.time_now, search_movie.duration)
            elif movie == search_movie.title:
                self.time_goes(search_movie.time_now, search_movie.duration)

    def time_goes(self, movie_now, movie_duration):  # определяем метод для текущего времени просмотра видео
        while movie_now <= movie_duration:
            if movie_now < 1:
                movie_now += 1
            else:
                print(movie_now, end=' ')
                movie_now += 1
                time.sleep(1)
        print('Конец видео')
        time.sleep(1)


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
