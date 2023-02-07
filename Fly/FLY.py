from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QDesktopWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import *
from PyQt5 import QtCore
import random


class Virus(QMainWindow):
    def __init__(self):
        super().__init__()

        # Get Screen, Window and Movable area - Widht and Height
        self.screen_width = QDesktopWidget().availableGeometry().width()
        self.screen_height = QDesktopWidget().availableGeometry().height()
        self.width = min(self.screen_width, self.screen_height) // 4
        self.height = self.width
        self.max_width = self.screen_width - self.width
        self.max_height = self.screen_height - self.height

        # Configure Window, Label and Pixmap
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.pixmap = QPixmap("horn-fly.png").scaled(self.width, self.height, QtCore.Qt.KeepAspectRatio)
        self.label = QLabel(self)
        self.label.setPixmap(self.pixmap)
        self.setGeometry(self.screen_width//2 - self.width//2, self.screen_height//2 - self.height//2, self.width, self.height)
        self.label.resize(self.width, self.height)

        # Modify label Mouse Enter Event
        self.label.installEventFilter(self)

    def eventFilter(self, object, event):
        if event.type() == QEvent.Enter:
            self.setGeometry(random.randint(0, self.max_width), random.randint(0, self.max_height), self.width, self.height)
        return False


app = QApplication([])

win = Virus()
win.show()

app.exec()