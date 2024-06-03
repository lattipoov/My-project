"""
Есть список list1 = [i for i in range(100)],
создайте новый список с пробросом каждого пятого элемента (используйте continue)
"""

list1 = [i for i in range(100)]
list2 = []
cnt = 0
for i in list1:
    cnt += 1
    if cnt == 5:
        cnt = 0
        continue
    else:
        list2.append(i)

print(list1)
print(list2)
