# В последовательности на n целых чисел умножить все элементы на последний минимальный элемент

from functools import reduce

def multiply_middle_third(lst):
    start = len(lst) // 3
    end = 2 * len(lst) // 3
    middle_third = lst[start:end]
    return reduce(lambda x, y: x*y, middle_third), middle_third

# Генерация списка чисел для примера
numbers = [i for i in range(1, 11)]  # Генерируем список чисел от 1 до 10

result, middle_sequence = multiply_middle_third(numbers)
print("Произведение элементов средней трети:", result)
print("Последовательность элементов средней трети:",numbers)