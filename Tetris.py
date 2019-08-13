#Tetris
#Written by Michael Wermert
#
#This code is a tetris clone written in Python. It is written in Python 3.7.2 and uses the pygame library.
#This code was written mainly to help me teach myself python and basic game development techniques. In this program,
#I reinforced my understanding of the basics of Python, basic graphic design, data structures such as dequeues and lists.
#
#If you would like to clone and use this code, you are welcome to do so, please just credit me
 

import pygame
import random
import copy
from collections import deque
pygame.init()

#initializes display
win = pygame.display.set_mode((600, 600))
font = pygame.font.SysFont('comicsans', 20, True)
clock = pygame.time.Clock()
pygame.display.set_caption("Tetris")

#initializes the colors
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)

scoreList = [0, 40, 100, 200, 300]


#draws the correct image to the screen
def DrawScreen(win, board, score, pieceQueue):
    win.fill((0,0,0))

    #goes through the board and assigns the correct color to each space in the board, using the mod operator
    for i in range(10):
        
        for j in range(22):
            if (board[j][i] % 4) == 0 and board[j][i] != 0 and board[j][i] != 1000:
                pygame.draw.rect(win, RED, (120+20*i, 100+20*j, 20, 20))
                pygame.draw.rect(win, (255, 100, 100), (125+20*i, 105+20*j, 10,10))
            elif (board[j][i] % 4) == 1:
                pygame.draw.rect(win, BLUE, (120+20*i, 100+20*j, 20, 20))
                pygame.draw.rect(win, (100, 100, 255), (125+20*i, 105+20*j, 10,10))
            elif (board[j][i] %4) == 2:
                pygame.draw.rect(win, GREEN, (120+20*i, 100+20*j, 20, 20))
                pygame.draw.rect(win, (100, 255, 100), (125+20*i, 105+20*j, 10,10))
            elif (board[j][i]%4) == 3:
                pygame.draw.rect(win, YELLOW, (120+20*i, 100+20*j, 20, 20))
                pygame.draw.rect(win, (255, 255, 100), (125+20*i, 105+20*j, 10,10))
            elif (board[j][i]) == 1000:
                pygame.draw.rect(win, (255, 255, 255), (120+20*i, 100+20*j, 20, 20))
            else:
                pygame.draw.rect(win, (0, 0, 0), (120+20*i, 100+20*j, 20, 20))
            
    #draws the border on the screen
    for i in range(12):
        pygame.draw.rect(win, (255, 255, 255), (100+20*i, (22*20 + 100), 20, 20))
    pygame.draw.rect(win, (255, 255, 255), (100, 100, 20, 20*22))
    pygame.draw.rect(win, (255, 255, 255), (320, 100, 20, 20*22))
    
    #draws next piece in line onto the board
    s = pieceQueue[0].retShape()
    for i in range(len(s)):
        for j in range(len(s[i])):
            if (s[i][j] % 4) == 0 and s[i][j] != 0 and s[i][j] != 1000:
                pygame.draw.rect(win, RED, (400+20*i, 300+20*j, 20, 20))
                pygame.draw.rect(win, (255, 100, 100), (405+20*i, 305+20*j, 10,10))
            elif (s[i][j] % 4) == 1:
                pygame.draw.rect(win, BLUE, (400+20*i, 300+20*j, 20, 20))
                pygame.draw.rect(win, (100, 100, 255), (405+20*i, 305+20*j, 10,10))
            elif (s[i][j] %4) == 2:
                pygame.draw.rect(win, GREEN, (400+20*i, 300+20*j, 20, 20))
                pygame.draw.rect(win, (100, 255, 100), (405+20*i, 305+20*j, 10,10))
            elif (s[i][j]%4) == 3:
                pygame.draw.rect(win, YELLOW, (400+20*i, 300+20*j, 20, 20))
                pygame.draw.rect(win, (255, 255, 100), (405+20*i, 305+20*j, 10,10))
            elif (s[i][j]) == 1000:
                pygame.draw.rect(win, (255, 255, 255), (120+20*i, 100+20*j, 20, 20))
            else:
                pygame.draw.rect(win, (0, 0, 0), (400+20*i, 300+20*j, 20, 20))
    
    #draws piece 2nd in line
    s = pieceQueue[1].retShape()
    for i in range(len(s)):
        for j in range(len(s[i])):
            if (s[i][j] % 4) == 0 and s[i][j] != 0 and s[i][j] != 1000:
                pygame.draw.rect(win, RED, (400+20*i, 400+20*j, 20, 20))
                pygame.draw.rect(win, (255, 100, 100), (405+20*i, 405+20*j, 10,10))
            elif (s[i][j] % 4) == 1:
                pygame.draw.rect(win, BLUE, (400+20*i, 400+20*j, 20, 20))
                pygame.draw.rect(win, (100, 100, 255), (405+20*i, 405+20*j, 10,10))
            elif (s[i][j] %4) == 2:
                pygame.draw.rect(win, GREEN, (400+20*i, 400+20*j, 20, 20))
                pygame.draw.rect(win, (100, 255, 100), (405+20*i, 405+20*j, 10,10))
            elif (s[i][j]%4) == 3:
                pygame.draw.rect(win, YELLOW, (400+20*i, 400+20*j, 20, 20))
                pygame.draw.rect(win, (255, 255, 100), (405+20*i, 405+20*j, 10,10))
            elif (s[i][j]) == 1000:
                pygame.draw.rect(win, (255, 255, 255), (120+20*i, 100+20*j, 20, 20))
            else:
                pygame.draw.rect(win, (0, 0, 0), (400+20*i, 400+20*j, 20, 20))

    #draws score and other labels to the screen
    font = pygame.font.SysFont('comicsans', 20, True)
    text = font.render('Score: '+ str(score), 1, (255, 255, 255))
    nextlabel = font.render('Next Pieces', 1, (255, 255, 255))
    win.blit(text, (500, 100))
    win.blit(nextlabel, (400, 250))

    #updates display
    pygame.display.update()

