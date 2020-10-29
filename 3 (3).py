def my_func(a, b, c):
    numbers = [a, b, c]
    numbers.remove(min(a, b, c))
    return sum(numbers)

print (my_func(3, 15, 8))

# второй вариант
list = sorted([10, 5, 13], reverse=True)
print(list[0]+list[1])

