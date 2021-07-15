from classes import Board

def alphabeta_opening(pos,depth=4):
        input_position = Board(pos)
        print("**********************************************************************************")
        print("*                                Input Position                                  *")
        print("**********************************************************************************")
        print("\n")
        input_position.display_position()
        print("************* Please wait..... computer is thinking hard to beat you *************")

        root_position = input_position
        root_position.depth=0

        # depth=3
        max_min(root_position,-1000000,1000000,depth)
            

        print("**********************************************************************************")
        print("*                                  computer plays                                *")
        print("**********************************************************************************")
        print("**********************************************************************************"+"\n\n")
        root_position.white_move.display_position()
        print("Static Estimate : ",root_position.static_estimate,"\n")
        print("Nodes Evaluated : ",dfs(root_position,1),"\n")
        print("**********************************************************************************")
        print("**********************************************************************************")
        return root_position.white_move

        
def max_min(node,a,b,depth):
    if node.depth == depth:
        node.static_estimate =  node.static_estimation_opening()
        return node.static_estimate

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

        temp = min_max(child,a,b,depth)
        if v<temp :
            v=temp
            node.white_move = child
            node.static_estimate = v            
        if v>=b:
            # node.static_estimate = v
            # node.white_move = child
            return v

        a = max(v,a)
    # node.static_estimate = v
    return v



def min_max(node,a,b,depth):
    if node.depth == depth:
        node.static_estimate =  node.static_estimation_opening()
        return node.static_estimate

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

        temp = max_min(child,a,b,depth)
        if v>temp :
            v=temp
            node.black_move = child
            node.static_estimate = v  
        if v<=a:
            # node.static_estimate = v
            # node.black_move = child
            return v

        b = min(v,b)
    # node.static_estimate = v
    return v    


def dfs(node,c):
    if node.child_positions ==[]:
        # print("============== ",c," Leaf Node================\n")
        # node.display_position()
        # print("================================================\n")
        return c

    # print("=========== ",c," Node===============\n")
    # node.display_position()
    # print("=======================================\n")
    for child in node.child_positions:
        c=dfs(child,c+1)
    return c

