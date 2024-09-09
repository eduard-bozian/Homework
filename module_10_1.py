from time import time, sleep
import threading

def write_words(word_count, file_name):
    with open(file_name, "w", encoding='utf-8') as f:
        for i in range(1, word_count + 1):
            f.write(f"Какое-то слово № {i}\n")
            sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")

if __name__ == "__main__":
    start_time = time()
    write_words(10, "example1.txt")
    write_words(30, "example2.txt")
    write_words(200, "example3.txt")
    write_words(100, "example4.txt")
    end_time = time()
    print(f"Работа функций {end_time - start_time}")

    start_time = time()
    threads = []
    for file_name in ["example5.txt", "example6.txt", "example7.txt", "example8.txt"]:
        thread = threading.Thread(target=write_words, args=(100, file_name))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
    end_time = time()
    print(f"Работа потоков {end_time - start_time}")
