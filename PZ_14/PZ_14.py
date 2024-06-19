# Из исходного текстового файла (expansion.txt) выбрать имена файлов, соответствующие типам: .xls, .xml, .html, .css, .py.
# Посчитать количество полученных элементов.

import re

with open('expansion.txt', 'r') as file:
    content = file.read()

# Определяем регулярное выражение для поиска имен файлов с расширениями .xls, .xml, .html, .css, .py
pattern = re.compile(r'\b[a-zA-Z0-9_\.-]+\.(xls|xml|html|css|py)\b')

matches = pattern.findall(content)

count = len(matches)

print(f'Нашел {count} файлов со следующими расширениями: .xls, .xml, .html, .css, .py')
print('Имена файлов:', ', '.join(matches))