#class that all special blocks are inherited from
class Block:
    def __init__(self, shape, ID):
        
        #represents the shape of a piece, represented as a 2d list
        self.shape = shape
        
        #piece location, store in row and column
        self.r = 0
        self.c = 5

        #returns the piece id that is used in the board 2d list
        self.ID = ID
    
    #rotates the piece by 90 degrees
    def rotate(self, board):
        temp = self.shape
        loc = self.retLoc()

        #erases shape from board
        for i in range(len(self.shape)):
            for j in range(len(self.shape[i])):
                board[loc[0]+i][loc[1]+j] = 0
        
        #resizes list to 90 degree orientation
        self.shape = [[0 for x in range(len(temp))] for y in range(len(temp[0]))]
        
        #fills in the object shape for the 90 degree rotation
        for i in range(len(temp)):
            for j in range(len(temp[0])):
                self.shape[j][len(temp)-1-i] = temp[i][j]
        
        #draws rotated piece onto the board
        for i in range(len(self.shape)):
            for j in range(len(self.shape[i])):
                board[loc[0]+i][loc[1]+j] = self.shape[i][j]
        
    
    #determines if piece can rotate
    def canRotate(self, board):
        if len(self.shape) + self.c > 10:
            return False
        loc = self.retLoc()
        
        #creates a temporary board that is identical to the in-game board
        tBoard = copy.deepcopy(board)

        for i in range(len(self.shape)):
            for j in range(len(self.shape[i])):
                tBoard[loc[0]+i][loc[1]+j] = 0
        #resizes list to 90 degree orientation
        temp = [[0 for x in range(len(self.shape))] for y in range(len(self.shape[0]))]
        
        #fills in the object shape for the 90 degree rotation
        for i in range(len(self.shape)):
            for j in range(len(self.shape[0])):
                temp[j][len(self.shape)-1-i] = self.shape[i][j]

        #compares all the spaces in the rotated shape and in the 
        #locations in the board that the rotated piece will go
        #if both spaces are not equal to zero, then the space is occpied,
        #and the piece cannot rotate
        for i in range(len(temp)):
            for j in range(len(temp[i])):
                if temp[i][j] != 0 and tBoard[loc[0]+i][loc[1]+j] != 0:
                    return False
        


        return True

    #determines if a passed in piece can move to a passed in location
    def canMove(self, board, r2, c2):
        
        longest = -999
        longestIndex = 0
        bumpFlag = True

        #returns false if the peice is at the bottom of the board
        if len(self.shape) + self.r >= 22:
            return False

        #if the column value is out of bounds, the function returns false
        #left side check
        if c2 < 0:
            return False

        for i in range(len(self.shape)):
            if len(self.shape[i]) > longest:
                longest = len(self.shape[i])
                longestIndex = i

        #right side check
        if c2 + len(self.shape[longestIndex]) > 10:
            return False

        #clears board where piece was previously
        loc = self.retLoc()
        for i in range(len(self.shape)):
            for j in range(len(self.shape[i])):
                if board[loc[0]+i][loc[1]+j] == self.ID:
                    board[loc[0]+i][loc[1]+j] = 0
        
        #if a space on the piece and a space on the board conflict,
        #the function returns false
        for i in range(len(self.shape)):
            for j in range(len(self.shape[i])):
                if board[r2+i][c2+j] != 0 and self.shape[i][j] != 0:
                    bumpFlag = False
        
        #redraws shape
        for i in range(len(self.shape)):
            for j in range(len(self.shape[i])):
                if self.shape[i][j] != 0:
                    board[loc[0]+i][loc[1]+j] = self.shape[i][j]

        if bumpFlag == False:
            return False
        else:
            return True

    #returns the piece id value
    def retID(self):
        return self.ID

    #updates the location of the piece
    def updateLoc(self, newX, newY):
        self.r = newX
        self.c = newY
    
    #returns the location of the piece as a list
    def retLoc(self):
        return [self.r, self.c]

    #returns the shape of the piece as a 2d list
    def retShape(self):
        return self.shape

