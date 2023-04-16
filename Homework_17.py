lst = [['a', 'c', 'd'], ['f', 'b', 'a'], ['a', 'n', 'k'], ['e', 'l', 'i']]

sorted_cols = [sorted(col) for col in zip(*lst)]

sorted_rows = [list(row) for row in zip(*sorted_cols)]

print(sorted_rows)
