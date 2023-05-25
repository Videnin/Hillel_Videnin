import functools

def memoize(func):
    cache = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        key = args + tuple(sorted(kwargs.items()))
        if key in cache:
            return cache[key]
        result = func(*args, **kwargs)
        cache[key] = result
        return result

    return wrapper
@memoize
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(5))  # Выполнится вычисление и вернет результат: 5
print(fibonacci(5))  # Вернет результат из кеша: 5
print(fibonacci(10))  # Выполнится вычисление и вернет результат: 55
print(fibonacci(10))  # Вернет результат из кеша: 55