# методы класса - пример с собакой
# class Dog:
#     species = "Canis familiaris"  # Атрибут класса
#
#     @classmethod
#     def get_species(cls):  # cls ссылается на класс Dog
#         return cls.species
#
# print(Dog.get_species())


# практика - задание 1
# class Animals:
#     species = []
#
#     def __init__(self, name):
#         #self.name = name
#         Animals.add_species(name)
#
#     @classmethod
#     def add_species(cls, name):
#         if name not in cls.species: #cls - ссылка на класс Animals
#             cls.species.append(name)
#
#     @classmethod
#     def show_species(cls):
#         print(cls.species)
#
# Animals('cat')
# Animals.show_species()
#
# Animals('cow')
# Animals.show_species()
#
# Animals('cow')
# Animals.show_species()



# создание объектов через cls()
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def create_anonymous(cls): #метод класса
      return cls("Anonymous", 0) # cls - ссылается на класс Person

    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old.")

# Обычное создание объекта
person1 = Person("Alice", 30)
person1.introduce()

# Создание объекта через метод класса
person2 = Person.create_anonymous()
person2.introduce()
print(type(person1))
print(type(person2))