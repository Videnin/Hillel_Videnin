def call_counter(file_name):
    def decorator(func):
        def wrapper(*args, **kwargs):
            wrapper.count += 1
            with open(file_name, 'a') as f:
                f.write(f"Function '{func.__name__}' was called {wrapper.count} times\n")
            return func(*args, **kwargs)
        wrapper.count = 0
        return wrapper
    return decorator
