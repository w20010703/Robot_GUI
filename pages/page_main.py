# This Python file uses the following encoding: utf-8
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from utils.scale import *
from utils.constant import *
from utils.thread_helper import *

import time
import random
import cv2
import sys

class Thread(QThread):
    changePixmap = pyqtSignal(QImage)

    def __init__(self, parent, w, h):
        super().__init__(parent)
        self.w = w
        self.h = h

    def run(self):
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            if ret:
                # https://stackoverflow.com/a/55468544/6622587
                rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                h, w, ch = rgbImage.shape
                bytesPerLine = ch * w
                convertToQtFormat = QImage(rgbImage.data, w, h, bytesPerLine, QImage.Format_RGB888)
                p = convertToQtFormat.scaled(self.w, self.h, Qt.KeepAspectRatio)
                self.changePixmap.emit(p)


class Streaming(QWidget):
    def __init__(self, parent, w, h):
        super().__init__(parent)
        self.w = w
        self.h = h
        self.initUI()

    @pyqtSlot(QImage)
    def setImage(self, image):
        self.label.setPixmap(QPixmap.fromImage(image))

    def initUI(self):
        # create a label
        self.label = QLabel(self)
        self.label.move(0, 0)
        self.label.resize(self.w, self.h)
        th = Thread(self, self.w, self.h)
        th.changePixmap.connect(self.setImage)
        th.start()


class PAGE_MAIN(QWidget):

    def __init__(self):
        """
        this is main page
        """
        super(PAGE_MAIN, self).__init__()
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
        self.backgroudWidget.setStyleSheet("background-color: #2D2D2D;")

        # streaming section
        video_xy = scale(10, 10)
        video_wh = scale(1900, 890)
        self.video_streaming = Streaming(self.backgroudWidget, video_wh.get_new_width(), video_wh.get_new_height())
        self.video_streaming.setGeometry(QtCore.QRect(video_xy.get_new_width(), video_xy.get_new_height(), video_wh.get_new_width(), video_wh.get_new_height()))
        self.video_streaming.setStyleSheet("background-color: #000000;")

        # btn section
        go_to_target_btn_xy = scale(10, 910)
        go_to_target_btn_wh = scale(467.5, 80)
        self.go_to_target_btn = QtWidgets.QPushButton(self.backgroudWidget)
        self.go_to_target_btn.setText("MOVE")
        self.go_to_target_btn.setFont(big_qfont_type)
        self.go_to_target_btn.setGeometry(QtCore.QRect(go_to_target_btn_xy.get_new_width(), go_to_target_btn_xy.get_new_height(), go_to_target_btn_wh.get_new_width(), go_to_target_btn_wh.get_new_height()))
        self.go_to_target_btn.setStyleSheet("background-color: #00b4d8; color: #000000")
        self.go_to_target_btn.clicked.connect(self.clicked_go_to_target_btn)

        pause_start_xy = scale(487.5, 910)
        pause_start_wh = scale(467.5, 80)
        self.pause_start_flag = False
        self.pause_start = QtWidgets.QPushButton(self.backgroudWidget)
        self.pause_start.setText("PAUSE")
        self.pause_start.setFont(big_qfont_type)
        self.pause_start.setGeometry(QtCore.QRect(pause_start_xy.get_new_width(), pause_start_xy.get_new_height(), pause_start_wh.get_new_width(), pause_start_wh.get_new_height()))
        self.pause_start.setStyleSheet("background-color: #edaf00; color: #000000")
        self.pause_start.clicked.connect(self.clicked_pause_start)

        start_action_xy = scale(965, 910)
        start_action_wh = scale(467.5, 80)
        self.start_action = QtWidgets.QPushButton(self.backgroudWidget)
        self.start_action.setText("START ACTION")
        self.start_action.setFont(big_qfont_type)
        self.start_action.setGeometry(QtCore.QRect(start_action_xy.get_new_width(), start_action_xy.get_new_height(), start_action_wh.get_new_width(), start_action_wh.get_new_height()))
        self.start_action.setStyleSheet("background-color: #08a045; color: #000000")
        self.start_action.clicked.connect(self.clicked_start_action)

        force_quit_xy = scale(1442.5, 910)
        force_quit_wh = scale(467.5, 80)
        self.force_quit = QtWidgets.QPushButton(self.backgroudWidget)
        self.force_quit.setText("QUIT")
        self.force_quit.setFont(big_qfont_type)
        self.force_quit.setGeometry(QtCore.QRect(force_quit_xy.get_new_width(), force_quit_xy.get_new_height(), force_quit_wh.get_new_width(), force_quit_wh.get_new_height()))
        self.force_quit.setStyleSheet("background-color: #FF6666; color: #000000")
        self.force_quit.clicked.connect(self.clicked_force_quit)

        # logo section
        logo_xy = scale(10, 1000)
        logo_wh = scale(372, 70)
        for x in range(5):
            if x % 2 == 0:
                _logo = QtWidgets.QWidget(self.backgroudWidget)
                _logo.setGeometry(QtCore.QRect(logo_xy.get_new_width()+(logo_xy.get_new_width()+logo_wh.get_new_width())*x, logo_xy.get_new_height(), logo_wh.get_new_width(), logo_wh.get_new_height()))
                _logo.setStyleSheet("border-image: url("+IMG_PATH+"nexuni_logo.png);")

    def clicked_go_to_target_btn(self):
        print("clicked_go_to_target_btn")

    def clicked_pause_start(self):
        print("clicked_pause_start")
        if self.pause_start_flag:
            # start to pause
            self.pause_start_flag = False
            self.pause_start.setText("PAUSE")
        else:
            # pause to start
            self.pause_start_flag = True
            self.pause_start.setText("START")

    def clicked_start_action(self):
        print("clicked_start_action")

    def clicked_force_quit(self):
        print("clicked_force_quit")

