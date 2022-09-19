import datetime
import os

path = os.path.abspath('file.txt')


def decorator(path):


    def log_decorator(function):

        def logger(*args, **kwargs):
            with open(path, 'w') as f:
                f.write(f'Дата и время - {datetime.datetime.now()}')
                f.write(f' Название функции - {function.__name__}')
                f.write(f' Аргументы - {args} и {kwargs}')
                result = function(*args, **kwargs)
                f.write(f' Результат - {result}')
                return(result)
        return logger
    return log_decorator


@decorator(path)
def summer(a, b):
    c = a + b
    return c

summer(1, 2)

