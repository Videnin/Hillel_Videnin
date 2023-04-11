multi_string = "Hello all. Here's pretty cold and hot. Choose yourself."
sentences = multi_string.split('.')
word_counts = []
for sentence in sentences:
    words = sentence.strip().split(' ')
    word_counts.append(len(words))
print(word_counts)

