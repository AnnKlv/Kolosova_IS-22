#Задание предполагает, что у студента есть проект с практическими работами (2-13),
#оформленный согласно требованиям. Все задания выполняются с использованием модуля OS:
# перейдите в каталог PZ11. Выведите список всех файлов в этом каталоге. Имена
#вложенных подкаталогов выводить не нужно.
# перейти в корень проекта, создать папку с именем test. В ней создать еще одну папку
#test1. В папку test переместить два файла из ПЗ6, а в папку test1 - один файл из ПЗ7.
#Файл из ПЗ7 переименовать в test.txt. Вывести в консоль информацию о размере
#файлов в папке test.
# перейти в папку с PZ11, найти там файл с самым коротким именем, имя вывести в
#консоль. Использовать функцию basename () (os.path.basename()).
# перейти в любую папку где есть отчет в формате .pdf и «запустите» файл в
#привязанной к нему программе. Использовать функцию os.startfile().
# удалить файл test.txt.

import os

os.chdir("..")
os.chdir("PZ_11")


files = os.listdir()
print("Файлы в каталоге PZ_11:")
for file in files:
    if os.path.isfile(file):
        print(file)


os.chdir("..")
os.makedirs("test/test1", exist_ok=True)


os.rename("PZ_6/PZ_6.1.py", "test/PZ_6.1.py")
os.rename("PZ_6/PZ_6.2.py", "test/PZ_6.2.py")


os.rename("PZ_7/PZ_7.1.py", "test/test1/test.txt")


os.chdir("test")
for file in os.listdir():
    if os.path.isfile(file):
        print(f"{file}: {os.path.getsize(file)} байт")


os.chdir("..")
os.chdir("PZ_11")
shortest_file = min(files, key=len)
print("Файл с самым коротким именем в PZ_11:", os.path.basename(shortest_file))

os.chdir("..")
for file in os.listdir():
    if file.endswith(".pdf"):
        os.startfile(file)

os.remove("test/test1/test.txt")