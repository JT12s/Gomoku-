#Group number 7
#Leiteng Huang, Chang Liu, Jie Tang
#Final Project
#Last edit on: 11/11/2018

##################################   Board Class   ##################################
# The Board class is the data structure that holds the Gomoku and the game operations

# The Gomoku board is 15 * 15 cells tall and wide

# The underlying data structure is a 2-d list
# The first dimension is the row; the second dimension is the column;
# Note: We init all cells to None at the beginning, and update after every step.

# Every cell in the above list contains either a 0 or 1 is represented by 0 tiles, and Player
# 2 is represented by 1 titles.
#####################################################################################
import copy #use copy to copy 2d array

class Board(object):

    HEIGHT = 15 # our board is a 15 * 15 cells baord
    WIDTH = 15

    ########################   Constructor   ###############################
    #
    #
    #  No arguments --> Creates a brand new empty board
    #
    #  orig         --> If you pass an existing board as the orig argument,
    #                   this will create a copy of that board
    #
    ########################################################################
    def __init__(self, orig = None):

        # copy
        if(orig):
            self.board = copy.deepcopy(orig.board)
            self.numMoves = orig.numMoves
            self.lastMove = orig.lastMove
            # self.history = orig.history
            return

        # create new board
        else:
            self.board = [[[] for y in range(self.HEIGHT)] for x in range(self.WIDTH)]
            for i in range (0, self.HEIGHT):
                for j in range (0, self.WIDTH):
                    self.board[i][j] = None  # fill none in it
            self.numMoves = 0
            self.lastMove = None
            # self.history = []
            return

    ########################################################################
    #                           Mutations
    ########################################################################

    # Puts a pirce in the appropriate column and checks to see if it was a winning move
    # Pieces are either 2 or 1; automatically decided
    # NOTE: does NOT check if the move is valid
    def makeMove(self, row, column):
        rownum = {'A':0, 'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,'L':11,'M':12,'N':13,'O':14}
        if type(row) is not int:
            rowN = rownum[row]
        else:
            rowN = row-1
        columnN = column - 1
        #update board data
        temp = self.numMoves % 2
        piece = temp + 1
        self.lastMove = [piece, columnN, rowN] #lastmove still base on 2-d array index
        self.numMoves += 1
        self.board[rowN][columnN] = piece  #makemove base on x-y coordinate axis
        # self.history.append((rowN, columnN))



    ########################################################################
    #                           Observations
    ########################################################################

    # Generates a list of the Valid children of the board
    # A child is of the form (move_to_make_child, child_object)
    def children(self):
        children = []
        tempCoord = []
        for i in range(0, 15):
            for j in range(0, 15):
                if self.board[i][j] is not None:
                    # print("last Move is: " + str(self.lastMove[2]+1) + ", " + str(self.lastMove[1]+1))
                    x = i-1
                    y = j-1
                    if x>=0 and x<=14:
                        if y>=0 and y<=14:
                            for t in range(0,3):
                                for h in range(0,3):
                                    if x+t>=0 and x+t <=14:
                                        if y+h>=0 and y+h <=14:
                                            if self.board[x+t][y+h] is None:
                                                coord = (x+t+1, y+h+1)
                                                if coord not in tempCoord:
                                                    tempCoord.append(coord)
                                                    child = Board(self)
                                                    child.makeMove(coord[0],coord[1])
                                                    children.append((coord,child))
        # print(tempCoord)
        return children















    # Returns:
    #  -1 if game is not over
    #   0 if the game is a draw
    #   1 if player 1 wins
    #   2 if player 2 wins
    def isTerminal(self):
        piece = self.lastMove[0]
        column = self.lastMove[1]
        row = self.lastMove[2]
        previous = piece
        current = 3
        #check row /horizontal
        rowacc = 1
        for i in range(1, 5):
            if column - i >= 0:
                current = self.board[row][column - i]


            if current == previous:
                rowacc += 1
                if current == 1 and rowacc == 5:
                    return 1
                if current == 2 and rowacc == 5:
                    return 2
            else:
                break

        for i in range(1, 5):
            if column +i <= 14:
                current = self.board[row][column + i]
            if current  == previous:
                rowacc += 1
                if current == 1 and rowacc == 5:
                    return 1
                if current == 2 and rowacc == 5:
                    return 2
            else:
                break


        #check column/vertical
        colacc = 1
        for i in range(1, 5):
            current = self.board[row - i][column]

            if current == previous:
                colacc += 1

                if current == 1 and colacc == 5:
                    return 1
                if current == 2 and colacc == 5:
                    return 2

            else:
                break

        for i in range(1, 5):
            if row + i <= 14:
                current = self.board[row + i][column]

            if current == previous:
                colacc += 1

                if current == 1 and colacc == 5:
                    return 1
                if current == 2 and colacc == 5:
                    return 2
            else:
                break
        #check diagonal
        #top left to bot right

        diaacc1 = 1

        for i in range(1,5):
            if row - i >=0 and column - i >=0:
                current = self.board[row - i][column - i]

            if current == previous:
                diaacc1 += 1

                if current == 1 and diaacc1 == 5:
                    return 1
                if current ==  2 and diaacc1 == 5:
                    return 2

            else:
                break

        for i in range(1,5):
            if row+i <= 14 and column + i <= 14:
                current = self.board[row + i][column + i]

            if current == previous:
                diaacc1 += 1

                if current == 1 and diaacc1 == 5:
                    return 1
                if current ==  2 and diaacc1 == 5:
                    return 2

            else:
                break

        # top right to bot left
        diaacc2 = 1

        for i in range(1, 5):
            if row - i >= 0 and column + i <= 14:
                current = self.board[row - i][column + i]

            if current == previous:
                diaacc2 += 1

                if current == 1 and diaacc2 == 5:
                    return 1
                if current == 2 and diaacc2 == 5:
                    return 2

            else:
                break

        for i in range(1, 5):
            if row+i <=14 and column-i >= 0:
                current = self.board[row + i][column - i]

            if current == previous:
                diaacc2 += 1

                if current == 1 and diaacc2 == 5:
                    return 1
                if current == 2 and diaacc2 == 5:
                    return 2

            else:
                break



        if self.isFull() is True:
            return 0

        return -1





    ########################################################################
    #                           Utilities
    ########################################################################

    # Return true iff the game is full
    def isFull(self):
        return self.numMoves == 225

    # Prints out a visual representation of the board
    # X's are 1's and 0's are 0s
    def printBoard(self):
        #chary = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O']
        chary = ['A1', 'B2', 'C3', 'D4', 'E5', 'F6', 'G7', 'H8', 'I9', 'J10', 'K11', 'L12', 'M13', 'N14', 'O15']
        print("")
        print("+" + "---+" * self.WIDTH)

        #print for origin board
        for i in range(0, self.HEIGHT ):
            row = "|"
            for cell in self.board[i]:
                if cell is not None:
                    if cell == 1:
                        row += " " + "X" + " |"
                    if cell == 2:
                        row += " " + "O" + " |"
                else:
                    row += " " + " " + " |"
            row += " " + chary[i]
            print(row)
            print("+" + "---+" * self.WIDTH)

        lastline = "  1   2   3   4   5   6   7   8   9   10  11  12  13  14  15"
        print(lastline)