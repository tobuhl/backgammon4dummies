#main.py

import os

from game import Game

#main file containing process loop 

#helper-class for colored console output
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    

#debug output
verbose = True

#process for running program until game is finished
def processLoop():
    if verbose: 
        print(bcolors.OKGREEN + os.path.basename(__file__) + "->processLoop(): started" + bcolors.ENDC)
    
    #ask user which game mode is prefered
    # PvP / player versus AI / AI versus AI
    
    #TODO: QT 
    
    #initialize game instance    
    g = Game(1)
    
    #main loop
    #TODO

    if verbose: 
        print(bcolors.OKGREEN + os.path.basename(__file__) + "->processLoop(): ended" + bcolors.ENDC)


processLoop()

