num1 = int(input("Введите первый аргумент "))
num2 = int(input('Введите второй аргумент '))
num3 = int(input('Введите третий аргумент '))
def my_func(num1 , num2, num3):
    if num1 >= num3 and num2 >= num3:
        return num1 + num2
    elif num1 > num2 and num1 < num3:
        return num1 + num3
    else:
        return num2 + num3

print(f'Результат:  {my_func(num1 , num2, num3)}')