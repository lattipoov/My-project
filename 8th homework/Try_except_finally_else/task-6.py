"""
Дописать код (нельзя использовать просто except)
"""
my_dict ={"key1":"value1","key2":"value2","key3":"value3"}

search_key = "non-existent key"
try:
   print(my_dict[search_key])
except KeyError:
    print(f'Сорян, {search_key} не правильный ключ ')
