import sys
from PyQt6.QtCore import QSize, Qt 
from PyQt6.QtWidgets import QDialog, QLabel, QLineEdit,QVBoxLayout, QWidget, QApplication, QMainWindow, QPushButton, QMessageBox, QGridLayout, QHBoxLayout, QStackedLayout
"""define page widgets"""

class StartPageGUI(QWidget):
    def __init__(self, parent, controller):
        super().__init__()
        self.controller = controller
        self.parent = parent

        self.layout_start_page = QVBoxLayout()
        self.setLayout(self.layout_start_page)

        button_start = QPushButton('Start')
        button_quit = QPushButton('Quit')

        self.layout_start_page.addWidget(button_start)
        self.layout_start_page.addWidget(button_quit)

        button_start.clicked.connect(self.button_start_clicked)
        button_quit.clicked.connect(self.button_quit_clicked)

    def button_start_clicked(self):
        pass
    def button_quit_clicked(self):
        pass