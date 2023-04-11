s = "aab qq c badcc a qqqqqaqqqqaa tpara"
result = ""
words = s.split()

for word in words:
    count_a = word.count('a')
    if count_a == 2:
        result += word + " "
print("Words with two 'a's: ", result)
