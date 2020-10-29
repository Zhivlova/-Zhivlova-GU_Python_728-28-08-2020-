from itertools import count
from itertools import cycle

for el in count(3):
    if el > 10:
        break
    else:
        print(el)

score = 0
for i in cycle('dog'):
    score += 1
    if score > 10:
        break
    print(i)
