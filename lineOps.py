import math


def get_line_koef(x_start, y_start, x_finish, y_finish):
    # line on plane: Y=K*X+B
    # return K, B  koefficients of line
    if (x_finish - x_start) == 0:
        k = (y_finish - y_start) / 1
        b = y_start - (k * x_start)
        return k, b
    k = (y_finish - y_start) / (x_finish - x_start)
    b = y_start - (k * x_start)
    return k, b


def line_Endpoint(B_map, x_start, y_start, x_finish, y_finish, obtType=1):
    k, b = get_line_koef(x_start, y_start, x_finish, y_finish)
    # obtType == 1 for "1" mask-obstacle on '0' map
    # obtType == 0 for "0" mask-obstacle on '1' map
    # return first point on line which touch the obtacle
    # for vertical line
    print('line;  ', k, b)
    if abs(x_start - x_finish) < abs(y_finish - y_start):
        for y in range(y_start, y_finish):
            # print(y_start, y_finish)
            x = (y - b) / k
            if B_map[y][math.trunc(x)] == obtType:
                y_stop = y
                x_stop = math.trunc(x)
                return x_stop, y_stop
    # for horizontal line
    if abs(x_start - x_finish) >= abs(y_finish - y_start):
        for x in range(x_start, x_finish):
            y = k * x + b
            elem = B_map[math.trunc(y)][x]
            if B_map[math.trunc(y)][x] == obtType:
                y_stop = math.trunc(y)
                x_stop = x
                return x_stop, y_stop


def get_distance(x_start, y_start, x_finish, y_finish):
    #find distance between points
    distance = math.sqrt((x_finish - x_start) * (x_finish - x_start) + (y_finish - y_start) * (y_finish - y_start))
    return distance


def Is_coincide(x_issue, y_issue, x_base, y_base):
    # check inaccuracy 2 points on plane
    if x_base - 1 <= x_issue <= x_base + 1:
        if y_base - 1 <= y_issue <= y_base + 1:
            return 1
    return 0


def Is_coincideOne(issue, base):
    # check inaccuracy 2 points on line
    if base - 1 <= issue <= base + 1:
        return 1
    return 0