"""
) Замените первый if на try/except/else
"""
import sys


try:
   city = sys.argv[1]
   city = city.lower()
except IndexError:
    print("Вы не указали название города")
    print("Try again")
else:
    if city == "tashkent"[0:len(city)]:
        print("В Ташкенте тепло и солнечно")
    elif city == "london"[0:len(city)]:
        print("В Лондоне пасмурно и сыро")
    elif city == "moskow"[0:len(city)]:
        print("В Москве идёт сильный дождь")
    elif city == "paris"[0:len(city)]:
        print("погода для романтики")
    elif city == "rio de janeyro"[0:len(city)]:
        print("В Рио постоянно карнавалы")

    else:
        print("прогноз не ясен, карантин")
