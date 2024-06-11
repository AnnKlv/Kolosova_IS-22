#Составить генератор (yield), который преобразует все буквенные символы в строчные.

def lowercase_char(char):
    yield char.lower() if char.isalpha() else char

input_string = "Hello, World!"

# Применение генераторного выражения к каждому символу строки input_string
lowercase_result = ''.join(char.lower() if char.isalpha() else char for char in input_string)

# Вывод результата lowercase_result
print(lowercase_result)