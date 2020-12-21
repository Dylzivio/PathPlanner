import random

from cellWalker import go_along_wall_W, go_along_wall
from lineOps import Is_coincideOne, line_Endpoint, Is_coincide
from mapOps import type_of_obtacle


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


def simple_detour_Fractal(B_map, x_start, y_start, x_finish, y_finish):
    # make go around obtacle to finish side with create one or two points for graf
    xfinish_fake, yfinish_fake = -1, -1
    new_node_info = []
    # while issue finish is closed for us by obtacle with some accuracy
    while not Is_coincideOne(xfinish_fake,x_finish) and not Is_coincideOne(yfinish_fake, y_finish):
        # print(xfinish_fake, yfinish_fake)
        # print(x_start, y_start)
        # print('----------')
        xfinish_fake, yfinish_fake = line_Endpoint(B_map, x_start, y_start, x_finish, y_finish)
        obt_type, C_map = type_of_obtacle(B_map, x_start, y_start)
        if obt_type == "coast":
            # for cost we get one graf point
            try:
                new_node_info.append(go_along_wall(B_map, x_start, y_start, x_finish, y_finish, "LeftHand"))
            except:
                new_node_info.append(go_along_wall(B_map, x_start, y_start, x_finish, y_finish, "RightHand"))
        if obt_type == "island":
            # print('/////////////////////////////////////////////////'
            #       '--------------------------------------------------')
            # for island we get two graf point
            new_node_info.append(go_along_wall(B_map, x_start, y_start, x_finish, y_finish, "LeftHand"))
            new_node_info.append(go_along_wall(B_map, x_start, y_start, x_finish, y_finish, "RightHand"))
    return new_node_info


def find_path_length(B_map, x_start, y_start, x_finish, y_finish):
    # find simple path length for sellWalker
    list_of_points = []
    way = 0
    ex_way= []
    obt_type, C_map = type_of_obtacle(B_map, x_start, y_start)
    if obt_type == "coast":
        # for cost we get one values
        try:
            way, list_of_points = go_along_wall_W(C_map, x_start, y_start, x_finish, y_finish, "LeftHand")
        except:
            way, list_of_points = go_along_wall_W(C_map, x_start, y_start, x_finish, y_finish, "RightHand")
    if obt_type == "island":
        # for island we get two values
        ex_way.append(go_along_wall_W(B_map, x_start, y_start, x_finish, y_finish, "LeftHand"))
        ex_way.append(go_along_wall_W(B_map, x_start, y_start, x_finish, y_finish, "RightHand"))
    # filter invalid values by choosing the littlest
    if ex_way[0][0] > ex_way[1][0]:
        way, list_of_points = ex_way[0][0], ex_way[1][0]
    if ex_way[0][0] < ex_way[1][0]:
        way, list_of_points = ex_way[1][0], ex_way[1][1]
    return way, list_of_points


# def path_list_smooth(B_map, list_of_points):
#     # smooth finally path-listPoint
#     is_end = 0
#     short_list_of_points = []
#     short_list_of_points.append(list_of_points[0])
#     #
#     while not is_end:
#         short_list_of_points = []
#     i = 0
#     for i in range(len(list_of_points)):
#         for k in range(i,len(list_of_points)):
#
#     return short_list_of_points


def Create_Dependence_Tree(B_map, startPoint, finishPoint):
    # block node creation and set dependence tree
    # correct duplicate points
    # print(".................")
    for i in B_map:
        print(i)
    print(".................")

    dep_tree = {}
    not_used_yet = [startPoint]
    nodeName = generateName()
    dep_tree[nodeName] = startPoint
    # while where are not unparsed point
    while len(not_used_yet) != 0:
        loadNode = not_used_yet[0]
        node_info = {}
        x_start, y_start = loadNode[0], loadNode[1]
        node_info['coordinates'] = loadNode
        # click childname to 1
        childName = 'child1'
        # pair of points, next from processed
        node_request = simple_detour_Fractal(B_map, x_start, y_start, finishPoint[0], finishPoint[1])
        for node in node_request:
            nextNodeName = generateName()
            for checkNode in dep_tree.keys():
                # if new point is inaccuracy of graf-point
                # rewrite any grafPoint with this adress
                if Is_coincide(node[0], node[1], dep_tree.get(checkNode).get('coordinates')[0],
                               dep_tree.get(checkNode).get('coordinates')[1]):
                    for parent_node in dep_tree.keys():
                        if parent_node['child1'] == loadNode:
                            dep_tree[parent_node['child1']] = (node[0], node[1])
                        elif parent_node['child2'] == loadNode:
                            dep_tree[parent_node['child2']] = (node[0], node[1])
                    continue
            # add to dependence tree
            not_used_yet.append(node)
            node_info['coordinates'] = (node[0], node[1])  # coordX and coordY
            node_info[childName] = node
            dep_tree[nextNodeName] = node_info
            childName = 'child2'
    return dep_tree


def Add_Weight_2dependence(B_map, dep_tree):
    #  block  dependence tree correction? and add weight
    for parent_node in dep_tree.keys():
        for childNode in dep_tree.get(parent_node).keys():
            if childNode != 'coordinates':
                pathLength, list_of_points = find_path_length(B_map,dep_tree.get(parent_node).get('coordinates')[0],
                                              dep_tree.get(parent_node).get('coordinates')[0],
                                              dep_tree.get(parent_node).get(childNode)[0],
                                              dep_tree.get(parent_node).get(childNode)[1])
                dep_tree[parent_node[childNode][2]] = pathLength
                dep_tree[parent_node[childNode][3]] = list_of_points
    return dep_tree