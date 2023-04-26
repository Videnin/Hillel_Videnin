import json

result = []

with open('users.txt', 'r') as file:
    for line in file:
        line = line.strip()
        if not line:
            continue
        fields = line.split(';')
        name = fields[0].strip()
        age = int(fields[1]) if fields[1].isdigit() else None
        phones = [phone.strip() for phone in fields[2].split(',')] if len(fields) > 2 else []

        user_dict = {
            'name': name,
            'age': age,
            'phones': phones
        }
        result.append(user_dict)

with open('users_out.json', 'w') as json_file:
    json.dump(result, json_file)

# Сохранение в TXT файл
with open('users_out.txt', 'w') as txt_file:
    for user in result:
        name = user['name']
        age = user['age'] if user['age'] is not None else ''
        phones = ', '.join(user['phones']) if len(user['phones']) > 0 else ''
        txt_file.write(f"{name};{age};{phones}\n")xx