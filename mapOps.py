from My_test_map import testmap


def create_zero_matrix(width, heigth, element = 0):
    # just matrix filled by 0
    NullMap = [[element] * width for n in range(heigth)]
    return NullMap


def map_sliser_deep_bubble(A_map, deep, bubble):
    # return bool map from original map
    # into given motion parameters of deep and safety of detour
    B_map = create_zero_matrix(len(A_map[0]), len(A_map))
    for stroka in range(len(B_map)):
        for number in range(len(B_map[stroka])):
            problem = A_map[stroka][number]
            if problem < deep:
                B_map[stroka][number] = 1
    for i in range(bubble):
        B_map = create_around_layer(B_map)
    return B_map


def is_obtacle_touch_frame(C_map, mask=1):
    # check the mask (by s=1) touching the frame
    # give mask = 0 if your mask is 0-filled
    for elem in C_map[0]:
        if elem == mask:
            return 1
    for elem in C_map[-1]:
        if elem == mask:
            return 1
    for elem in range(1, len(C_map) - 1):
        if C_map[elem][0] == mask or C_map[elem][-1] == mask:
            return 1
    return 0


def MapAddFrame(map, overwidth=1):
    for i in range(overwidth):
        for y in range(len(map)):
            for x in range(len(map[0])):
                if x == 0 + overwidth or x == len(map[0]) - 1 - overwidth or y == 0 + overwidth or y == len(
                        map) - 1 - overwidth:
                    map[y][x] = 0
    return map


def SS_min_RR(x, y, SS, RR):
    # unused function of bool matrix subtraction
    TS = create_zero_matrix(x, y)
    for stroka in range(len(SS)):
        for number in range(len(SS[stroka])):
            elemS = SS[stroka][number]
            elemR = RR[stroka][number]
            if elemS == 1:
                if elemR == 1:
                    TS[stroka][number] = 0
                if elemR == 0:
                    TS[stroka][number] = 1
            if elemS == 0:
                TS[stroka][number] = 0
    return TS


def create_filled_contour(x_stop, y_stop, B_map):
    # create around obtacle 1-cell border
    x_edge, y_edge = len(B_map[1]), len(B_map)
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
                        if B_map[stroka][number + 1] != 0 and OBT[stroka][number + 1] != 1:  # right
                            OBT[stroka][number + 1] = 1
                            nums += 1

                    if (0 <= stroka < y_edge) and (0 <= number - 1 < x_edge):
                        if B_map[stroka][number - 1] != 0 and OBT[stroka][number - 1] != 1:  # left
                            OBT[stroka][number - 1] = 1
                            nums += 1

                    if (0 <= stroka - 1 < y_edge) and (0 <= number < x_edge):
                        if B_map[stroka - 1][number] != 0 and OBT[stroka - 1][number] != 1:  # up
                            OBT[stroka - 1][number] = 1
                            nums += 1

                    if (0 <= stroka + 1 < y_edge) and (0 <= number < x_edge):
                        if B_map[stroka + 1][number] != 0 and OBT[stroka + 1][number] != 1:  # down
                            OBT[stroka + 1][number] = 1
                            nums += 1

                    if (0 <= stroka -1 < y_edge) and (0 <= number + 1 < x_edge):
                        if B_map[stroka - 1][number + 1] != 0 and OBT[stroka - 1][number + 1] != 1:  # right- up
                            OBT[stroka - 1][number + 1] = 1
                            nums += 1

                    if (0 <= stroka - 1 < y_edge) and (0 <= number - 1 < x_edge):
                        if B_map[stroka - 1][number - 1] != 0 and OBT[stroka - 1][number - 1] != 1:  # left- up
                            OBT[stroka - 1][number - 1] = 1
                            nums += 1

                    if (0 <= stroka + 1 < y_edge) and (0 <= number + 1 < x_edge):
                        if B_map[stroka + 1][number + 1] != 0 and OBT[stroka + 1][number + 1] != 1:  # right - down
                            OBT[stroka + 1][number + 1] = 1
                            nums += 1

                    if (0 <= stroka + 1 < y_edge) and (0 <= number - 1 < x_edge):
                        if B_map[stroka + 1][number - 1] != 0 and OBT[stroka + 1][number - 1] != 1:  # left-down
                            OBT[stroka + 1][number - 1] = 1
                            nums += 1
    return OBT


# def create_filled_contour(x_stop, y_stop, B_map):
#     # create around obtacle 1-cell border
#     x_edge, y_edge = len(B_map[1]), len(B_map)
#     OBT = create_zero_matrix(x_edge, y_edge)
#     OBT[y_stop][x_stop] = 1
#     C_map_ = create_around_layer(MAP1)
#
#     MapAddFrame(map, overwidth=1):
#     SS_min_RR(x, y, SS, RR):
#     return OBT


def type_of_obtacle(B_map, x_stop, y_stop):
    # return type of finding object- island or coast
    obt_type = '0'
    print(x_stop, y_stop)
    C_map = create_filled_contour(x_stop, y_stop, B_map)  # add check outsides in contour
    for i in C_map:
        print(i)
    if is_obtacle_touch_frame(C_map):
        obt_type = "coast"
        return obt_type
    obt_type = "island"

    return obt_type, C_map


def create_around_layer(MAP1):
    # in create 1-tail layer aroudn bool "true" obtacle
    width, height = len(MAP1[1]), len(MAP1)
    MAP2 = create_zero_matrix(width, height)
    for stroka in range(len(MAP1)):
        for number in range(len(MAP1[stroka])):
            if MAP1[stroka][number] == 1:
                MAP2[stroka][number] = MAP1[stroka][number]
                if (0 <= stroka < height) and (0 <= number + 1 < width):  # right
                    MAP2[stroka][number + 1] = 1
                if (0 <= stroka < height) and (0 <= number - 1 < width):  # left
                    MAP2[stroka][number - 1] = 1
                if (0 <= stroka - 1 < height) and (0 <= number < width):  # up
                    MAP2[stroka - 1][number] = 1
                if (0 <= stroka + 1 < height) and (0 <= number < width):  # down
                    MAP2[stroka + 1][number] = 1
    return MAP2


def strait_safety(B, width):
    # detect and connect unsafety straits to delete it from pathfindng
    # now bad
    # B_1 = B
    # for n in range(width//2):
    #     B_1 = create_1st_S(B)
    #
    # B_2
    return