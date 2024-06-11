#Создание базового класса “Транспортное средство” и его наследование для создания классов
#“Автомобиль” и “Мотоцикл”.  В классе “Транспортное средство” будут общие свойства, такие как
#максимальная скорость и количество колес, а классы-наследники будут иметь свои уникальные свойства и методы.
class Transport:
    def __init__(self, max_speed, wheels):
        self.max_speed = max_speed
        self.wheels = wheels

class Car(Transport):
    def __init__(self, max_speed, wheels, brand, fuel_type):
        super().__init__(max_speed, wheels)
        self.brand = brand
        self.fuel_type = fuel_type

    def drive(self):
        return f"Автомобиль {self.brand} едет."

class Motorbike(Transport):
    def __init__(self, max_speed, wheels, brand, engine_type):
        super().__init__(max_speed, wheels)
        self.brand = brand
        self.engine_type = engine_type

    def start_engine(self):
        return f"Мотоцикл {self.brand} заводится."

car1 = Car(200, 4, "Toyota", "Бензин")
print(car1.drive())

motorbike1 = Motorbike(300, 2, "Yamaha", "Электричество")
print(motorbike1.start_engine())