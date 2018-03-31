#Claire Yegian
#2/28/18
#othello.py - creates othello game board

from ggame import *

#Creates gameboard
def buildBoard():
    return [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,1,2,0,0,0],[0,0,0,2,1,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]

def redrawAll():
    for item in App().spritelist[:]:
        item.destroy()
    rowNum = 0
    for row in data['gameBoard']:
        columnNum = 0
        for column in row:
            if data['gameBoard'][rowNum][columnNum] == 0:
                Sprite(data['empty'],(columnNum*50,rowNum*50))
            if data['gameBoard'][rowNum][columnNum] == 1:
                Sprite(data['empty'],(columnNum*50,rowNum*50))
                Sprite(data['player'],(columnNum*50,rowNum*50))
            if data['gameBoard'][rowNum][columnNum] == 2:
                Sprite(data['empty'],(columnNum*50,rowNum*50))
                Sprite(data['computer'],(columnNum*50,rowNum*50))
            columnNum += 1
        rowNum += 1

def boardFull():
    emptyCount = 0
    rowNum = 0
    for row in data['gameBoard']:
        columnNum = 0
        for column in row:
            if data['gameBoard'][rowNum][columnNum] == 0:
                emptyCount += 1
            columnNum += 1
        rowNum += 1
    if emptyCount > 0:
        return('False')
    elif emptyCount == 0:
        return('True')

def winner():
    computerCount = 0
    playerCount = 0
    rowNum = 0
    for row in data['gameBoard']:
        columnNum = 0
        for column in row:
            if data['gameBoard'][rowNum][columnNum] == 1:
                playerCount += 1
            elif data['gameBoard'][rowNum][columnNum] == 2:
                computerCount += 1
            columnNum += 1
        rowNum += 1
    if computerCount > playerCount:
        print('computer wins')
    elif playerCount > computerCount:
        print('player wins')
    else:
        print('tie')

def flipPieces(row,column):
    flipEast(row,column)
    flipWest(row,column)
    flipNorth(row,column)
    flipSouth(row,column)
    flipNorthWest(row,column)
    flipNorthEast(row,column)
    flipSouthWest(row,column)
    flipSouthEast(row,column) 
    redrawAll()

def flipEast(row,column):
    ogColumn = column
    blackSquare = 0
    while blackSquare < 1:
        if data['gameBoard'][row][column] == 1:
            blackSquare = 0
            column += 1
        elif data['gameBoard'][row][column] == 0:
            break
        elif data['gameBoard'][row][column] == 2:
            blackSquare = 1
            while ogColumn <= column:
                data['gameBoard'][row][ogColumn] = 2
                ogColumn += 1
            break

def flipWest(row,column):
    ogColumn = column
    blackSquare = 0
    while blackSquare < 1:
        if data['gameBoard'][row][column] == 1:
            blackSquare = 0
            column -= 1
        elif data['gameBoard'][row][column] == 0:
            break
        elif data['gameBoard'][row][column] == 2:
            blackSquare = 1
            while ogColumn <= column:
                data['gameBoard'][row][ogColumn] = 2
                ogColumn -= 1
            break

def flipNorth(row,column):
    ogRow = row
    blackSquare = 0
    while blackSquare < 1:
        if data['gameBoard'][row][column] == 1:
            blackSquare = 0
            row -= 1
        elif data['gameBoard'][row][column] == 0:
            break
        elif data['gameBoard'][row][column] == 2:
            blackSquare = 1
            while ogRow <= row:
                data['gameBoard'][ogRow][column] = 2
                ogRow -= 1
            break

def flipSouth(row,column):
    ogRow = row
    blackSquare = 0
    while blackSquare < 1:
        if data['gameBoard'][row][column] == 1:
            blackSquare = 0
            row += 1
        elif data['gameBoard'][row][column] == 0:
            break
        elif data['gameBoard'][row][column] == 2:
            blackSquare = 1
            while ogRow <= row:
                data['gameBoard'][ogRow][column] = 2
                ogRow += 1
            break

def flipNorthWest(row,column):
    ogRow = row
    ogColumn = column
    blackSquare = 0
    while blackSquare < 1:
        if data['gameBoard'][row][column] == 1:
            blackSquare = 0
            row -= 1
            column -= 1
        elif data['gameBoard'][row][column] == 0:
            break
        elif data['gameBoard'][row][column] == 2:
            blackSquare = 1
            while ogRow <= row and ogColumn <= column:
                data['gameBoard'][ogRow][ogColumn] = 2
                ogRow -= 1
                ogColumn -= 1
            break
    

def flipNorthEast(row,column):
    ogRow = row
    ogColumn = column
    blackSquare = 0
    while blackSquare < 1:
        if data['gameBoard'][row][column] == 1:
            blackSquare = 0
            row -= 1
            column += 1
        elif data['gameBoard'][row][column] == 0:
            break
        elif data['gameBoard'][row][column] == 2:
            blackSquare = 1
            while ogRow <= row and ogColumn <= column:
                data['gameBoard'][ogRow][ogColumn] = 2
                ogRow -= 1
                ogColumn += 1
            break
    

def flipSouthWest(row,column):
    ogRow = row
    ogColumn = column
    blackSquare = 0
    while blackSquare < 1:
        if data['gameBoard'][row][column] == 1:
            blackSquare = 0
            row += 1
            column -= 1
        elif data['gameBoard'][row][column] == 0:
            break
        elif data['gameBoard'][row][column] == 2:
            blackSquare = 1
            while ogRow <= row and ogColumn <= column:
                data['gameBoard'][ogRow][ogColumn] = 2
                ogRow += 1
                ogColumn -= 1
            break
    

def flipSouthEast(row,column):
    ogRow = row
    ogColumn = column
    blackSquare = 0
    while blackSquare < 1:
        if data['gameBoard'][row][column] == 1:
            blackSquare = 0
            row += 1
            column += 1
        elif data['gameBoard'][row][column] == 0:
            break
        elif data['gameBoard'][row][column] == 2:
            blackSquare = 1
            while ogRow <= row and ogColumn <= column:
                data['gameBoard'][ogRow][ogColumn] = 2
                ogRow += 1
                ogColumn += 1
            break
    

def mouseClick(event):
    row = event.y//50
    column = event.x//50
    if data['gameBoard'][row][column] == 0:
        Sprite(data['empty'],(column*50,row*50))
        Sprite(data['player'],(column*50,row*50))
        if boardFull() == 'False':
            flipPieces(row,column)
            if boardFull() == 'True':
                winner()
        elif boardFull() == 'True':
                winner()

if __name__ == '__main__':
    computer = Color(0xffffff,1) #Colors used in program
    empty = Color(0x7CACE4,1)
    player = Color(0x000000,1)
    boarder = Color(0x5788C0,1)
    
    data = {} #Program dictionary
    data['empty'] = RectangleAsset(50,50,LineStyle(1,boarder),empty)
    data['computer'] = CircleAsset(24,LineStyle(1,boarder),computer)
    data['player'] = CircleAsset(24,LineStyle(1,boarder),player)

    data['gameBoard'] = buildBoard()
    redrawAll()
    boardFull()
    
    App().listenMouseEvent('click',mouseClick)
    App().run()