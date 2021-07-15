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

        max_min(root_position,depth)

        
        print("**********************************************************************************")
        print("*                                  computer plays                                *")
        print("**********************************************************************************")
        print("**********************************************************************************"+"\n\n")
        root_position.white_move.display_position()
        print("Static Estimate : ",root_position.static_estimate)
        print("Nodes Evaluated : ",dfs(root_position,c=1),"\n")
        print("**********************************************************************************")
        print("**********************************************************************************")
        return root_position.white_move


###################################################################################
# Input:
# Output:
###################################################################################
def max_min(node,depth):
    if node.depth == depth:
        node.static_estimate =  node.static_estimation_midgame()
        return node.static_estimate

    v = float('-inf')

    child_positions = node.generate_moves_mid_endgame(color="w")
    for c in child_positions:
        child = Board(c)
        child.parent = node

        if node.depth is None:
            node.depth=0
        child.depth = node.depth+1
        node.child_positions.append(child)

        temp = min_max(child,depth)
        if v<temp :
            v=temp
            node.white_move = child
            node.static_estimate = v

    return v


###################################################################################
# Input:
# Output:
###################################################################################
def min_max(node,depth):
    if node.depth == depth:
        node.static_estimate =  node.static_estimation_midgame()
        return node.static_estimate

    v = float('inf')

    child_positions = node.generate_moves_mid_endgame(color="b")
    for c in child_positions:
        child = Board(c)
        child.parent = node

        if node.depth is None:
            node.depth=0
        child.depth = node.depth+1
        node.child_positions.append(child)

        temp = max_min(child,depth)
        if v>temp :
            v=temp
            node.black_move = child
            node.static_estimate = v      

    return v


###################################################################################
# Input: Node in search tree and count of nodes evaluated till given node
# Output: Count of total nodes evaluated
###################################################################################
def dfs(node,c=1):
    if node.child_positions ==[]:
        return c

    for child in node.child_positions:
        c=dfs(child,c+1)
    return c