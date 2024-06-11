#В матрице найти среднее арифметическое элементов последних двух столбцов.

#Создаем матрицу
matrix = [[x * y for x in range(2, 5)] for y in range(2, 5)]
print("Матрица:")
for line in matrix:
    print(line)

rows = len(matrix)

sum_last_two_columns = 0
count_elements = 0

for row in matrix:
    sum_last_two_columns += row[-2] + row[-1]
    count_elements += 2

average_last_two_columns = sum_last_two_columns / count_elements

#Выводим результат
print("Среднее арифметическое элементов последних двух столбцов: ", average_last_two_columns)