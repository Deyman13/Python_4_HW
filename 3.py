lst = list(map(int, input("Введите числа через пробел: ").split(" ")))
print(lst)
changed_list = []
for i in lst:
    if i not in changed_list:
        changed_list.append(i)
print(changed_list)


# set выполнит за вас всю работу
print(set(list(map(int, input("Введите числа через пробел: ").split(" ")))))



