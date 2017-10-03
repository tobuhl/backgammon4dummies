#game.py

#represents a backgammon game (singleton)
class Game:
    __instance = None     
    t = 2
         
    #ctor
    def __init__(self,x):
        self.t = x
    
    
    
    def __new__(cls, val):
       if Game.__instance is None:
           Game.__instance = object.__new__(cls)
       Game.__instance.val = val
       return Game.__instance    
    
    #TODO
    #add player
    #add currentState
    

    