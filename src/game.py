#game.py

import os
from logger import Log

#represents a backgammon game (singleton)
class Game:
    __instance = None
    __t = 2

    #ctor
    def __init__(self, x):
        self.__t = x

    def __new__(cls, val):
        #inititalize logger
        l = Log(str(os.path.basename(__file__)))

        if Game.__instance is None:
            Game.__instance = object.__new__(cls)
        else: 
            l.log("y","__new__(): Instance already existing!")
        Game.__instance.val = val
        return Game.__instance  

    def getter(self):
        return self.__t  
    
    #TODO
    #add player
    #add currentState
    

    
