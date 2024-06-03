#task 1
"""
Напишите функцию, чтобы найти максимальное из трех чисел
"""
def max_num(a: int,b: int, c: int):
    if a > b and a > c:
        return a
    if b > a and b > c:
        return b
    if c > a and c > b:
        return c

num = max_num(124, -1, 8)
print(num)
nums = input('Введите 3 числа через запятую: ')
list_int = [int(i) for i in nums.split(', ')]
print(f'Максимальное из указанных чисел: {max(list_int)}')



#task 2
"""
Напишите функцию, для суммирования всех чисел в списке. Не использовать встроенную функцию sum

Образец списка: (8, 2, 3, 0, 7)
"""

def my_sum(*args: int):
    cnt = 0
    for i in args:
        cnt += i
    return cnt

num_sum = my_sum(10, -2, 4, 2, 9)
print(num_sum)


#task 3
"""
 Напишите функцию, для умножения всех чисел в спискe
"""
def my_pr(*args: int):
    cnt = 1
    for i in args:
        cnt *= i
    return cnt

num_pr = my_pr(2, -1, -10, 24)
print(num_pr)



#task 4
"""
Напишите функцию, для переворота строки
"""

def my_reverse(*args):
    ''' реверс списка '''
    list1 = []
    for i in args:
        list1.append(i)
    list_rev = list1[::-1]
    return list_rev

def my_str_reverse(a: str):
    ''' реверс строки '''
    a = a[::-1]
    return a

rev_str = my_str_reverse('Дай свою машину')
print(rev_str)

rev1 = my_reverse(1, 'e', 's', 3, 'q', 5)
print(rev1)


#task 5
"""
Напишите функцию, для вычисления факториала числа (неотрицательное целое число).
Функция принимает число в качестве аргумента
"""
def my_fact(num: int):
    cnt = 1
    for i in range(1, num+1):
        cnt *= i
    return cnt

fact = my_fact(5)
print(fact)


#task 6
"""
Напишите функцию, которая принимает строку и вычисляет количество букв верхнего и нижнего регистра
"""
def reg_cnt(a: str):
    up = 0
    low = 0
    for j in a:
        if j.isupper():
            up += 1
        if j.islower():
            low += 1
        print(f'Кол-во символов в нижнем регистре: {low}')
        print(f'Кол-во символов в верхнем регистре: {up}')

reg_cnt('ЗахвотИ ЗонТиК')



#task 7
"""
Напишите функцию, которая принимает слово и определяет является ли оно палиндромом
(палиндром — Слово или фраза, которые одинаково читаются слева направо и справа налево.)
"""

def if_pal(a: str):
    if a == a[::-1]:
        print(f'Слово "{a}" - палиндром')
    else:
        print(f'Слово "{a}" -не является палиндромом')


if_pal('оно')


#task 8
"""
Пользователь делает вклад в размере n рублей сроком на years лет под 10% годовых.
Написать функцию bank, принимающая количество денег и лет, и возвращающую сумму,
которая будет на счете через years лет
"""
def bank(n: int, years: int):
    for i in range(years):
        n *=1.1
    print(f'Через {years} лет сумма составит: {round(n, 2)}')

    bank(100, 4)



#task 9
"""
С помощью функции извлеките из списка числа, делимые на 15
"""
def nums_del_15(*args):
    list1 =[]
    for i in args:
        if i % 15 == 0:
            pass
        else:
            list1.append(i)
        return list1

new_list = nums_del_15(5, 15, 30, 12, 40, 45)
print(new_list)


#task 10
"""
Напишите функцию, которое принимает целое число и возвращает сумму цифр целого числа 108 -> 9
"""
def sum_nums(a: int):
    cnt = 0
    str1 = str(a)
    for i in str1:
        cnt += int(i)
    return cnt


amn = sum_nums(1239)
print(amn)



#task1 11
"""
Напишите функцию, которая будет принимать количество секунд и возвращать их в днях-часах-минутах-секундах
"""
def sec_convert(secs: int):
    s = secs % 60
    m = secs // 60 % 60
    h = (secs // 3600) % 24
    d = (secs // 86400) % 365
    print(f'{secs} секунд = {d} дней, {h} час, {m} минутб {s} секунд')


sec_convert(91000)