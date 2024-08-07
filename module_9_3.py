first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']
first_result = (abs(len(first_string) - len(second_string)) for first_string, second_string in zip(first, second)
                if len(first_string) != len(second_string))
second_result = (len(first_string) == len(second_string) for first_string, second_string in zip(first, second))
print(list(first_result))
print(list(second_result))
