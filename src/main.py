#main.py

import os
from game import Game
from logger import Log

#main file containing process loop 

#process for running program until game is finished
def processLoop():

    #inititalize logger
    l = Log(str(os.path.basename(__file__)))
    
    l.log("g","processLoop(): started")
    
    #ask user which game mode is prefered
    # PvP / player versus AI / AI versus AI
    
    p1Mode = "human"
    p2Mode = "human"
     
    #ask user for player names + colors
    p1Name = "Hans"
    p1Color = "white"
    
    p2Name = "Roswitha"
    p2Color = "black"

    #initialize game instance    
    game = Game(p1Name,p1Color,p2Name,p2Color)
    game.setGameMode(p1Mode,p2Mode)
    
    
    l.log("g","processLoop(): killed")

processLoop()

