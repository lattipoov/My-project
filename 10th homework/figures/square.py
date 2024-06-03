def square_perimeter(*args):
    a = 15
    try:
        print(f'Периметр квадрата: {4 * int(args[0])}')
    except:
        print(f'Периметр квадрата: {4 * a}')


def square_area(*args):
    a = 15
    try:
        print(f'Площадь квадрат: {int(args[0])**2}')
    except:
        print(f'Площадь квадрат: {a**2}')