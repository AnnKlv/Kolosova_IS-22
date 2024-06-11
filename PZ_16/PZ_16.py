#Создайте класс “Круг”, который имеет атрибут радиуса и методы для вычисления площади,
#длины окружности и диаметра.
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14159 * self.radius ** 2

    def calculate_circumference(self):
        return 2 * 3.14159 * self.radius

    def calculate_diameter(self):
        return 2 * self.radius

radius = 5
circle = Circle(radius)

print("Площадь круга:", circle.calculate_area())
print("Длина окружности:", circle.calculate_circumference())
print("Диаметр круга:", circle.calculate_diameter())