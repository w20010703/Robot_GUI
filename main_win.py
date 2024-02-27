# This Python file uses the following encoding: utf-8
import sys
import time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from utils.scale import *
from utils.constant import *
# from util.file_helper import *

# SCREEN_ORIENTATION = int(turkey_load_config().get("screen_orientation", 270))
SCREEN_ORIENTATION = 0

class MAIN_WIN(QMainWindow):
    def __init__(self, inner_widget):
        """
        this is main window function
        """

        super().__init__(None)

        # main window
        self.centralwidget = QtWidgets.QWidget()
        self.setCentralWidget(self.centralwidget)
        self.inner_widget = inner_widget

        self.scene = QGraphicsScene()
        self.scene.setSceneRect(0, 0, WIN_WIDTH, WIN_HEIGHT)
        self.proxy = QGraphicsProxyWidget()
        self.proxy = self.scene.addWidget(self.inner_widget)

        self.view = QGraphicsView(self.centralWidget())
        self.view.setScene(self.scene)

        self.view.setFixedSize(WIN_WIDTH, WIN_HEIGHT);
        self.view.setSceneRect(0, 0, WIN_WIDTH, WIN_HEIGHT);

        self.view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        # Adjust this so that main window rotate.
        self.view.rotate(SCREEN_ORIENTATION)
        self.resize(WIN_WIDTH, WIN_HEIGHT)
        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)


        self.show()



    def closeEvent(self, event):
        """
        close the system
        """

        write_log("end")
        return sys.exit()