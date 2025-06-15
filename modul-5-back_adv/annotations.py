from typing import Optional
from typing import Union

# простые аннотации
def multiply(a: int, b:int) -> int:
    return a * b

# аннотации коллекций
def sum_numbers(numbers: list[int]) -> int:
    return sum(numbers)

# когда значение или None
def find_user(user_id: int) -> Optional[str]:
    if user_id == 1:
        return 'Пользователь найден'
    return None

# когда функция принимает разные типы данных
def process_input(value: Union[int, str]) -> str:
    return f'Ты передал: {value}'

# работа с классами
class User:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def greet(self) -> str:
        return f'Привет, меня зовут {self.name}!'

user1 = User('Артем', 25)

#
def get_even_numbers(numbers: list[int]) -> list[int]:
    return [num for num in numbers if num % 2 == 0]