# backgammon4dummies
A simple backgammon game with AI

Python version
==============

We will use _Python3.5.2_ and maybe an IDE _Spider3_.
Checkstyle installation ```sudo apt install flake8```

output
======

To make the program usable (and improve testing), we will program a GUI. Since the board is static, the GUI will use some kind of Background picture

requirements
============

Packages needed for running backgammon4dummies:
 * python3.5
 * python3-pip
 * sudo pip3 install pyqt5

Packages needed for developement:
 * spyder3
 * sudo pip3 install rope_py3k  (for autocompletion in spyder)

start
=====

 * data structure?
 * possible moves
  * rules
  * was one token kicked (outside of board) <-- this must be the token to move
  * are all tokens in the _house_ (i.e. last quarter of board)?


Implementation
==============

 * state - class
  * dice roll
  * who is next?
  * two arrays holding the token allocation
  * method: proposed_move_valid()?
 * GUI
 * tests
 * no server-client model, but only single program.

Design Patterns
===============

For architecture of a structured software, design patterns should be used.

model-view-controller:
* view
  * GUI
* model
  * state
* controller
  * main
  * etc.

singleton:
* game

TODOs
=====
* GUI:
  We need the functionality of closing the current window when a button (OK, Cancel) is clicked.
  * GameModeWindow: 
    * add the members okClicked,cancelClicked which are initially false and set true when the certain button is clicked
    * add the members p1Mode, p2Mode which are initially "human" and set to the respective value due to the radio button state
  * PlayerModeWindow: 
    * add the members okClicked,cancelClicked which are initially false and set true when the certain button is clicked
    * add the members p1Name,p2Name which represents the names and set to the values in the text boxes
    * add the members p1Color,p2Color which are the colors ("black", "white") of the players
  * WinnerWindow: 
    * add the members okClicked,cancelClicked which are initially false and set true when the certain button is clicked



