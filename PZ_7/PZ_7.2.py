#дана строка, состоящая из русских слов, разделенных пробелами (одним или несколькими).
# Вывести строку, содержащую эти же слова, разделенные одним пробелом и расположенные в обратном порядке.
def reverse_words_order(sentence):
    words = sentence.split() #разделение строки на слова
    reversed_sentence = ' '.join(words[::-1]) #объединение слов через пробел
    return reversed_sentence

input_sentence = "Привет, мир!"
output_sentence = reverse_words_order(input_sentence)
print(output_sentence)