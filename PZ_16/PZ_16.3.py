#Для задачи из блока 1 создать две функции, save_def и load_def, которые позволяют сохранять информацию
#из экземпляров класса (3 шт.) в файл и загружать ее обратно. Использовать модуль pickle для сериализации и
#десериализации объектов Python в бинарном формате.

import pickle

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14159 * self.radius ** 2

    def calculate_circumference(self):
        return 2 * 3.14159 * self.radius

    def calculate_diameter(self):
        return 2 * self.radius

def save_def(circle, filename):
    with open(filename, 'wb') as file:
        pickle.dump(circle, file)

def load_def(filename):
    with open(filename, 'rb') as file:
        obj = pickle.load(file)
    return obj

radius = 5
circle = Circle(radius)

save_def(circle, 'circle_data.pkl')

loaded_circle = load_def('circle_data.pkl')

print("Площадь круга:", loaded_circle.calculate_area())
print("Длина окружности:", loaded_circle.calculate_circumference())
print("Диаметр круга:", loaded_circle.calculate_diameter())
