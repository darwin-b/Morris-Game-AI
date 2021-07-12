from classes import Board
import sys

pos = {
        "a0" : None,
        "a3" : "w",
        "a6" : None,
        "b1" : None,
        "b3" : "w",
        "b5" : None,
        "c2" : None,
        "c3" : "w",
        "c4" : None,
        "d4" : None,
        "d5" : None,
        "d6" : None,
        "e2" : "w",
        "e3" : "w",
        "e4" : None,
        "f1" : "b",
        "f3" : "b",
        "f5" : None,
        "g0" : "b",
        "g3" : "b",
        "g6" : "b", 
}

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


def minimax_opening(pos):
        input_position = Board(pos)
        print("*******************************************************")
        print("*                   Input Position                    *")
        print("*******************************************************")
        print("\n")
        input_position.display_position()
        print("*******************************************************")
        print("*******************************************************")

        color="w"
        root_position = input_position
        root_position.depth=0

        depth=5
        levels ={}

        for lvl in range(0,depth+1):
            levels[lvl] = []
        
        levels[0].append(root_position)
        temp_positions =[root_position]

        for lvl in levels:
            temp = []
            _positions = []
    
            if lvl %2 ==0:
                color ="w"
            else:
                color="b"

            if lvl < depth:
                for each_board in levels[lvl]:
                    _positions = each_board.generate_moves_opening(color=color)
                    for _pos in _positions:
                        child = Board(_pos)
                        child.parent = each_board
                        child.depth = each_board.depth+1
                        each_board.child_positions.append(child)
                        levels[lvl+1].append(child)
            
        # calculating static estimate function at leaf nodes [given depth]
        for board in levels[depth] :
            board.static_estimate = board.static_estimation_opening()


        for level in range(depth-1,-1,-1):
            nodes = levels[level]
            for node in nodes:
                if level % 2 ==0:
                    node.static_estimate = node.child_positions[0].static_estimate
                    node.white_move = node.child_positions[0]

                    for child in node.child_positions:
                        if node.static_estimate < child.static_estimate:
                            node.static_estimate = child.static_estimate
                            node.white_move = child

                else:
                    node.static_estimate = node.child_positions[0].static_estimate
                    node.black_move = node.child_positions[0]

                    for child in node.child_positions:
                        if node.static_estimate > child.static_estimate:
                            node.static_estimate = child.static_estimate
                            node.black_move = child
        
        root_position.white_move.display_position()
        

        



minimax_opening(pos)