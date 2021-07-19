from classes import Board
import sys
import os

def minimax_midgame(pos,depth=3,move="w"):
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
            node.static_estimate =  node.static_estimation_midgame()
        else:
            node.static_estimate =  node.static_estimation_midgame_black()        
        return node.static_estimate

    v = float('-inf')

    child_positions = node.generate_moves_mid_endgame(color=max_color)
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
            node.static_estimate =  node.static_estimation_midgame()
        else:
            node.static_estimate =  node.static_estimation_midgame_black()
        return node.static_estimate


    v = float('inf')

    child_positions = node.generate_moves_mid_endgame(color=min_color)
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


###################################################################################
###                                    Main                                     ###
###################################################################################
cwd = os.getcwd()
try:
    arg = sys.argv[1]
except:
    print("\n","        No argument provided for Input Board position: Defauting to board3.txt  ")
    print("\n")
    arg = "board3.txt"
    

try:
    depth = int(sys.argv[2])
except:
    print("\n","        No argument provided for depth: Defauting to depth = 5  ")
    print("\n")
    depth = 5

input_file = cwd +os.path.sep+arg
output_file = cwd+os.path.sep+"board2.txt"
output_file2 = cwd+os.path.sep+"board4.txt"


def read(file_path):
    with open(file_path) as file:
        _input = file.read()
    return _input

try:
    _input = read(input_file)
except:
    print("Please check if input file exist")
    exit()

# change this initialization for different order of filling when there is tie in static estimate
input_pos = {
        "a0" : None,
        "g0" : None,
        "b1" : None,
        "f1" : None,
        "c2" : None,
        "e2" : None,
        "a3" : None,
        "b3" : None,
        "c3" : None,
        "e3" : None,
        "f3" : None,
        "g3" : None,
        "c4" : None,
        "d4" : None,
        "e4" : None,
        "b5" : None,
        "d5" : None,
        "f5" : None,
        "a6" : None,
        "d6" : None,
        "g6" : None,
}

for count,_location in enumerate(input_pos):
    if _input[count] =="x":
        input_pos[_location]=None
    else:
        input_pos[_location]= _input[count].lower()


computer_move=minimax_midgame(input_pos,depth,move="w")
computer_move.write(output_file2)

print("\n")
print("Input file: ",input_file)
print("Output file: ",output_file2)