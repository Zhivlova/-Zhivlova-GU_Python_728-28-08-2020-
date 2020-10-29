my_list = [7, 5, 3, 3, 2]
answer = input('Введите число: ')
for index, number in enumerate(my_list):
    if int(answer) < int(number):
        continue
    my_list.insert(index, answer)
    break
else:
    my_list.append(answer)
print(my_list)