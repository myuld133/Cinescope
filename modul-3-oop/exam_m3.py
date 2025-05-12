# Задание 1: Зелье восстановления. Тема: Функции.
def restore_health(current_health, potion):
    max_health = 100
    restored_health = current_health + potion
    if restored_health > max_health:
        restored_health = max_health
    return restored_health

# print(restore_health(50, 10))
# print(restore_health(50, 60))


# Задание 2: Гоблинский торговец. Тема: Методы класса.
class GoblinTrader:
    def __init__(self, gold):
       self.__gold = gold

    def buy_item(self, item_name, item_price):
        if self.__gold >= item_price:
            self.__gold -= item_price
            print(f'Куплен {item_name}')
        else:
            print('Недостаточно золота!')

# trader = GoblinTrader(200)
# trader.buy_item('свиток скорости', 150)
# trader.buy_item('книга заклинаний', 100)


# Задание 2.1: Гоблинский торговец. Тема: Методы класса и статические методы.
class GoblinMerchant:
    def __init__(self, gold):
        self.__gold = gold

    @staticmethod
    def tax_rate():
        return 0.1

    @classmethod
    def from_rich_merchant(cls):
        return cls(1000)

    def buy_item(self, item_name, item_price):
        total_price = item_price + item_price * self.tax_rate()
        if self.__gold >= total_price:
            self.__gold -= total_price
            return f'{item_name} куплен.'
        else:
            return f'Недостаточно золота!'

# merchant1 = GoblinMerchant(200)
# print(merchant1.buy_item('Зелье удачи', 150))
# rich_merchant = GoblinMerchant.from_rich_merchant()
# print(rich_merchant.buy_item('Карта леса', 500))


# Задание 3: Боец и маг. Тема: Наследование.
class Hero:
    def __init__(self, name, health):
        self.name = name # спросить у Николая все ли атрибуты надо приватить если логика этого не требует
        self.__health = health

    def take_damage(self, damage):
        if self.__health > damage:
            self.__health -= damage
            print(f'{self.name} получил {damage} урона. Осталось здоровья: {self.__health}')
        else:
            self.__health = 0
            print('Fatality')

class Warrior(Hero):
    def attack(self):
        super().take_damage(20)
        return 'Нанес 20 урона мечом'

class Mage(Hero):
    def attack(self):
        super().take_damage(15)
        return 'Нанес 15 урона заклинанием'

warrior = Warrior('Тралл', 120)
mage = Mage('Джайна', 80)

# for _ in range(5):
#     warrior.attack()
# print(warrior.attack())
#print(mage.attack())


# Задание 4: Полиморфизм.
class Peon:
    def work(self):
        return 'Собирает золото'

class Knight:
    def work(self):
        return 'Сражается с врагами'


def daily_work(hero):
    return hero.work()

peon = Peon()
knight = Knight()

# print(daily_work(peon))
# print(daily_work(knight))


# Задание 5: Секретные артефакты. Тема: Абстракция.
from abc import ABC, abstractmethod

class Artifact(ABC):
    @abstractmethod
    def activate(self):
        pass

class HealingArtifact(Artifact):
    def activate(self):
        return 'Восстановлено 50 здоровья'

class DamageArtifact(Artifact):
    def activate(self):
        return 'Нанесено 30 урона врагу'


heal_artifact = HealingArtifact()
damage_artifact = DamageArtifact()

# print(heal_artifact.activate())
# print(damage_artifact.activate())


# Задание 6: Гоблинский банк. Тема: Инкапсуляция.
class GoblinBank:
    def __init__(self, gold):
        if gold >= 0:
            self.__gold = gold
        else:
            raise ValueError('Количество золота не может быть отрицательным!')

    def get_gold(self):
        return self.__gold

    def deposit_gold(self, amount):
        if amount > 0:
            self.__gold += amount
            print(f'Добавлено {amount} золота. Текущий баланс: {self.__gold}')
        else:
            print('Нельзя добавить отрицательное количество!')

    def withdraw_gold(self, amount):
        if self.__gold >= amount:
            self.__gold -= amount
            print(f'Снято {amount} золота. Текущий баланс: {self.__gold}')
        else:
            print('Недостаточно золота!')

bank = GoblinBank(100)

# print(bank.get_gold())
# bank.deposit_gold(50)
# bank.withdraw_gold(30)
# bank.withdraw_gold(200)


# Задача от Наиля.
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        return f'{self.name} is eating'

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def bark(self):
        return f'Dog named {self.name} is barking'

class Cat(Animal):
    def meow(self):
        return f'{self.name} says Meow'

class Frog(Animal):
    def eat(self):
        return f'Frog with name {self.name} is eating'

dog = Dog('Pushok', 'mongrel')
print(dog.eat())
print(dog.bark())
print(dog.breed)

cat = Cat('Zhivoglot')
print(cat.eat())
print(cat.meow())

frog = Frog('Traver')
print(frog.eat())