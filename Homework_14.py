numbers = [15, 9, 4, 10, 30, 27, 8, 25, 45, 12]
divisible_by_3_not_5 = []
divisible_by_5_not_3 = []
divisible_by_3_and_5 = []

for number in numbers:
    if number % 3 == 0 and number % 5 == 0:
        divisible_by_3_and_5.append(number)
    elif number % 3 == 0 and number % 5 != 0:
        divisible_by_3_not_5.append(number)
    elif number % 5 == 0 and number % 3 != 0:
        divisible_by_5_not_3.append(number)

print("Numbers divisible by 3 but not by 5:", divisible_by_3_not_5)
print("Numbers divisible by 5 but not by 3:", divisible_by_5_not_3)
print("Numbers divisible by both 3 and 5:", divisible_by_3_and_5)
