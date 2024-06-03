# Latipov Rustam
# lesson 3,exercise 1
"""
Дано целое число. Если оно является положительным то прибавить к нему 20,
в противном случае вычесть из него 5. Вывести полученное число
"""
num = int(input('Введите целое число: '))
if num >= 0:
    num += 20
elif num < 0:
    num -= 5
    print(num)

# lesson 3,exercise 2
"""
Дано два числа. Если их сумма кратна 5, прибавить 1, иначе вычесть 2.
"""
num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))
sum1 = num1 + num2
if sum1 % 5 == 0:
    sum1 += 1
else:
    sum1 -= 2
    print(sum1)


# lesson 3,exercise 3
"""
Ввести 2 числа. Если их произведение отрицательно, умножить его на 8 и вывести на экран,
в противном случае увеличить его в 1,5 раза и вывести на экран
"""
x = int(input('Введите первое число: '))
y = int(input('Введите второе число: '))
if x * y < 0:
    print(f'{x * y * 8}')
else:
    print(f'{x * y * 1.5}')


# lesson 3,exercise 4
"""
Составить программу, которая запрашивает ввод температуры тела человека и определяет, здоров он или болен
"""
temp = float(input('Введите температуру тела: '))
if 36.3 <= temp <= 36.8:
    print('Вы здоровы.')
else:
    print('Вы заболели,вызовите скороую помощь.')


# lesson 3,exercise 5
"""
Составить программу, которая запрашивает ввод трех значений температуры и проверяет,
есть ли среди них температура таяния льда. Если такая температура введена,
вывести на экран сообщение «Введена температура таяния льда», иначе «Такой температуры нет»
"""
temp1 = float(input('Введена первое значение: '))
temp2 = float(input('Введена второе значение: '))
temp3 = float(input('Введена третье значение: '))
if temp1 > 0:
    print(f'Введена температура таяния льда: {temp1}.')
if temp2 > 0:
    print(f'Введена температура таяния льда: {temp2}.')
if temp3 > 0:
    print(f'Введена температура таяния льда: {temp3}.')
if temp1 < 0 and temp2 <=0 and temp3 <=0:
    print('Температура таяния льда не была введена.')


# lesson 3,exercise 6
"""
Составить программу, чтобы компьютер запросил имя пользователя и его год рождения,
затем подсчитал возраст человека, в зависимости от года рождения.
"""
from datetime import  datetime
year_now = datetime.now().year
name = input('Введите имя: ')
birth_year = int(input('Введите год рождения: '))
age = year_now - birth_year
print(f'Здраствуйте, {name}. Ваш возраст: {age}.')


# lesson 3,exercise 7
"""
Программа спрашивает возраст пользователя.
— Если возраст меньше или равен 18, то вывести: «Вам нужно учиться».
— Если возраст больше 18, но меньше или равен 50 — «Вам нужно работать»
— Если возраст больше 50, но меньше или равен 59 — «Вам скоро на пенсию»
— Если возраст больше 59, но меньше 110 — «Вы пенсионер».
"""
age = int(input('Введите ваш возраст:'))
if 0 < age <=18:
    print(f'{age} - подходящий возраст для учебы!)')
elif 18 < age <= 50:
    print(f'{age} - вы должны работать!)')
elif 50 < age <= 59:
    print(f'{age} - вам скоро на пенсию!)')
elif 59 < age <= 110:
    print(f'{age} - вы уже пенсионер, берегите свое здоровья!)')
else:
    print('Ничего не нашлось попробуйте еще!')


# lesson 3,exercise 8
"""
Напишите программу, которая принимает целое число от 1 до 12 и возвращает название месяца и количество дней.
"""
month = int(input('Введите номер месяца: '))
if month == 1:
    print('Январь')
elif month == 2:
    print('Февраль')
elif month == 3:
    print('Март')
elif month == 4:
    print('Апрель')
elif month == 5:
    print('Май')
elif month == 6:
    print('Июнь')
elif month == 7:
    print('Июль')
elif month == 8:
    print('Август')
elif month == 9:
    print('Сентябрь')
elif month == 10:
    print('Октябрь')
elif month == 11:
    print('Ноябрь')
elif month == 12:
    print('Декабрь')
else:
    print('Ничего не нашлось попытайтесь еще')


# lesson 3,exercise 9
"""
Написать программу, которая спрашивает у пользователя три числа и выводит количество совпадающих.
"""
var1 = int(input('Введите первое число: '))
var2 = int(input('Введите второе число: '))
var3 = int(input('Введите третье число: '))
if var1 == var2 == var3:
    print('Количество совпадающих чисел: 3')
elif var1 == var2 or var1 == var3 or var2 == var3:
    print('Количество совпадающих чисел: 2')
else:
    print('Совпадений нет.')


# lesson 3,exercise 10
"""
Если заданы два целых числа, они возвращают свое произведение только в том случае,
если произведение не больше 1000, иначе возвращают свою сумм
"""
number1 = int(input('Введите первое целое число: '))
number2 = int(input('Введите второе целое число: '))
if number1 * number2 <= 1000:
    print(number1 * number2)
else:
    print(number1 + number2)


# lesson 3,exercise 11
"""
Напишите программу для отображения «Hello», если введенное пользователем число кратно пяти,
в противном случае выведите «Bye».
"""
num5 = int(input('Введите число: '))
if num5 % 5 == 0:
    print('Hello')
else:
    print('BYE')


# lesson 3,exercise 12
"""
Написать программу, которая спрашивает у пользователя год и определяет является ли год високосным.
(справка: В соответствии с григорианским календарем, год является високосным, если его номер кратен 4,
но не кратен 100 или кратен 400).
"""
year1 = int(input('Введите год: '))
if year1 % 4 == 0 and ((year1 % 100 != 0) or (year1 % 400 == 0)):
     print(f'{year1} год - високосный.')
else:
     print(f'{year1} год - невисокосный.')


# lesson 3,exercise 13
"""
Шоколадка имеет вид прямоугольника, разделенного на width×length долек.
Шоколадку можно один раз разломить по прямой на две части.
Определите, можно ли таким образом отломить от шоколадки часть,
состоящую ровно из x долек. Программа получает на вход три числа:
width, length, parts и должна вывести YES или NO.
(учтите что пользователь может ввести не правильные параметры, ваша программа не должна вылетать с ошибкой)
"""
width = int(input('Введите ширину: '))
length = int(input('Введите длину: '))
parts = int(input('Введите количество долек: '))
S = width * length
if parts <=0:
    print('Введите корректное количество долек.')
elif S > parts and ((parts % width == 0) or (parts % length  == 0)):
    print('YES')
else:
    print('NO')