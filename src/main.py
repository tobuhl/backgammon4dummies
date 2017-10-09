#main.py

import os
from game import *
from logger import *
from GUI import *
from PyQt5.QtCore import *
from PyQt5 import QtCore

#main file containing process loop 

#process for running program until game is finished
def processLoop():

    #inititalize logger
    l = Log(str(os.path.basename(__file__)))
    
    l.log("g","processLoop(): started")

    #start QApplication for QT GUI    
    application = QApplication(sys.argv)
    l.log("g","processLoop(): QApplication started")
    
    #ask user which game mode is prefered
    # PvP / player versus AI / AI versus AI    
    gmw = GameModeWindow()
    application.exec_()
    p1Mode = "human" #TODO
    p2Mode = "human" #TODO    
     
    #ask player1 for player name + color
    if p1Mode=="human":
        player1Window = PlayerModeWindow(True, 'white')
        application.exec_()
        p1Name = "Mensch1" #TODO
        p1Color = "white" #TODO
    else:
        p1Name = "KI1"
        p1Color = "white"

    l.log("g","processLoop(): Player1: Name=" + p1Name + " Color=" + p1Color)

    #ask player2 for player name + color
    if p2Mode=="human":
        if p1Mode=="human":
    
            #check color of human player1
            if p1Color=="white":
                player2Window = PlayerModeWindow(False, 'black')                
            else:
                player2Window = PlayerModeWindow(False, 'white')            
        else:
            #if p1 is AI -> 
            player2Window = PlayerModeWindow(True, 'black')

        application.exec_()
        p2Name = "Mensch2" #TODO
        p2Color = "black" #TODO
    else:
        p2Name = "KI2"
        p2Color = "black"
    
    l.log("g","processLoop(): Player2: Name=" + p2Name + " Color=" + p2Color)
    

    #initialize game instance    
    game = Game(p1Name,p1Color,p2Name,p2Color)
    game.setGameMode(p1Mode,p2Mode)
    
    #TODO
    #show main window



    #TODO
    #show winner window
    
    l.log("g","processLoop(): killed")
    l.log("g","\n\n\n")

processLoop()

