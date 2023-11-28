# Программа для перевода числа из одной системы исчисления в другую

# Функция для перевода числа из десятичной системы в другую систему
def decimal_to_base(num, base): # num для вводимого числа # base для вводной системе исчисления
    digits = "0123456789ABCDEF" # символы для системы счисления до 16
    result = "" # объявление пустой переменной
    while num > 0: # Пока вводное число > 0 цикл
        digit = num % base # Объявление элемента типо i который получается при делении без остатка от вводного числа на систему исчисления
        result = digits[digit] + result # присваивание result, digits в котором все допустимые знаки, под индексом digit + пока пустая переменная, после второго цикла будет число которе будет складываться
        num = num // base # обновление num, '//' деление до  пример 12//5 = 2
    return result

# Функция для перевода числа из заданной системы исчисления в десятичную систему
def base_to_decimal(number, base): # вводное число, система из
    digits = "0123456789ABCDEF" # символы для системы счисления до 16
    number = str(number).upper() # вводное число присваивается к str т.к возможны ABC и тд, капсом
    result = 0 # 0 потому что при расчётах нужно
    for i in range(len(number)): # для i в range(возвращает последовательность заданого числа между заданным дипозоном) от len(возвращает длну строки) вводного числа
        digit = digits.index(number[i]) # Метод index () в Python помогает найти значение индекса элемента в последовательности вводного числа
        result = result * base + digit # обновление result с помощью старого result который умножается на вводное из которое складывается с
    return result

# Ввод числа
print('\n')
number = input("Введите число: ")

# Ввод системы исчисления ИЗ
base_from = int(input("Из какой системы исчисления перевести (2): "))

# Ввод системы исчисления В
base_to = int(input("В какую систему исчисления перевести (2-16): "))

# Перевод числа из заданной системы исчисления в десятичную
decimal_number = base_to_decimal(number, base_from)

# Перевод числа из десятичной системы в указанную систему исчисления
result = decimal_to_base(decimal_number, base_to)

# Вывод результата
print("Результат перевода:", result,'\n')