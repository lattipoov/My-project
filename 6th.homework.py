#Rustam Latipov
# lesson 6,exersise 1
"""
Выведите в отдельный список числа, которые меньше или равны 5 и числа, которые больше 5.
"""

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list1 = [i for i in a if i <= 5]
list2 = [i for i in a if i > 5]
print(f'Список чисел меньше или равных 5: {list1}.')
print(f'Список чисел больше 5: {list2}.')


# lesson 6,exersise 2
"""
Вы принимаете от пользователя его имя, фамилию, возраст. Сохраните их в соответствующие переменные.
Сохраните полученные значения в список.
"""
name = input('Введите имя: ')
surname = input('Введите фамилию: ')
age = input('Введите возраст: ')
list = [name, surname, age]
print(f'Список данных пользователя: (list).')


# lesson 6,exersise 3
"""
Напишите программу, которая принимает от пользователя секвенцию чисел,
разделенных запятой и пробелом. После чего запишите каждое число в список.
"""
nums= input('Введите секвенцию чисел, разделенных запятой и пробелом: ')
string1 = nums.split(', ')
print(string1)


# lesson 6,exersise 4
"""
Напишите программу, которая принимает пример со СЛОЖЕНИЕМ у пользователя и затем выдает результат.
(решите с помощью генератора списка)
"""
nums = input('Введите пример со сложением: ')
list1 = nums.split(' + ')
nums_for_sum = [int(i) for i in list1]
print(sum(nums_for_sum))


# lesson 6,exersise 5
"""
Напишите программу, которая будет принимать три имени в качестве входных данных от
пользователя в одном input() вызове функции.
"""
names = input('Введите три имени разделенных между собой пробелом: ')
names_list = names.split(' ')
print(f'Первое имя: {names_list[0]}')
print(f'Второе имя: {names_list[1]}')
print(f'Третье имя: {names_list[2]}')


# lesson 6,exersise 6
"""
Дан список чисел numbers = [1, 2, 3, 4, 5, 6, 7]. напишите программу, которая превращает 
каждый элемент списка в его квадрат.
"""
numbers = [1, 2, 3, 4, 5, 6, 7]
nums2 = [i ** 2 for i in numbers]
print(f'Список чисел: {numbers}\nСписок квадратов: {nums2}')


# lesson 6,exersise 7
"""
 Создайте список из любимых вами блюд.

Создайте список из любимых блюд вашего друга, скопировав свой список.
Убедитесь что два списка разные, добавив по одному разному блюду в каждый список.
Выведите два списка.
"""
my_fav_food = ['Сомса', 'Лагман', 'Плов']
friends_fav_food = my_fav_food.copy()
my_fav_food.append('Шашлык')
friends_fav_food.append('Суши')
print(f'Список моих блюд: {my_fav_food}.')
print(f'Список блюд друга:{friends_fav_food}.')


# lesson 6,exersise 8
"""
Создайте переменную user_num, которая будет принимать от пользователя число.
Создайте числовой список от 1 до значения из переменной user_num (значение из переменной включительно).
Выведите сам список и сумму его чисел.
"""
user_num = int(input('Введите число: '))
list1 = [int(i) for i in range (1, user_num+1)]
print(f'Список чисел в диапозоне от 1 до {user_num}: {list1}.')
print(f'Сумма списка чисел равна: {sum(list1)}')


# lesson 6,exersise 9
"""
Создайте два числовых списка от 1 до 100. Первый будет состоять только из четных чисел,
а второй из нечётных. Выведите сам список и сумму его чисел.
"""
list1 = [i for i in range(2, 101, 2)]
print(f'Список четных чисел: {list1}\nСумма четных чисел: {sum(list1)}')
list2 = [i for i in range(1, 101, 2)]
print(f'Список нечетных чисел: {list2}\nСумма нечетных чисел: {sum(list2)}')


# lesson 6,exersise 10
"""
 Напишите программу, которая выводит все четные числа из списка в исходном порядке, и останавливается когда число равно 815.
"""
numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958,743, 527]
list1 = []
for i in numbers:
    if i == 815:
        break
    elif i % 2 == 0:
        list1.append(i)
    print(list1)



# lesson 6,exersise 11
"""
Подсчитайте общее количество цифр в числе.

Например, число 75869 , поэтому на выходе должно быть 5 .
"""
num = input('Введите число: ')
list_num = '-'.join(num)
list_num1 = list_num.split('-')
print(f'Кол-во цифр в числе {num}: {len(list_num1)}')


# lesson 6,exersise 12
"""
Напишите программу для отображения всех простых чисел в диапазоне 
(Учтите что пользователь может ввести отрицательное число)
"""
start = int(input('Введите положительный стартовый номер: '))
finish = int(input('Введите положительный конечный номер: '))
for num in range(start, finish+1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)



# lesson 6,exersise 13
"""
Обработать строку ospf_route и вывести информацию на стандартный поток вывода как на картинке ниже:
"""
ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
parts = ospf_route.split()
protocol = parts[0]
if protocol == '0':
    protocol = 'OSPF'
subnet = parts[1]
ad_metric = parts[2]
next_hop = parts[4][:-1]
last_update = parts[5].rstrip(',')
interface = parts[6]

print(f"protocol:{protocol}")
print(f"subnet: {subnet}")
print(f"AD/Metric: {ad_metric}")
print(f"next-hop: {next_hop}")
print(f"last update {last_update}")
print(f"interface {interface}")



# lesson 6,exersise 14
"""
Получите список VLANов со строки:
"""
config = 'switchport trunk allowed vlan 1,3,10,20,30,100'
list1 = config.split()
vlan = list1.pop()
vlan = vlan.split(',')
print(vlan)