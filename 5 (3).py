with open('text 3.txt') as f:
    salaries = []
    lines = f.readlines()
    for line in lines:
        name, salary = line.split('-')
        salaries.append(int(salary))
        if int(salary) < 20000:
            print(line, end='')
    print('\n Средняя зп:  ', sum(salaries)/ len(salaries))