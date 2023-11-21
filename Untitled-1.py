number = int(input('Введите число: '))
numberiz = int(input('Введите numberiz: '))
numberv = int(input('Введите numberv: '))

# Из 10 в 2

if numberiz == 10 and numberv == 2:
   q10to2number = bin(number)
   print (q10to2number)
elif numberiz == 10 and numberv == 8:
   q10to8number = oct(number)
   print(q10to8number)
elif numberiz == 10 and numberv == 16:
   q10to16number = hex(number)
   print(q10to16number)
else:
   print('error')