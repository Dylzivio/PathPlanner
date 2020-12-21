from lineOps import get_distance, Is_coincide, line_Endpoint


def check_forward(x, y, DIR, direction, C_map):
    y_check = y + direction.get(DIR)[0]
    x_check = x + direction.get(DIR)[1]
    barier = C_map[y_check][x_check]
    return barier


def check_left(x, y, DIR, direction, C_map):
    barier = 0
    if DIR == 'Left':
        barier = C_map[y + direction.get('Down')[0]][x + direction.get('Down')[1]]
    if DIR == 'Right':
        barier = C_map[y + direction.get('Up')[0]][x + direction.get('Up')[1]]
    if DIR == 'Up':
        barier = C_map[y + direction.get('Left')[0]][x + direction.get('Left')[1]]
    if DIR == 'Down':
        barier = C_map[y + direction.get('Right')[0]][x + direction.get('Right')[1]]
    return barier


def check_back_left(x, y, DIR, direction_, C_map):
    barier = 0
    if DIR == 'Left':
        barier = C_map[y + direction_.get('dr')[0]][x + direction_.get('dr')[1]]
    if DIR == 'Right':
        barier = C_map[y + direction_.get('ul')[0]][x + direction_.get('ul')[1]]
    if DIR == 'Up':
        barier = C_map[y + direction_.get('dl')[0]][x + direction_.get('dl')[1]]
    if DIR == 'Down':
        barier = C_map[y + direction_.get('ur')[0]][x + direction_.get('ur')[1]]
    return barier


def check_right(x, y, DIR, direction, C_map):
    barier = 0
    if DIR == 'Left':
        barier = C_map[y + direction.get('Up')[0]][x + direction.get('Up')[1]]
    if DIR == 'Right':
        barier = C_map[y + direction.get('Down')[0]][x + direction.get('Down')[1]]
    if DIR == 'Up':
        barier = C_map[y + direction.get('Right')[0]][x + direction.get('Right')[1]]
    if DIR == 'Down':
        barier = C_map[y + direction.get('Left')[0]][x + direction.get('Left')[1]]
    return barier


def check_back_right(x, y, DIR, direction_, C_map):
    barier = 0
    if DIR == 'Left':
        barier = C_map[y + direction_.get('ur')[0]][x + direction_.get('ur')[1]]
    if DIR == 'Right':
        barier = C_map[y + direction_.get('dl')[0]][x + direction_.get('dl')[1]]
    if DIR == 'Up':
        barier = C_map[y + direction_.get('dr')[0]][x + direction_.get('dr')[1]]
    if DIR == 'Down':
        barier = C_map[y + direction_.get('ul')[0]][x + direction_.get('ul')[1]]
    return barier


def step_forward(x, y, direction, DIR):
    y = y + direction.get(DIR)[0]
    x = x + direction.get(DIR)[1]
    return x, y


def turn_left(DIR, direction):
    if DIR == 'Left':
        DIR = 'Down'
        return DIR
    if DIR == 'Right':
        DIR = 'Up'
        return DIR
    if DIR == 'Up':
        DIR = 'Left'
        return DIR
    if DIR == 'Down':
        DIR = 'Right'
        return DIR


def turn_right(DIR, direction):
    if DIR == 'Left':
        DIR = 'Up'
        return DIR
    if DIR == 'Right':
        DIR = 'Down'
        return DIR
    if DIR == 'Up':
        DIR = 'Right'
        return DIR
    if DIR == 'Down':
        DIR = 'Left'
        return DIR


def filter_start_pos(x_start, y_start, direction, direction_, B_map):
    # return valid start position for L-R-Hand detour
    if B_map[x_start + direction.get('Up')[0]][y_start + direction.get('Up')[1]] and \
            B_map[x_start + direction.get('Down')[0]][
                y_start + direction.get('Down')[1]] and B_map[x_start + direction.get('Right')[0]][
                y_start + direction.get('Right')[1]] and B_map[
                x_start + direction.get('Left')[0]][y_start + direction.get('Left')[1]]:
        # print(B_map[x_start + direction.get('Up')[0]][y_start + direction.get('Up')[1]])
        # print(B_map[x_start + direction.get('Down')[0]][y_start + direction.get('Down')[1]])
        # print(B_map[x_start + direction.get('Left')[0]][y_start + direction.get('Left')[1]])
        # print(B_map[x_start + direction.get('Right')[0]][y_start + direction.get('Right')[1]])
        for i in direction_.keys():
            if B_map[y_start + direction_.get(i)[0]][y_start + direction_.get(i)[1]] == 0:
                y_start = y_start + direction_.get(i)[0]
                x_start = y_start + direction_.get(i)[1]
                return x_start, y_start
    if not B_map[x_start + direction.get('Up')[0]][y_start + direction.get('Up')[1]] and not \
            B_map[x_start + direction.get('Down')[0]][
                y_start + direction.get('Down')[1]] and not B_map[x_start + direction.get('Right')[0]][
        y_start + direction.get('Right')[1]] and not B_map[
        x_start + direction.get('Left')[0]][y_start + direction.get('Left')[1]]:
        for i in direction_.keys():
            if B_map[y_start + direction_.get(i)[0]][y_start + direction_.get(i)[1]] == 0:
                y_start = y_start + direction_.get(i)[0]
                x_start = y_start + direction_.get(i)[1]
                return x_start, y_start
    return x_start, y_start


