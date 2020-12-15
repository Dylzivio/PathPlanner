from megamap import A
import math
import random


def create_zero_matrix(x, y):
    A = [[0] * x for n in range(y)]
    return A


def get_line(x_start, y_start, x_finish, y_finish):
    if (x_finish - x_start) == 0:
        k = (y_finish - y_start) / 1
        b = y_start - (k * x_start)
        return k, b
    k = (y_finish - y_start) / (x_finish - x_start)
    b = y_start - (k * x_start)
    return k, b


def end_of_line(A_map, x_start, y_start, x_finish, y_finish, transon=1):
    k, b = get_line(x_start, y_start, x_finish, y_finish)
    x_stop, y_stop = math.trunc(x_finish), math.trunc(y_finish)
    if abs(x_start - x_finish) < abs(y_finish - y_start):
        for y in range(y_start, y_finish):
            x = (y - b) / k
            if A_map[y][math.trunc(x)] == transon:
                y_stop = y
                x_stop = math.trunc(x)
                return x_stop, y_stop
    if abs(x_start - x_finish) >= abs(y_finish - y_start):
        for x in range(x_start, x_finish):
            y = k * x + b
            if A_map[math.trunc(y)][x] == transon:
                y_stop = math.trunc(y)
                x_stop = x
                return x_stop, y_stop


# неиспользуеемая функция вычета массивов
# def SS_min_RR(x, y, SS, RR):
#     TS = create_zero(x, y)
#     for stroka in range(len(SS)):
#         for number in range(len(SS[stroka])):
#             elemS = SS[stroka][number]
#             elemR = RR[stroka][number]
#             if elemS == 1:
#                 if elemR == 1:
#                     TS[stroka][number] = 0
#                 if elemR == 0:
#                     TS[stroka][number] = 1
#             if elemS == 0:
#                 TS[stroka][number] = 0
#     return TS


def create_filled_contour(x_stop, y_stop, A_map):  # simple deep filter
    x_edge, y_edge = len(A_map[1]), len(A_map)
    OBT = create_zero_matrix(x_edge, y_edge)
    OBT[y_stop][x_stop] = 1
    nums = 1
    k = nums - 1
    while k != nums:
        k = nums
        for stroka in range(len(OBT)):
            for number in range(len(OBT[stroka])):
                if OBT[stroka][number] == 1:

                    if (0 <= stroka < y_edge) and (0 <= number + 1 < x_edge):
                        if A_map[stroka][number + 1] != 0 and OBT[stroka][number + 1] != 1:  # right
                            OBT[stroka][number + 1] = 1
                            nums += 1

                    if (0 <= stroka < y_edge) and (0 <= number - 1 < x_edge):
                        if A_map[stroka][number - 1] != 0 and OBT[stroka][number - 1] != 1:  # left
                            OBT[stroka][number - 1] = 1
                            nums += 1

                    if (0 <= stroka - 1 < y_edge) and (0 <= number < x_edge):
                        if A_map[stroka - 1][number] != 0 and OBT[stroka - 1][number] != 1:  # up
                            OBT[stroka - 1][number] = 1
                            nums += 1

                    if (0 <= stroka + 1 < y_edge) and (0 <= number < x_edge):
                        if A_map[stroka + 1][number] != 0 and OBT[stroka + 1][number] != 1:  # down
                            OBT[stroka + 1][number] = 1
                            nums += 1
    return OBT  # nums could be added as needed


def create_1st_S(MAP1):
    x, y = len(MAP1[1]), len(MAP1)
    MAP2 = create_zero_matrix(x, y)
    for stroka in range(len(MAP1)):
        for number in range(len(MAP1[stroka])):
            elem0 = MAP1[stroka][number]
            if elem0 == 1:
                MAP2[stroka][number] = elem0
                if (0 <= stroka < y) and (0 <= number + 1 < x):  # right
                    MAP2[stroka][number + 1] = 1
                if (0 <= stroka < y) and (0 <= number - 1 < x):  # left
                    MAP2[stroka][number - 1] = 1
                if (0 <= stroka - 1 < y) and (0 <= number < x):  # up
                    MAP2[stroka - 1][number] = 1
                if (0 <= stroka + 1 < y) and (0 <= number < x):  # down
                    MAP2[stroka + 1][number] = 1
    return MAP2


def strait_safety(B, width):
    # B_1 = B
    # for n in range(width//2):
    #     B_1 = create_1st_S(B)
    #
    # B_2
    return


