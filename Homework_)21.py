

import json

users = []
with open('users_in.txt', 'r') as f:
    for line in f:
        # Удаляем символы переноса строки и разделяем строку по точке с запятой
        data = line.strip().split(';')
        name = data[0].strip()
        # Пытаемся преобразовать возраст в целое число, если не получается - присваиваем None
        try:
            age = int(data[1].strip())
        except (ValueError, IndexError):
            age = None
        # Создаем список телефонов, удаляя лишние пробелы
        phones = [phone.strip() for phone in data[2].split(',')]
        # Создаем словарь пользователя
        user = {'name': name, 'age': age, 'phones': phones}
        # Добавляем словарь в список пользователей
        users.append(user)

# Записываем список пользователей в JSON-файл
with open('users_out.json', 'w') as f:
    json.dump(users, f)

# Записываем список пользователей в текстовый файл
with open('users_out.txt', 'w') as f:
    for user in users:
        # Преобразуем возраст и список телефонов в пустую строку, если они не указаны
        age = str(user['age']) if user['age'] is not None else ''
        phones = ','.join(user['phones']) if user['phones'] else ''
        # Записываем данные в файл, разделяя точкой с запятой
        f.write(f"{user['name']};{age};{phones}\n")
