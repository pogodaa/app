import tkinter as tk

def decimal_to_base(num, base):
    digits = "0123456789ABCDEF"
    result = ""
    while num > 0:
        digit = num % base
        result = digits[digit] + result
        num = num // base
    return result

def base_to_decimal(number, base):
    digits = "0123456789ABCDEF"
    number = str(number).upper()
    result = 0
    for i in range(len(number)):
        if number[i] not in digits[:base]:
            return None
        digit = digits.index(number[i])
        result = result * base + digit
    return result

def convert_number():
    number = entry_number.get()
    base_from = int(entry_base_from.get())
    base_to = int(entry_base_to.get())

    max_lenght = 15
    if len(number) > max_lenght:
        result_label.config(text="Ошибка: Ваше число превышает: 15 символов.")
        return

    valid_bases = [2, 8, 10, 16] 
    if base_from not in valid_bases or base_to not in valid_bases:
        result_label.config(text="Ошибка: Недопустимая система исчисления")
        return

    if base_from == 2 and not all(digit in "01" for digit in number):
        result_label.config(text="Ошибка: Введено некорректное двоичное число")
        return
    
    if base_from == 8 and not all(digit in "01234567"
     for digit in number): 
     result_label.config(text="Ошибка: Введено некорректное восьмиричное число")
     return
    
    if base_from == 10 and not all(digit in "0123456789"
     for digit in number): 
     result_label.config(text="Ошибка: Введено некорректное десятичное число")
     return
    
    if base_from == 16 and not all(digit in "0123456789ABCDEF"
     for digit in number): 
     result_label.config(text="Ошибка: Введено некорректное шестнадцатеричное число")
     return

    decimal_number = base_to_decimal(number, base_from)
    if decimal_number is None:
        result_label.config(text="Ошибка: Введено некорректное число для указанной системы исчисления")
        return

    result = decimal_to_base(decimal_number, base_to)
    result_label.config(text="Результат перевода: " + result)

window = tk.Tk()
window.title("Перевод числа из одной системы исчисления в другую")

number_label = tk.Label(window, text="Введите число:")
number_label.pack()

entry_number = tk.Entry(window)
entry_number.pack()

base_from_label = tk.Label(window, text="Из какой системы исчисления перевести:")
base_from_label.pack()

entry_base_from = tk.Entry(window)
entry_base_from.pack()

base_to_label = tk.Label(window, text="В какую систему исчисления перевести:")
base_to_label.pack()

entry_base_to = tk.Entry(window)
entry_base_to.pack()

convert_button = tk.Button(window, text="Перевести", command=convert_number)
convert_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()