#         # set widget
#         bar_wh = scale(ORIGIN_WIDTH, 150)
#         main_wh = scale(ORIGIN_WIDTH, 780)
#         nav_bar_xy = scale(0, 0)
#         self.nav_bar = QtWidgets.QWidget(self.backgroudWidget)
#         self.nav_bar.setObjectName("nav_bar")
#         self.nav_bar.setGeometry(QtCore.QRect(nav_bar_xy.get_new_width(), nav_bar_xy.get_new_height(), bar_wh.get_new_width(), bar_wh.get_new_height()))
#         self.nav_bar.setStyleSheet("background-color: "+BLUE_NAV_BAR+";")

#         page_bg_xy = scale(0, 150)
#         self.page_bg = QtWidgets.QWidget(self.backgroudWidget)
#         self.page_bg.setObjectName("page_bg")
#         self.page_bg.setGeometry(QtCore.QRect(page_bg_xy.get_new_width(), page_bg_xy.get_new_height(), main_wh.get_new_width(), main_wh.get_new_height()))
#         self.page_bg.setStyleSheet("background-color: "+BLUE_BG+";")

#         footer_bar_xy = scale(0, 930)
#         self.footer_bar = QtWidgets.QWidget(self.backgroudWidget)
#         self.footer_bar.setObjectName("footer_bar")
#         self.footer_bar.setGeometry(QtCore.QRect(footer_bar_xy.get_new_width(), footer_bar_xy.get_new_height(), bar_wh.get_new_width(), bar_wh.get_new_height()))
#         self.footer_bar.setStyleSheet("background-color: "+BLUE_FOOTER_BAR+";")

#         # nav btn section (btn)
#         logo_xy = scale(54, 31)
#         logo_wh = scale(388, 85)
#         self.logo = QtWidgets.QWidget(self.nav_bar)
#         self.logo.setObjectName("logo")
#         self.logo.setGeometry(QtCore.QRect(logo_xy.get_new_width(), logo_xy.get_new_height(), logo_wh.get_new_width(), logo_wh.get_new_height()))
#         self.logo.setStyleSheet("border-image: url("+IMG_PATH+"nexuni_logo.png);")

#         manual_btn_xy = scale(1105, 31)
#         manual_btn_wh = scale(371, 88)
#         self.manual_btn = QtWidgets.QPushButton(self.nav_bar)
#         self.manual_btn.setText("MANUAL CONTROL")
#         self.manual_btn.setFont(big_qfont_type)
#         self.manual_btn.setGeometry(QtCore.QRect(manual_btn_xy.get_new_width(), manual_btn_xy.get_new_height(), manual_btn_wh.get_new_width(), manual_btn_wh.get_new_height()))
#         self.manual_btn.setObjectName("manual_btn")
#         self.manual_btn.setStyleSheet("background-color: " + YELLOW_BTN_BG + "; border-radius: " + str(int(manual_btn_wh.get_new_height() * 1 / 2)) + "px; color: " + YELLOW_BTN_WORD + ";\n")

#         quit_btn_xy = scale(1497, 31)
#         quit_btn_wh = scale(371, 88)
#         self.quit_btn = QtWidgets.QPushButton(self.nav_bar)
#         self.quit_btn.setText("EMERGECY STOP")
#         self.quit_btn.setFont(big_qfont_type)
#         self.quit_btn.setGeometry(QtCore.QRect(quit_btn_xy.get_new_width(), quit_btn_xy.get_new_height(), quit_btn_wh.get_new_width(), quit_btn_wh.get_new_height()))
#         self.quit_btn.setObjectName("quit_btn")
#         self.quit_btn.setStyleSheet("background-color: " + RED_BTN_BG + "; border-radius: " + str(int(quit_btn_wh.get_new_height() * 1 / 2)) + "px; color: " + RED_BTN_WORD + ";\n")


