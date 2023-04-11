email = input("Введите адрес электронной почты: ")

if email.count('@') != 1 or email.count('.') != 1:
    print(False)
else:
    at_index = email.index('@')
    dot_index = email.index('.')
    if at_index < dot_index:
        if email[0] != '@' and email[-1] != '.':
            print(True)
        else:
            print(False)
    else:
        print(False)

