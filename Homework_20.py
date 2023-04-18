longest_line = ''
with open('file.txt', 'r') as file:
    for line in file:
        if len(line) > len(longest_line):
            longest_line = line
print(longest_line)
