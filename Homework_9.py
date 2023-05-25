def print_number_pattern(n):
    # Определение максимального числа в строке
    max_num = n

    # Формирование паттерна чисел
    pattern = []
    for i in range(1, n + 1):
        line = list(range(1, i + 1)) + list(range(i - 1, 0, -1))
        pattern.append(line)

    # Определение максимальной длины строки
    max_length = len(' '.join(map(str, pattern[-1])))

    # Вывод паттерна чисел
    for line in pattern:
        # Центрирование строки
        line_str = ' '.join(map(str, line)).center(max_length)

        print(line_str)


n = int(input("Введите число n: "))
print_number_pattern(n)
