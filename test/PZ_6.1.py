#Дан целочисленный список A размера 10. Вывести порядковый номер последнего из тех его элементов Ak,
# которые удовлетворяют двойному неравенству A1<Ak<A10. Если таких элементов нет, то вывести 0.
def find_last_element(A): #нахождение последнего элемента
    try:
        last_element = A[-1]
        if 1 < last_element < 10:
            return last_element
        else:
            return 9
    except IndexError:
        return 0

A = [1, 2, 3, 4, 5, 6, 7, 8, 10]
result = find_last_element(A)
print("Последний элемент, удовлетворяющий условию:", result)