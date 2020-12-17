from My_test_map import testmap

from graf_only import Graph
from graf_only import Node
from lineOps import Is_coincide
from mapOps import map_sliser_deep_bubble
from plannerOps import generateName, simple_detour_Fractal, find_path_length, Create_Dependence_Tree, \
    Add_Weight_2dependence


def PATH_GLOBAL(A_map, startPoint, finishPoint, deep, bubble):
    B_map = map_sliser_deep_bubble(A_map, deep, bubble)
    dep_tree = Create_Dependence_Tree(B_map, startPoint, finishPoint)
    dep_tree = Add_Weight_2dependence(B_map, dep_tree)

    # add horizontal corrrection
    # block graf creation from dependence tree

    for NodeName in dep_tree.keys():
        NodeName = Node("F")  # NAME from tree.keys
    path_planner_graph = Graph.create_from_nodes([dep_tree.keys()])
    for parent_node in dep_tree.keys():
        for childNode in dep_tree.get(parent_node).keys():
            if childNode != 'coordinates':
                weight = dep_tree.get(parent_node).get(childNode)[2]  # 0-x 1-y 2-weight 3-list
                path_planner_graph.connect(parent_node, childNode, weight)



#   block of calculate our way by A*
print([(weight, [n.data for n in node]) for (weight, node) in path_planner_graph.dijkstra(a)])
