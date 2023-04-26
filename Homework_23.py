def to_dict(lst):
    if len(lst) % 2 != 0:
        raise ValueError("Число элементов в списке должно быть четным")

    result_dict = {}
    for i in range(0, len(lst), 2):
        result_dict[lst[i]] = lst[i+1]

    return result_dict