def find_center(B_map):
    sum_x, sum_y = 0, 0
    num = 0
    for stroka in range(len(B_map)):
        for number in range(len(B_map[stroka])):
            if B_map[stroka][number] == 1:
                sum_x = sum_x + number
                sum_y = sum_y + stroka
                num += 1
    x_center = sum_x / num
    y_center = sum_y / num
    return x_center, y_center


def find_rad_obtacle(x_center, y_center, B_map):
    r_max = 0
    for y in range(len(B_map)):
        for x in range(len(B_map[y])):
            if B_map[y][x] == 1:
                R_iteration = math.sqrt((x - x_center) * (x - x_center) + (y - y_center) * (y - y_center))
                if R_iteration > r_max:
                    r_max = math.ceil(R_iteration)
    return r_max


def find_alfa(x_stop, y_stop, x_center, y_center):
    gip = math.sqrt((x_center - x_stop) * (x_center - x_stop) + (y_stop - y_center) * (y_stop - y_center))
    alfa = math.asin((x_center - x_stop) / gip)
    alfa_grad = alfa * 57.3
    alfa_start = 0
    if x_stop <= x_center:
        if alfa_grad >= 0:
            alfa_start = alfa_grad
            return alfa_start
        alfa_start = 180 - alfa_grad
    if x_stop > x_center:
        if alfa_grad >= 0:
            alfa_start = 360 - alfa_grad
            return alfa_start
        alfa_start = 180 + alfa_grad
    return alfa_start


# # dont use now
# def radius_flow(A, yc, xc, r, alfa):
#     rend_x = xc + r * math.sin(math.radians(alfa))
#     rend_y = yc + r * math.cos(math.radians(alfa))
#     x_stop, y_stop = end_of_line(A, xc, yc, rend_x, rend_y, 0)
#     x_stop = math.trunc(x_stop)
#     y_stop = math.trunc(y_stop)
#     return x_stop, y_stop


def check_forward(x, y, DIR, C_map):
    x_check = x + DIR[0]
    y_check = y + DIR[1]
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


def step_forward(x, y, DIR):
    x = x + DIR[0]
    y = y + DIR[1]
    return x, y


def turn_left(DIR, direction):
    if DIR == 'Left':
        DIR = direction.get('Down')
    if DIR == 'Right':
        DIR = direction.get('Up')
    if DIR == 'Up':
        DIR = direction.get('Left')
    if DIR == 'Down':
        DIR = direction.get('Right')
    return DIR


def turn_right(DIR, direction):
    if DIR == 'Left':
        DIR = direction.get('Up')
    if DIR == 'Right':
        DIR = direction.get('Down')
    if DIR == 'Up':
        DIR = direction.get('Right')
    if DIR == 'Down':
        DIR = direction.get('Left')
    return DIR


def distance(x_start, y_start, x_finish, y_finish):
    distance = math.sqrt((x_finish - x_start) * (x_finish - x_start) + (y_finish - y_start) * (y_finish - y_start))
    return distance


#   функция убрана из оборота тк несовершенна для широкого спектра препятствий
#   подходит только для небольших кругов
#   подфункции незакомментированы
# def around_obstacle(B, xf, yf, x_stop, y_stop):  # add safe Radius
#     C = []
#     xc, yc = find_center(B)
#     r = find_rad_obtacle(xc, yc, B)
#     alfa_start = find_alfa(x_stop, y_stop, xc, yc)
#     for alfa in range(alfa_start, 360 + alfa_start, 5):
#         x_new, y_new = radius_flow(A, yc, xc, r, alfa)
#         xf_try, yf_try = end_of_line(A, x_new, y_new, xf, yf)
#         if B[yf_try][xf_try] == 0:
#             C.append(x_new)
#             C.append(y_new)
#     for alfa in range(alfa_start, -360 - alfa_start, -5):
#         x_new, y_new = radius_flow(A, yc, xc, r, alfa)
#         xf_try, yf_try = end_of_line(A, x_new, y_new, xf, yf)
#         if B[yf_try][xf_try] == 0:
#             C.append(x_new)
#             C.append(y_new)
#     return C


def filter_start_pos(x_start, y_start, direction, direction_, B_map):
    if B_map[x_start + direction.get('Up')[0]][y_start + direction.get('Up')[1]] and \
            B_map[x_start + direction.get('Down')[0]][
                y_start + direction.get('Down')[1]] and B_map[x_start + direction.get('Right')[0]][
        y_start + direction.get('Right')[1]] and B_map[
        x_start + direction.get('Left')[0]][y_start + direction.get('Left')[1]]:
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
            if B_map[y_start + direction_.get(i)[0]][y_start + direction_.get(i)[1]] == 1:
                y_start = y_start + direction_.get(i)[0]
                x_start = y_start + direction_.get(i)[1]
                return x_start, y_start
    return x_start, y_start


