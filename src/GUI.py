#basic window with pyqt5

import sys	
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class Window(QWidget):

	def __init__(self):
		super().__init__()
		self.title = 'Backgammon4Dummies'
		self.left = 10	#to do: change position to center
		self.top = 10
		self.width = 500
		self.height = 400
		self.showWinner()
		
	def showOptions(self):
		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.top, self.width, self.height)
		self.show()

	def showWinner(self):
		self.setGeometry(self.left, self.top, 300, 200)

		button = QPushButton('Yeah!', self)
		button.setToolTip('Hui')
		button.move(100,70)	#to do: change position to center
		button.clicked.connect(self.on_click)		

		self.show()

	@pyqtSlot()
	def on_click(self):
		print('PyQt5 button click')

		
if __name__=='__main__':
	application = QApplication(sys.argv)
	win = Window()
	sys.exit(application.exec_())
		
