#Запросить у пользователя два целых числа.

#Вывести на одной строке выражение их суммы, на второй выражение для произведения:

first_number = int(input( "Enter first number : "))
second_number = int(input( "Enter second number: "))
sum = first_number + second_number
multiply = first_number * second_number
print(f"{first_number} + {second_number} = {sum}")
print(f"{first_number} * {second_number} = {multiply}")