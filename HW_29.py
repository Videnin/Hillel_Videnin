def linearize_list(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(linearize_list(item))
        else:
            result.append(item)
    return result
