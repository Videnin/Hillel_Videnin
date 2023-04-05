min_width = int(input("Введите минимальную ширину: "))
max_width = int(input("Введите максимальную ширину: "))

if min_width > max_width:
    print("Ошибка! Минимальная ширина больше максимальной.")
elif (max_width - min_width) % 2 != 0:
    print("Ошибка! Разность максимальной и минимальной ширины не кратна 2.")
else:
    diamond_width = max_width
    diamond_height = diamond_width // 2 + 1

    for i in range(1, diamond_height):
        print(" " * (diamond_height - i) + "*" * (i * 2 - 1))

    for i in range(diamond_height, 0, -1):
        print(" " * (diamond_height - i) + "*" * (i * 2 - 1))

