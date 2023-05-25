def combine_sequences(*sequences, full=False, default=None):
    results = []

    if full:
        max_length = max(len(seq) for seq in sequences)
        for i in range(max_length):
            tuple_items = [seq[i] if i < len(seq) else default for seq in sequences]
            results.append(tuple(tuple_items))
    else:
        min_length = min(len(seq) for seq in sequences)
        for i in range(min_length):
            tuple_items = [seq[i] for seq in sequences]
            results.append(tuple(tuple_items))

    return results
