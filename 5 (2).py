with open('text 2.txt') as f_obj:
    lines = f_obj.readlines()
    print('Количество строк:  ', len(lines))
    for num_line, line in enumerate(lines, start=1):
        print('{} строка содержит - {}'.format(num_line, len(line.split())))