#         # start btn (step 1)
#         start_btn_xy = scale(575, 230)
#         start_btn_wh = scale(770, 320)
#         self.start_btn = QtWidgets.QPushButton(self.page_bg)
#         self.start_btn.setGeometry(QtCore.QRect(start_btn_xy.get_new_width(), start_btn_xy.get_new_height(), start_btn_wh.get_new_width(), start_btn_wh.get_new_height()))
#         self.start_btn.setObjectName("start_btn")
#         self.start_btn.setStyleSheet("border-image: url("+IMG_PATH+"start_btn.png);")
#         self.start_btn.clicked.connect(self.clicked_btn)

#         # qrcode section (step 2)
#         qr_img_xy = scale(408, 87)
#         qr_img_wh = scale(1104, 606)
#         self.qr_img = QtWidgets.QPushButton(self.page_bg)
#         self.qr_img.setObjectName("qr_img")
#         self.qr_img.setGeometry(QtCore.QRect(qr_img_xy.get_new_width(), qr_img_xy.get_new_height(), qr_img_wh.get_new_width(), qr_img_wh.get_new_height()))
#         self.qr_img.setStyleSheet("border-image: url("+IMG_PATH+"qr_scan.png);")
#         self.qr_img.clicked.connect(self.start_processing)
#         self.qr_img.hide()

#         # processing section (step 3)
#         processing_gif_xy = scale(720, 320)
#         processing_gif_wh = scale(480, 140)
#         self.processing_gif = QtWidgets.QLabel(self.page_bg)
#         self.processing_gif.setObjectName("processing_gif")
#         self.processing_gif.setGeometry(QtCore.QRect(processing_gif_xy.get_new_width(), processing_gif_xy.get_new_height(), processing_gif_wh.get_new_width(), processing_gif_wh.get_new_height()))
#         self.movie = QMovie(IMG_PATH+"processing.gif")
#         self.processing_gif.setMovie(self.movie)
#         self.processing_gif.hide()

#         # log section
#         log_section_xy = scale(1115, 34)
#         log_section_wh = scale(753, 82)
#         self.log_section = QtWidgets.QLabel(self.footer_bar)
#         self.log_section.setText("[MANUAL CONTROL]")
#         self.log_section.setFont(semi_big_qfont_type)
#         self.log_section.setWordWrap(True)
#         self.log_section.setObjectName("log_section")
#         self.log_section.setGeometry(QtCore.QRect(log_section_xy.get_new_width(), log_section_xy.get_new_height(), log_section_wh.get_new_width(), log_section_wh.get_new_height()))
#         self.log_section.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
#         self.log_section.setStyleSheet("color: " + BLUE_LOG + ";\n")
        
#     def reset_data(self):
#         self.start_btn.show()
#         self.qr_img.hide()
#         self.processing_gif.hide()
#         self.log_section.setText("[MANUAL CONTROL]")

#     def clicked_btn(self):
#         self.start_btn.hide()
#         self.qr_img.show()
#         self.qrcode_thread.start()

#     def start_processing(self):
#         self.qr_img.hide()
#         self.processing_gif.show()
#         self.movie.start()

#     def handle_qrcode_data(self, qr_data):
#         print("qr_data: ", qr_data)
#         if qr_data != "None":
#             self.start_processing()
#         else:
#             print("[Error]: qr_data == None")
#             self.start_processing()

# class STATUS_BAR(QWidget):

#     def __init__(self, list_len):
#         super(STATUS_BAR, self).__init__(list_len)
#         self.list_len = list_len
#         self.selected_status_wh = scale(548, 83)
#         self.unselected_status_wh = scale(49, 49)
#         self.setupUi()

#     def setupUi(self):
#         self.selected_status = QtWidgets.QLabel(self)
#         self.selected_status.setText("[MANUAL CONTROL]")
#         self.selected_status.setFont(semi_big_qfont_type)
#         self.selected_status.setWordWrap(True)
#         self.selected_status.setObjectName("selected_status")
#         self.selected_status.setAlignment(Qt.AlignCenter)
#         self.selected_status.setGeometry(QtCore.QRect(selected_status_xy.get_new_width(), selected_status_xy.get_new_height(), self.selected_status_wh.get_new_width(), self.selected_status_wh.get_new_height()))
#         self.selected_status.setStyleSheet("background-color: "+BLUE_selected_status+";")

#         self.unselected_list = []
#         for i in range(list_len):
#             _unselected_status = QtWidgets.QLabel(self)
#             _unselected_status.setObjectName("_unselected_status")
#             _unselected_status.setAlignment(Qt.AlignCenter)
#             _unselected_status.setGeometry(QtCore.QRect(selected_status_xy.get_new_width(), selected_status_xy.get_new_height(), self.unselected_status_wh.get_new_width(), self.unselected_status_wh.get_new_height()))
#             _unselected_status.setStyleSheet("background-color: "+BLUE_selected_status+";")
#             self.unselected_list.append(_unselected_status)













