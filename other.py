import math

from lineOps import line_Endpoint
from mapOps import create_zero_matrix


def create_around_layer_diag(MAP1):
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
                if (0 <= stroka - 1 < height) and (0 <= number + 1 < width):  # right-u
                    MAP2[stroka - 1][number + 1] = 1  # r-u
                if (0 <= stroka + 1 < height) and (0 <= number - 1 < width):  # r-d
                    MAP2[stroka + 1][number - 1] = 1  # r-d
                if (0 <= stroka - 1 < height) and (0 <= number - 1 < width):  # l-u
                    MAP2[stroka - 1][number - 1] = 1  # l-u
                if (0 <= stroka + 1 < height) and (0 <= number - 1 < width):  # down
                    MAP2[stroka + 1][number - 1] = 1  # l-d
    return MAP2


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
    return OBT


def get_alfa(x_from, y_from, x_to, y_to):
    # find angle between two points
    # now broken
    gipotenuza = math.sqrt((x_to - x_from) **2 + (y_from - y_to) **2)
    # clear ange from 0
    alfa = math.asin((x_to - x_from) / gipotenuza)
    alfa_grad = alfa * 57.3
    alfa_start = 0
    # detect quarter, I and IV
    if x_from <= x_to:
        if alfa_grad >= 0:
            alfa_start = alfa_grad
            return alfa_start
        alfa_start = 180 - alfa_grad
    # detect quarter, II and III
    if x_from > x_to:
        if alfa_grad >= 0:
            alfa_start = 360 - alfa_grad
            return alfa_start
        alfa_start = 180 + alfa_grad
    return alfa_start


def radius_flow(A, yc, xc, r, alfa):
    # find real touch-radius from necessary radius
    #from  safety walk around island mass center
    rend_x = xc + r * math.sin(math.radians(alfa))
    rend_y = yc + r * math.cos(math.radians(alfa))
    x_stop, y_stop = lineEndpoint(A, xc, yc, rend_x, rend_y, 0)
    x_stop = math.trunc(x_stop)
    y_stop = math.trunc(y_stop)
    return x_stop, y_stop



def around_obstacle(B, xf, yf, x_stop, y_stop):
    #   Func for fast sliding off obtacle by using radius
    #   and alfa-interval
    #   usefull for not big bad-ring-form
    C = []
    xc, yc = find_center(B)
    r = get_rad_obtacle(xc, yc, B)
    alfa_start = find_alfa(x_stop, y_stop, xc, yc)
    for alfa in range(alfa_start, 360 + alfa_start, 5):
        x_new, y_new = radius_flow(A, yc, xc, r, alfa)
        xf_try, yf_try = line_Endpoint(A, x_new, y_new, xf, yf)
        if B[yf_try][xf_try] == 0:
            C.append(x_new)
            C.append(y_new)
    for alfa in range(alfa_start, -360 - alfa_start, -5):
        x_new, y_new = radius_flow(A, yc, xc, r, alfa)
        xf_try, yf_try = end_of_line(A, x_new, y_new, xf, yf)
        if B[yf_try][xf_try] == 0:
            C.append(x_new)
            C.append(y_new)
    return C


def get_radius_obtacle(x_center, y_center, B_map):
    # takes bool-true map of obtacle and mass center
    # return return max radius from center to border
    # find necessary radius to safety walk around island mass center
    r_max = 0
    for y in range(len(B_map)):
        for x in range(len(B_map[y])):
            if B_map[y][x] == 1:
                r_iteration = math.sqrt((x - x_center) * (x - x_center) + (y - y_center) * (y - y_center))
                if r_iteration > r_max:
                    r_max = math.ceil(r_iteration)
    return r_max


def get_center_obtacle(B_map):
    # find mass center of obtacle
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
