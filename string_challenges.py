# Вывести последнюю букву в слове
word = 'Архангельск'
print(f"Последняя буква в слове {word}: {word[-1]}")


# Вывести количество букв "а" в слове
word = 'Архангельск'
count = 0
for character in word.lower():
    if character == 'а':
        count += 1
print(f"Количество букв \"а\" в слове {word}: {count}")


# Вывести количество гласных букв в слове
word = 'Архангельск'
vowels = 'аоэеиыуёюя'
count = 0
for character in word.lower():
    if character in vowels:
        count += 1
print(f"Количество гласных букв в слове {word}: {count}")        


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
words = sentence.split()
count_words = len(words)
count = 0
for word in words:
    if len(word) >= 2:
        count += 1
print(f"Количество слов в предложении \"{sentence}\": {count}")


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
words = sentence.split()
for word in words:
    if len(word) >= 2:
        print(word[0])


# Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'
words = sentence.split()
words_count = 0
for word in words:
    if len(word) >= 2:
        words_count += len(word)
middle_length = words_count/len(words)
print(middle_length)