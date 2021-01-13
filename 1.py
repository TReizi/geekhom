def work():
    try:
        pay_per_time = float(input('Укажите выроботку в час '))
        money_h = int(input('Укажите ставку в час '))
        bonus = int(input('Укажите примию '))
        payng = pay_per_time * money_h + bonus
        print(f'Зарплата сотрудника {payng}')
    except ValueError:
        return
work()