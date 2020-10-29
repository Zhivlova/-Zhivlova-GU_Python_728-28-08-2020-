from random import randint
from functools import reduce

new_list = [i for i in range(100, 1000) if i % 2 == 0]
print(new_list)
print (reduce(lambda x, y: x * y, new_list))