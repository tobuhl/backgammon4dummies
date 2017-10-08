#game.py

import os
from logger import Log
from bg_state import *

#represents a backgammon game (singleton)
class Game:
    __instance = None

    def __init__(self, player1Name, player1Color, player2Name, player2Color):
        self.player1 = Player(player1Name, player1Color)
        self.player2 = Player(player2Name, player2Color)
        self.p1Mode = "human"
        self.p2Mode = "human"
    
        #create initital state
        stateArray = [Points() for x in range(25)]
        stateArray[0].color = "white"
        stateArray[0].count = 2

        stateArray[11].color = "white"
        stateArray[11].count = 5

        stateArray[17].color = "white"
        stateArray[17].count = 3

        stateArray[19].color = "white"
        stateArray[19].count = 5

        stateArray[5].color = "black"
        stateArray[5].count = 5

        stateArray[7].color = "black"
        stateArray[7].count = 3

        stateArray[12].color = "black"
        stateArray[12].count = 5

        stateArray[23].color = "black"
        stateArray[23].count = 2

        self.currentState = State(stateArray, self.player1, self.player2)
 
    def __new__(cls, player1Name, player1Color, player2Name, player2Color): 
        #inititalize logger
        l = Log(str(os.path.basename(__file__)))

        if Game.__instance is None:
            Game.__instance = object.__new__(cls)
        else: 
            l.log("y","__new__(): Instance already existing!")

        #set members to instance (instance overwritten if reinitialized)
        Game.__instance.player1 = Player(player1Name, player1Color)
        Game.__instance.player2 = Player(player2Name, player2Color)
        Game.__instance.p1Mode = "human"
        Game.__instance.p2Mode = "human"
        stateArray = [Points() for x in range(25)]
        Game.__instance.currentState = State(stateArray, Game.__instance.player1, Game.__instance.player2)

        return Game.__instance  

    def setGameMode(self,p1Mode,p2Mode):
        #inititalize logger
        l = Log(str(os.path.basename(__file__)))

        l.log("g","setGameMode(): Player1: " +p1Mode + " ; Player2: " +p2Mode)
        self.p1Mode = p1Mode
        self.p2Mode = p2Mode
    
    
