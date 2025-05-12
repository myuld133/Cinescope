# # множественное наследование - пример порядка разрешения методов (MRO)
class Actor:
    @classmethod
    def greet(cls):
        print('Hi, I\'m an Actor!')

class Singer:
    @classmethod
    def greet(cls):
        print('Hi, I\'m a Singer!')

class Showman(Actor, Singer):
    pass

p2 = Showman()
p2.greet()
print(Showman.mro())

class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        assert self.balance > 0, f'ValueError'

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        assert amount > 0, f'Negative amount'
        if self.balance > amount:
            self.balance -= amount
        else:
            self.balance = 0

class SavingsAccount(Account):
    def __init__(self, name, balance, interest_rate):
        super().__init__(name, balance) # вызов метода родительского класса
        self.interest_rate = interest_rate

    def withdraw(self, amount):
        assert (self.balance - amount) >= 100, f'Минимальный остаток должен быть 100'
        super().withdraw(amount)

    def add_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.deposit(interest)


# acc1 = Account('Yulka', 20)
# acc1.deposit(10)
# acc1.withdraw(-40)
# print(acc1.balance)

# acc2 = SavingsAccount('Goshka', 200, 20)
# acc2.withdraw(50)
# print(acc2.balance)