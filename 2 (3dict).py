answer = int(input('Введите месяц от 1 до 12: '))
seasons_dict = {12: 'winter', 1: 'winter', 2: 'winter', 3: 'spring', 4: 'spring', 5 : 'spring', 6: 'summer', 7: 'summer', 8: 'summer', 9: 'autumn', 10: 'autumn', 11: 'autumn'}
print(seasons_dict.get(answer))
