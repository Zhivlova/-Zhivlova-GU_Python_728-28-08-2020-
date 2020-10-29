from my_module import my_func
import sys
params = int(sys.argv[])
production = params[0]
salary_per_hour = params[1]
bonus = params[2]

print('Выработка в часах: ', production)
print('Ставка в час: ', salary_per_hour)
print('Премия: ', bonus)
print(my_func(production, salary_per_hour, bonus))
