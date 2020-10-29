answer = input('Введите несколько слов: ')
words = answer.split()
for i, word in enumerate(words):
    print(i, word[:10])

