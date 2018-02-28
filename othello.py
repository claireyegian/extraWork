#Claire Yegian
#2/28/18
#othello.py - creates othello game board

#Creates gameboard
def buildBoard():
    return [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,1,2,0,0,0],[0,0,0,2,1,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]

def redrawAll():
    for item in App().spritelist[:]:
        item.destroy()
    rowNum = 0
    for row in data['gameBoard1']:
        columnNum = 0
        for column in row:
            if data['gameBoard1'][rowNum][columnNum] == 0:
                Sprite(data['empty'],(columnNum*50,rowNum*50))
            if data['gameBoard1'][rowNum][columnNum] == 1:
                Sprite(data['player'],(columnNum*50,rowNum*50))
            if data['gameBoard1'][rowNum][columnNum] == 2:
                Sprite(data['computer'],(columnNum*50,rowNum*50))
            columnNum += 1
        rowNum += 1

if __name__ == '__main__':
    computer = Color(0xffffff,1) #Colors used in program
    empty = Color(0xDA70D6,1)
    player = Color(0x000000,1)
    
    data = {} #Program dictionary
    data['empty'] = RectangleAsset(50,50,LineStyle(1,empty),empty)
    data['computer'] = CircleAsset(50,50,LineStyle(1,computer),computer)
    data['player'] = CircleAsset(50,50,LineStyle(1,player),player)

    data['gameBoard'] = buildBoard()
    redrawAll()
    
    App().listenMouseEvent('click',mouseClick)
    App().run()