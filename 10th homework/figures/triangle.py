def triangle_perimeter(*args):
    a = 7
    b = 2
    c = 8
    try:
        print(f'Периметр треугольника: {int(args[0]) + int(args[1]) + int(args[2])}')
    except:
        print(f'Периметр треугольника: {a + b + c}')

def triangle_area(*args):
    a = 7
    b = 2
    c = 8
    p2 = (a + b + c)/2
    try:
        p = (int(args[0]) + int(args[1]) + int(args[2])) / 2
        print(p)
        print(f'Площадь треугольника: {(p*(p - int(args[0]))*(p - int(args[1]))*(p - int(args[2])))**0.5}')
    except:
        print(f'Площадь треугольника: {(p2*(p2-a)*(p2-b)*(p2-c))}')


triangle_area(13, 14, 15)