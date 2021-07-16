from classes import Board
import sys

###################################################################################
# Input:
# Output:
###################################################################################
def minimax_opening(pos,depth=3,move="w"):
        input_position = Board(pos)
        print("**********************************************************************************")
        print("*                                Input Position                                  *")
        print("**********************************************************************************")
        print("\n")
        input_position.display_position()
        print("************* Please wait..... computer is thinking hard to beat you *************")

        root_position = input_position
        root_position.depth=0

        max_min(root_position,depth,move)

        
        print("**********************************************************************************")
        print("*                                  computer plays                                *")
        print("**********************************************************************************")
        print("**********************************************************************************"+"\n\n")
        root_position.ai_move.display_position()
        print("Static Estimate : ",root_position.static_estimate)
        print("Nodes Evaluated : ",dfs(root_position,c=1),"\n")
        print("**********************************************************************************")
        print("**********************************************************************************")
        return root_position.ai_move

        
###################################################################################
# Input:
# Output:
###################################################################################
def max_min(node,depth=3,move="w"):
    if move=="w":
        max_color="w"
        min_color="b"
    else:
        max_color="b"
        min_color="w"

    if node.depth == depth:
        if max_color=="w":
            node.static_estimate =  node.static_estimation_opening()
        else:
            node.static_estimate =  node.static_estimation_opening_black()        
        return node.static_estimate

    v = float('-inf')

    child_positions = node.generate_moves_opening(color=max_color)
    for c in child_positions:
        child = Board(c)
        child.parent = node

        if node.depth is None:
            node.depth=0
        child.depth = node.depth+1
        node.child_positions.append(child)

        temp = min_max(child,depth,move=min_color)
        if v<temp :
            v=temp
            node.ai_move = child
            node.static_estimate = v

    return v


###################################################################################
# Input:
# Output:
###################################################################################
def min_max(node,depth=3,move="b"):
    if move=="b":
        min_color="b"
        max_color="w"
    else:
        min_color="w"
        max_color="b"

    if node.depth == depth:
        if min_color=="b":
            node.static_estimate =  node.static_estimation_opening()
        else:
            node.static_estimate =  node.static_estimation_opening_black()
        return node.static_estimate

    v = float('inf')

    child_positions = node.generate_moves_opening(color=min_color)
    for c in child_positions:
        child = Board(c)
        child.parent = node

        if node.depth is None:
            node.depth=0
        child.depth = node.depth+1
        node.child_positions.append(child)

        temp = max_min(child,depth,move=max_color)
        if v>temp :
            v=temp
            node.ai_move = child
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

# minimax_opening(pos)