number_1 = int(input('Введите первое число: '))
number_2 = int(input('Введите второе число: '))
try:
    division = number_1 / number_2
except ZeroDivisionError:
    division = 0
    print(division)
print('Операция выполнена, результат = ' + str(number_1/number_2))

# второй вариант
#number_1 = int(input('Введите первое число: '))
#number_2 = int(input('Введите второе число: '))
#if number_2 == 0:
#    print('Делитель равен нулю')
#else:
#    print(number_1 / number_2)
