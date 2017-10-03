# backgammon4dummies
A simple backgammon game with AI

Python version
==============

We will use _Python3.5.2_ and maybe an IDE _Spider3_.

output
======

To make the program usable (and improve testing), we will progrm a GUI. Since the board is static, the GUI will use some kind of Background picture

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
  *
 * GUI
 * tests
 * no server-client model, but only single program.

Design Patterns
===============

For architecture of a software, a design pattern should be found. (controller, modell, view).
 * view
  * GUI
* model
 * state
* controller
  * main
  * etc.
