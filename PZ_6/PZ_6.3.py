#дан список размера N, все элементы которого, кроме первого,
# упорядочены по возрастанию. Сделать список упорядоченным, переместив первый элемент на новую позицию.
def sort_list(lst):
    first_element = lst[0]
    sorted_lst = sorted(lst[1:])  #сортируем все элементы кроме первого
    sorted_lst.insert(1, first_element)  #вставляем первый элемент в начало отсортированного списка
    return sorted_lst

N = 10
lst = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
sorted_lst = sort_list(lst)
print(sorted_lst)