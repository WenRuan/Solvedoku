import sys, pygame
from matplotlib.pyplot import text

    #Temporary Grid numbers
grid = [
    ['', 5, 4, 6, '', 8, '', 3, 1],
    ['', '', '', '', '', '', '', 6, ''],
    ['', '', 3, 4, 2, '', 7, '', ''],
    ['', '', 7, 2, 3, 4, 6, '', ''],
    [3, 6, '', '', 9, '', 4, 8, ''],
    ['', 4, 2, '', '', '', 3, '', 7],
    [8, 1, '', 3, '', '', '', 2, 6],
    ['', '', '', 5, '', '', '', '', 9],
    ['', 2, 5, '', '', '', 8, 4, '']
    ]

gridPerm = [
    ['', 'x', 'x', 'x', '', 'x', '', 'x', 'x'],
    ['', '', '', '', '', '', '', 'x', ''],
    ['', '', 'x', 'x', 'x', '', 'x', '', ''],
    ['', '', 'x', 'x', 'x', 'x', 'x', '', ''],
    ['x', 'x', '', '', 'x', '', 'x', 'x', ''],
    ['', 'x', 'x', '', '', '', 'x', '', 'x'],
    ['x', 'x', '', 'x', '', '', '', 'x', 'x'],
    ['', '', '', 'x', '', '', '', '', 'x'],
    ['', 'x', 'x', '', '', '', 'x', 'x', '']
    ]

board = pygame.Surface((362, 400))
board.fill((250,250,250))

pygame.font.init()
font = pygame.font.Font(None, 40)
blockSize = 40

def main():

    #Global variables
    global screen
    global sudokuGrid

    sudokuGrid = [] 
    rectXPos = ''
    rectYPos = ''


    pygame.init()

    logo = pygame.image.load("logo32x32.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Solvedoku")

    screen = pygame.display.set_mode((362,400))
    screen.fill((250,250,250))

    running = True
    while running:
        drawGrid()
        drawGridLines()
        drawGridNumbers()
        screen.blit(board, (0,0))


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                board.fill((250,250,250))
                pressedGrid = pygame.mouse.get_pos()
                rectXPos = pressedGrid[0] - (pressedGrid[0] % 40)
                rectYPos = pressedGrid[1] - (pressedGrid[1] % 40)
                rect = pygame.Rect(rectXPos, rectYPos, blockSize, blockSize)
                pygame.draw.rect(board, (240,0,0), rect)

            if event.type == pygame.KEYDOWN and rectXPos != '':

                board.fill((250,250,250))
                xPosition = int(rectXPos / 40)
                yPosition = int(rectYPos / 40)

                if event.key == pygame.K_1 and gridPerm[xPosition][yPosition] != 'x':

                    if(checkValidMove(xPosition, yPosition, 1)):
                        grid[xPosition][yPosition] = 1
                    else:
                        valid = font.render('Invalid Move', True, (120, 120, 250))
                        validRect = valid.get_rect()
                        validRect.center = (362/2, 380)
                        board.blit(valid, validRect)
                    
                elif event.key == pygame.K_2 and gridPerm[xPosition][yPosition] != 'x':
                    
                    if(checkValidMove(xPosition, yPosition, 2)):
                        grid[xPosition][yPosition] = 2
                    else:
                        valid = font.render('Invalid Move', True, (120, 120, 250))
                        validRect = valid.get_rect()
                        validRect.center = (362/2, 380)
                        board.blit(valid, validRect)
                
                elif event.key == pygame.K_3 and gridPerm[xPosition][yPosition] != 'x':
                    
                    if(checkValidMove(xPosition, yPosition, 3)):
                        grid[xPosition][yPosition] = 3
                    else:
                        valid = font.render('Invalid Move', True, (120, 120, 250))
                        validRect = valid.get_rect()
                        validRect.center = (362/2, 380)
                        board.blit(valid, validRect)

                elif event.key == pygame.K_4 and gridPerm[xPosition][yPosition] != 'x':
                    
                    if(checkValidMove(xPosition, yPosition, 4)):
                        grid[xPosition][yPosition] = 4
                    else:
                        valid = font.render('Invalid Move', True, (120, 120, 250))
                        validRect = valid.get_rect()
                        validRect.center = (362/2, 380)
                        board.blit(valid, validRect)

                elif event.key == pygame.K_5 and gridPerm[xPosition][yPosition] != 'x':
                    
                    if(checkValidMove(xPosition, yPosition, 5)):
                        grid[xPosition][yPosition] = 5
                    else:
                        valid = font.render('Invalid Move', True, (120, 120, 250))
                        validRect = valid.get_rect()
                        validRect.center = (362/2, 380)
                        board.blit(valid, validRect)

                elif event.key == pygame.K_6 and gridPerm[xPosition][yPosition] != 'x':
                    
                    if(checkValidMove(xPosition, yPosition, 6)):
                        grid[xPosition][yPosition] = 6
                    else:
                        valid = font.render('Invalid Move', True, (120, 120, 250))
                        validRect = valid.get_rect()
                        validRect.center = (362/2, 380)
                        board.blit(valid, validRect)

                elif event.key == pygame.K_7 and gridPerm[xPosition][yPosition] != 'x':
                    
                    if(checkValidMove(xPosition, yPosition, 7)):
                        grid[xPosition][yPosition] = 7
                    else:
                        valid = font.render('Invalid Move', True, (120, 120, 250))
                        validRect = valid.get_rect()
                        validRect.center = (362/2, 380)
                        board.blit(valid, validRect)

                elif event.key == pygame.K_8 and gridPerm[xPosition][yPosition] != 'x':
                    
                    if(checkValidMove(xPosition, yPosition, 8)):
                        grid[xPosition][yPosition] = 8
                    else:
                        valid = font.render('Invalid Move', True, (120, 120, 250))
                        validRect = valid.get_rect()
                        validRect.center = (362/2, 380)
                        board.blit(valid, validRect)

                elif event.key == pygame.K_9 and gridPerm[xPosition][yPosition] != 'x':
                    
                    if(checkValidMove(xPosition, yPosition, 9)):
                        grid[xPosition][yPosition] = 9 
                    else:
                        valid = font.render('Invalid Move', True, (120, 120, 250))
                        validRect = valid.get_rect()
                        validRect.center = (362/2, 380)
                        board.blit(valid, validRect)

                elif event.key == pygame.K_BACKSPACE and gridPerm[xPosition][yPosition] != 'x':
                    
                    grid[xPosition][yPosition] = ''    

                elif event.key == pygame.K_RETURN:
                    total = 0
                    print('test')
                    for i in range(9):
                        for j in range(9):
                            if(grid[i][j] == ''):
                                complete = font.render('Incomplete', True, (120, 120, 250))
                                completeRect = complete.get_rect()
                                completeRect.center = (362/2, 380)
                                board.blit(complete, completeRect)
                            else:
                                total += grid[i][j]
                    if(total == 405):
                        complete = font.render("Completed", True, (120, 250, 120))
                        completeRect = complete.get_rect()
                        completeRect.center = (362/2, 400/2)
                        board.blit(complete, completeRect)
                        running = False
                                      

        pygame.display.update()

        # for i in range(9):
        #     for j in range(9):
        #         if(grid[i][j] == ''):
        #             running = True
        # print("Completed")

