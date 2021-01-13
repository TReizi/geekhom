from functools import reduce


def my_func(el_p, el):
    return el_p * el

print(f'Чётные значения {[el for el in range(100, 1002) if el % 2 == 0]}')
print(f'Результат вычисления произведенний всех элементов {reduce(my_func, [el for el in range(100, 1002) if el % 2 == 0])}')