#basic windows with pyqt5

import sys	
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
#from PyQt5 import QtGui, QtCore

class GameModeWindow(QWidget):

	def __init__(self):
		super().__init__()
		self.title = 'Backgammon4Dummies'
		self.left = 10
		self.top = 10
		self.width = 200
		self.height = 100

		self.gameMode()

	@pyqtSlot()	#create slot for OK
	def okClick(self):
		print('PyQt5 button click')

	@pyqtSlot()	#create slot for cancel
	def cancelClick(self):
		print('PyQt5 button click')

	def	gameMode(self):
		#main layout
		mainLayout = QVBoxLayout()

		#radiobuttons
		self.b1a = QRadioButton("human")
		self.b1a.setChecked(True)
		self.b2a = QRadioButton("computer")

		self.b1b = QRadioButton("human")
		self.b1b.setChecked(True)
		self.b2b = QRadioButton("computer")

		#groupbox
		group1 = QGroupBox('PLAYER 1')
		layoutGroup1 = QVBoxLayout()
		layoutGroup1.addWidget(self.b1a)
		layoutGroup1.addWidget(self.b2a)
		group1.setLayout(layoutGroup1)

		group2 = QGroupBox('PLAYER 2')
		layoutGroup2 = QVBoxLayout()
		layoutGroup2.addWidget(self.b1b)
		layoutGroup2.addWidget(self.b2b)
		group2.setLayout(layoutGroup2)

		upperLayout = QHBoxLayout()
		upperLayout.addWidget(group1)
		upperLayout.addWidget(group2)		

		#buttons
		okButton = QPushButton('Go on!', self)
		okButton.clicked.connect(self.okClick)

		cancelButton = QPushButton('Cancel', self)
		cancelButton.clicked.connect(self.cancelClick)

		buttonLayout = QHBoxLayout()
		buttonLayout.addWidget(okButton)
		buttonLayout.addWidget(cancelButton)

		mainLayout.addLayout(upperLayout)
		mainLayout.addLayout(buttonLayout)

		self.setLayout(mainLayout)

		self.setGeometry(self.left, self.top, self.width, self.height)
		self.setWindowTitle(self.title)
		self.show()

#__________________________________________________________________

class PlayerModeWindow(QWidget):

	def __init__(self):
		super().__init__()
		self.title = 'Backgammon4Dummies'
		self.left = 10
		self.top = 10
		self.width = 200
		self.height = 100

		self.playMode()

	@pyqtSlot()	#create slot for OK
	def okClick(self):
		print('PyQt5 button click')

	@pyqtSlot()	#create slot for cancel
	def cancelClick(self):
		print('PyQt5 button click')

	def	playMode(self):
		#main layout
		mainLayoutLarge = QVBoxLayout()

		#Player1 heading

		#NAME

		#radiobuttons
		self.buttonB = QRadioButton("black")
		self.buttonB.setChecked(True)
		self.buttonW = QRadioButton("white")

		group2PlayerMode = QGroupBox('What colour do you wanna have?')
		layoutGroup2Player = QVBoxLayout()
		layoutGroup2Player.addWidget(self.buttonB)
		layoutGroup2Player.addWidget(self.buttonW)
		group2PlayerMode.setLayout(layoutGroup2Player)

		mainLayoutLarge.addWidget(group2PlayerMode)	#Verschachtelung

		self.setLayout(mainLayoutLarge)

		self.setGeometry(self.left, self.top, self.width, self.height)
		self.setWindowTitle(self.title)
		self.show()

if __name__=='__main__':
	application = QApplication(sys.argv)
	win = PlayerModeWindow()
	sys.exit(application.exec_())
	
