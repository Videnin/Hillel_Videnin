def generate_sentence(text: str) -> str:
    sentences = [s.strip() for s in re.split(r'(?<=[.?!])\s+', text) if s.strip()]
    first_words = [s.split()[0].lower() for s in sentences]
    result = ' '.join(first_words)
    return result.capitalize() + '.'
