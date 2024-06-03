def circle_perimeter(*args):
    default_radius = 5
    pi = 3.14
    try:
        print(f'Длина окружности равна: {2 * pi * int(args[0])}')
    except:
        print(f'Длина окружности равна: {2 * pi * default_radius}')



def circle_area(*args):
    default_radius = 5
    pi = 3.14
    try:
        print(f'Площадь окружности равна: {pi * int(args[0])**2}')
    except:
        print(f'Площадь окружности равна: {pi * default_radius**2}')