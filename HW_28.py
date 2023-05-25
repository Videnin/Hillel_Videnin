import re

def construct_sentence(text):
    sentence_regex = r'[A-Z][^.!?]*[.!?]'
    sentences = re.findall(sentence_regex, text)
    words = [sentence.split(',')[0].strip().lower() for sentence in sentences]

    # Составляем итоговое предложение
    first_word = words[0].capitalize()
    rest_of_sentence = ' '.join(words[1:])
    final_sentence = f"{first_word} {rest_of_sentence}."

    return final_sentence

# Пример использования
text = "Это первое предложение. второе предложение, третье предложение. И последнее предложение!"
result = construct_sentence(text)
print(result)
