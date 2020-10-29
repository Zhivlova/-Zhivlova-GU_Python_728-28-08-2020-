with open('text.txt', 'w+') as f_obj:
    while True:
        text = input('Введите текст: ')
        f_obj.write(text)
        if text == '':
            break
    for line in f_obj:
        print(line + '\n')