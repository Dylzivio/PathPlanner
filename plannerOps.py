import random

from My_test_map import test3
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
    new_node_info = []
    xfinish_fake, yfinish_fake = line_Endpoint(B_map, x_start, y_start, x_finish, y_finish)
    print('lep',xfinish_fake, yfinish_fake)
    obt_type, C_map = type_of_obtacle(B_map, x_start, y_start)

    if obt_type == "coast":
        # for cost we get one graf point
        try:
            new_node_info.append(go_along_wall(C_map, x_start, y_start, x_finish, y_finish, "LeftHand"))
            print(new_node_info)
        except:
            new_node_info.append(go_along_wall(C_map, x_start, y_start, x_finish, y_finish, "RightHand"))
            print(new_node_info)

    if obt_type == "island":
        print('i')
        for i in C_map:
            print(i)
        print(x_start, y_start, x_finish, y_finish)
        new_node_info.append(go_along_wall(C_map, x_start, y_start, x_finish, y_finish, "LeftHand"))
        print(new_node_info)

        new_node_info.append(go_along_wall(C_map, x_start, y_start, x_finish, y_finish, "RightHand"))
        print(new_node_info)

    print('++++++++++', new_node_info)
    return new_node_info

obt_type, C_map = type_of_obtacle(test3, 1, 5)
print(C_map[5][1])
print(test3[5][1])
# print(simple_detour_Fractal(test3, 1, 5, 10, 10))
# print(line_Endpoint(test3, 1, 5, 10, 10))

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
    dep_tree = {}
    not_used_yet = []
    node_info = {}

    node_info['coordinates'] = startPoint
    childName = 'child1'
    node_request = simple_detour_Fractal(B_map, startPoint[0], startPoint[1], finishPoint[0], finishPoint[1])
    for node in node_request:
        nextNodeName = generateName()
        not_used_yet.append(node)
        node_info[childName] = [nextNodeName, node]
        childName = 'child2'
    dep_tree['START'] = node_info

    ###########################
    # while where are not unparsed point
    while len(not_used_yet) != 0:
        print('cycle--------------------------------------------------------')
        print('not used yet ', not_used_yet)
        print('dep tree ', dep_tree)
        loadNode = not_used_yet[0]
        print('loading: ',loadNode)
        node_info = {}
        x_start, y_start = loadNode[0], loadNode[1]
        node_info['coordinates'] = loadNode
        # click childname to 1
        childName = 'child1'
        # pair of points, next from processed
        node_request = simple_detour_Fractal(B_map, x_start, y_start, finishPoint[0], finishPoint[1])
        print('REC_fractal: ', node_request)
        PARENT_Name = ' '
        for _node in dep_tree.keys():
            if dep_tree.get(_node).get('child1')[1] == loadNode:
                PARENT_Name = dep_tree.get(_node).get('child1')[0]
            if dep_tree.get(_node).get('child2')[1] == loadNode:
                PARENT_Name = dep_tree.get(_node).get('child1')[0]
        print('we find PARent: ',PARENT_Name)
        for node in node_request:
            nextNodeName = generateName()
            for checkNode in dep_tree.keys():
                # print(checkNode, dep_tree.keys())
                # if new point is inaccuracy of graf-point
                # rewrite any grafPoint with this adress
                if len(dep_tree.keys()) > 0:
                    if Is_coincide(node[0], node[1], dep_tree.get(checkNode).get('coordinates')[0],
                                   dep_tree.get(checkNode).get('coordinates')[1]):
                        for parent_node in dep_tree.keys():
                            if parent_node['child1'][1] == loadNode:
                                dep_tree[parent_node['child1']] = [node[0], node[1]]
                            elif parent_node['child2'][1] == loadNode:
                                dep_tree[parent_node['child2']] = [node[0], node[1]]
                        continue
            # add to dependence tree
            not_used_yet.append(node)
            node_info[childName] = [nextNodeName, node]

            # PARENT_Name = ' '
            # for _node in dep_tree.keys():
            #     if dep_tree.get(_node).get('coordinates') == loadNode:
            #         PARENT_Name = _node

            childName = 'child2'
        dep_tree[PARENT_Name] = node_info
        print("NOTUYET_new ",not_used_yet)
        print('DTR_new: ',dep_tree)
        not_used_yet.remove(loadNode)
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