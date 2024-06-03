"""
Ловить ошибки это конечно здорово, но уметь логировать их и записывать в файл еще лучше,
задача разобраться со стандартной библиотекой logging
"""
import logging # Загрузка библиотеки
FORMAT = '%(asctime)s ERROR: %(message)s'
logging.basicConfig(filename='my_error.log') # Файл появится в том каталоге где запущен скрипт
logger = logging

try:
    1 / 0
except ZeroDivisionError as error:
    logger.error(error)