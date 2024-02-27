# This Python file uses the following encoding: utf-8
# from util.file_helper import *

# WIN_WIDTH = int(turkey_load_config()["width"])
# WIN_HEIGHT = int(turkey_load_config()["height"])

ORIGIN_WIDTH = 1920
ORIGIN_HEIGHT = 1080
WIN_WIDTH = 960
WIN_HEIGHT = 540

class scale():
    def __init__(self, current_width, current_height, origin_width = ORIGIN_WIDTH, origin_height = ORIGIN_HEIGHT, win_width = WIN_WIDTH, win_height = WIN_HEIGHT):
        self.new_width = win_width * current_width / origin_width
        self.new_height = win_height * current_height / origin_height

    def get_new_width(self):
        return int(self.new_width)
        

    def get_new_height(self):
        return int(self.new_height)

class font():
    def __init__(self, current_font_size, origin_width = ORIGIN_WIDTH, win_width = WIN_WIDTH):
        self.new_font_size = win_width * current_font_size / origin_width

    def get_font_size(self):
        return int(self.new_font_size)

