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
        self.height = 200
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create min textbox
        self.textbox_min = QLineEdit(self)
        self.textbox_min.move(20, 20)
        self.textbox_min.resize(130,40)
        self.textbox_min.setPlaceholderText("Min")

        # Create max textbox
        self.textbox_max = QLineEdit(self)
        self.textbox_max.move(160, 20)
        self.textbox_max.resize(130,40)
        self.textbox_max.setPlaceholderText("Max")

        # Create a textbox for the user's guess
        self.textbox_guess = QLineEdit(self)
        self.textbox_guess.move(20, 80)
        self.textbox_guess.resize(130,40)
        self.textbox_guess.setPlaceholderText("Guess")

        # Create a button in the window
        self.button = QPushButton('Guess', self)
        self.button.move(20,140)

        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        self.show()

    @pyqtSlot()
    def on_click(self):
        try:
            min_value = int(self.textbox_min.text())
            max_value = int(self.textbox_max.text())
            self.number_to_guess = random.randint(min_value, max_value)  # generate a random number between min and max

            user_guess = int(self.textbox_guess.text())
            if user_guess < self.number_to_guess:
                QMessageBox.information(self, "Hint", "Too low! Try again.")
            elif user_guess > self.number_to_guess:
                QMessageBox.information(self, "Hint", "Too high! Try again.")
            else:
                QMessageBox.information(self, "Congratulations", "You guessed it!")
                self.textbox_guess.setText("")
                self.number_to_guess = random.randint(min_value, max_value)  # generate a new random number
        except ValueError:
            QMessageBox.warning(self, "Error", "Please enter valid numbers for min, max and guess")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec())