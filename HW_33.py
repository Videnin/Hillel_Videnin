import random

def generate_random_string(length):
    result = ""
    for _ in range(length):
        random_char = chr(random.randint(48, 57) if random.randint(0, 1) else random.randint(65, 90))
        result += random_char
    return result
