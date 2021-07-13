from classes import Board


def minimax_midgame(pos,depth=4):
        input_position = Board(pos)
        print("**********************************************************************************")
        print("*                                Input Position                                  *")
        print("**********************************************************************************")
        print("\n")
        input_position.display_position()
        print("************* Please wait..... computer is thinking hard to beat you *************")

        root_position = input_position
        root_position.depth=0


        levels ={}

        for lvl in range(0,depth+1):
            levels[lvl] = []
        
        levels[0].append(root_position)
        
        color="w"
        # first_move_color=color

        for lvl in levels:
            temp = []
            _positions = []

            if lvl %2 ==0:
                color ="w"
            else:
                color ="b"

            if lvl < depth:
                for each_board in levels[lvl]:
                    _positions = each_board.generate_moves_mid_endgame(color=color)
                    for _pos in _positions:
                        child = Board(_pos)
                        child.parent = each_board
                        child.depth = each_board.depth+1
                        each_board.child_positions.append(child)
                        levels[lvl+1].append(child)
            
        # calculating static estimate function at leaf nodes [given depth]
        # if first_move_color =="w":
        for board in levels[depth] :
            n_moves = len(board.parent.child_positions)
            board.static_estimate = board.static_estimation_midgame(n_moves=n_moves)


        for level in range(depth-1,-1,-1):
            nodes = levels[level]

            for node in nodes:
                # Max strategy
                if level % 2 ==0:
                    node.static_estimate = node.child_positions[0].static_estimate
                    node.white_move = node.child_positions[0]

                    for child in node.child_positions:
                        if node.static_estimate < child.static_estimate:
                            node.static_estimate = child.static_estimate
                            node.white_move = child

                # Min strategy 
                else:
                    node.static_estimate = node.child_positions[0].static_estimate
                    node.black_move = node.child_positions[0]

                    for child in node.child_positions:
                        if node.static_estimate > child.static_estimate:
                            node.static_estimate = child.static_estimate
                            node.black_move = child

        print("**********************************************************************************")
        print("*                                  computer plays                                *")
        print("**********************************************************************************")
        print("**********************************************************************************"+"\n\n")
        root_position.white_move.display_position()
        print("Static Estimate : ",root_position.static_estimate,"\n")
        print("**********************************************************************************")
        print("**********************************************************************************")
        return root_position.white_move   