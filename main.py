from classes import Board


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
# generate move for white test case 
# (adding e4 causes removing black pieces from f1,f3 but not from mill on g file)
pos1 = {
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

# no moves for whites test case
pos2 = {
        "a0" : "b",
        "a3" : "w",
        "a6" : "b",
        "b1" : "w",
        "b3" : "w",
        "b5" : "b",
        "c2" : "b",
        "c3" : "w",
        "c4" : "b",
        "d4" : None,
        "d5" : None,
        "d6" : None,
        "e2" : "w",
        "e3" : "w",
        "e4" : "b",
        "f1" : "b",
        "f3" : "b",
        "f5" : "b",
        "g0" : "b",
        "g3" : "b",
        "g6" : "b", 
}

# hopping for whites test case
pos3 = {
        "a0" : "b",
        "a3" : "w",
        "a6" : "b",
        "b1" : None,
        "b3" : "w",
        "b5" : "b",
        "c2" : "b",
        "c3" : "w",
        "c4" : "b",
        "d4" : None,
        "d5" : None,
        "d6" : None,
        "e2" : "b",
        "e3" : None,
        "e4" : "b",
        "f1" : "b",
        "f3" : "b",
        "f5" : "b",
        "g0" : "b",
        "g3" : "b",
        "g6" : "b", 
}

# generate_moves mid_endgame and opening test postions pos3 and pos4
pos4 = {
        "a0" : "b",
        "a3" : "w",
        "a6" : "b",
        "b1" : None,
        "b3" : "w",
        "b5" : "b",
        "c2" : "b",
        "c3" : "w",
        "c4" : "b",
        "d4" : None,
        "d5" : None,
        "d6" : None,
        "e2" : "b",
        "e3" : "w",
        "e4" : "b",
        "f1" : "b",
        "f3" : "b",
        "f5" : "b",
        "g0" : "b",
        "g3" : "b",
        "g6" : "b", 
}

b = Board(pos3)

# b.test()
print("=====================================")
print("====================================="+"\n")
b.display_position()
print("====================================="+"\n")
print("=====================================")
# b.generate_add()
# b.generate_move()
# b.generate_hopping()
# b.generate_moves_mid_endgame()
b.generate_moves_opening()
# print(b.self.board)
# print(b.test())
# print(b.closemill("a0"))
# b.display_position()