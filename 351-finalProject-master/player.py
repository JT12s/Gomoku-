#Group number 7
#Leiteng Huang, Chang Liu, Jie Tang
#Final Project
#Last edit on: 11/26/2018


   #       0
   #       0
   #       0
   # 0000000000000            GOD BLESS NO BUG!
   #       0
   #       0
   #       0
   #       0
   #       0
   #       0
   #       0

import math
import copy

class Player:

    def __init__(self, depthLimit, isPlayerOne):

        self.isPlayerOne = isPlayerOne
        self.depthLimit = depthLimit


    ############################################### Heuristic Idea #####################################################
    #   assume we are current process piece 1
    #   This is how we grade our move
    #   None 1 None  -> 10
    #   None 1 2  or 2 1 None -> 1
    #   2 1 2 -> 0
    #
    #   None 1 1 None -> 100
    #   None 1 1 1 None -> 1000
    #   None 1 1 1 1 None -> 10000
    #   None 1 1 1 1 1 None -> 1000000
    #
    #   None 1 1 2 -> 10
    #   None 1 1 1 2 -> 100
    #   None 1 1 1 1 2 -> 1000
    #   None 1 1 1 1 1 2 -> 1000000
    #
    #   Other:
    #   2 1 1 2
    #   2 1 1 1 2    ---> 0
    #   2 1 1 1 1 2
    #
    #   But:
    #   2 1 1 1 1 1 2  ---> 1000000
    #



    # for now we considered this moves
    # there are powerful moves we consider
    # we would like to implement but no enought time
    #    1
    #  1 1 1
    #    1
    #
    # 1 1 1
    #     1
    #     1
    #
    # 1   1
    #   1
    # 1   1
    #
    # 1       1
    #   1   1
    #     1
    #
    def heuristic(self, board):

        board2 = copy.deepcopy(board.board)

        P1point = 0 #total player 1 points
        P2point = 0 #total plyaer 2 points

        ##################################################### Check ###################################################
        #lets check every row first
            #init counters
        current = (-1,-1)
        count = 1
        close = 0

        lastMove = (board.lastMove[2], board.lastMove[1])
        start = (lastMove[0]-3, lastMove[1]-3)
        for a in range(0,15):
            for b in range(0,15):
                if board2[a][b] is not None:
                    current = board2[a][b]
                    #print("inner test of count " + count)
                    # We check to the LEFT and RIGHT
                    # print("To the left, we are checking", a,b)
                    for i in range(1, 5):  # we want start by center, and move one more farther each time
                        # Left <- Current
                        if b-i >= 0: # avoid index out of range
                            next = board2[a][b-i]  # the new piece
                            if next == current: # if the new one is same as center one!
                                # print("we added: ", a, b-i)
                                # print("i is:", i)
                                count += 1 # count increase by 1
                            if next != current and next is not None:
                                close += 1 # if one side has different piece, close increase by 1
                                # print('closed')
                                break # stop this side checking
                            if next != current and next is None: # if one side has no more same piece as center
                                count += 1 # one more for next move
                                break
                    current = board2[a][b]
                    # print("Left check ended, to the right, we are checking: ", a, b)
                    for j in range(1, 5):  # same as above just the direction different
                        # Current -> Right
                        if b+j <= 14: # avoid index out of range
                            next = board2[a][b+j]
                            if next == current:
                                count += 1
                                # print("We added: ", a, b+j)
                            if next != current  and next is not None:
                                close += 1

                                # print('closed')
                                break
                            if next != current and next is None:
                                count += 1
                                break
                    finalPoint = self.point(count, close) # a helper function, to decided how many point we get from this
                    if current == 1: # if we have same 1 connected
                        P1point += finalPoint
                    elif current == 2: # if we have same 2 connected
                        P2point += finalPoint
                    # reset counters
                    # print(count)
                    count = 1
                    close = 0

                    # print('to top')
                    # We check current to the TOP and BOTTOM
                    current = board2[a][b]
                    for k in range(1, 5):
                        # Top <- Current
                        if a-k >= 0: # avoid index out of range
                            next = board2[a-k][b]
                            if next == current:
                                count += 1
                                # print("We added: ", a-k, b)
                            if next != current and next is not None:
                                close += 1
                                # print('closed')
                                break
                            if next != current and next is None:
                                count += 1
                                break
                    # Current -> Bottom
                    current = board2[a][b]

                    # print('to bottom')
                    for m in range(1, 5):
                        if a+m <= 14: # avoid index out of range
                            next = board2[a+m][b]
                            if next == current:
                                count += 1
                                # print("We added: ", a+m, b)
                            if next != current and next is not None:
                                close += 1
                                # print('closed')
                                break
                            if next != current and next is None:
                                count += 1
                                break
                    finalPoint = self.point(count, close)
                    if current == 1:
                        P1point += finalPoint
                    elif current == 2:
                        P2point += finalPoint
                    # reset counters
                    # print(count)
                    count = 1
                    close = 0

                    # We check current from top left to bottom right
                    # Current to top left
                    # print('to top left')
                    current = board2[a][b]
                    for n in range(1,5):
                        if a-n >=0 and b-n>=0: # avoid index out of range
                            next = board2[a-n][b-n]
                            if next == current:
                                count += 1
                                # print("We added: ", a-n, b-n)
                            if next != current and next is not None:
                                close += 1
                                # print('closed')
                                break
                            if next != current and next is None:
                                count += 1
                                break
                    # Current to bottom right

                    # print('to bottom right')
                    current = board2[a][b]
                    for o in range(1,5):
                        if a+o <=14 and b+o <=14: # avoid index out of range
                            next = board2[a+o][b+o]
                            if next == current:
                                count += 1
                                # print("We added: ", a+o, b+o)
                            if next != current and next is not None:
                                close += 1
                                # print('closed')
                                break
                            if next != current and next is None:
                                count += 1
                                break
                    finalPoint = self.point(count, close)
                    if current == 1:
                        P1point += finalPoint
                    elif current == 2:
                        P2point += finalPoint
                    # reset counters
                    # print(count)
                    count = 1
                    close = 0

                    #We check current from bottom left to top right
                    # Current to bottom left
                    # print('to bottom left')
                    current = board2[a][b]
                    for p in range(1, 5):
                        if a + p <=14  and b -p >=0:  # avoid index out of range
                            next = board2[a + p][b -p]
                            if next == current:
                                count += 1
                                # print("We added: ", a+p, b -p)
                            if next != current and next is not None:
                                # print('closed')
                                close += 1
                                break
                            if next != current and next is None:
                                count += 1
                                break
                    # Current to top right
                    # print('to top right')
                    current = board2[a][b]
                    for q in range(1, 5):
                        if a - q >=0 and  b+q <=14:  # avoid index out of range
                            next = board2[a - q][b +q]
                            if next == current:
                                count += 1
                                # print("We added: ", a-q, b+q)
                            if next != current and next is not None:
                                close += 1
                                # print('closed')
                                break
                            if next != current and next is None:
                                count += 1
                                break
                    finalPoint = self.point(count, close)
                    if current == 1:
                        P1point += finalPoint
                    elif current == 2:
                        P2point += finalPoint
                    # reset counters
                    # print(count)
                    count = 1
                    close = 0
        return P1point-P2point



    def point(self, count, close):
        if close == 0: # two side has no block
            if count == 1:
                return 10
            if count == 2:
                return 100
            if count == 3:
                return 1000
            if count == 4:
                return 100000
            if count >= 5:
                # print("Do we reach here?")
                return 1000000
        elif close == 1: # one side has block
            if count == 1:
                return 1
            if count == 2:
                return 10
            if count == 3:
                return 100
            if count == 4:
                return 10000
            if count >= 5:
                return 1000000
        else:
            if count >= 5:
                return 1000000
            else:
                return  0

















