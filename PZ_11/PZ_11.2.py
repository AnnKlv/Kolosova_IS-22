# Задача 2: Из предложенного текстового файла (text18-18.txt) вывести на экран его содержимое, количество знаков пунктуации в первых четырёх строках.
# Сформировать новый файл, в который поместить текст в стихотворной форме выведя строки в обратном порядке.

with open('text18-18.txt', 'r', encoding='utf-16') as file:
    lines = file.readlines()

print("Содержимое файла:")
for line in lines:
    print(line.strip())

punctuation_count = 0
for line in lines[:4]:
    for char in line:
        if char in ',.!?:;-':
            punctuation_count += 1

print(f"\nКоличество знаков пунктуации в первых четырёх строках: {punctuation_count}")

with open('poem.txt', 'w', encoding='utf-16') as new_file:
    for line in reversed(lines):
        new_file.write(line)

print("\nНовый файл 'poem.txt' создан с текстом в стихотворной форме в обратном порядке.")