import sys
from PyQt6.QtCore import QSize, Qt 
from PyQt6.QtWidgets import QDialog, QLabel, QLineEdit,QVBoxLayout, QWidget, QApplication, QMainWindow, QPushButton, QMessageBox, QGridLayout, QHBoxLayout, QStackedLayout, QPlainTextEdit
"""define page widgets"""

class StartPageWidget(QWidget):
    def __init__(self, parent, controller):
        super().__init__()
        self.controller = controller
        self.parent = parent

        self.layout_page = QVBoxLayout()
        self.setLayout(self.layout_page)

        button_start = QPushButton('Start')
        button_quit = QPushButton('Quit')

        self.layout_page.addWidget(button_start)
        self.layout_page.addWidget(button_quit)

        button_start.clicked.connect(self.button_start_clicked)
        button_quit.clicked.connect(self.button_quit_clicked)

    def button_start_clicked(self):
        self.parent.set_central_widget(1)
        pass
    def button_quit_clicked(self):
        self.parent.close()
        pass

class InterfacePageWidget(QWidget):
    def __init__(self, parent, controller):
        super().__init__()
        self.controller = controller
        self.parent = parent

        self.layout_page = QVBoxLayout() 
        self.setLayout(self.layout_page)

        self.layout_header = QHBoxLayout()
        self.layout_line_edits = QGridLayout()
        self.layout_button_bar = QHBoxLayout()

        widget_header = QWidget()
        widget_line_edits = QWidget()
        widget_button_bar = QWidget()
        
        widget_header.setLayout(self.layout_header)
        widget_line_edits.setLayout(self.layout_line_edits)
        widget_button_bar.setLayout(self.layout_button_bar)

        self.layout_page.addWidget(widget_header)
        self.layout_page.addWidget(widget_line_edits)
        self.layout_page.addWidget(widget_button_bar)

        label_buy = QLabel('Buy')
        label_sell = QLabel('Sell')
        label_plant = QLabel('Plant')        
        label_feed = QLabel('Feed')

        self.plain_text_stats = QPlainTextEdit(f'{self.controller.get_stats()}')

        self.text_buy = QLineEdit()
        self.text_sell = QLineEdit()
        self.text_plant = QLineEdit()
        self.text_feed = QLineEdit()
        
        button_exit = QPushButton('Exit')
        button_clear = QPushButton('Clear')
        button_enter = QPushButton('Enter')

        button_exit.clicked.connect(self.button_exit_clicked)
        button_clear.clicked.connect(self.button_clear_clicked)
        button_enter.clicked.connect(self.button_enter_clicked)


        self.layout_header.addWidget(self.plain_text_stats)


        self.layout_line_edits.addWidget(label_buy, 0, 0)
        self.layout_line_edits.addWidget(label_sell, 1, 0)
        self.layout_line_edits.addWidget(label_plant, 2, 0)
        self.layout_line_edits.addWidget(label_feed, 3, 0)

        self.layout_line_edits.addWidget(self.text_buy, 0, 1)
        self.layout_line_edits.addWidget(self.text_sell, 1, 1)
        self.layout_line_edits.addWidget(self.text_plant, 2, 1)
        self.layout_line_edits.addWidget(self.text_feed, 3, 1)


        self.layout_button_bar.addWidget(button_exit)
        self.layout_button_bar.addWidget(button_clear)
        self.layout_button_bar.addWidget(button_enter)

    def button_exit_clicked(self):
        self.button_clear_clicked()
        self.parent.set_central_widget(0)
        pass

    def button_clear_clicked(self):
        self.text_buy.setText('')
        self.text_sell.setText('')
        self.text_plant.setText('')
        self.text_feed.setText('')
        pass

    def button_enter_clicked(self):
        try:
            buy = abs(int(self.text_buy.text()))
            sell = abs(int(self.text_sell.text()))
            plant = abs(int(self.text_plant.text()))
            feed = abs(int(self.text_feed.text()))
        except:
            button = QMessageBox.warning(self, 'Input Exception', 'Input invalid: non integer input')
            if button == QMessageBox.StandardButton.Ok:
                return
        
        try:
            self.controller.enter_input(buy, sell, plant, feed)
            self.refresh()
            self.button_clear_clicked()
        except:
            button = QMessageBox.warning(self, 'Input Exception', 'GameModel exception to input')
            if button == QMessageBox.StandardButton.Ok:
                return
        pass

    def refresh(self):
        self.plain_text_stats.setPlainText(self.controller.get_stats())

    
