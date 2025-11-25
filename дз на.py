# Задание 1
def basnya():
    with open("article.txt", 'w+') as question:
        question.write("Вечерело \n"
                   "Жужжали мухи \n"
                   "Кипела вода в чайнике \n"
                   "Венера зажглась на небе \n"
                   "Деревья шумели \n"
                   "Тучи разошлись \n"
                   "Листва Зеленела \n")
    with open ("article.txt", 'r') as file:
        for i in file.readlines():
            print(i, end='')

def task2():
    try:
        with open('vorona_i_lisitsa.txt', 'r') as file:
            content = file.read()

        words = content.split()
        long_words = [word for word in words if len(word.strip('.,!?;:"')) >= 7]

        with open('long_words.txt', 'w') as output_file:
            for word in long_words:
                output_file.write(word + '\n')

        print(f"Задание 2 выполнено! Найдено {len(long_words)} слов из 7+ букв.")
        print("Результат записан в файл 'long_words.txt'")

    except FileNotFoundError:
        print("Ошибка: Файл 'vorona_i_lisitsa.txt' не найден!")
        print("Создайте файл с басней или измените имя файла.")

def task3():
    try:
        with open('file1.txt', 'r') as file1:
            lines = file1.readlines()

        with open('file2.txt', 'w') as file2:
            for line in lines:
                file2.write(line)
        print("файлы переписаны, хорошего дня!")
    except FileNotFoundError:
        print("Ошибка: Файл 'file1.txt' не найден!")

def task4():
    try:
        with open('file1.txt', 'r') as file1:
            lines = file1.readlines()

        with open('file2_reversed.txt', 'w') as file2:
            for line in reversed(lines):
                file2.write(line)

        print("Задание 4 выполнено! Строки переписаны в обратном порядке в 'file2_reversed.txt'")

    except FileNotFoundError:
        print("Ошибка: Файл 'file1.txt' не найден!")

def task5():
    try:
        with open('text_file.txt', 'r') as file:
            lines = file.readlines()

        last_no_comma_index = -1
        for i, line in enumerate(lines):
            if ',' not in line:
                last_no_comma_index = i

        if last_no_comma_index != -1:
            lines.insert(last_no_comma_index + 1, '*' * 12 + '\n')
        else:
            lines.append('*' * 12 + '\n')

        with open('text_file.txt', 'w') as file:
            file.writelines(lines)

        print("Задача выполнена!")

    except FileNotFoundError:
        print("Ошибка: Файл 'text_file.txt' не найден!")

def task6():
    try:
        char = input("Введите символ для поиска: ").strip()
        if len(char) != 1:
            print("Ошибка: нужно ввести один символ!")
            return

        with open('text_file.txt', 'r') as file:
            content = file.read()

        words = content.split()
        count = 0
        matching_words = []

        for word in words:
            clean_word = word.strip('.,!?;:"').lower()
            if clean_word and clean_word[0] == char.lower():
                count += 1
                matching_words.append(word)

        print(f"Найдено {count} слов, начинающихся с символа '{char}':")
        for word in matching_words[:10]:  # Показываем первые 10 слов
            print(f"  {word}")
        if len(matching_words) > 10:
            print(f"  ... и еще {len(matching_words) - 10} слов")

    except FileNotFoundError:
        print("Ошибка: Файл 'text_file.txt' не найден!")

def task7():
    try:
        with open('file_with_stars.txt', 'r') as file1:
            lines = file1.readlines()

        modified_lines = [line.replace('*', '&') for line in lines]

        with open('file_with_ampersands.txt', 'w') as file2:
            file2.writelines(modified_lines)

        print("Задача выполнена! Символы * заменены на & в новом файле.")

    except FileNotFoundError:
        print("Ошибка: Файл 'file_with_stars.txt' не найден!")

def task8():
    strings = [
        "Первая строка",
        "Вторая строка",
        "Третья строка",
        "Четвертая строка",
        "Пятая строка"
    ]

    print("Массив для записи:")
    for i, string in enumerate(strings, 1):
        print(f"{i}. {string}")

    with open('array_output.txt', 'w') as file:
        for string in strings:
            file.write(string + '\n')

    print("Задача выполнена! Массив записан в файл 'array_output.txt'")

def task9():
    try:
        filename = input("Введите имя файла (по умолчанию 'text_file.txt'): ").strip()
        if not filename:
            filename = 'text_file.txt'

        with open(filename, 'r') as file:
            content = file.read()

        char_count = len(content)
        print(f"Файл '{filename}' содержит {char_count} символов.")

    except FileNotFoundError:
        print(f"Ошибка: Файл '{filename}' не найден!")

def task10():
    try:
        filename = input("Введите имя файла (по умолчанию 'text_file.txt'): ").strip()
        if not filename:
            filename = 'text_file.txt'

        with open(filename, 'r') as file:
            lines = file.readlines()

        line_count = len(lines)
        print(f"Файл '{filename}' содержит {line_count} строк.")

    except FileNotFoundError:
        print(f"Ошибка: Файл '{filename}' не найден!")

def main():
    while True:
        print("\n" + "=" * 50)
        print("Меню: \n"
                    "1. Создать примеры файлов для демонстрации \n"
                    "2. Задание 2 - Слова из 7+ букв из басни \n"
                    "3. Задание 3 - Переписать строки с сохранением порядка \n"
                    "4. Задание 4 - Переписать строки в обратном порядке \n"
                    "5. Задание 5 - Добавить строку из звездочек \n"
                    "6. Задание 6 - Подсчитать слова по первой букве \n"
                    "7. Задание 7 - Заменить * на & \n"
                    "8. Задание 8 - Записать массив в файл \n"
                    "9. Задание 9 - Подсчитать символы в файле \n"
                    "10. Задание 10 - Подсчитать строки в файле \n"
                    "0. Выход")

        choice = input("Выберите задание (0-10): ").strip()

        if choice == '0':
            print("Выход из программы.")
            break
        elif choice == '1':
            basnya()
        elif choice == '2':
            task2()
        elif choice == '3':
            task3()
        elif choice == '4':
            task4()
        elif choice == '5':
            task5()
        elif choice == '6':
            task6()
        elif choice == '7':
            task7()
        elif choice == '8':
            task8()
        elif choice == '9':
            task9()
        elif choice == '10':
            task10()
        else:
            print("Неверный выбор! Попробуйте снова.")

        input("\nНажмите Enter для продолжения...")

if __name__ == "__main__":
    main()