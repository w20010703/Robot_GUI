#-*-coding:utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from main_win import MAIN_WIN

from pages.page_main import PAGE_MAIN
from pages.page_manual import PAGE_MANUAL

from utils.scale import *
from utils.constant import *

# from DodayUtils.order.OrderInfo import *
# from DodayUtils.order.DodayItem import *

# from gadgethiServerUtils.GadgethiClient import *

# from util.file_helper import *
# from util.menu_helper import *
# from util.thread_helper import *
# from util.availability_helper import *
# from util.member_coupon_helper import *

import yaml
import copy
import json
import ast
import time
from ctypes import *

class PageHandler:
	start_payment_signal = pyqtSignal()
	terminate_payment_signal = pyqtSignal()

	def __init__(self, **configs):
		super().__init__()

		# load all pages
		# ===========================================================
		self.page_main = PAGE_MAIN()
		# self.page_manual = PAGE_MANUAL()
		

		self.last_page = self.page_main
		self.next_page = []

		# set the main window
		self.main_p = MAIN_WIN(self.page_main)
		# # ===========================================================
		# # ===========================================================
		

		# connect the switching and data transforming between pages
		# ===========================================================
		# self.page_main.manual_btn.clicked.connect(self.general_switch_page(self.page_main, self.page_manual, action_before=[self.page_manual.reset_data], action_after=[]))
		# self.page_manual.auto_btn.clicked.connect(self.general_switch_page(self.page_manual, self.page_main, action_before=[self.page_main.reset_data], action_after=[]))
		
		# self.page_main.quit_btn.clicked.connect(self.quit_system)
		# self.page_manual.quit_btn.clicked.connect(self.quit_system)
		# ===========================================================
		# ===========================================================



	# utils function
	# ===============================================================
	def general_switch_page(self, now_page, next_page, action_before=[], action_after=[]):
		"""
		This is the funciton to switch page for all condition 
		If you want to do some extra action before/after switching page
		put the function in action_before/action_after, and it will execute the function before/after switching.
		and this function will also mamorize the last page for the last_page action
		"""
		inside_now_page = now_page
		inside_next_page = next_page


		def returnFunc(event="", inside_now_page=inside_now_page, inside_next_page=inside_next_page):
			for action in action_before:
				action()

			if inside_next_page == "last_page":
				inside_next_page = self.last_page

			self.last_page = inside_now_page
			self.main_p.proxy.setWidget(inside_next_page)
			self.main_p.scene.update()
			self.main_p.show()

			for action in action_after:
				action()

		return returnFunc

	def reset_data(self):
		pass

	def quit_system(self):
		print("[QUIT SYSTEM]")
	# ===============================================================
	# ===============================================================
		

		
