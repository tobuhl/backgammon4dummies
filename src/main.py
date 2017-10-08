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
    
    #TODO: QT 
    
    #initialize game instance    
    g1 = Game(3)
    g2 = Game(4)
    
    #main loop
    #TODO

    l.log("g","processLoop(): ended")

processLoop()

