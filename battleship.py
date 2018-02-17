#Claire Yegian
#2/16/17
#battleship.py - creates the game battleship

from random import randint
from ggame import *

#Creates gameboard
def buildBoard():
    return [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
    
#Prints gameboard (with any updates)
def redrawAll():
    rowNum = 0
    for row in data['gameBoard1']:
        columnNum = 0
        for column in row:
            if data['gameBoard1'][rowNum][columnNum] == 0:
                Sprite(data['empty'],(columnNum*50,rowNum*50))
            if data['gameBoard1'][rowNum][columnNum] == 1:
                Sprite(data['miss'],(columnNum*50,rowNum*50))
            if data['gameBoard1'][rowNum][columnNum] == 2:
                Sprite(data['hit'],(columnNum*50,rowNum*50))
            if data['gameBoard1'][rowNum][columnNum] == 3:
                Sprite(data['ship'],(columnNum*50,rowNum*50))
            columnNum += 1
        rowNum += 1
    rowNum = 0
    for row in data['gameBoard2']:
        columnNum = 0
        for column in row:
            if data['gameBoard2'][rowNum][columnNum] == 0:
                Sprite(data['empty'],((columnNum*50)+550,rowNum*50))
            if data['gameBoard2'][rowNum][columnNum] == 1:
                Sprite(data['miss'],((columnNum*50)+550,rowNum*50))
            if data['gameBoard2'][rowNum][columnNum] == 2:
                Sprite(data['hit'],((columnNum*50)+550,rowNum*50))
            if data['gameBoard2'][rowNum][columnNum] == 3:
                Sprite(data['ship'],((columnNum*50)+550,rowNum*50))
            columnNum += 1
        rowNum += 1

def mouseClick(event):
    row = event.y//50
    column = event.x//50
    while data['numShips1'] < 3:
        data['gameBoard1'][row][column] = 3
        data['numShips1'] += 1
    redrawAll()
    pickComputerShips()
    if data['gameBoard2'][row][column] == 0:
        data['gameBoard2'][row][column] = 1
    if data['gameBoard2'][row][column] == 3:
        data['gameBoard2'][row][column] = 2
    redrawAll()

def pickComputerShips():
    while data['numShips2'] < 3:
        row = randint(0,8)
        column = randint(0,8)
        if data['gameBoard2'][row][column] != 3:
            data['gameBoard2'][row][column] = 3
            data['numShips2'] += 1
    redrawAll()
    

if __name__ == '__main__':
    empty = Color(0xffffff,1) #Colors used in program
    miss = Color(0xD3D3D3,1)
    hit = Color(0xff0000,1)
    ship = Color(0x000000,1)
    
    data = {} #Program dictionary
    data['empty'] = RectangleAsset(50,50,LineStyle(1,miss),empty)
    data['miss'] = RectangleAsset(50,50,LineStyle(1,miss),miss)
    data['hit'] = RectangleAsset(50,50,LineStyle(1,hit),hit)
    data['ship'] = RectangleAsset(50,50,LineStyle(1,ship),ship)
    data['numShips1'] = 0
    data['numShips2'] = 0
    
    data['gameBoard1'] = buildBoard()
    data['gameBoard2'] = buildBoard()
    redrawAll()
    
    Sprite(TextAsset('Player',fill=black,style="bold 50pt Times"),(150,450))
    Sprite(TextAsset('Computer',fill=black,style="bold 50pt Times"),(650,450))
    App().listenMouseEvent('click',mouseClick)
    App().run()
