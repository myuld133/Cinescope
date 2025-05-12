
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Собака лает."

class Cat(Animal):
    def speak(self):
        return "Кошка мяукает."

class Mouse(Animal):
    pass # пример не реализованного абстрактного метода спик

mickey = Mouse() # ошибка: нельзя создать объект