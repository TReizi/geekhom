string = input("Введите слова через пробел: ").split()
for i, word in enumerate(string, 1):
    print(f'{i}, {word[:10]}')
