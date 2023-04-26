def skip(condition, reason):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if condition:
                print(reason)
            else:
                return func(*args, **kwargs)
        return wrapper
    return decorator
