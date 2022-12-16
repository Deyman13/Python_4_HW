def prime_factors(number, d = 2): # начинаем с 2, так как простые делители начинаются с 3
    list_1 = []
    while number > 1:
        num1, num2 = divmod(number, d) # аналогично (a // b, a % b) для целых чисел
        if num2 > 0: # если остаток больше 0
            d += 1 # берем следующий делитель, пока не найдется делитель с остатком 0
        else: 
            list_1.append(d) # добавляем в список подходящий делитель
            number = num1 # текущее число, уже поделенное на d делитель присваиваем к num1, чтобы повторять цикл
    return list_1 # место return списка, можем возвращать генератор с помощью yield

number = int(input())
print(f"{' * '.join(map(str, prime_factors(number)))}")


