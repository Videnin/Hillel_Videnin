#Создать список из трех стран.

#Создать словарь из трех пар ключ-значение. Ключом должна быть строка с названием страны из первого списка, значением строка со столицей.

#Вывести каждую пару на отдельной строке, разделить ключ-значение двоеточием и пробелом


countries = ['USA', 'China', 'Italy']
capitals = {
    countries[0]: 'Washington',
    countries[1]: 'Pekin',
    countries[2]: 'Rome'}
for country in countries:
print(country + ': ' + capitals[country])