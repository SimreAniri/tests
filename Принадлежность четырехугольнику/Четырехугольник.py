x = []
y = []


def vector(x1, y1, x2, y2):
    return [x2 - x1, y2 - y1]


def polygon(i, X, Y):

    if i == 0:
        return 1

    a = vector(x[0-i], y[0-i], x[1-i], y[1-i])
    b = vector(x[0-i], y[0-i], X, Y)

    if (b[0]*a[1] - b[1]*a[0]) > 0:
        return polygon(i-1, X, Y)

    elif (b[0]*a[1] - b[1]*a[0]) < 0:
        return -1

    elif (b[0] * a[1] - b[1] * a[0]) == 0:
        if polygon(i-1, X, Y):
            return 0
        else:
            return -1


with open('Четырехугольник_test.txt') as file:
    for line in file:
        x_i, y_i = map(float, line.split())
        x.append(x_i)
        y.append(y_i)

print(x ,y)


while input('Продолжаем? [Y/N]') == 'Y':

    test = 1

    X, Y = map(float, input('Введите координату: ').split())

    for i in range(4):
        if x[i] == X and y[i] == Y:
            print('точка - вершина четырехугольника')
            test = 0

    if test:

        if polygon(len(x), X, Y) == 1:
            print('точка внутри четырехугольника')

        elif polygon(len(x), X, Y) == -1:
            print('точка снаружи четырехугольника')

        elif polygon(len(x), X, Y) == 0:
            print('точка лежит на сторонах четырехугольника')
