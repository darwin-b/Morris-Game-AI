from classes import Board

# pos = {
#         "a0" : None,
#         "a3" : "w",
#         "a6" : None,
#         "b1" : None,
#         "b3" : "w",
#         "b5" : None,
#         "c2" : None,
#         "c3" : "w",
#         "c4" : None,
#         "d4" : None,
#         "d5" : None,
#         "d6" : None,
#         "e2" : "w",
#         "e3" : "w",
#         "e4" : None,
#         "f1" : "b",
#         "f3" : "b",
#         "f5" : None,
#         "g0" : "b",
#         "g3" : "b",
#         "g6" : "b", 
# }

# pos = {
#         "a0" : None,
#         "a3" : None,
#         "a6" : "w",
#         "b1" : None,
#         "b3" : None,
#         "b5" : "b",
#         "c2" : None,
#         "c3" : None,
#         "c4" : "b",
#         "d4" : None,
#         "d5" : None,
#         "d6" : None,
#         "e2" : None,
#         "e3" : None,
#         "e4" : None,
#         "f1" : None,
#         "f3" : None,
#         "f5" : None,
#         "g0" : None,
#         "g3" : None,
#         "g6" : "w",
# }


# pos = {
#         "a0" : None,
#         "a3" : "w",
#         "a6" : None,
#         "b1" : None,
#         "b3" : "w",
#         "b5" : None,
#         "c2" : None,
#         "c3" : "w",
#         "c4" : None,
#         "d4" : None,
#         "d5" : None,
#         "d6" : None,
#         "e2" : "w",
#         "e3" : "w",
#         "e4" : None,
#         "f1" : "b",
#         "f3" : "b",
#         "f5" : None,
#         "g0" : "b",
#         "g3" : "b",
#         "g6" : "b", 
# }

pos = {
        "a0" : None,
        "a3" : None,
        "a6" : "b",
        "b1" : None,
        "b3" : None,
        "b5" : "w",
        "c2" : None,
        "c3" : None,
        "c4" : "w",
        "d4" : None,
        "d5" : None,
        "d6" : None,
        "e2" : None,
        "e3" : None,
        "e4" : None,
        "f1" : None,
        "f3" : None,
        "f5" : None,
        "g0" : None,
        "g3" : None,
        "g6" : "b",
}


def minimax_opening(pos,depth=4):
        input_position = Board(pos)
        print("**********************************************************************************")
        print("*                                Input Position                                  *")
        print("**********************************************************************************")
        print("\n")
        input_position.display_position()
        print("************* Please wait..... computer is thinking hard to beat you *************")

        root_position = input_position
        root_position.depth=0


        # levels ={}

        # for lvl in range(0,depth+1):
        #     levels[lvl] = []
        
        # levels[0].append(root_position)
        
        # color="w"
        # # first_move_color=color

        # for lvl in levels:
        #     temp = []
        #     _positions = []

        #     if lvl %2 ==0:
        #         color ="w"
        #     else:
        #         color ="b"

        #     if lvl < depth:
        #         for each_board in levels[lvl]:
        #             _positions = each_board.generate_moves_opening(color=color)
        #             for _pos in _positions:
        #                 child = Board(_pos)
        #                 child.parent = each_board
        #                 child.depth = each_board.depth+1
        #                 each_board.child_positions.append(child)
        #                 levels[lvl+1].append(child)
            
        # # calculating static estimate function at leaf nodes [given depth]
        # # if first_move_color =="w":
        # for board in levels[depth] :
        #     board.static_estimate = board.static_estimation_opening()

        depth=3
        max_min(root_position,depth)

        print("No of nodes evaluated: ",dfs2(root_position,1))
        x=1
        root_position.white_move.display_position()
        print("Static estimate : ",root_position.static_estimate )

def max_min(node,depth):
    if node.depth == depth:
        node.static_estimate =  node.static_estimation_opening()
        return node.static_estimate
    else:
        v = float('-inf')

        child_positions = node.generate_moves_opening(color="w")
        for c in child_positions:
            child = Board(c)
            child.parent = node

            if node.depth is None:
                node.depth=0
            child.depth = node.depth+1
            node.child_positions.append(child)

        # for child in node.child_positions:
        #     v = max(v,min_max(child))
            temp = min_max(child,depth)
            if v<temp :
                v=temp
                node.white_move = child
                node.static_estimate = v

        return v


def min_max(node,depth):
    if node.depth == depth:
        node.static_estimate =  node.static_estimation_opening()
        return node.static_estimate
    else:
        v = float('inf')

        child_positions = node.generate_moves_opening(color="b")
        for c in child_positions:
            child = Board(c)
            child.parent = node

            if node.depth is None:
                node.depth=0
            child.depth = node.depth+1
            node.child_positions.append(child)

        # for child in node.child_positions:
        #     v = max(v,min_max(child))
            temp = max_min(child,depth)
            if v>temp :
                v=temp
                node.black_move = child
                node.static_estimate = v      
        return v


def dfs2(node,c):
    if node.child_positions ==[]:
        # print("============== ",c," Leaf Node================\n")
        # node.display_position()
        # print("================================================\n")
        return c
    else:
        # print("=========== ",c," Node===============\n")
        # node.display_position()
        # print("=======================================\n")
        for child in node.child_positions:
            c=dfs2(child,c+1)
        return c





minimax_opening(pos)