def go_along_wall(A, x_start, y_start, x_finish, y_finish, side):
    x, y = x_start, y_start
    xff, yff = x_start, y_start
    direction = {'Up': [-1, 0], 'Down': [1, 0], 'Left': [0, -1], 'Right': [0, 1]}
    direction_ = {'ul': [-1, -1], 'ur': [-1, 1], 'dr': [1, 1], 'dl': [1, -1]}
    x, y = filter_start_pos(x, y, direction, direction_, A)
    DIR = direction.get('Left')
    path = 0
    if side == 'LeftHand':
        while distance(x_finish, y_finish, xff, yff) < 2:
            if path >= 7 and Is_coincide(xff, yff, x_start, y_start):
                raise Exception('return2start')
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
            xff, yff = end_of_line(A, x, y, x_finish, y_finish)
        return x, y
    if side == 'RightHand':
        while distance(x, y, xff, yff) < 2:
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
            xff, yff = end_of_line(A, x, y, x_finish, y_finish)
        return x, y
    # дописать остановку или масштабирование при конце фрагмента карты
    # дописать заплатку обхода при наступлении на рамку  !!!!!! done


def go_along_wall_W(A, x_start, y_start, x_finish, y_finish, side):
    x, y = x_start, y_start
    xff, yff = x_start, y_start
    direction = {'Up': [-1, 0], 'Down': [1, 0], 'Left': [0, -1], 'Right': [0, 1]}
    direction_ = {'ul': [-1, -1], 'ur': [-1, 1], 'dr': [1, 1], 'dl': [1, -1]}
    x, y = filter_start_pos(x, y, direction, direction_, A)
    DIR = direction.get('Left')
    path = 0
    _path = 0
    list_of_points = []
    if side == 'LeftHand':
        while distance(x_finish, y_finish, xff, yff) < 2:
            if path >= 7 and Is_coincide(xff, yff, x_start, y_start):
                raise Exception('return2start')
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
            xff, yff = end_of_line(A, x, y, x_finish, y_finish)
            if _path <= path - 3:
                list_of_points.append((x,y))
                _path = path
        return x, y, path, list_of_points
    if side == 'RightHand':
        while distance(x, y, xff, yff) < 2:
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
            xff, yff = end_of_line(A, x, y, x_finish, y_finish)
            if _path <= path - 3:
                list_of_points.append((x,y))
                _path = path
        return path, list_of_points
    # дописать остановку или масштабирование при конце фрагмента карты
    # дописать заплатку обхода при наступлении на рамку  !!!!!! done


def map_sliser_deep_bubble(A_map, deep, bubble):
    B_map = create_zero_matrix(len(A_map[0]), len(A))
    for stroka in range(len(B_map)):
        for number in range(len(B_map[stroka])):
            if A_map[stroka][number] < deep:
                B_map[stroka][number] = 1
    for i in range(bubble):
        B_map = create_1st_S(B_map)
    return B_map


def is_obtacle_touch_frame(C_map, s=1):
    for elem in C_map[0]:
        if elem == s:
            return 1
    for elem in C_map[-1]:
        if elem == s:
            return 1
    for elem in range(1, len(C_map) - 1):
        if C_map[elem][0] == s or C_map[elem][-1] == s:
            return 1
    return 0


def generateName():
    alfawit = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
               'V', 'W', 'X', 'Y', 'Z']
    numbs = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    my_name = random.choice(alfawit)
    for i in range(2):
        my_name += random.choice(alfawit)
    for i in range(3):
        my_name += random.choice(numbs)
    return my_name


def type_of_obtacle(B_map, x_stop, y_stop):
    obt_type = '0'
    C_map = create_filled_contour(x_stop, y_stop, B_map)  # add check outsides in contour
    if is_obtacle_touch_frame(C_map):
        obt_type = "coast"
        return obt_type
    obt_type = "island"
    return obt_type, C_map


def Is_coincide(x_issue, y_issue, x_base, y_base):
    if x_base - 1 <= x_issue <= x_base + 1:
        if y_base - 1 <= y_issue <= y_base + 1:
            return 1
    return 0


def Is_coincideOne(issue, base):
    if base - 1 <= issue <= base + 1:
            return 1
    return 0


