my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(f'исходный список {my_list}')

new_my_list = [el for num, el in enumerate(my_list) if my_list[num - 1] < my_list[num]]
print(f'результат  {new_my_list}')