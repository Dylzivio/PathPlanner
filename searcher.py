import math


def create_zero(x, y):
    A = [[0] * x for n in range(y)]
    return A


def where_unknown(A, B, error):
    F = create_zero(len(A[1]), len(A))
    for y in range(len(A)):
        for x in range(len(A[y])):
            if A[y][x] == B[0]:
                for alfa in range(0, 360, 45):
                    deep, x_now, y_now = trans_sys(A, y, x, 1, alfa)
                    if B[1] <= (deep + error) and (B[1] >= deep - error):
                        y_now, x_now = contine_side(A, B, y, x, alfa, error)
                        if y_now != 0 and x_now != 0:
                            F[to_int(y_now)][to_int(x_now)] = 1
    return F


def where_your_know(A, B, alfa, error):
    F = create_zero(len(A[1]), len(A))
    for y in range(len(A)):
        for x in range(len(A[y])):
            if A[y][x] == B[0]:
                deep, x_now, y_now = trans_sys(A, y, x, 1, alfa)
                if B[1] <= (deep + error) and (B[1] >= deep - error):
                    y_now, x_now = contine_side(A, B, y, x, alfa, error)
                    if y_now != 0 and x_now != 0:
                        F[to_int(y_now)][to_int(x_now)] = 1
    return F


def contine_side(A, B, y, x, alfa, error):
    x_now = x
    y_now = y
    for i in range(2, len(B)):
        deep, x_now, y_now = trans_sys(A, y, x, i, alfa)
        if B[i] <= (deep + error) and (B[i] >= deep - error):
            continue
        if B[i] > (deep + error) or (B[i] < deep - error):
            return 0, 0
        #####
        # для создания памяти направления для сложной навигации сюда придется записывать угол
    return (y_now, x_now)


def expand_matrix(A):
    B = create_zero(len(A) * 2, len(A[0]) * 2)      #### changes from biomGenerator
    ######  nodes
    for y in range(len(A)):
        for x in range(len(A[y])):
            B[y * 2][x * 2] = A[y][x]
    ####  1st stroka
    for y in range(0, len(B), 2):
        for x in range(1, len(B[y]) - 1, 2):
            B[y][x] = ((B[y][x - 1] + B[y][x + 1]) / 2)
    #####  1st stolbik
    for y in range(1, len(B) - 1, 2):
        for x in range(0, len(B[y]), 2):
            B[y][x] = ((B[y - 1][x] + B[y + 1][x]) / 2)
    ####3 center
    for y in range(1, len(B) - 1, 2):
        for x in range(1, len(B[y]) - 1, 2):
            B[y][x] = (((B[y][x - 1] + B[y][x + 1]) / 2) + ((B[y - 1][x] + B[y + 1][x]) / 2)) / 2
    return B


def trans_sys(A, y, x, i, alfa):
    add_pos_x = i * math.sin(math.radians(alfa))
    add_pos_y = i * math.cos(math.radians(alfa))
    x_real = x + add_pos_x
    y_real = y + add_pos_y
    x_min = math.floor(x_real)
    x_max = math.ceil(x_real)
    y_min = math.floor(y_real)
    y_max = math.ceil(y_real)
    about_x = x_real - x_min
    about_y = y_real - y_min
    delta_deep_xU = A[y_min][x_max] - A[y_min][x_min]
    delta_deep_xD = A[y_max][x_max] - A[y_max][x_min]
    deep_xU = A[y_min][x_min] + delta_deep_xU * about_x
    deep_xD = A[y_max][x_min] + delta_deep_xD * about_x
    delta_deep_yC = deep_xD - deep_xU
    deep = deep_xU + delta_deep_yC * about_y
    return deep, x_real, y_real


def to_int(z):
    if (z - math.floor(z)) < (math.ceil(z) - z):
        z = math.floor(z)
    else:
        z = math.ceil(z)
    return z