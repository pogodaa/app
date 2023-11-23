symbol_for_check = [0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F']

print('\n','\t','\t','Приложение, переводящее из вводимой пользователем системы исчисления в другую систему исчисления указанную пользователем','\n')

# Юзер вводит число
user_number = int(input("Введите число: "))
print('\n','Ваше число: ',user_number,'\n','\n')

# Юзер вводит систему исчисления введённого числа
user_system_iz = int(input(("Укажите систему исчисления введённого вами числа (2-двоичная,8-восьмиричная,10-десятичная,16-шестнадцатеричная): ")))
if user_system_iz != 2 or 8 or 10 or 16:
    print('\n','Система исчисления вашего введённого числа: ',user_system_iz,'\n','\n')
else:
    print('\n','Ошибка','\n')

# Проверка, соответсвует ли указанное число пользователя, той системе исчисления которую он указал

# Если 2
if user_system_iz == 2:
    if symbol_for_check[0,1] in user_number:
        print('Проверка: введённое вами число соответствует введённой вами системе исчисления')
        dop_pomosh_dlya_perevoda_chisla_iz = int('0b')
        result_user_number_after_check = user_number+dop_pomosh_dlya_perevoda_chisla_iz
    else:
        print('Проверка: введённое вами число НЕ соответствует введённой вами системе исчисления')
else:
    print("Ошибка")

# Если 8
if user_system_iz == 8:
    if symbol_for_check[0:8] in user_number:
        print('Проверка: введённое вами число соответствует введённой вами системе исчисления')
        dop_pomosh_dlya_perevoda_chisla2 = int('0o')
        result_user_number_after_check = user_number+dop_pomosh_dlya_perevoda_chisla2
    else:
        print('Проверка: введённое вами число НЕ соответствует введённой вами системе исчисления')
else:
    print("Ошибка")

# Если 10
if user_system_iz == 10:
    if symbol_for_check[0:10] in user_number:
        print('Проверка: введённое вами число соответствует введённой вами системе исчисления')
    else:
        print('Проверка: введённое вами число НЕ соответствует введённой вами системе исчисления')
else:
    print("Ошибка")

# Если 16
if user_system_iz == 16:
    if symbol_for_check in user_number:
        print('Проверка: введённое вами число соответствует введённой вами системе исчисления')
        dop_pomosh_dlya_perevoda_chisla2 = int('0h')
        result_user_number_after_check = user_number+dop_pomosh_dlya_perevoda_chisla2
    else:
        print('Проверка: введённое вами число НЕ соответствует введённой вами системе исчисления')
else:
    print("Ошибка")

user_system_v = int(input('Укажите систему исчисления, в которую вы желаете перевести указанное вами число: '))
print('\n','Система исчисления для перевода вашего введённого числа: ',user_system_v,'\n','\n')

