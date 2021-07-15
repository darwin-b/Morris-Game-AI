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


        # levels ={}

        # for lvl in range(0,depth+1):
        #     levels[lvl] = []
        
        # levels[0].append(root_position)
        
        # color="w"
        # # first_move_color=color

        # for lvl in levels:
        #     temp = []
        #     _positions = []

        #     if lvl %2 ==0:
        #         color ="w"
        #     else:
        #         color ="b"

        #     if lvl < depth:
        #         for each_board in levels[lvl]:
        #             _positions = each_board.generate_moves_opening(color=color)
        #             for _pos in _positions:
        #                 child = Board(_pos)
        #                 child.parent = each_board
        #                 child.depth = each_board.depth+1
        #                 each_board.child_positions.append(child)
        #                 levels[lvl+1].append(child)
            
        # calculating static estimate function at leaf nodes [given depth]
        # if first_move_color =="w":
        # for board in levels[depth] :
        #     board.static_estimate = board.static_estimation_opening()

        # s=[root_position]
        # # dfs(root_position,s)
        # x=dfs2(root_position,1)
        depth=3
        max_min(root_position,-1000000,1000000,depth)
        
        print("No of nodes: ",dfs2(root_position,1))
        x=1
        # root_position.white_move.display_position()
        # print("Static estimate : ",root_position.static_estimate )

            

        print("**********************************************************************************")
        print("*                                  computer plays                                *")
        print("**********************************************************************************")
        print("**********************************************************************************"+"\n\n")
        root_position.white_move.display_position()
        print("Static Estimate : ",root_position.static_estimate,"\n")
        print("**********************************************************************************")
        print("**********************************************************************************")
        return root_position.white_move

        
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


s= set()
def dfs(root,s=[]):
    while s!= []:
        node=s.pop()
        if node.child_positions ==[]:
            print("==========================\n")
            node.display_position()
            print("==========================\n")
        
        for child in node.child_positions:
            s.append(child)
        

# def dfs2(node,c):
#     if node.child_positions ==[]:
#         print("============== ",c," Leaf Node================\n")
#         node.display_position()
#         print("================================================\n")
#         return c
#     else:
#         print("=========== ",c," Node===============\n")
#         node.display_position()
#         print("=======================================\n")
#         for child in node.child_positions:
#             c=dfs2(child,c+1)
#         return c



def max_min(node,a,b,depth):
    if node.depth == depth:
        node.static_estimate =  node.static_estimation_opening()
        return node.static_estimate
    else:
        v = float('-inf')

        child_positions = node.generate_moves_opening(color="w")
        for c in child_positions:
            child = Board(c)
            child.parent = node

            if node.depth is None:
                node.depth=0
            child.depth = node.depth+1
            node.child_positions.append(child)

        for child in node.child_positions:

            temp = min_max(child,a,b,depth)
            if v<temp :
                v=temp
                node.white_move = child
                node.static_estimate = v            
            if v>=a:
                node.static_estimate = v
                node.white_move = child
                return v
            else:
                a = max(v,a)
        node.static_estimate = v
        return v



def min_max(node,a,b,depth):
    if node.depth == depth:
        node.static_estimate =  node.static_estimation_opening()
        return node.static_estimate
    else:
        v = float('inf')

        child_positions = node.generate_moves_opening(color="b")
        for c in child_positions:
            child = Board(c)
            child.parent = node

            if node.depth is None:
                node.depth=0
            child.depth = node.depth+1
            node.child_positions.append(child)


        for child in node.child_positions:

            temp = max_min(child,a,b,depth)
            if v>temp :
                v=temp
                node.black_move = child
                node.static_estimate = v  
            if v<=a:
                node.static_estimate = v
                node.black_move = child
                return v
            else:
                b = min(v,b)
        node.static_estimate = v
        return v    


def dfs2(node,c):
    if node.child_positions ==[]:
        # print("============== ",c," Leaf Node================\n")
        # node.display_position()
        # print("================================================\n")
        return c
    else:
        # print("=========== ",c," Node===============\n")
        # node.display_position()
        # print("=======================================\n")
        for child in node.child_positions:
            c=dfs2(child,c+1)
        return c



        # for level in range(depth-1,-1,-1):
        #     nodes = levels[level]

        #     for node in nodes:
        #         # Max strategy
        #         if level % 2 ==0:
        #             node.static_estimate = node.child_positions[0].static_estimate
        #             node.white_move = node.child_positions[0]

        #             for child in node.child_positions:
        #                 if node.static_estimate < child.static_estimate:
        #                     node.static_estimate = child.static_estimate
        #                     node.white_move = child

        #         # Min strategy 
        #         else:
        #             node.static_estimate = node.child_positions[0].static_estimate
        #             node.black_move = node.child_positions[0]

        #             for child in node.child_positions:
        #                 if node.static_estimate > child.static_estimate:
        #                     node.static_estimate = child.static_estimate
        #                     node.black_move = child

        # for level in range(depth-1,0,-1):
        #     nodes = levels[level]

        #     first_node = True
        #     for node in nodes:
        #         # Max strategy
        #         if level % 2 ==0:
        #             node.static_estimate = node.child_positions[0].static_estimate
        #             node.white_move = node.child_positions[0]

        #             flag_prune =False
        #             for child in node.child_positions:
        #                 if node.static_estimate >= node.parent.static_estimate:
        #                     flag_prune=True
        #                     break
        #                 else:
        #                     if node.static_estimate < child.static_estimate:
        #                         node.static_estimate = child.static_estimate
        #                         node.white_move = child

        #             if first_node:
        #                 node.parent.static_estimate = node.static_estimate
        #             else:
        #                 node.static_estimate=node.parent.static_estimate  
        #         # Min strategy 
        #         else:
        #             node.static_estimate = node.child_positions[0].static_estimate
        #             node.black_move = node.child_positions[0]

        #             for child in node.child_positions:
        #                 if node.static_estimate <= node.parent.static_estimate:
        #                     break
        #                 else:
        #                     if node.static_estimate > child.static_estimate:
        #                         node.static_estimate = child.static_estimate
        #                         node.black_move = child

                    
        #             if first_node:
        #                 node.parent.static_estimate = node.static_estimate
        #             else:
        #                 node.static_estimate=node.parent.static_estimate
                
        #         first_node = False