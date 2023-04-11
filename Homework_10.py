string = input('Введите строку: ').lower().replace(' ', '')
if string == string[::-1]:
    print(True)
else:
    print(False)



string = input('Введите строку: ').lower().replace(' ', '')
is_palindrome = True
for i in range(len(string)//2):
    if string[i] != string[-i-1]:
        is_palindrome = False
        break
if is_palindrome:
    print(True)
else:
    print(False)

