
class Instrument:
    def play(self):
        raise NotImplementedError("Метод должен быть переопределён в дочернем классе")

class Piano(Instrument):
    def play(self):
        print("Пианино играет мелодию")

class Guitar(Instrument):
    def play(self):
        print("Гитара играет аккорды")

class Drums(Instrument):
    def play(self):
        print("Барабаны задают ритм")

# # Оркестр
# instruments = [Piano(), Guitar(), Drums()]
#
# for instrument in instruments:
#     instrument.play()



class Delivery:
    def deliver(self):
        raise NotImplementedError("Метод должен быть переопределён в дочернем классе")

class Car(Delivery):
    def deliver(self):
        print("Доставляет на машине")

class Bike(Delivery):
    def deliver(self):
        print("Доставляет на велосипеде")

class Drone(Delivery):
    def deliver(self):
        print("Доставляет на дроне")

# Система доставки
vehicles = [Car(), Bike(), Drone()]

# for vehicle in vehicles:
#     vehicle.deliver()