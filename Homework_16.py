lst = [3.5, 2, 4, 6.2, 8]
new_lst = [lst[0]]

for i in range(len(lst) - 1):
    avg = (lst[i] + lst[i+1]) / 2
    new_lst.append(avg)
    new_lst.append(lst[i+1])

print(new_lst)