#moves the piece from the old location and
#redraws it at the new location
def Move(currBlock, board, r1, c1):

    #gets shape and location information, changes location in piece object
    loc = currBlock.retLoc()
    currBlock.updateLoc(r1, c1)
    shape = currBlock.retShape()
    
    #erases piece in previous location on board
    for i in range(len(shape)):
        for j in range(len(shape[i])):
            if board[loc[0]+i][loc[1]+j] == currBlock.retID():
                board[loc[0]+i][loc[1]+j] = 0

    #draws the piece to the new location
    for i in range(len(shape)):
        for j in range(len(shape[i])):
            if shape [i][j] != 0:
                board[r1+i][c1+j] = shape[i][j]

#starts at an empty row and moves all blocks above the empty row
def PercolateDown(win, board):
    eFlag = False
    
    #locates empty row
    for i in range(21, -1, -1):
        for j in range(10):
            if board[i][j] == 0:
                eFLag = True
            else:
                eFLag =False
                break
        if eFLag == True:
            eRow = i
            break

    #moves all non zero blocks downwards
    for i in range(eRow-1, -1,-1):
        for j in range(10):
            if board[i][j] != 0 and board[i+1][j] == 0:
                board[i+1][j] = board[i][j]
                board[i][j] = 0
    

#checks for a full line and deletes it if one is found,
#if a full line is found, then the function returns false
#if one is not found, the function returns false
def CheckandDeleteLine(win, board, score, pieceQueue):
    fullFlag = False
    eTime = 0
    
    #searches for a fill line
    for i in range(21, -1, -1):
        eTime = 0
        for j in range(10):
            if board[i][j] != 0:
                fullFLag = True
            else:
                fullFLag =False
                break
        if fullFLag == True:
            break
    #if fullFlag is true, then a full line was found, the row turns white for 300 seconds and 
    #then it is deleted
    if fullFLag == True:
        for j in range(10):
            board[i][j] = 1000
        while eTime <= 300:
            dt = clock.tick()
            eTime += dt
            DrawScreen(win, board, score, pieceQueue)
        for j in range(10):
            board[i][j] = 0
        return True
    #fullFlag returns false, which means that a full line was not found
    else:
        return False

