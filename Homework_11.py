multi_string = "Hello all. Here's pretty cold and hot. Choose yourself."
multi_string = multi_string.rstrip('.')
sentences = multi_string.split('.')
words_number = []

for sentence in sentences:
    words = sentence.strip().split()
    words_number.append(len(words))

print(words_number)



