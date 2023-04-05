min_width = 2
max_width = 8

if (max_width - min_width) % 2 != 0:
else:

    if min_width > max_width:
    else:
        for i in range(min_width, max_width + 1, 2):
            print(" " * ((max_width - i) // 2) + "*" * i)
        for i in range(max_width - 2, min_width - 1, -2):
            print(" " * ((max_width - i) // 2) + "*" * i)


