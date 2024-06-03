"""
Есть список: list1 = [‘micros’, ‘python’, ‘linux’, ‘windows’, ‘bobo’],
из него составить новый список, но без буквы ‘i’,
результат: list2 = [‘mcros’, ‘python’, ‘lnux’, ‘wndows’, ‘bobo’] (используйте pass)
"""
list1 = ['micros', 'python', 'linux', 'windows', 'bobo']
list2 = []
new_word = ''
for i in list1:
    for j in i:
        if j == 'i':
            pass
        else:
            new_word = new_word + j
    else:
        list2.append(new_word)
        new_word = ''
print(list2)
