def num_av(*args):
    try:
        num_a = int(input('Введите первое число '))
        num_b = int(input('Введите второе число '))
        num_as =  num_a /  num_b
    except ValueError:
        return
    except ZeroDivisionError:
        return
    return num_as

print(f'результат {(num_av())}')

