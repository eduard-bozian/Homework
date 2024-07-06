class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age


class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, login, password):
        for user in self.users:
            if user.nickname == login and user.password == password:
                self.current_user = user
                return
            print("Invalid login or password")

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f"User {nickname} already exists")
                return

        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user

    def log_out(self):
        self.current_user = None

    def add(self, *videos):
        for video in videos:
            for existing_video in self.videos:
                if existing_video.title == video.title:
                    print(f"Video {video.title} already exists")
                    return
                    self.videos.append(video)

    def get_videos(self, search_word):
        search_word = search_word.lower()
        result = []
        for video in self.videos:
            if search_word in video.title.lower():
                result.append(video.title)
                return result

    def watch_video(self, video_title):
        if self.current_user is None:
            print("Log in to watch videos")
            return

        for video in self.videos:
            if video.title.lower() == video_title.lower():
                if video.adult_mode and self.current_user.age < 18:
                   print("You are under 18, please leave the page")
                return
            print(" ".join(str(i) for i in range(1, video.duration + 1)), "Конец видео")
            video.time_now = 0
        return
    print("Video not found")


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
ur.add(v1, v2)
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))
ur.log_in('vasya_pupkin', 'lolkekcheburek')
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.log_in('urban_pythonist', 'iScX4vIJClb9YQavjAgF')
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)
ur.watch_video('Лучший язык программирования 2024 года!')
