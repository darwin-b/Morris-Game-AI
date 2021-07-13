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
# b.display_position()
print("====================================="+"\n")
print("=====================================")
# b.generate_add()
# b.generate_move()
# b.generate_hopping()
# b.generate_moves_mid_endgame()
# b.generate_moves_opening()
# print(b.self.board)
# print(b.test())
# print(b.closemill("a0"))
# b.display_position()


##############################################
 
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

pos = {
        "a0" : None,
        "a3" : None,
        "a6" : "w",
        "b1" : None,
        "b3" : None,
        "b5" : "b",
        "c2" : None,
        "c3" : None,
        "c4" : "b",
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
        "g6" : "w",
}

b = Board(pos)

x = b.generate_moves_opening(color="w")
l = [] 
for count,_pos in enumerate(x):
        each_pos = Board(_pos)
        each_pos.depth = 1
        print("==================",count,"===================")
        print("====================================="+"\n")
        each_pos.display_position()
        print("====================================="+"\n")
        print("=====================================")
        l.append(each_pos)

# l2 = []
# y = l[0].generate_moves_opening(color="b")

# for count,_pos in enumerate(y):

#         each_pos = Board(_pos)
#         each_pos.depth = 2
#         print("==================",count,"===================")
#         print("====================================="+"\n")
#         each_pos.display_position()
#         print("====================================="+"\n")
#         print("=====================================")
#         l2.append(each_pos)
