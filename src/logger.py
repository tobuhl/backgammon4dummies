#logger.py

import os
import datetime

#class for logging and output
class Log:

    __fileName = 'log.txt'
    __debug = True

    baseName = " "
    
    def __init__(self, basename):
        self.baseName = basename
        __debug = True

    def setVerbose(val):
        __debug = val

    def setBasename(basename):
        basename=basename

    def log(self, color,msg):
        #timestamp
        ts= str(datetime.datetime.now())

        #prepare string for output
        output = ts + "\t" + self.baseName + "\t" + msg

        #log to file
        with open(Log.__fileName, "a") as logFile:
            logFile.write(output + "\n")


        #console output 
        if Log.__debug:        
            if color == 'g':
                print(bcolors.OKGREEN + output + bcolors.ENDC)
            if color == 'r':
                print(bcolors.FAIL + output + bcolors.ENDC)   
            if color == 'y':
                print(bcolors.WARNING + output + bcolors.ENDC)
            
             
            
        



#helper class for colored console output
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
            
