def user_list(user_name, user_f_name, user_age, user_city,user_mail,user_phone):
    user_name = input('Введите своё имя: ')
    user_f_name = input('Введите свою фамилию: ')
    user_age = input('Введите свой возраст: ')
    user_city = input('Введите свой город: ')
    user_mail = input('Введите свой mail ')
    user_phone = input('Введите свой телефон через: ')
    return ' '.join([ user_name,user_f_name, user_age, user_city ,user_mail , user_phone])

print(user_list(user_name='', user_f_name= '',user_age ='' , user_city = '', user_mail = '', user_phone= ''))