# #implement AB pruning, MAY NEED CHANGE, THIS IS NOT FINAL VER.

class PlayerAB(Player):

    def __init__(self, depthLimit, isPlayerOne):
        super().__init__(depthLimit, isPlayerOne)

    def findMove(self, board):
        if self.isPlayerOne:
            optimal = self.maxV(board, self.depthLimit, -math.inf, math.inf)
        else:
            optimal = self.minV(board, self.depthLimit, -math.inf, math.inf)
        return optimal[1]

    def maxV(self, board, depthLimit, alpha, beta):
        state = board.isTerminal()
        if state == 0:
            return 0, None
        if state == 1:
            return 10, None
        if state == 2:
            return -10, None

        if depthLimit == 0:
            return self.heuristic(board), None

        bestVal = -math.inf, None
        for child in board.children():
            value = self.minV(child[1], depthLimit - 1, alpha, beta)[0]
            if value >= bestVal[0]:
                bestVal = value, child[0]
            alpha = max(alpha, value)
            if alpha > beta:
                break
        return bestVal

    def minV(self, board, depthLimit, alpha, beta):
        state = board.isTerminal()
        if state == 0:
            return 0, None
        if state == 1:
            return 10, None
        if state == 2:
            return -10, None

        if depthLimit == 0:
            return self.heuristic(board), None

        bestVal = math.inf, None
        for child in board.children():
            value = self.maxV(child[1], depthLimit - 1, alpha, beta)[0]
            if value <= bestVal[0]:
                bestVal = value, child[0]
            beta = min(beta, value)
            if alpha > beta:
                break
        return bestVal



