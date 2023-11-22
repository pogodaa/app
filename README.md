# Приложение, переводящее из вводимой пользователем системы исчисления в другую систему исчисления указанную пользователем

## юзер вводит само число 'number'

## юзер вводит желаюмую систему исчисления через цифры (2 - двоичная, 8 - восьмеричная и тд) ИЗ

# Микро проверка числа (системы исчисления (ИЗ))


if цифраиз == 2:

 if '1' or '0' in number

 print (число во 2-ой системе исчисления)

 dop2 = '0b'

 dop2 = type(int)

 res2 = dop2 + number

 else:

 print (число не во 2-ой системе исчисления)

else:

print ('error')


if цифраиз == 8:

 if '7' or '6' or '5' or '4' or '3' or '2' or '1' or '0' in number

 print (число в 8-ой системе исчисления)

 dop8 = '0o'

 dop8 = type(int)

 res8 = dop8 + number

 else:

 print (число не в 8-ой системе исчисления)

else:

print ('error')


if цифраиз == 10:

 if '9' or '8' or '7' or '6' or '5' or '4' or '3' or '2' or '1' or '0' in number

 print (число в 10-ой системе исчисления)

 else:

 print (число не в 10-ой системе исчисления)

else:

print ('error')


if цифраиз == 16:

 if 'A' or 'B' or 'C' or 'D' or 'E' or 'F' or '9' or '8' or '7' or '6' or '5' or '4' or '3' or '2' or '1' or '0' in number

 print (число в 16-ой системе исчисления)

 dop16 = '0h'

 dop16 = type(int)

 res16 = dop16 + number

 else:

 print (число не в 16-ой системе исчисления)

else:

print ('error')


## юзер вводит желаюмую систему исчисления через цифры (2 - двоичная, 8 - восьмеричная и тд) В

# Микро проверка числа (системы исчисления (В))


if цифрав == 2:

 if '1' or '0' in number

 print (число во 2-ой системе исчисления)

 else:

 print (число не во 2-ой системе исчисления)

else:

print ('error')


if цифрав == 8:

 if '7' or '6' or '5' or '4' or '3' or '2' or '1' or '0' in number

 print (число в 8-ой системе исчисления)

 else:

 print (число не в 8-ой системе исчисления)

else:

print ('error')


if цифрав == 10:

 if '9' or '8' or '7' or '6' or '5' or '4' or '3' or '2' or '1' or '0' in number

 print (число в 10-ой системе исчисления)

 else:

 print (число не в 10-ой системе исчисления)

else:

print ('error')


if цифрав == 16:

 if 'A' or 'B' or 'C' or 'D' or 'E' or 'F' or '9' or '8' or '7' or '6' or '5' or '4' or '3' or '2' or '1' or '0' in number

 print (число в 16-ой системе исчисления)

 else:

 print (число не в 16-ой системе исчисления)

else:

print ('error')


## Из 2

if цифраиз == 2 and цифрав == 8:

 print (int(res2,8))


elif цифраиз == 2 and цифрав == 10:

 print (int(res2,10))


elif цифраиз == 2 and цифрав == 16:

 print (int(res2,16))


else:

 print('error')


## Из 8

if цифраиз == 8 and цифрав == 2:

 print (int(res8,2))


elif цифраиз == 8 and цифрав == 10:

 print (int(res8,10))


elif цифраиз == 8 and цифрав == 16:

 print (int(res8,16))


else:

 print('error')


## Из 10


if цифраиз == 10 and цифрав == 2:


 q10to2number = bin(number)


 print (q10to2number)


elif цифраиз == 10 and цифрав == 8:


 q10to8number = oct(number)


 print(q10to8number)


elif цифраиз == 10 and цифрав == 16:


 q10to16number = hex(number)


 print(q10to16number)


else:


 print('error')


# Из 16


if цифраиз == 16 and цифрав == 2:

 print (int(res16,2))


elif цифраиз == 16 and цифрав == 8:

 print (int(res16,8))


elif цифраиз == 16 and цифрав == 10:

 print (int(res16,10))


else:

 print('error')