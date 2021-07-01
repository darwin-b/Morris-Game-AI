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
        "f5" : "b",
        "g0" : "b",
        "g3" : "b",
        "g6" : "b", 
}

pos1 = {
        "a0" : "W23",
        "a3" : "w",
        "a6" : None,
        "b1" : None,
        "b3" : "w",
        "b5" : None,
        "c2" : None,
        "c3" : "w",
        "c4" : "b",
        "d4" : "b",
        "d5" : None,
        "d6" : None,
        "e2" : "w",
        "e3" : "w",
        "e4" : None,
        "f1" : "b",
        "f3" : "b",
        "f5" : None,
        "g0" : None,
        "g3" : "b",
        "g6" : None, 
}


b = Board(pos)

# b.test()

b.generate_add()
# print(b.self.board)
# print(b.test())
# print(b.closemill("a0"))
