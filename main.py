import random
import numpy

# STEPS
#
# MAKE GRAPH OF POSSIBLE BOARDS
# PAYOFF MATRIX OF MOVE BASED OFF OF GRAPH
# Make AI reflect best moves

debug = False
matrix = False

# GRAPH CLASS

class Graph:
    class Node:

        def __init__(self, board, player, lastPlayed = -1, justPlayed = -1):
            self.board = board
            self.val = self.quantifyState()
            self.player = player
            self.lastPlayed = lastPlayed
            self.justPlayed = justPlayed

        def quantifyState(self):
            score = 0
            if self.board.checkWin(1):
                score -= 5000
            elif self.board.checkWin(2):
                score += 5000
            else:
                score = self.board.calcScore(2) - (4*self.board.calcScore(1)//5)
            return score

        def __repr__(self):
            return 'State Value: ' + str(self.val) + '\n' + str(self.board)


    def __init__(self, board, player):
        self.state = Graph.Node(board, player, )
        self.player = player
        self.payoffMatrix = [[0 for i in range(self.state.board.width)] for j in range(self.state.board.width)]


    def __repr__(self):
        stg = '    P     L     A     Y     E     R     1\n'
        s2 = 'PLAYER2'
        for i in range(len(self.payoffMatrix)):
            s = '['
            for j in range(len(self.payoffMatrix)):
                points = str(self.payoffMatrix[i][j])
                while len(points) < 6:
                    points += ' '
                s += points
            stg += s + ']  ' + s2[i] + '\n'
        return stg


    def createStateGraph(self):
        # queue (0,0,0) then find permutations of buckets that can be made, add those to queue if they aren't in graph, remove first node, go to next node and repeat process, go until nothing in queue
        queue=[]
        queue.append(self.state)
        numStates = 0
        numTurns = 2
        for i in range(numTurns, 0, -1):
            numStates += 7**i
        genStates = 0
        while(genStates < numStates):
            perms = self.getPermutaions(queue.pop(0))
            for n in perms:
                if debug:
                    print(n)
                queue.append(n)
                self.payoffMatrix[n.justPlayed][n.lastPlayed] = n.val
                genStates += 1
    
    
    def getPermutaions(self,n):
        l = []
        availables = n.board.getAvailable()
        for spot in range(len(availables)):
            if availables[spot] == True:
                #Determine Next Node's Player to Simulate
                p = 1
                if n.player == 1:
                    p = 2
                #Make Temp Board
                temp = [[0 for i in range(n.board.width)] for j in range(n.board.height)]
                for i in range(n.board.height):
                    for j in range(n.board.width):
                        temp[i][j] = n.board.getPiece(i,j)
                tempB = Board(temp) 
                tempB.playPiece(spot, n.player)
                l.append(Graph.Node(tempB, p, n.justPlayed, spot))
        return l



# BOARD CLASS

class Board:

    def __init__(self, b = None):
        if b == None:
            b = [[0 for i in range(7)] for j in range(6)]
        self.board = b
        self.height = len(self.board)
        self.width = len(self.board[0])
    
    def __repr__(self):
        stb = "  1 2 3 4 5 6 7\n"
        for i in range(self.height):
            s = '| '
            for j in range(self.width):
                if self.board[i][j] == 0:
                    s += '_ '
                elif self.board[i][j] == 1:
                    s += 'X '
                elif self.board[i][j] == 2:
                    s += 'O '
                #s += str(self.board[i][j]) + ' '
            stb += s + '|' + '\n'
        return stb

    def calcScore(self, num):
        #Score between -5000 and 5000
        score = 0

        oppNum = 1
        if num == 1:
            oppNum = 2

        #Find number of 2 connections (5 points)
        for r in range(self.height):
            for c in range(self.width-1):
                if self.board[r][c] == num and self.board[r][c+1] == num:
                    score += 5
        for r in range(self.height-1):
            for c in range(self.width):
                if self.board[r][c] == num and self.board[r+1][c] == num:
                    score += 5
        for r in range(self.height-1):
            for c in range(self.width-1):
                if self.board[r][c] == num and self.board[r+1][c+1] == num:
                    score += 5
        for r in range(self.height-1, 0, -1):
            for c in range(self.width-1):
                if self.board[r][c] == num and self.board[r-1][c+1] == num:
                    score += 5

        #Find number of 3 connections (35 points (+15 from 2 piece connections))
        for r in range(self.height):
            for c in range(self.width-2):
                if self.board[r][c] == num and self.board[r][c+1] == num and self.board[r][c+2] == num:
                    score += 35
        for r in range(self.height-2):
            for c in range(self.width):
                if self.board[r][c] == num and self.board[r+1][c] == num and self.board[r+2][c] == num:
                    score += 35
        for r in range(self.height-2):
            for c in range(self.width-2):
                if self.board[r][c] == num and self.board[r+1][c+1] == num and self.board[r+2][c+2] == num:
                    score += 35
        for r in range(self.height-1, 1, -1):
            for c in range(self.width-2):
                if self.board[r][c] == num and self.board[r-1][c+1] == num and self.board[r-2][c+2] == num:
                    score += 35
        
        #Find central checkers (5, 3, 1 points)
        for c in range(self.width):
            for r in range(self.height):
                if self.board[r][c] == num:
                    score += -2*abs(c-(self.width//2)) + 2*(self.width//2)

        #Find 2 piece blocks (30 points)
        for r in range(self.height):
            for c in range(self.width-2):
                if self.board[r][c] == oppNum and self.board[r][c+1] == oppNum and self.board[r][c+2] == num:
                    score += 30
                if self.board[r][c] == num and self.board[r][c+1] == oppNum and self.board[r][c+2] == oppNum:
                    score += 30
        for r in range(self.height-2):
            for c in range(self.width):
                if self.board[r][c] == oppNum and self.board[r+1][c] == oppNum and self.board[r+2][c] == num:
                    score += 30
                if self.board[r][c] == num and self.board[r+1][c] == oppNum and self.board[r+2][c] == oppNum:
                    score += 30
        for r in range(self.height-2):
            for c in range(self.width-2):
                if self.board[r][c] == oppNum and self.board[r+1][c+1] == oppNum and self.board[r+2][c+2] == num:
                    score += 30
                if self.board[r][c] == num and self.board[r+1][c+1] == oppNum and self.board[r+2][c+2] == oppNum:
                    score += 30
        for r in range(self.height-1, 1, -1):
            for c in range(self.width-2):
                if self.board[r][c] == oppNum and self.board[r-1][c+1] == oppNum and self.board[r-2][c+2] == num:
                    score += 30
                if self.board[r][c] == num and self.board[r-1][c+1] == oppNum and self.board[r-2][c+2] == oppNum:
                    score += 30

        #Find 3 piece blocks (120 points (+30 from 2 piece block))
        for r in range(self.height):
            for c in range(self.width-3):
                if self.board[r][c] == oppNum and self.board[r][c+1] == oppNum and self.board[r][c+2] == oppNum and self.board[r][c+3] == num:
                    score += 120
                if self.board[r][c] == num and self.board[r][c+1] == oppNum and self.board[r][c+2] == oppNum and self.board[r][c+3] == oppNum:
                    score += 120
                if self.board[r][c] == oppNum and self.board[r][c+1] == oppNum and self.board[r][c+2] == num and self.board[r][c+3] == oppNum:
                    score += 120
                if self.board[r][c] == oppNum and self.board[r][c+1] == num and self.board[r][c+2] == oppNum and self.board[r][c+3] == oppNum:
                    score += 120
        for r in range(self.height-3):
            for c in range(self.width):
                if self.board[r][c] == oppNum and self.board[r+1][c] == oppNum and self.board[r+2][c] == oppNum and self.board[r+3][c] == num:
                    score += 120
                if self.board[r][c] == num and self.board[r+1][c] == oppNum and self.board[r+2][c] == oppNum and self.board[r+3][c] == oppNum:
                    score += 120
                if self.board[r][c] == oppNum and self.board[r+1][c] == oppNum and self.board[r+2][c] == num and self.board[r+3][c] == oppNum:
                    score += 120
                if self.board[r][c] == oppNum and self.board[r+1][c] == num and self.board[r+2][c] == oppNum and self.board[r+3][c] == oppNum:
                    score += 120
        for r in range(self.height-3):
            for c in range(self.width-3):
                if self.board[r][c] == oppNum and self.board[r+1][c+1] == oppNum and self.board[r+2][c+2] == oppNum and self.board[r+3][c+3] == num:
                    score += 120
                if self.board[r][c] == num and self.board[r+1][c+1] == oppNum and self.board[r+2][c+2] == oppNum and self.board[r+3][c+3] == oppNum:
                    score += 120
                if self.board[r][c] == oppNum and self.board[r+1][c+1] == oppNum and self.board[r+2][c+2] == num and self.board[r+3][c+3] == oppNum:
                    score += 120
                if self.board[r][c] == oppNum and self.board[r+1][c+1] == num and self.board[r+2][c+2] == oppNum and self.board[r+3][c+3] == oppNum:
                    score += 120
        #for r in range(self.height-1, 2, -1):
            #for c in range(self.width-3):
        for c in range(self.width-1, 2, -1):
            for r in range(self.height-3):
                if self.board[r][c] == oppNum and self.board[r+1][c-1] == oppNum and self.board[r+2][c-2] == oppNum and self.board[r+3][c-3] == num:
                    score += 120
                if self.board[r][c] == num and self.board[r+1][c-1] == oppNum and self.board[r+2][c-2] == oppNum and self.board[r+3][c-3] == oppNum:
                    score += 120
                if self.board[r][c] == oppNum and self.board[r+1][c-1] == oppNum and self.board[r+2][c-2] == num and self.board[r+3][c-3] == oppNum:
                    score += 120
                if self.board[r][c] == oppNum and self.board[r+1][c-1] == num and self.board[r+2][c-2] == oppNum and self.board[r+3][c-3] == oppNum:
                    score += 120
        
        return score

    
    def getPiece(self, row, col):
        return self.board[row][col]

    def getAvailable(self):
        l = [True] * self.width
        for i in range(self.width):
            if self.board[0][i] != 0:
                l[i] = False
        return l

    def playPiece(self, spot, num):
        i = self.height-1
        while self.board[i][spot] != 0:
            i -= 1
        self.board[i][spot] = num

    def checkWin(self, num):
        #Check Rows
        for r in range(self.height):
            for i in range(self.width-3):
                row = True
                for j in range(i, i+4):
                    if self.board[r][j] != num:
                        row = False
                if row:
                    return True
        #Check Cols
        for c in range(self.width):
            for i in range(self.height-3):
                col = True
                for j in range(i, i+4):
                    if self.board[j][c] != num:
                        col = False
                if col:
                    return True
        #Check Right-Down
        for c in range(self.width-3):
            for r in range(self.height-3):
                diag = True
                for i in range(4):
                    if self.board[r+i][c+i] != num:
                        diag = False
                if diag:
                    return True
        #Check Left-Down
        for c in range(self.width-1, 2, -1):
            for r in range(self.height-3):
                diag = True
                for i in range(4):
                    if self.board[r+i][c-i] != num:
                        diag = False
                if diag:
                    return True
        #No Win
        return False
            



class Connect4Player:

    def __init__(self):
        self.board = Board()
        self.finished = 0
    
    def play(self):
        while self.finished == 0:
            self.takeTurn()
        if self.finished == 3:
            print('Tie Game!')
        else:
            print('Player ' + str(self.finished) + ' Wins!')

    def takeTurn(self):

        g = Graph(self.board, 1)
        g.createStateGraph()
        if debug or matrix:
            print(g)
        print(self.board)

        #Ask where to place while checking if available
        availables = self.board.getAvailable()
        empty = True
        for i in range(self.board.width):
            if availables[i] == True:
                empty = False
        if empty:
            self.finished = 3
            return
        spot = input('Select the column to place your piece (1 - ' + str(self.board.width) + '): ')
        while int(spot) < 1 or int(spot) > self.board.width or availables[int(spot)-1] == False:
            spot = input('Select the column to place your piece (1 - ' + str(self.board.width) + '): ')
        print('')
        self.board.playPiece(int(spot)-1,1)

        #Check win
        if self.board.checkWin(1):
            print(self.board)
            self.finished = 1
            return

        #Place enemy piece
        availables = self.board.getAvailable()
        empty = True
        for i in range(self.board.width):
            if availables[i] == True:
                empty = False
        if empty:
            self.finished = 3
            return
        
        spot2 = 0
        spot1 = int(spot)-1
        while availables[spot2] == False:
            spot2 += 1
        maxNum = int(g.payoffMatrix[spot2][spot1])
        for i in range(spot2, len(g.payoffMatrix[0])):
            if (int(g.payoffMatrix[i][spot1]) > maxNum) and (availables[spot2] == True):
                maxNum = int(g.payoffMatrix[i][spot1])
                spot2 = i

        self.board.playPiece(spot2, 2)

        #Check win
        if self.board.checkWin(2):
            print(self.board)
            self.finished = 2
            return




print('---- Welcome to Connect 4! ----')
print('Made by Tommy, Janel, and Kevin')
print('')
print(' Player 1 -> X   Player 2 -> O ')
print('')
s = input("Press ENTER to start... ")
if s == 'd':
    debug = True
if s == 'm':
    matrix = True
print('')
p = Connect4Player()
p.play()