def go_along_wall(A, x_start, y_start, x_finish, y_finish, side):
    print('                       ..')
    for i in A:
        print(i)
    # go along the wall by 1-cell steps by L-F-hand rules
    x, y = x_start, y_start
    xff, yff = x_start, y_start
    direction = {'Up': [-1, 0], 'Down': [1, 0], 'Left': [0, -1], 'Right': [0, 1]}
    direction_ = {'ul': [-1, -1], 'ur': [-1, 1], 'dr': [1, 1], 'dl': [1, -1]}
    x, y = filter_start_pos(x, y, direction, direction_, A)
    # set start counter and dirrection meaning
    # DIR = direction.get('Left')
    DIR = 'Right'
    path = 0
    if side == 'LeftHand':
        # standart Left-Hand-Algorithm
        while get_distance(x_finish, y_finish, xff, yff) >= 2:
            if path >= 10 and Is_coincide(xff, yff, x_start, y_start):
                # if we chose cost-side and return to start position
                raise Exception('return2start')
            if check_forward(x, y, DIR, direction, A) == 1 and check_left(x, y, DIR, direction, A) == 1:
                DIR = turn_right(DIR, direction)
            if check_left(x, y, DIR, direction, A) == 0:
                if check_back_left(x, y, DIR, direction_, A) == 1:
                    DIR = turn_left(DIR, direction)
                    x, y = step_forward(x, y, direction, DIR)
                    path += 1
                    continue
                DIR = turn_left(DIR, direction)
            if check_forward(x, y, DIR,direction, A) == 0 and check_left(x, y, DIR, direction, A) == 1:
                x, y = step_forward(x, y, direction, DIR)
                path += 1
            print(A, x, y, x_finish, y_finish)
            xff, yff = line_Endpoint(A, x, y, x_finish, y_finish)
            print('start: ',x_start, y_start)
            print('finish: ',x_finish, y_finish)
            print('fake: ',xff, yff)
            print('dist: ', get_distance(x_finish, y_finish, xff, yff))
            print('now: ',x,y )
        return x, y
    if side == 'RightHand':
        # standart Right-Hand-Algorithm
        while get_distance(x_finish, y_finish, xff, yff) >= 2:
            if path >= 10 and Is_coincide(xff, yff, x_start, y_start):
                raise Exception('return2start')
            if check_forward(x, y, DIR, direction, A) == 1 and check_right(x, y, DIR, direction, A) == 1:
                DIR = turn_left(DIR, direction)
            if check_right(x, y, DIR, direction, A) == 0:
                if check_back_right(x, y, DIR, direction_, A) == 1:
                    DIR = turn_right(DIR, direction)
                    x, y = step_forward(x, y, direction, DIR)
                    path += 1
                    continue
                DIR = turn_right(DIR, direction)
            if check_forward(x, y, DIR, direction, A) == 0 and check_right(x, y, DIR, direction, A) == 1:
                x, y = step_forward(x, y, direction, DIR)
                path += 1

            print(A, x, y, x_finish, y_finish)
            xff, yff = line_Endpoint(A, x, y, x_finish, y_finish)
        return x, y


def go_along_wall_W(A, x_start, y_start, x_finish, y_finish, side):
    x, y = x_start, y_start
    xff, yff = x_start, y_start
    direction = {'Up': [-1, 0], 'Down': [1, 0], 'Left': [0, -1], 'Right': [0, 1]}
    direction_ = {'ul': [-1, -1], 'ur': [-1, 1], 'dr': [1, 1], 'dl': [1, -1]}
    x, y = filter_start_pos(x, y, direction, direction_, A)
    # set start counter and dirrection meaning
    DIR = direction.get('Left')
    path = 0
    _path = 0
    list_of_points = []
    if side == 'LeftHand':
        while get_distance(x_finish, y_finish, xff, yff) < 2:
            if path >= 7 and Is_coincide(xff, yff, x_start, y_start):
                # if we chose cost-side and return to start position
                raise Exception('return2start')
            # standart Left-Hand-Algorithm
            if check_forward(x, y, DIR, A) == 1 and check_left(x, y, DIR, direction, A) == 1:
                turn_right(DIR, direction)
            if check_left(x, y, DIR, direction, A) == 0:
                if check_back_left(x, y, DIR, direction_, A) == 1:
                    turn_left(DIR, direction)
                    x, y = step_forward(x, y, DIR)
                    path += 1
                    continue
                turn_left(DIR, direction)
            if check_forward(x, y, DIR, A) == 0 and check_left(x, y, DIR, direction, A) == 1:
                x, y = step_forward(x, y, DIR)
                path += 1
            xff, yff = line_Endpoint(A, x, y, x_finish, y_finish)
        # writing point of path ewery 3 steps and refresh  counter
            if _path <= path - 3:
                list_of_points.append((x, y))
                _path = path
        return x, y, path, list_of_points
    if side == 'RightHand':
        # standart Right-Hand-Algorithm
        while get_distance(x, y, xff, yff) < 2:
            if path >= 7 and Is_coincide(xff, yff, x_start, y_start):
                raise Exception('return2start')
            if check_forward(x, y, DIR, A) == 1 and check_right(x, y, DIR, direction, A) == 1:
                turn_left(DIR, direction)
            if check_right(x, y, DIR, direction, A) == 0:
                if check_back_right(x, y, DIR, direction_, A) == 1:
                    turn_right(DIR, direction)
                    x, y = step_forward(x, y, DIR)
                    path += 1
                    continue
                turn_right(DIR, direction)
            if check_forward(x, y, DIR, A) == 0 and check_right(x, y, DIR, direction, A) == 1:
                x, y = step_forward(x, y, DIR)
                path += 1
            xff, yff = line_Endpoint(A, x, y, x_finish, y_finish)
        # writing point of path ewery 3 steps and refresh  counter
            if _path <= path - 3:
                list_of_points.append((x, y))
                _path = path
        return path, list_of_points