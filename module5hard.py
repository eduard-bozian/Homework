
class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = self.hash_password(password)
        self.age = age
    def hash_password(self, password):
        return hash(password)


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode
class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None
    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.password == password:
                self.current_user = user
                print(f"Вход выполнен успешно, добро пожаловать, {user.nickname}!")
                return True
        print(f"Неверный логин или пароль!")
        return False
    def register(self, nickname, password, age):
        if any(user.nickname == nickname for user in self.users):
            print(f"Пользователь {nickname} уже существует.")
        else:
            new_user = User(nickname, password, age)
            self.users.append(new_user)
            self.current_user = new_user
            print(f"Регистрация прошла успешно, добро пожаловать, {nickname}!")
    def log_out(self):
        self.current_user = None
        print("Выход из системы.")
    def add(self, *videos):
        for video in videos:
            if not any(v.title == video.title for v in self.videos):
                self.videos.append(video)
                print(f" {video.title}")
    def get_videos(self, search_term):
        search_term = search_term.lower()
        found_videos = [video.title for video in self.videos if search_term in video.title.lower()]
        return found_videos
    def watch_video(self, title):
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return
        video = next((v for v in self.videos if v.title == title), None)
        if not video:
            print(f"Видео '{title}' не найдено.")
            return
        if video.adult_mode and self.current_user.age < 18:
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
            return
        print(f"Проигрывание видео '{title}'...")
        while video.time_now < video.duration:
            print(f"Время просмотра: {video.time_now} cek")
            video.time_now += 1
        print("Конец видео")


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
ur.add(v1, v2)
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)
ur.watch_video('Лучший язык программирования 2024 года!')
