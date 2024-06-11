#составить программу, в которой функция генерирует четырехзначное число и определяет, есть ли в числе одинаковые цифры.

import random

def generate_four_digit_number():
    return random.randint(1000, 9999)

def check_for_identical_digits(number):
    return len(set(str(number))) != 4

#cгенерируйте четырехзначное число
random_number = generate_four_digit_number()
print("Случайное четырехзначное число:", random_number)

#gроверьте наличие идентичных цифр
if check_for_identical_digits(random_number):
    print("Номер состоит из одинаковых цифр")
else:
    print("В номере нет одинаковых цифр")


