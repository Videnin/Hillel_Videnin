import random
def get_random_string(length: int) -> str:
    chars = list(range(48, 58)) + list(range(65, 91)) + list(range(97, 123))

    result = ""
    for i in range(length):
        char_code = random.choice(chars)
        result += chr(char_code)

    return result
