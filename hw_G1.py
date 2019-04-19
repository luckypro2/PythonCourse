def logger(func):
    def wrapped(*args, **kwargs):
        print(f'[LOG] Вызвана функция {func.__name__} c аргументами: {args}, {kwargs}')
        result = func(*args, **kwargs)
        with open ('function.txt', 'w') as file_out:
            file_out.write(f'{func.__name__}: {result}')
        return result
    return wrapped


