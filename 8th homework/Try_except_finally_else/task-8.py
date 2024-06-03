"""
Следующий код работает отлично, если пользователь вводит цифровое значение, но всегда есть НО:
"""
try:
    min_num = int(input("Введите первое число: "))
    max_num = int(input("Введите второе число: "))
except ValueError:
    ...
else:
    for i in range(min_num, max_num+1):
       print(f"Квадрат числа {i} равен {i*i}")


