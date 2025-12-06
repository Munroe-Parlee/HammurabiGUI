import sys
from PyQt6.QtCore import QSize, Qt 
from PyQt6.QtWidgets import QTableView, QDialog, QLabel, QLineEdit,QVBoxLayout, QWidget, QApplication, QMainWindow, QPushButton, QMessageBox, QGridLayout, QHBoxLayout, QStackedLayout
from controller import Controller
from page_gui import StartPageGUI

class GameGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Hammurabi GUI')
        self.resize(1000, 500)

        self.controller = Controller()
        self.layout_stack = QStackedLayout()
        self.widget_stack = QWidget()

        self.widget_stack.setLayout(self.layout_stack)
        self.setCentralWidget(self.widget_stack)

        widget_start_page = StartPageGUI(self, self.controller)
        self.layout_stack.addWidget(widget_start_page)



def main():
    app = QApplication(sys.argv)
    window = GameGUI()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()
