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

# pos = {
#         "a0" : None,
#         "a3" : None,
#         "a6" : "w",
#         "b1" : None,
#         "b3" : None,
#         "b5" : "b",
#         "c2" : None,
#         "c3" : None,
#         "c4" : "b",
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
#         "g6" : "w",
# }


# pos = {
#         "a0" : None,
#         "a3" : "w",
#         "a6" : None,
#         "b1" : None,
#         "b3" : "w",
#         "b5" : None,
#         "c2" : None,
#         "c3" : "w",
#         "c4" : None,
#         "d4" : None,
#         "d5" : None,
#         "d6" : None,
#         "e2" : "w",
#         "e3" : "w",
#         "e4" : None,
#         "f1" : "b",
#         "f3" : "b",
#         "f5" : None,
#         "g0" : "b",
#         "g3" : "b",
#         "g6" : "b", 
# }

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


def minimax_opening(pos):
        input_position = Board(pos)
        print("*******************************************************")
        print("*                   Input Position                    *")
        print("*******************************************************")
        print("\n")
        input_position.display_position()
        print("*******************************************************")
        print("*******************************************************")

        color="w"
        root_position = input_position
        root_position.depth=0

        # positions_list = root_position.generate_moves_opening(color=color)
        # root_position.child_positions = [Board(position) for position in positions_list ]
        # print("No: of Positions = ",len(root_position.child_positions))



        # for count,child in enumerate(root_position.child_positions):
        #         # print("                               ", count)
        #         # child.display_position()
        #         # print("")
        #         # print("=====================================")
        #         # print("=====================================")
        #         child.parent = root_position

        
        level =0
        not_visited = [root_position]
        depth =3
        color=""

        level_wise = { depth:[]}

        while level < depth:
                level_wise[level] = []
                for parent in not_visited:
                        if parent.depth == level:
                                level_wise[level].append(parent)
                                if parent.depth % 2 ==0:
                                        color = "w"
                                else:
                                        color="b"
                                positions_list = parent.generate_moves_opening(color=color)
                                for position in positions_list:
                                        pos = Board(position)
                                        pos.parent = parent
                                        pos.depth = parent.depth+1
                                        if pos.depth ==depth:
                                                pos.static_estimate = pos.static_estimation_opening()
                                                level_wise[depth].append(pos)
                                        parent.child_positions.append(pos)
                                        not_visited.append(pos) 
                level +=1
        
        x= 1


        # for level in range(depth-1,0,-1):
        #         for node in level_wise[level]:
                        
        


        # postions_estimate = [board_position.static_estimation_opening(position) for position in positions_list]
        # print(postions_estimate)

        # board_position.child_positions = n_positions
        # not_visited = n_positions 
        # depth = 5

        # level=1
        # while not_visited != []:
        #         new_postions = []
        #         if color == "b":
        #                 color="w"
        #         else:
        #                 color="b"
        #         for position in not_visited:
        #                 new_postions = board_position.generate_moves_opening(color=color)
        #         level +=1
        

        

        



minimax_opening(pos)