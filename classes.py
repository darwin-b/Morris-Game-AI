
class Board:
    def __init__(self,board_postion=None):
        if board_postion is not None:
            self.board_position = board_postion
        else:
            self.board_position = {
                "a0" : None,
                "a3" : None,
                "a6" : None,
                "b1" : None,
                "b3" : None,
                "b5" : None,
                "c2" : None,
                "c3" : None,
                "c4" : None,
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
                "g6" : None,
            }


        # Input: board position (self)
        # output: list of board positions
        def generate_add(self):
            l=[]
            for location in self.board_position:
                if self.board_postion[location] is None:
                    new_position = self.board_postion[location]
                    new_position[location] = "w"
                
                if closemill(self,location,new_position):
                    generate_remove(new_position,l)
                else:
                    l.append(new_position)
        
        
        def generate_moves_opening(self):
            pass
        
        def generate_moves_mid_endgame(self):
            pass

        def generate_move(self):
            pass

        def generate_remove(self):
            pass

        def generate_hopping(self):
            pass

        def neighbours(self):
            pass



        # input : location of piece placed (key in dictionary) and board_position (dictionary)
        # output: boolean --> true if the move closes a mill
        def closemill(self,location,board):
            color = board[location]
            mills = {
                        "a0" : [["a3","a6"], ["b1","c2"]],
                        "a3" : [["a0","a6"], ["b3","c3"]],
                        "a6" : [["a3","a0"], ["d6","g6"]],
                        "b1" : [["a0","c2"], ["b3","b5"]],
                        "b3" : [["a3","c3"], ["b1","b5"]],
                        "b5" : [["b1","b3"], ["d5","f5"]],
                        "c2" : [["a0","b1"], ["c3","c4"]],
                        "c3" : [["a3","b3"], ["c2","c4"]],
                        "c4" : [["c2","c3"], ["d4","e4"]],
                        "d4" : [["c4","e4"], ["d5","d6"]],
                        "d5" : [["b5","f5"], ["d4","d6"]],
                        "d6" : [["a6","g6"], ["d5","d4"]],
                        "e2" : [["e3","e4"]],
                        "e3" : [["e2","e4"], ["f3","g3"]],
                        "e4" : [["e2","e3"]],
                        "f1" : [["f3","f5"]],
                        "f3" : [["e3","g3"], ["f1","f5"]],
                        "f5" : [["b5","d5"], ["f1","f3"]],
                        "g0" : [["g3","g6"]],
                        "g3" : [["e3","f3"], ["g0","g6"]],
                        "g6" : [["a6","d6"], ["g0","g3"]],
            }

            for mill in mills[location]:
                # mill_closed = True
                # for pos in mill:
                #     if board[pos] != color:
                #         mill_closed = False
                #         break
                # if mill_closed == True:
                #     return True
                if board[mill[0]] == board[mill[1]] == board[location]:
                    return True

            return False



        # input: location on the board "g0"
        # output: list of neighbouring locations ["d6","g3"]
        def neighbors(self,location):
            graph = {
                        "a0" : ["a3","g0","b1"],
                        "a3" : ["a0","a6","b3"],
                        "a6" : ["a3","d6"],
                        "b1" : ["a0","b3","c2"],
                        "b3" : ["a3","b1","b5","c3"],
                        "b5" : ["b3","d5"],
                        "c2" : ["b1","c3","e2"],
                        "c3" : ["b3","c2","c4"],
                        "c4" : ["c3","d4"],
                        "d4" : ["c4","d5","e4"],
                        "d5" : ["b5","d4","d6","f5"],
                        "d6" : ["a6","d5","g6"],
                        "e2" : ["c2","e3"],
                        "e3" : ["e2","e4","f3"],
                        "e4" : ["d4","e3"],
                        "f1" : ["b1","f3","f5"],
                        "f3" : ["e3","f1","f5"],
                        "f5" : ["d5","f3"],
                        "g0" : ["a0","g3"],
                        "g3" : ["f3","g0","g6"],
                        "g6" : ["d6","g3"]
                    }

            return graph[location]

        def static_estimation(self):
            pass


