with open('5.txt', 'w') as f:
    nums = input('Введите целые числа через пробел:  ')
    f.write('Введенные числа: ' + nums + '/n')
    nums = map(int, nums.split())
    sum_nums = sum(nums)
    f.write('Сумма чисел: ' + str(sum_nums))
    print('Сумма введенных чисел: ', sum_nums)
print('Все записано в файл')
