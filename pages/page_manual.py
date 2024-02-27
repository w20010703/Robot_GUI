# This Python file uses the following encoding: utf-8
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from utils.scale import *
from utils.constant import *

import time
import random

# import img_src.info_bg


class PAGE_MANUAL(QWidget):

    def __init__(self):
        """
        this is page manual
        """
        super(PAGE_MANUAL, self).__init__()
        self.setupUi()

    def setupUi(self):
        """
        set up page ui
        """

        # set main widget
        self.resize(ORIGIN_WIDTH, ORIGIN_HEIGHT)

        # set backgroud widget
        self.backgroudWidget = QtWidgets.QWidget(self)
        self.backgroudWidget.setObjectName("backgroudWidget")
        self.backgroudWidget.resize(ORIGIN_WIDTH, ORIGIN_HEIGHT)

        # set widget
        bar_wh = scale(ORIGIN_WIDTH, 150)
        main_wh = scale(ORIGIN_WIDTH, 780)
        nav_bar_xy = scale(0, 0)
        self.nav_bar = QtWidgets.QWidget(self.backgroudWidget)
        self.nav_bar.setObjectName("nav_bar")
        self.nav_bar.setGeometry(QtCore.QRect(nav_bar_xy.get_new_width(), nav_bar_xy.get_new_height(), bar_wh.get_new_width(), bar_wh.get_new_height()))
        self.nav_bar.setStyleSheet("background-color: "+YELLOW_NAV_BAR+";")

        page_bg_xy = scale(0, 150)
        self.page_bg = QtWidgets.QWidget(self.backgroudWidget)
        self.page_bg.setObjectName("page_bg")
        self.page_bg.setGeometry(QtCore.QRect(page_bg_xy.get_new_width(), page_bg_xy.get_new_height(), main_wh.get_new_width(), main_wh.get_new_height()))
        self.page_bg.setStyleSheet("background-color: "+YELLOW_BG+";")

        footer_bar_xy = scale(0, 930)
        self.footer_bar = QtWidgets.QWidget(self.backgroudWidget)
        self.footer_bar.setObjectName("footer_bar")
        self.footer_bar.setGeometry(QtCore.QRect(footer_bar_xy.get_new_width(), footer_bar_xy.get_new_height(), bar_wh.get_new_width(), bar_wh.get_new_height()))
        self.footer_bar.setStyleSheet("background-color: "+YELLOW_FOOTER_BAR+";")


        # nav btn section (btn)
        logo_xy = scale(54, 31)
        logo_wh = scale(388, 85)
        self.logo = QtWidgets.QWidget(self.nav_bar)
        self.logo.setObjectName("logo")
        self.logo.setGeometry(QtCore.QRect(logo_xy.get_new_width(), logo_xy.get_new_height(), logo_wh.get_new_width(), logo_wh.get_new_height()))
        self.logo.setStyleSheet("border-image: url("+IMG_PATH+"nexuni_logo.png);")

        auto_btn_xy = scale(1105, 31)
        auto_btn_wh = scale(371, 88)
        self.auto_btn = QtWidgets.QPushButton(self.nav_bar)
        self.auto_btn.setText("AUTO CONTROL")
        self.auto_btn.setFont(big_qfont_type)
        self.auto_btn.setGeometry(QtCore.QRect(auto_btn_xy.get_new_width(), auto_btn_xy.get_new_height(), auto_btn_wh.get_new_width(), auto_btn_wh.get_new_height()))
        self.auto_btn.setObjectName("auto_btn")
        self.auto_btn.setStyleSheet("background-color: " + BLUE_BTN_BG + "; border-image: url(:/img/img/transparent.png); border-radius: " + str(int(auto_btn_wh.get_new_height() * 1 / 2)) + "px; color: " + BLUE_BTN_WORD + ";\n")

        quit_btn_xy = scale(1497, 31)
        quit_btn_wh = scale(371, 88)
        self.quit_btn = QtWidgets.QPushButton(self.nav_bar)
        self.quit_btn.setText("EMERGECY STOP")
        self.quit_btn.setFont(big_qfont_type)
        self.quit_btn.setGeometry(QtCore.QRect(quit_btn_xy.get_new_width(), quit_btn_xy.get_new_height(), quit_btn_wh.get_new_width(), quit_btn_wh.get_new_height()))
        self.quit_btn.setObjectName("quit_btn")
        self.quit_btn.setStyleSheet("background-color: " + RED_BTN_BG + "; border-image: url(:/img/img/transparent.png); border-radius: " + str(int(quit_btn_wh.get_new_height() * 1 / 2)) + "px; color: " + RED_BTN_WORD + ";\n")


        # btn section
        btn_wh = scale(278, 168)
        stop_btn_wh = scale(408, 168)

        up_btn_xy = scale(821, 69)
        self.up_btn = QtWidgets.QPushButton(self.page_bg)
        self.up_btn.setGeometry(QtCore.QRect(up_btn_xy.get_new_width(), up_btn_xy.get_new_height(), btn_wh.get_new_width(), btn_wh.get_new_height()))
        self.up_btn.setObjectName("up_btn")
        self.up_btn.setStyleSheet("border-image: url("+IMG_PATH+"up_btn.png);")
        self.up_btn.clicked.connect(lambda: self.clicked_btn("UP!!!!!!!", "up_sign"))

        down_btn_xy = scale(821, 543)
        self.down_btn = QtWidgets.QPushButton(self.page_bg)
        self.down_btn.setGeometry(QtCore.QRect(down_btn_xy.get_new_width(), down_btn_xy.get_new_height(), btn_wh.get_new_width(), btn_wh.get_new_height()))
        self.down_btn.setObjectName("down_btn")
        self.down_btn.setStyleSheet("border-image: url("+IMG_PATH+"down_btn.png);")
        self.down_btn.clicked.connect(lambda: self.clicked_btn("DOWN!!!!!!!", "down_sign"))

        left_btn_xy = scale(376, 306)
        self.left_btn = QtWidgets.QPushButton(self.page_bg)
        self.left_btn.setGeometry(QtCore.QRect(left_btn_xy.get_new_width(), left_btn_xy.get_new_height(), btn_wh.get_new_width(), btn_wh.get_new_height()))
        self.left_btn.setObjectName("left_btn")
        self.left_btn.setStyleSheet("border-image: url("+IMG_PATH+"left_btn.png);")
        self.left_btn.clicked.connect(lambda: self.clicked_btn("LEFT!!!!!!!", "left_sign"))

        right_btn_xy = scale(1266, 306)
        self.right_btn = QtWidgets.QPushButton(self.page_bg)
        self.right_btn.setGeometry(QtCore.QRect(right_btn_xy.get_new_width(), right_btn_xy.get_new_height(), btn_wh.get_new_width(), btn_wh.get_new_height()))
        self.right_btn.setObjectName("right_btn")
        self.right_btn.setStyleSheet("border-image: url("+IMG_PATH+"right_btn.png);")
        self.right_btn.clicked.connect(lambda: self.clicked_btn("RIGHT!!!!!!!", "right_sign"))

        stop_btn_xy = scale(756, 306)
        self.stop_btn = QtWidgets.QPushButton(self.page_bg)
        self.stop_btn.setGeometry(QtCore.QRect(stop_btn_xy.get_new_width(), stop_btn_xy.get_new_height(), stop_btn_wh.get_new_width(), stop_btn_wh.get_new_height()))
        self.stop_btn.setObjectName("stop_btn")
        self.stop_btn.setStyleSheet("border-image: url("+IMG_PATH+"stop_btn.png);")
        self.stop_btn.clicked.connect(lambda: self.clicked_btn("STOP!!!!!!!", "stop_sign"))


        # log section
        direction_sign_xy = scale(51, 34)
        direction_sign_wh = scale(75, 82)
        self.direction_sign = QtWidgets.QPushButton(self.footer_bar)
        self.direction_sign.setGeometry(QtCore.QRect(direction_sign_xy.get_new_width(), direction_sign_xy.get_new_height(), direction_sign_wh.get_new_width(), direction_sign_wh.get_new_height()))
        self.direction_sign.setObjectName("direction_sign")
        self.direction_sign.setStyleSheet("border-image: url("+IMG_PATH+"stop_sign.png);")

        log_section_xy = scale(1115, 34)
        log_section_wh = scale(753, 82)
        self.log_section = QtWidgets.QLabel(self.footer_bar)
        self.log_section.setText("[MANUAL CONTROL]")
        self.log_section.setFont(semi_big_qfont_type)
        self.log_section.setWordWrap(True)
        self.log_section.setObjectName("log_section")
        self.log_section.setGeometry(QtCore.QRect(log_section_xy.get_new_width(), log_section_xy.get_new_height(), log_section_wh.get_new_width(), log_section_wh.get_new_height()))
        self.log_section.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.log_section.setStyleSheet("color: " + YELLOW_LOG + ";\n")

    def clicked_btn(self, direction, direction_img):
        self.log_section.setText("[MANUAL CONTROL: MOVE ROBOT " + direction + "]")
        self.direction_sign.setStyleSheet("border-image: url("+IMG_PATH+direction_img+".png);")

    def reset_data(self):
        self.log_section.setText("[MANUAL CONTROL]")
        self.direction_sign.setStyleSheet("border-image: url("+IMG_PATH+"stop_sign.png);")



