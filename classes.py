
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

    # Ignore this method
    # test function to check pass by val and reference
    def test(self):
        print(self.board_position)
        # pos = self.board_position.copy()
        # pos["a3"]=None
        # print("=========new postion===============")
        # print(pos)
        # print("===========self.board position===========")
        # print(self.board_position)



###################################################################################
# Input: board position (self)
# output: list of board positions
###################################################################################
    def generate_add(self,board=None,color=None):
        positions_list=[]
        if color is None:
            color ="w"
            
        if board is None:
            print("Board position Not entered"
                 +" Return empty list or copy board configuration")
            board = self.board_position
            # return []

        print("")
        print("")
        for location in board:
            if board[location] is None:
                new_position = board.copy()
                new_position[location] = color
            else:
                continue

            print("location : "+location)
            if self.closemill(location,new_position):
                self.generate_remove(new_position,positions_list)        
            else:
                self.display_position(new_position)
                print("=======================")
                print("=======================")
                print("")
                positions_list.append(new_position)

        return positions_list


        
###################################################################################
# Input: board position (self)
# Output: list of board positions (positions_list)
###################################################################################
    def generate_moves_opening(self,color=None):
        if color is None:
            color = "w"
        return self.generate_add(color=color)
        pass


###################################################################################
# Input: board position (self)
# Output: list of board positions (positions_list)
###################################################################################
    def generate_moves_mid_endgame(self,color=None):
        if color is None:
            color="w"

        board = self.board_position
        count_color_pieces = 0

        for location in board:
            if board[location] == color:
                count_color_pieces += 1
        
        if count_color_pieces == 3:
            return self.generate_hopping(color)
        else:
            return self.generate_move(color)
        
        pass


###################################################################################
# input : location of piece placed (key in dictionary) and board_position (dictionary)
# output: boolean --> true if the move closes a mill
###################################################################################
    def closemill(self,location,board=None):
        if board is None:
            board = self.board_position

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

        # print(board)
        # print("=====================")

        for mill in mills[location]:
            # print(mill[0],mill[1],location)
            # print(board[mill[0]], board[mill[1]], board[location])
            if (board[mill[0]] == board[mill[1]] == board[location]) and board[location] is not None:
                # print("Mill True")
                return True

        return False



###################################################################################
# Input: board position (self)
# Output: list of board positions (positions_list)
###################################################################################
    def generate_move(self,color=None):
        positions_list = []
        board = self.board_position
        if color is None:
            color ="w"

        for location in board:
            if board[location] == color:
                neighbors = self.neighbors(location)
                for neighbor in neighbors:
                    if board[neighbor] == None:
                        new_position = board.copy()
                        new_position[location]  = None
                        new_position[neighbor] = color

                        print("Moving : "+location+ " to "+neighbor)
                        if self.closemill(neighbor,new_position):
                            self.generate_remove(new_position,positions_list)
                        else:
                            self.display_position(new_position)
                            print("=======================")
                            print("=======================")
                            print("")
                            positions_list.append(new_position)

        return positions_list
        pass



###################################################################################
# Input: board_position and list of positions (positions_list))
# Output: list of positions added to L by removing black pieces
# Q: how de we flip colors without taking color parameter ?
###################################################################################
    def generate_remove(self,board,positions_list,color=None):
        count_positions_added=0
        if color is None:
            color ="b"

        for location in board:
            if board[location] == color:
                if not self.closemill(location,board):
                    new_position = board.copy()
                    new_position[location] = None

                    print("location removed:  "+location)
                    self.display_position(new_position)
                    print("=======================")
                    print("=======================")
                    print("")
                    positions_list.append(new_position)
                    count_positions_added +=1

        if count_positions_added == 0:

            print("location removed:  "+"none as all black in mill positions")
            self.display_position(board)
            print("=======================")
            print("=======================")
            print()
            positions_list.append(board)

        return positions_list



###################################################################################        
# Input: board postion (self)
# Output: list of board positions (positions_list)
###################################################################################
    def generate_hopping(self,color=None):
        positions_list = []
        board = self.board_position
        if color is None:
            color ="w"

        for location1 in board:
            if board[location1] == color:
                for location2 in board:
                    if board[location2] is None:
                        new_position = board.copy()
                        new_position[location1] = None
                        new_position[location2] = color
                        
                        print("hopping : "+location1+ " to "+location2)
                        if self.closemill(location2,new_position):
                            self.generate_remove(new_position,positions_list)
                        else:
                            self.display_position(new_position)
                            print("=======================")
                            print("=======================")
                            print("")                           
                            positions_list.append(new_position)

        return positions_list

        pass


###################################################################################
# input: location on the board "g0"
# output: list of neighbouring locations ["d6","g3"]
###################################################################################
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



###################################################################################
# Input:
# Output:
###################################################################################
    def display_position(self,board=None):
        if board is None:
            board = self.board_position.copy()

        for location in board:
            if board[location] is None:
                board[location]=" "
            else:
                board[location]=board[location].upper()
        
        r=6
        c=6

        for i in range(r,-1,-1):
            display =""
            for j in range(0,7):
                location = chr(j+97)+str(i)
                if location in board:
                    display+=" "+board[location]+" "
                else:
                    display+="---"
            print(display)
            
            if i==6:
                print(" | "+"   "+"   "+" | "+"   "+"   "+" | ")
                print(" | "+"   "+"   "+" | "+"   "+"   "+" | ")
            elif i==5:
                print(" | "+" | "+"   "+" | "+"   "+" | "+" | ")
                print(" | "+" | "+"   "+" | "+"   "+" | "+" | ")
            elif i ==4:
                print(" | "+" | "+" | "+"   "+" | "+" | "+" | ")
                print(" | "+" | "+" | "+"   "+" | "+" | "+" | ")
            elif i==3:
                print(" | "+" | "+" | "+"   "+" | "+" | "+" | ")
                print(" | "+" | "+" | "+"   "+" | "+" | "+" | ")
            elif i==2:
                print(" | "+" | "+"   "+" | "+"   "+" | "+" | ")
                print(" | "+" | "+"   "+" | "+"   "+" | "+" | ")
            elif i==1:
                print(" | "+"   "+"   "+" | "+"   "+"   "+" | ")
                print(" | "+"   "+"   "+" | "+"   "+"   "+" | ")
            else:
                print("")
                print("")
                
       

###################################################################################
# Input:
# Output:
###################################################################################
    def static_estimation(self):
        pass


