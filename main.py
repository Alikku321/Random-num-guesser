import sys
import random
from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QLineEdit, QMessageBox
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import pyqtSlot

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Random number guesser'
        self.left = 10
        self.top = 10
        self.width = 400
        self.height = 140
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
    
        # Create min textbox
        self.textbox_min = QLineEdit(self)
        self.textbox_min.move(20, 20)
        self.textbox_min.resize(130,40)
        self.textbox_min.setPlaceholderText("Min")

        #second max textbox
        self.textbox_max = QLineEdit(self)
        self.textbox_max.move(160, 20)
        self.textbox_max.resize(130,40)
        self.textbox_max.setPlaceholderText("Max")
        
        
        # Create a button in the window
        self.button = QPushButton('Generate', self)
        self.button.move(20,80)
        
        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        self.show()
    
    @pyqtSlot()
    def on_click(self):
        try:
            min_value = int(self.textbox_min.text())
            max_value = int(self.textbox_max.text())
            random_value = random.randint(min_value, max_value)
            QMessageBox.information(self, "Random number", f"Your random number is {random_value}")
            self.textbox_min.setText("")
            self.textbox_max.setText("")
        except ValueError:
            QMessageBox.warning(self, "Error", "Please enter valid numbers")
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec())