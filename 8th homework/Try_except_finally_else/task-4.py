"""
Приведенный ниже код назначает 5-ю букву каждого слова в food новый список fifth.
Однако код в настоящее время выдает ошибки. Вставьте предложение
try/except, которое позволит запустить код и создать список 5-й буквы в каждом слове.
Если слово недостаточно длинное, оно не должно ничего выводить. Примечание.
pass — Оператор является нулевой операцией; ничего не произойдет при его выполнении.
"""
food = ["chocolate", "chicken", "corn", "sandwich", "soup", "potatoes", "beef", "lox", "lemonade"]
fifth = []
for x in food:
    try:
        fifth.append(x[4])
    except IndexError:
        pass

print(fifth)