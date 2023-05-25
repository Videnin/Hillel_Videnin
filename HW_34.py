def apply_function(func, *sequences):
    results = []

    min_length = min(len(seq) for seq in sequences)
    for i in range(min_length):
        args = [seq[i] for seq in sequences]
        result = func(*args)
        results.append(result)

    return results
