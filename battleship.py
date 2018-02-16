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
                """Sprite(data['deadCell'],(columnNum*50,rowNum*50))"""
            if data['gameBoard'][rowNum][columnNum] == 1:
                """Sprite(data['liveCell'],(columnNum*50,rowNum*50))"""
            if data['gameBoard'][rowNum][columnNum] == 2:
                DO THING
            columnNum += 1
        rowNum += 1

pickComputerShips():
    rowShip1 = randint(1,9)
