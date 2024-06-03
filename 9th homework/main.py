#Latipov Rustam
#exersise 1
"""
Откройте файл mbox-short.txt, “прочитайте” каждую строку в этом файле и найдите строки,
соответствующие данной: “From Stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008”.
Затем распечатайте все ВХОДЯЩИЕ email адреса и их общее количество.
Для решения данной задачи используйте методы строк. (используйте with open)
"""

with open('txt/mbox-short.txt', mode='r', encoding='UTF-8') as file:
    cnt = 0
    for line in file:
        if line.startswith('From '):
            print(line.split()[1])
            cnt += 1
    print(f'Кол-во входящих писем: {cnt}')



#exersise 2
"""
Откройте файл romeo.txt. “Прочитайте” в нем каждую строку.
Получите отдельные слова из каждой строки, после чего составьте список слов.
В списке слова не должны дублироваться. После чего распечатайте список,
в котором все слова будут отсортированы в алфавитном порядке. (используйте open)
"""
file = open('txt/romeo.txt', encoding='UTF-8')
context = file.read()
file.close()
context = sorted(list(set(context.split())))
print(context)



#exersise 3
"""
апишите код программы, которая будет открывать файл «article.txt»
и выводить на печать построчно последние строки в количестве lines
(число которую можно запросить у пользователя). 
Число должно быть положительным (используйте with open)
"""
number = int(input("Сколько последних строк распечатать: "))
if number < 0: print("Укажите положительное число")

with open('txt/article.txt', encoding='UTF-8') as f1:
    vline = f1.readlines()
    result = len(vline)
    cnt = result - number
    npp = 0
    for i in vline:
        npp += 1
        if npp > cnt:
            print(i.strip())



#exersise 4
"""
Требуется реализовать код программы, которая выводит слово, имеющее максимальную длину
(или список слов, если таковых несколько).
"""
file = open('txt/article.txt', encoding='UTF=8')
context = file.read()
list1 = context.split()
list2 = [len(i) for  i in list1]
list3 = []
for j in list1:
    if len(j) == max(list2):
        list3.append(j)

print(list3)



#exersise 5
"""
Объедините содержимое файлов pushkin.txt, byron.txt, romeo.txt в один файл Poems.txt. 
(используйте with open и просто open)
"""
with open('txt/pushkin.txt', encoding='UTF-8') as file:
    vline = file.readlines()
    list1 = []
    for line in vline:
        list1.append(line.strip())

    new_file = open('Poems.txt', mode='w', encoding='UTF-8')
    new_file.write("\n\t--------pushkin.txt---------\n")
    cnt = 0
    for line1 in list1[::-1]:
        if cnt == len(line1) // 2:
            new_file.write(f"{list1[cnt]:50}\t  =>  \t{line1}\n")
        else:
            new_file.write(f"{list1[cnt]:50}\t      \t{line1}\n")
        cnt += 1

    new_file.close()




with open('txt/byron.txt', encoding='UTF-8') as file:
    vline = file.readlines()
    list1 = []
    for line in vline:
        list1.append(line.strip())

    new_file = open('Poems.txt', mode='a', encoding='UTF-8')
    new_file.write("\n\t--------byron.txt---------\n")
    cnt = 0
    for line1 in list1[::-1]:
        if cnt == len(line1) // 2:
            new_file.write(f"{list1[cnt]:50}\t  =>  \t{line1}\n")
        else:
            new_file.write(f"{list1[cnt]:50}\t      \t{line1}\n")
        cnt += 1

    new_file.close()



with open('txt/romeo.txt', encoding='UTF-8') as file:
    vline = file.readlines()
    list1 = []
    for line in vline:
        list1.append(line.strip())

    new_file = open('Poems.txt', mode='z', encoding='UTF-8')
    new_file.write("\n\t--------romeo.txt---------\n")
    cnt = 0
    for line1 in list1[::-1]:
        if cnt == len(line1) // 2:
            new_file.write(f"{list1[cnt]:50}\t  =>  \t{line1}\n")
        else:
            new_file.write(f"{list1[cnt]:50}\t      \t{line1}\n")
        cnt += 1

    new_file.close()