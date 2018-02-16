#Claire Yegian
#2/16/17
#battleship.py - creates the game battleship

from random import randint
from game import *

#Creates gameboard
def buildBoard():
    return [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
    
#Prints gameboard (with any updates)
def redrawAll():
    rowNum = 0
    for row in data['gameBoard']:
        columnNum = 0
        for column in row:
            if data['gameBoard'][rowNum][columnNum] == 0:
                Sprite(data['empty'],(columnNum*50,rowNum*50))
            if data['gameBoard'][rowNum][columnNum] == 1:
                Sprite(data['miss'],(columnNum*50,rowNum*50))
            if data['gameBoard'][rowNum][columnNum] == 2:
                Sprite(data['hit'],(columnNum*50,rowNum*50))
            columnNum += 1
        rowNum += 1

"""pickComputerShips():
    rowShip1 = randint(1,9)

def mouseClick(event):
    if data['numShips'] == 3"""

if __name__ == '__main__':
    empty = Color(0xffffff,1) #Colors used in program
    miss = Color(0xD3D3D3,1)
    hit = Color(0xff0000,1)
    
    data = {} #Program dictionary
    data['empty'] = RectangleAsset(50,50,LineStyle(1,miss),empty)
    data['miss'] = RectangleAsset(50,50,LineStyle(1,miss),miss)
    data['hit'] = RectangleAsset(50,50,LineStyle(1,hit),hit)
    data['numShips'] = 0
    data['gameBoardUpdate'] = []
    
    data['gameBoard'] = gameBoard()
    redrawAll()
    
    """nextGen = TextAsset('NextGeneration')
    Sprite(nextGen,(190,520))
    
    App().listenMouseEvent('click',mouseClick)"""
    App().run()
