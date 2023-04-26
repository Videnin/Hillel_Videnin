def second_largest_number(lst):
    if not lst:
        return None

    largest = second_largest = float('-inf')

    for num in lst:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num

    return second_largest

