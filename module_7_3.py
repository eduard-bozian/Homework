import string


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names  # Сохраняем названия файлов в виде кортежа

    def get_all_words(self):
        all_words = {}

        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as f:
                    # Читаем содержимое файла и переводим его в нижний регистр
                    content = f.read().lower()
                    # Убираем пунктуацию
                    content = content.translate(str.maketrans('', '', string.punctuation + '-'))
                    # Разбиваем текст на слова
                    words = content.split()
                    all_words[file_name] = words  # Добавляем в словарь

            except FileNotFoundError:
                print(f"Файл {file_name} не найден.")

        return all_words

    def find(self, word):
        result = {}
        all_words = self.get_all_words()  # Получаем все слова из файлов

        for file_name, words in all_words.items():
            if word.lower() in words:  # Поиск с учетом регистра
                result[file_name] = words.index(word.lower()) + 1  # Позиция (счёт с 1)

        return result

    def count(self, word):
        result = {}
        all_words = self.get_all_words()  # Получаем все слова из файлов

        for file_name, words in all_words.items():
            count = words.count(word.lower())  # Считаем количество вхождений слова
            if count > 0:
                result[file_name] = count  # Сохраняем количество, если больше 0

        return result


# Пример использования класса
finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