#function that displays the lose screen
def loseScreen(score):
    
    loseFlag = True
    elapsed_time = 0
    qFlag = False
    while loseFlag and not qFlag:
        
        #displays the lose screen
        win.fill((0,0,0))
        font = pygame.font.SysFont('comicsans', 50, True)
        text = font.render('GAME OVER!', 1, (255, 0, 0))
        font = pygame.font.SysFont('comicsans', 20, True)
        text2 = font.render('Your Score was '+str(score), 1, (255, 0,0))
        win.blit(text, (200, 100))
        win.blit(text2, (300, 75))

        #updates display
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                qFlag = True

        #after 5 seconds, the game resets
        dt = clock.tick()
        elapsed_time += dt
        if elapsed_time >= 5000:
            loseFlag = False
    if qFlag:
        pygame.display.quit()
        pygame.quit()
    #the game starts over
    main()

#These are the inherited classes for the different blocks

#inherited class for the straight line block
class LineBlock(Block):
    def __init__(self, ID):
        s = [[1],[1],[1],[1]]
        for i in range(len(s)):
            for j in range(len(s[i])):
                if s[i][j] != 0:
                    s[i][j] = ID
        Block.__init__(self, s, ID)

#inherited class for the 'L' block
class LBlock(Block):
    def __init__(self, ID):
        s = [[1,0], [1,0], [1,1]]
        for i in range(len(s)):
            for j in range(len(s[i])):
                if s[i][j] != 0:
                    s[i][j] = ID
        Block.__init__(self, s, ID)

#inherited class for the reverse 'L' block
class RevLBlock(Block):
    def __init__(self, ID):
        s = [[0,1], [0,1], [1,1]]
        for i in range(len(s)):
            for j in range(len(s[i])):
                if s[i][j] != 0:
                    s[i][j] = ID
        Block.__init__(self, s, ID)

#inherited class for the square block
class Square(Block):
    def __init__(self, ID):
        s = [[1,1],[1,1]]
        for i in range(len(s)):
            for j in range(len(s[i])):
                if s[i][j] != 0:
                    s[i][j] = ID
        Block.__init__(self, s, ID)

#inherited class for the 'T' block
class TBlock(Block):
    def __init__(self, ID):
        s = [[0,1],[1,1],[0,1]]
        for i in range(len(s)):
            for j in range(len(s[i])):
                if s[i][j] != 0:
                    s[i][j] = ID
        Block.__init__(self, s, ID)

##inherited class for the 's' block
class SBlock(Block):
    def __init__(self, ID):
        s = [[1,0],[1,1],[0,1]]
        for i in range(len(s)):
            for j in range(len(s[i])):
                if s[i][j] != 0:
                    s[i][j] = ID
        Block.__init__(self, s, ID)

#inherited class for the reverse 's' block
class RevSBlock(Block):
    def __init__(self, ID):
        s = [[0,1],[1,1],[1,0]]
        for i in range(len(s)):
            for j in range(len(s[i])):
                if s[i][j] != 0:
                    s[i][j] = ID
        Block.__init__(self, s, ID)



#randomly selects what shape a new piece will be
def GenerateBlock(board, ID):
    choice = random.randint(0,6)

    if choice == 0:
        currBlock = LineBlock(ID)
    elif choice == 1:
        currBlock = LBlock(ID)
    elif choice == 2:
        currBlock = RevLBlock(ID)
    elif choice == 3:
        currBlock = TBlock(ID)
    elif choice == 4:
        currBlock = RevSBlock(ID)
    elif choice == 5:
        currBlock = SBlock(ID)
    else:
        currBlock = Square(ID)

    s = currBlock.retShape()
    loc = currBlock.retLoc()

    return currBlock

