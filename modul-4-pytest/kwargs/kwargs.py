def greet(**kwargs):
    print(f'Hello, {kwargs["name"]}! You are {kwargs["age"]} years old.')

#greet(name="Alice", age=25)


def create_dict(**kwargs):
    return kwargs

#print(create_dict(mom='Irina', dad='Dmitrii', son='Sasha', doughter='Yulka'))


def update_settings(default_settings, **kwargs):
    default_settings.update(kwargs)
    return default_settings

default_settings = {"theme": "light", "notifications": True}
#print(update_settings(default_settings, theme="dark", volume=80))


def filter_kwargs(**kwargs):
    filtered_kwargs = dict()
    for key in kwargs.keys():
        if kwargs[key] > 10:
            filtered_kwargs[key] = kwargs[key]
    return filtered_kwargs

#print(filter_kwargs(a=5, b=20, c=15, d=3))


# создание декоратора
# ниче не понятно, но оно работает
def log_kwargs(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print('Called with kwargs: ', kwargs)
        return res
    return wrapper


@log_kwargs
def my_function(a, b, **kwargs):
    return a + b

my_function(5, 10, debug=True, verbose=False)