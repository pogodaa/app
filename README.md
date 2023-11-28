# Приложение, переводящее из вводимой пользователем системы исчисления в другую систему исчисления, указанную пользователем

# Функция для перевода числа из десятичной системы в другую систему

def decimal_to_base(n, base):

    digits = "0123456789ABCDEF" # символы для системы счисления до 16

    result = ""

    while n > 0:

        digit = n % base

        result = digits[digit] + result

        n = n // base

    return result

# Функция для перевода числа из заданной системы исчисления в десятичную систему

def base_to_decimal(number, base):

    digits = "0123456789ABCDEF" # символы для системы счисления до 16

    number = str(number).upper()

    result = 0

    for i in range(len(number)):

        digit = digits.index(number[i])

        result = result * base + digit
        
    return result

# Функция для проверки 

def check_number_system(input_string):

    binary_digits = {'0', '1'}

    octal_digits = {'0', '1', '2', '3', '4', '5', '6', '7'}

    decimal_digits = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}

    hexadecimal_digits = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'}

    if all(digit in binary_digits for digit in input_string):

        return "Двоичная система исчисления."

    elif all(digit in octal_digits for digit in input_string):

        return "Восьмеричная система исчисления."

    elif all(digit in decimal_digits for digit in input_string):

        return "Десятичная система исчисления."

    elif all(digit in hexadecimal_digits for digit in input_string):

        return "Шестнадцатеричная система исчисления."

    else:
    
        return "Введенная система исчисления не поддерживается."


## Ввод данных от пользователя

# Ввод числа и системы исчисления

number = input("Введите число: ")

base_from = int(input("Из какой системы исчисления перевести (2-16): "))

base_to = int(input("В какую систему исчисления перевести (2-16): "))

# Перевод числа из заданной системы исчисления в десятичную

decimal_number = base_to_decimal(number, base_from)

# Перевод числа из десятичной системы в указанную систему исчисления

result = decimal_to_base(decimal_number, base_to)

print("Результат перевода:", result)