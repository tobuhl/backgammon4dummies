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

	def __init__(self, complexWindow):
		super().__init__()
		self.title = 'Backgammon4Dummies'
		self.left = 10
		self.top = 10
		self.width = 200
		self.height = 100
		self.complexWindow = complexWindow

		self.playMode()

	@pyqtSlot()	#create slot for OK
	def okClickPlayerMode(self):
		print('PyQt5 button click')

	@pyqtSlot()	#create slot for cancel
	def cancelClickPlayerMode(self):
		print('PyQt5 button click')

	def	playMode(self):
		#main layout
		mainLayoutPlayMode = QVBoxLayout()

		#Player1 heading
		if self.complexWindow == True:
			self.boxHeading = QLabel('                            player 1')
		else:
			self.boxHeading = QLabel('                      player 2')
		boxHeadingPlayer1 = QVBoxLayout()
		boxHeadingPlayer1.addWidget(self.boxHeading)
		
		#text box
		self.textbox = QLineEdit(self)
		self.textbox.move(20, 20)
		self.textbox.resize(280,40)

		group1PlayerMode = QGroupBox('What´s yout name?')
		layoutGroup1Player = QVBoxLayout()
		layoutGroup1Player.addWidget(self.textbox)
		group1PlayerMode.setLayout(layoutGroup1Player)

		#radiobuttons
		if self.complexWindow == True:
			self.buttonB = QRadioButton("black")
			self.buttonB.setChecked(True)
			self.buttonW = QRadioButton("white")

			group2PlayerMode = QGroupBox('What colour do you wanna have?')
			layoutGroup2Player = QVBoxLayout()
			layoutGroup2Player.addWidget(self.buttonB)
			layoutGroup2Player.addWidget(self.buttonW)
			group2PlayerMode.setLayout(layoutGroup2Player)
		else:
			self.group2PlayerOther = QLabel('Your colour is black.')
			player2 = QVBoxLayout()
			player2.addWidget(self.group2PlayerOther)

		#OK/Cancel button
		okButtonPlayerMode = QPushButton('I wanna play now!', self)
		okButtonPlayerMode.clicked.connect(self.okClickPlayerMode)

		cancelButtonPlayerMode = QPushButton('Cancel', self)
		cancelButtonPlayerMode.clicked.connect(self.cancelClickPlayerMode)

		buttonLayoutPlayerMode = QHBoxLayout()
		buttonLayoutPlayerMode.addWidget(okButtonPlayerMode)
		buttonLayoutPlayerMode.addWidget(cancelButtonPlayerMode)

		mainLayoutPlayMode.addLayout(boxHeadingPlayer1)
		mainLayoutPlayMode.addWidget(group1PlayerMode)
		if self.complexWindow == True:
			mainLayoutPlayMode.addWidget(group2PlayerMode)
		else:
			mainLayoutPlayMode.addLayout(player2)
		mainLayoutPlayMode.addLayout(buttonLayoutPlayerMode)

		self.setLayout(mainLayoutPlayMode)

		self.setGeometry(self.left, self.top, self.width, self.height)
		self.setWindowTitle(self.title)
		self.show()

if __name__=='__main__':
	application = QApplication(sys.argv)
	win = PlayerModeWindow(True)
	sys.exit(application.exec_())
	
