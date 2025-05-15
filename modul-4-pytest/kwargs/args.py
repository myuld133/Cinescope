# сложение чисел
from operator import ilshift


def add_numbers(*args):
    return sum(args)

#print(add_numbers(1, 2, 3))
#print(add_numbers(10, 20, 30, 40))


# формирование списка
def create_list(*args):
    lst = list()
    i = 0
    while i < len(args):
        lst.append(args[i])
        i += 1
    return lst

#print(create_list(1, "apple", True, 3.14))


# передача аргументов
def print_args(*args):
    for arg in args:
        print(arg)

def pass_arguments(*args):
    print_args(*args)

#pass_arguments("Hello", 42, False)


# максимальное значение
def find_max(*args):
    x = 0
    for e in args:
        if e > x:
            x = e

    return x

#print(find_max(10, 20, 5, 100, 50))


# объединение строк
def join_strings(*args):
    return ' '.join(args)

#print(join_strings("Hello", "world", "!"))


# комбинированные задания для args и *kwargs
# смешанные аргументы
def process_data(*args, **kwargs):
    print('Positional arguments: ', args)
    print('Keyword arguments: ', kwargs)

#process_data(1, 2, 3, name="Alice", age=25)


# конфигурация функции
def configure_function(*args, **kwargs):
    res_dict = dict()
    i = 0
    while i < len(args):
        res_dict[args[i]] = kwargs[args[i]]
        i += 1
    return res_dict

#print(configure_function("theme", "volume", theme="dark", volume=50))


# функция-декоратор
def log_args_kwargs(func):
    def wrapper(*args, **kwargs):
        print('Positional arguments: ', args)
        print('Keyword arguments: ', kwargs)

        origin_result = func(*args, **kwargs)
        return origin_result
    return wrapper

@log_args_kwargs
def my_function(x, y, **kwargs):
    return x + y

my_function(10, 20, debug=True, verbose=False)