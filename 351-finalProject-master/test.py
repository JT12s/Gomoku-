from board import Board
from player import *

HEIGHT = 15
WIDTH = 15
board = [[[] for y in range(HEIGHT)] for x in range(WIDTH)]
for i in range(0, HEIGHT):
    for j in range(0, WIDTH):
        board[i][j] = 0  # fill 0 in it


# test
class Game:

    def __init__(self, startBoard,player1,player2):
        self.startBoard = startBoard
        self.player1 = player1
        self.player2 = player2


    def simulateLocalGame(self):

        board = Board(orig=self.startBoard)
        isPlayer1 = True
        #board.printBoard()
        hand = int(input('Please select your hand, 1 for first hand, 2 for second hand: '))
        if hand == 1:
            isPlayer1 = False
            board.printBoard()
        n = 0
        while(True):
            #finds the move to make
            if isPlayer1:
                if n == 0:
                    board.makeMove('H',8)


                else:
                    move = self.player1.findMove(board)
                    board.makeMove(move[0],move[1])
                    # board.history.append(move)
                    print("AI move to " + str(move[0]) + " " + str(move[1]))
            else:
                result = input('Move you want to make: ')
                if len(result) == 2 :
                    tuple = (result[0], result[1])
                elif len(result) == 3:
                    tuple = (result[0], result[1] + result[2])
                else: print("Invalid move")
                board.makeMove(tuple[0], int(tuple[1]))


                #if isPlayer1:
                #    move = self.player1.findMove(board)
                #    board.makeMove(move)
                #else:
                #    result = input('Move you want to make: ')
                #    tuple = (result[0], result[1])
                #    board.makeMove(tuple[0], int(tuple[1]))
            n = n + 1


            board.printBoard()

            isOver = board.isTerminal()
            if isOver == 0:
                print("It is a draw!")
                break
            elif isOver == 1:
                print("I am sorry, but our AI win!")
                break
            elif isOver == 2:
                print("Wow! You beat our AI, you must have secret talent about Gomoku!")
                break

            else:
                isPlayer1 = not isPlayer1

    # def printBoard(WIDTH, HEIGHT):
    #     print("")
    #     print("+" + "---+" * WIDTH)
    #     for rowNum in range(HEIGHT - 1, -1, -1):
    #         row = "|"
    #         for colNum in range(WIDTH):
    #             if len(board[colNum]) > rowNum:
    #                 row += " " + ('X' if board[colNum][rowNum] else 'O') + " |"
    #             else:
    #                 row += "   |"
    #         print(row)
    #         print("+" + "---+" * WIDTH)




if __name__ == "__main__":
    b = Board()
    print('Welcome to Group 7 final project demo!')
    print("For put in piece, please type Capital Letter and number as Row and Colomn")
    print("For example, if you want make move G - 8, please Type G8 as input, if you want G - 10, type G10")
    g = Game(b, PlayerAB(3,True),None)
    g.simulateLocalGame()


