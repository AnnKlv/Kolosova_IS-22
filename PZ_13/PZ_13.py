#В матрице элементы кратные 3 увеличить в 3 раза

matrix = [[x * y for x in range(2, 5)] for y in range(2, 5)]
print("Матрица:")
for line in matrix:
    print(line)

def multiply_by_3_if_multiple_of_3(num):
    return num * 3 if num % 3 == 0 else num

new_matrix = list(map(lambda row: list(map(multiply_by_3_if_multiple_of_3, row)), matrix))

#Выводим измененную матрицу
for row in new_matrix:
    print("Измененная матрица:", row)