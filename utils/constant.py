from PyQt5 import QtGui
from PyQt5.QtGui import *
from utils.scale import *

IMG_PATH = "/Users/julia/Documents/GitHub/Robot_GUI/img/"

# color constant
BLUE_NAV_BAR = "#00b4d8"
BLUE_FOOTER_BAR = "#90e0ef"
BLUE_BG = "#caf0f8"
BLUE_LOG = "#0077B6"

YELLOW_NAV_BAR = "#A86E2F"
YELLOW_FOOTER_BAR = "#F4CE89"
YELLOW_BG = "#FFF6CF"
YELLOW_LOG = "#914C00"

YELLOW_BTN_BG = "#FFE473"
YELLOW_BTN_WORD = "#D17200"
RED_BTN_BG = "#FF6666"
RED_BTN_WORD = "#FFFFFF"
BLUE_BTN_BG = "#00AAC1"
BLUE_BTN_WORD = "#FFFFFF"




DODAY_COLOR="#edaf00"
BG_COLOR="#ffffff"
MAIN_COLOR="#edaf00"
SUB_COLOR="#F0D89A"
WHITE_COLOR="#ffffff"
DARK_COLOR="#2d2d2d"
GREY_COLOR="#5a5a5a"
LIGHT_GREY="#dddddd"
SEMI_GREY="#a1a1a1"
BLACK_COLOR="#000000"

SWITCH_COLOR="rgba(0, 0, 0, 30%)"
BLACK_TRANSPARENT_COLOR="rgba(0, 0, 0, 60%)"
WHITE_TRANSPARENT_COLOR="rgba(255, 255, 255, 30%)"

# font size constant
win_size = scale(1080, 1920)

extreme_big_qfont_size = font(200)
extreme_big_qfont_type = QFont("Microsoft YaHei", extreme_big_qfont_size.get_font_size(), QtGui.QFont.Bold)

really_big_font_size = font(90)
really_big_qfont_type = QFont("Microsoft YaHei", really_big_font_size.get_font_size(), QtGui.QFont.Bold)

intermediate_big_font_size = font(70) # footer
intermediate_big_qfont_type = QFont("Microsoft YaHei", intermediate_big_font_size.get_font_size(), QtGui.QFont.Normal)

super_big_font_size = font(50)
super_big_qfont_type = QFont("Microsoft YaHei", super_big_font_size.get_font_size(), QtGui.QFont.Bold)

very_big_font_size = font(46)
very_big_qfont_type = QFont("Microsoft YaHei", very_big_font_size.get_font_size(), QtGui.QFont.Bold)

big_font_size = font(32) # togo, footer
big_qfont_type = QFont("Microsoft YaHei", big_font_size.get_font_size(), QtGui.QFont.Light)

semi_big_font_size = font(28)
semi_big_qfont_type = QFont("Microsoft YaHei", semi_big_font_size.get_font_size(), QtGui.QFont.Light)

intermediate_font_size = font(24) # nav bar, cart_item
intermediate_qfont_type = QFont("Microsoft YaHei", intermediate_font_size.get_font_size(), QtGui.QFont.Bold)

normal_font_size = font(18) # nav bar, cart_item
normal_qfont_type = QFont("Microsoft YaHei", normal_font_size.get_font_size(), QtGui.QFont.Bold)

small_font_size = font(14)
small_qfont_type = QFont("Microsoft YaHei", small_font_size.get_font_size(), QtGui.QFont.Normal)
