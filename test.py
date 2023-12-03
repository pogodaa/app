import tkinter as tk
# Функция для перевода числа из десятичной системы в другую систему
def decimal_to_base(num, base):
    digits = "0123456789ABCDEF"
    result = ""
    while num > 0: # Пока вводное число > 0 цикл
        digit = num % base # Вводное число делится на вводную систему исчисления
        result = digits[digit] + result # присваивание result, digits в котором все допустимые знаки под индексом digit, + result
        num = num // base # обновление num (деление до ближайшего целого числа)
    return result

# Функция для перевода числа из заданной системы исчисления в десятичную систему
def base_to_decimal(number, base):
    digits = "0123456789ABCDEF"
    number = str(number).upper()
    result = 0
    for i in range(len(number)): #начинается цикл for, который перебирает каждую цифру вводного числа. Для этого используется функция range, которая создает последовательность чисел от 0 до длины вводного числа (len(number)).
        if number[i] not in digits[:base]: 
            # Внутри цикла проверяется, содержится ли текущая цифра в диапазоне допустимых цифр для заданной системы счисления. Если нет, то функция возвращает значение None.
            # Диапазон digits[:base] представляет собой подстроку digits, содержащую только первые base символов. Например, если задана система счисления с основанием 16 (шестнадцатеричная система), то digits[:base] будет содержать символы "0", "1", "2", ..., "E", "F". 
            # Если текущая цифра не содержится в этом диапазоне, то это означает, что цифра не является допустимой в данной системе счисления. В таком случае функция возвращает значение None, чтобы указать на ошибку в исходном числе.
            return None 
        digit = digits.index(number[i]) # если number[i] равно "A", а digits содержит символы "0", "1", ..., "9", "A", "B", ..., "F", то digits.index(number[i]) вернет значение 10, так как индекс символа "A" в строке digits равен 10.
        result = result * base + digit #  происходит умножение итогового результата на основание системы счисления base и добавления текущей цифры digit.
    return result

def convert_number():
    number = entry_number.get() 
    base_from = int(entry_base_from.get())
    base_to = int(entry_base_to.get())
    # Когда вызывается метод .get() на объекте виджета, он возвращает текущее значение, введенное пользователем в этот виджет. 
    # entry_number.get() вернет значение, введенное пользователем в entry_number, аналогично для entry_base_from.get() и entry_base_to.get().

    if base_from == 2 and not all(digit in "01" # base_from == 2 проверяет, является ли введенная система счисления двоичной (со значением равным 2).
        for digit in number): # all(digit in "01" for digit in number) проверяет, что каждая цифра в числе number является либо "0", либо "1".
        result_label.config(text="Ошибка: Введено некорректное двоичное число")
        # config() используется для изменения свойства text, которое отображает текст внутри виджета.
        return
    
    decimal_number = base_to_decimal(number, base_from)
    
    if decimal_number is None:
        result_label.config(text="Ошибка: Введено некорректное число для указанной системы исчисления")
        return

    result = decimal_to_base(decimal_number, base_to)
    result_label.config(text="Результат перевода: " + result)

window = tk.Tk() # Создает главное окно приложения
window.title("Перевод числа из одной системы исчисления в другую") #  Устанавливает заголовок для главного окна.

number_label = tk.Label(window, text="Введите число:") # Создает виджет Label с текстом "Введите число:" и добавляет его в главное окно.
number_label.pack() #  Размещает виджет Label в окне

entry_number = tk.Entry(window) # Создает виджет Entry для ввода числа и добавляет его в главное окно.
entry_number.pack() # Размещает виджет Entry в окне. и тд

base_from_label = tk.Label(window, text="Из какой системы исчисления перевести:") 
base_from_label.pack()

entry_base_from = tk.Entry(window)
entry_base_from.pack()

base_to_label = tk.Label(window, text="В какую систему исчисления перевести:")
base_to_label.pack()

entry_base_to = tk.Entry(window)
entry_base_to.pack()

convert_button = tk.Button(window, text="Перевести", command=convert_number) # Создает кнопку с надписью "Перевести" и связывает ее с функцией convert_number().
convert_button.pack() # Размещает виджет button в окне

result_label = tk.Label(window, text="") # Создает виджет Label для отображения результата перевода и добавляет его в главное окно.
result_label.pack() # Размещает виджет Label в окне.

window.mainloop() # Запуск

## Баги:
##                1. Можно вводить "ИЗ","В" любые числа, и получать результат
##                2. 