def drawGrid():
    
    for x in range(0, 360, blockSize):
        for y in range(0, 360, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)

            pygame.draw.rect(board, (230,230,230), rect, 1)

def drawGridLines():
    black = (0, 0, 0)
    pygame.draw.line(board, black, (0, 0), (360, 0), width=2)
    pygame.draw.line(board, black, (0, 120), (360, 120), width=2)
    pygame.draw.line(board, black, (0, 240), (360, 240), width=2)
    pygame.draw.line(board, black, (0, 360), (360, 360), width=2)
    pygame.draw.line(board, black, (0, 0), (0, 360), width=2)
    pygame.draw.line(board, black, (120, 0), (120, 360), width=2)
    pygame.draw.line(board, black, (240, 0), (240, 360), width=2)
    pygame.draw.line(board, black, (360, 0), (360, 360), width=2)


def drawGridNumbers():
    row = 0
    while row < 9:
        col = 0
        while col < 9:
            if(gridPerm[row][col] == 'x'):
                
                numbers = font.render(str(grid[row][col]), True, (30,30,30))
                board.blit(numbers, ((row * 40 + 12), (col * 40 + 8)))

            else:
                numbers = font.render(str(grid[row][col]), True, (240,0,0))
                board.blit(numbers, ((row * 40 + 12), (col * 40 + 8)))
            
            col += 1
        row += 1

def checkValidMove(xPosition, yPosition, keyDown):
    for i in range(9):
        if(grid[i][yPosition] == keyDown and gridPerm[i][yPosition] == 'x'):
            return False
        if(grid[xPosition][yPosition] == keyDown and gridPerm[xPosition][i] == 'x'):
            return False

    quadrant = findQuadrant(xPosition, yPosition)
    i = quadrant[0]
    while i < quadrant[0] + 3:
        j = quadrant[1]
        while j < quadrant[1] + 3:
            if(keyDown == grid[i][j] and gridPerm[i][j] == 'x'):
                return False
            j += 1
        i += 1
    return True

def findQuadrant(xPosition, yPosition):

    xQuad = 0
    yQuad = 0
    #find x quadrant 
    if(xPosition <= 2):
        xQuad = 1
    elif(xPosition >=3 and xPosition <= 5):
        xQuad = 2
    elif(xPosition >=6 and xPosition <=8):
        xQuad = 3
    
    #find y quadrant 
    if(yPosition <= 2):
        yQuad = 1
    elif(yPosition >=3 and yPosition <= 5):
        yQuad = 2
    elif(yPosition >=6 and yPosition <=8):
        yQuad = 3

    if(xQuad == 1 and yQuad == 1):
        return (0,0)
    elif(xQuad == 2 and yQuad == 1):
        return (3,0)
    elif(xQuad == 3 and yQuad == 1):
        return (6,0)
    elif(xQuad == 1 and yQuad == 2):
        return (0,3)
    elif(xQuad == 2 and yQuad == 2):
        return (3,3)
    elif(xQuad == 3 and yQuad == 2):
        return (6,3)
    elif(xQuad == 1 and yQuad == 3):
        return (0,6)
    elif(xQuad == 2 and yQuad == 3):
        return (3,6)
    elif(xQuad == 3 and yQuad == 3):
        return (6,6)



if __name__=="__main__":
    main();