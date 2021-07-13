from MiniMaxOpening import minimax_opening
from MiniMaxMidgame import minimax_midgame
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
    depth = 3

try:
    depth = int(sys.argv[2])
except:
    print("\n","        No argument provided for depth: Defauting to depth = 4  ")
    print("\n")
    depth = 4

input_file = cwd +os.path.sep+arg
output_file = cwd+os.path.sep+"board2.txt"


def read(file_path):
    with open(file_path) as file:
        input = file.read()
    return input

try:
    input = read(input_file)
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
    if input[count] =="x":
        input_pos[_location]=None
    else:
        input_pos[_location]= input[count].lower()

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
input_pos = pos

# computer_move=minimax_opening(input_pos,depth)
computer_move = minimax_midgame(input_pos,depth=2)
computer_move.write(output_file)

print("\n")
print("Input file: ",input_file)
print("Output file: ",output_file)

