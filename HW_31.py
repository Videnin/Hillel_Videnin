from itertools import zip_longest

def custom_zip(*sequences, full=False, default=None):
    if full:
        return list(zip_longest(*sequences, fillvalue=default))
    else:
        return list(zip(*sequences))