def simple_detour_Fractal(B_map, x_start, y_start, x_finish, y_finish):
    xf_fake, yf_fake = -1, -1
    new_node_info = []
    while not Is_coincideOne(xf_fake,x_finish) and not Is_coincideOne(yf_fake, y_finish):
        xf_fake, yf_fake = end_of_line(B_map, x_start, y_start, x_finish, y_finish)
        obt_type, C_map = type_of_obtacle(B_map, x_start, y_start)
        if obt_type == "coast":
            try:
                new_node_info.append(go_along_wall(A, x_start, y_start, x_finish, y_finish, "LeftHand"))
            except:
                new_node_info.append(go_along_wall(A, x_start, y_start, x_finish, y_finish, "RightHand"))
        if obt_type == "island":
            new_node_info.append(go_along_wall(A, x_start, y_start, x_finish, y_finish, "LeftHand"))
            new_node_info.append(go_along_wall(A, x_start, y_start, x_finish, y_finish, "RightHand"))
    return new_node_info


def find_path_length(B_map, x_start, y_start, x_finish, y_finish):
    list_of_points = []
    way = 0
    ex_way= []
    obt_type, C_map = type_of_obtacle(B_map, x_start, y_start)
    if obt_type == "coast":
        try:
            way, list_of_points = go_along_wall_W(C_map, x_start, y_start, x_finish, y_finish, "LeftHand")
        except:
            way, list_of_points = go_along_wall_W(C_map, x_start, y_start, x_finish, y_finish, "RightHand")
    if obt_type == "island":
        ex_way.append(go_along_wall_W(B_map, x_start, y_start, x_finish, y_finish, "LeftHand"))
        ex_way.append(go_along_wall_W(B_map, x_start, y_start, x_finish, y_finish, "RightHand"))
    if ex_way[0][0] > ex_way[1][0]:
        way, list_of_points = ex_way[0][0], ex_way[1][0]
    if ex_way[0][0] < ex_way[1][0]:
        way, list_of_points = ex_way[1][0], ex_way[1][1]
    return way, list_of_points


def path_list_smooth(B_map, list_of_points):
    short_list_of_points = []
    i = 0
    for i in range(len(list_of_points)):
        while e
        for k in range(i,len(list_of_points)):


    return short_list_of_points

def PATH_GLOBAL(A_map, start, finish, deep, bubble):
    B_map = map_sliser_deep_bubble(A_map, deep, bubble)
    dep_tree = {}  # start node dict depend
    not_used_yet = [start]
    nodeName = generateName()

    # block node creation and set dependence tree
    while len(not_used_yet) != 0:
        loadNode = not_used_yet[0]
        node_info = {}
        x_start, y_start = loadNode[0], loadNode[1]
        node_info['coordinates'] = loadNode
        childName = 'child1'
        node_request = simple_detour_Fractal(B_map, x_start, y_start, finish[0], finish[1])
        for node in node_request:
            nextNodeName = generateName()
            for checkNode in dep_tree.keys():
                if Is_coincide(node[0], node[1], dep_tree.get(checkNode).get('coordinates')[0],
                               dep_tree.get(checkNode).get('coordinates')[1]):
                    for parent_node in dep_tree.keys():
                        if parent_node['child1'] == loadNode:
                            dep_tree[parent_node['child1']] = (node[0], node[1])
                        elif parent_node['child2'] == loadNode:
                            dep_tree[parent_node['child2']] = (node[0], node[1])
                    continue
            not_used_yet.append(node)
            node_info['coordinates'] = (node[0], node[1])  # coordX and coordY
            node_info[childName] = node
            dep_tree[nextNodeName] = node_info
            childName = 'child2'

    #  block  dependence tree correction and add weight
    for parent_node in dep_tree.keys():
        for childNode in dep_tree.get(parent_node).keys():
            if childNode != 'coordinates':
                pathLength, list_of_points = find_path_length(B_map,dep_tree.get(parent_node).get('coordinates')[0],
                                              dep_tree.get(parent_node).get('coordinates')[0],
                                              dep_tree.get(parent_node).get(childNode)[0],
                                              dep_tree.get(parent_node).get(childNode)[1])
                dep_tree[parent_node[childNode][2]] = pathLength
                dep_tree[parent_node[childNode][3]] = list_of_points

    # block graf creation from dependence tree
    for NodeName in dep_tree.keys():
        NodeName = Node("F")  # NAME add
    w_graph = Graph.create_from_nodes([dep_tree.keys()])
    for parent_node in dep_tree.keys():
        for childNode in dep_tree.get(parent_node).keys():
            if childNode != 'coordinates':
                weight = dep_tree.get(parent_node).get(childNode)[2]  # 0-x 1-y 2-weight 3-list
                graph.connect(parent_node, childNode, weight)

                #   block of calculate our way by A*
    print([(weight, [n.data for n in node]) for (weight, node) in w_graph.dijkstra(a)])
