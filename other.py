import math

from lineOps import line_Endpoint
from mapOps import create_zero_matrix


def SS_min_RR(x, y, SS, RR):
      #unused function of bool matrix subtraction
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