def main():
    
    #initializes empty board
    board = [[0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0]]
    
    #queue that stores the next two blocks
    blockQueue = deque()
    
    #used to calculate the piece.ID value
    pieceCount = 1
    
    #stores the score of a game
    score = 0
    
    #stores how many rows were filled in one turn
    scoreCount = 0

    #used to calculate score, is true as long as there rows destroyed in a single turn
    scoreFlag = False

    #keeps the game loop running, becomes false if user closes the window
    gameFlag = True

    #becomes true if the user loses
    loseFlag = False

    #used for continuous movement for piece
    eTimeRight = 0
    eTimeLeft = 0
    eTimeDown = 0
    eTimeR = 0
    elapsed_time = 0

    time_to_fall = 1000
    #initializes the block queue with three blocks
    for i in range(3):
        tempBlock = GenerateBlock(board, pieceCount)
        blockQueue.append(tempBlock)
        pieceCount += 1
    
    #draws first block onto screen
    currBlock = blockQueue.popleft()
    s = currBlock.retShape()
    for i in range(len(s)):
        for j in range(len(s[i])):
            board[i][5+j] = s[i][j]
    
    #main game loop, repeats as long as user does not exit out of window
    while gameFlag:

        dt = clock.tick()
        elapsed_time += dt

        #if 1 second has passed, this executes
        if elapsed_time >= time_to_fall:
            elapsed_time = 0
            newLoc = currBlock.retLoc()

            #if the piece can move downwards, it will
            if (currBlock.canMove(board,newLoc[0]+1, newLoc[1] )): 
                Move(currBlock, board, newLoc[0]+1, newLoc[1])
            
            #determines if the piece that cannot move down is in the top row, in which case the game is over
            else:
                
                #switches screen to the lose screen
                if newLoc[0] == 0:
                    gameFlag = False
                    loseScreen(score)
                pieceCount += 1
                if pieceCount%10 == 0 and time_to_fall > 100:
                    time_to_fall -= 100
                #the piece does not end the game, so it checks if any rows were completed by the piece,
                #repeats as long as there are rows that are found that are completed
                while (CheckandDeleteLine(win, board, score, blockQueue)):
                    
                    #moves all of the non-zero pieces downwards by the 
                    PercolateDown(win, board)
                    scoreCount += 1
                    scoreFlag = True
                
                #if at least one row is destroyed, then the appropriate score is added to the score variable
                if scoreFlag:
                    score += scoreList[scoreCount]
                    scoreCount = 0
                    scoreFlag = False
                
                #generates a new block and sets the old block into the list
                tempBlock = GenerateBlock(board,pieceCount)
                blockQueue.append(tempBlock)
                currBlock = blockQueue.popleft()
                s = currBlock.retShape()
                for i in range(len(s)):
                    for j in range(len(s[i])):
                        board[i][5+j] = s[i][j]
        
        #if the user closes the game window, the loop ends
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameFlag = False 
        
        #gets the keys that were pressed
        keys = pygame.key.get_pressed()
        
        loc = currBlock.retLoc()

        #manages movement to the left, if the key is held, and the piece can move,
        #the piece moves every .5 seconds
        eTimeLeft += dt
        if keys[pygame.K_LEFT]:
            if eTimeLeft >= 500:
                eTimeLeft = 0
                if (currBlock.canMove(board, loc[0], loc[1] -1)):
                    Move(currBlock, board, loc[0], loc[1] -1)

        #manages movement to the right, if the key is held, and the piece can move,
        #the piece moves every .5 seconds
        eTimeRight += dt
        if keys[pygame.K_RIGHT]:
            if eTimeRight >= 500:
                eTimeRight = 0
                if (currBlock.canMove(board, loc[0], loc[1] +1)):
                    Move(currBlock, board, loc[0], loc[1] +1)

        #manages movement to the down, if the key is held, and the piece can move,
        #the piece moves every .25 seconds
        eTimeDown += dt
        if keys[pygame.K_DOWN]:
            if eTimeDown >= 250:
                eTimeDown = 0
                if (currBlock.canMove(board, loc[0]+1, loc[1])):
                    Move(currBlock, board, loc[0]+1, loc[1])
        
        #manages rotation, if the key is held, and the piece can rotate,
        #the piece moves every .5 seconds
        eTimeR += dt
        if keys[pygame.K_r]:
            if(currBlock.canRotate(board)):
                if eTimeR >= 500:
                    eTimeR = 0
                    currBlock.rotate(board)
        
        #Draws appropriate objects to the screen
        DrawScreen(win, board, score, blockQueue)
    
    
if __name__ == "__main__":
    main()

#the window was closed and the game exits
pygame.display.quit()
pygame.quit()
