"""
Приведенный ниже код делит значения элемента на самого себя, но вылетает с ошибками,
необходимо учесть все типы ошибок и дописать код (условия цикла менять нельзя,
использовать полный синтаксис try/except/else)
"""
my_list = [2, "C", 10, "20", "micros", 50, 0, '0', '30']
for index in range(len(my_list)+5):
    try:
        print(f"{my_list[index]} / {my_list[index]} = {my_list[index] / my_list[index]}")
    except TypeError:
        print(f"Ошибка TypeError: '{my_list[index]}' так как тип элемента {type(my_list[index])}")
        try:
            print(f"{my_list[index]} / {my_list[index]} = {int(my_list[index]) / int(my_list[index])}")
    except ZeroDivisionError:
        print("На ноль делить нельзя")
    except ValueError:
        pass
    else:
        print(f"Но я сконвертировал значение {my_list[index]} в число, и результат уже распечатал")

    except ZeroDivisionError:
        print("На ноль делить нельзя")
    except IndexError:
        print(f"Список оказался слишком мал,индекс под номером {index} не существует")
    else:
        print(f"Все получилось с первой попытки,так как элемент {my_list[index]} является числом")
