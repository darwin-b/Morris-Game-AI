from MiniMaxOpening import minimax_opening
from MiniMaxMidgame import minimax_midgame
from ABOpening import alphabeta_opening
from ABMidgame import alphabeta_midgame

from classes import Board
import sys
import os


cwd = os.getcwd()
try:
    arg = sys.argv[1]
except:
    print("\n","        No argument provided for Input Board position: Defauting to board1.txt  ")
    print("\n")
    arg = "board1.txt"
    

try:
    depth = int(sys.argv[2])
except:
    print("\n","        No argument provided for depth: Defauting to depth = 3  ")
    print("\n")
    depth = 3

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
#         "a6" : "b",
#         "b1" : None,
#         "b3" : None,
#         "b5" : "w",
#         "c2" : None,
#         "c3" : None,
#         "c4" : "w",
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
#         "g6" : "b",
# }
input_pos2 = pos
# depth=3
# computer_move=minimax_opening(input_pos,depth,move="w")
# computer_move=minimax_opening(input_pos,depth,move="b")
# computer_move = alphabeta_opening(input_pos,depth,move="w")
# computer_move = alphabeta_opening(input_pos,depth,move="b")

# computer_move = minimax_midgame(input_pos,depth,move="w")
# computer_move = minimax_midgame(input_pos2,depth,move="b")
# computer_move = alphabeta_midgame(input_pos,depth,move="w")
# computer_move = alphabeta_midgame(input_pos2,depth,move="b")
# computer_move.write(output_file)

choice =""
while choice!="0":
    print("Choose From the following:")
    print("1. MiniMax opening")
    print("2. MiniMax midgame")
    print("3. AlphaBeta opening")
    print("4. AlphaBeta midgame")
    print("5. Game for black: Minimax opening")
    print("6. Game for black: Minimax midgame")
    # print("7. Improved: Minimax openning")
    # print("8. Improved: Minimax midgame")
    print("0. Exit (choose 0 to exit the program) ")
    print("")
    print("Enter your choice: ")
    choice = input()

    if choice=="1":
        computer_move=minimax_opening(input_pos,depth,move="w")
        computer_move.write(output_file)

        print("\n")
        print("Input file: ",input_file)
        print("Output file: ",output_file)

    elif choice=="2":
        computer_move=minimax_midgame(input_pos,depth,move="w")
        computer_move.write(output_file2)

        print("\n")
        print("Input file: ",input_file)
        print("Output file: ",output_file2)

    elif choice=="3":
        computer_move=alphabeta_opening(input_pos,depth,move="w")
        computer_move.write(output_file)

        print("\n")
        print("Input file: ",input_file)
        print("Output file: ",output_file)

    elif choice=="4":
        computer_move=alphabeta_midgame(input_pos,depth,move="w")
        computer_move.write(output_file2)

        print("\n")
        print("Input file: ",input_file)
        print("Output file: ",output_file2)

    elif choice=="5":
        computer_move=minimax_opening(input_pos,depth,move="b")
        computer_move.write(output_file)

        print("\n")
        print("Input file: ",input_file)
        print("Output file: ",output_file)

    elif choice=="6":
        computer_move=minimax_midgame(input_pos,depth,move="b")
        computer_move.write(output_file2)

        print("\n")
        print("Input file: ",input_file)
        print("Output file: ",output_file2)
    
    # elif choice=="7":
        # computer_move=minimax_midgame(input_pos,depth,move="w")
        # computer_move.write(output_file)
    # elif choice=="8":
        # computer_move=minimax_midgame(input_pos,depth,move="w")
        # computer_move.write(output_file)
    elif choice=="8":
        print("Exiting...........")
    else:
        print("Choose valid Choice!")
    
    # print("\n")
    # print("Input file: ",input_file)
    # print("Output file: ",output_file)




