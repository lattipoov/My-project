"""
Есть список: list1 = [1, ‘a’, 3, ‘b’, 5, ‘6’, 7, ‘8’, 9, ‘c’],
необходимо разделить на два списка, в первом только цифровые значения, а во втором только строки
"""
list1 = [1, 'a', 3, 'b', 5, '6', 7, '8', 9, 'c']
int_list = []
str_list = []
for i in list1:
    try:
        i / 1
        int_list.append(i)
    except:
        str_list.append(i)

print(int_list)
print(str_list)