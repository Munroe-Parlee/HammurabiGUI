import sys
from PyQt6.QtCore import QSize, Qt 
from PyQt6.QtWidgets import QTableView, QDialog, QLabel, QLineEdit,QVBoxLayout, QWidget, QApplication, QMainWindow, QPushButton, QMessageBox, QGridLayout, QHBoxLayout, QStackedLayout

class GameGUI(QMainWindow):
    def __init__(self):
        super().__init__()

def main():
    app = QApplication(sys.argv)
    window = GameGUI()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()
