from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sys
import time
import json
import logging
import threading
from ctypes import *

from DodayUtils.peripherals.DodayApiLib import *

# yaml_config = turkey_load_config()
yaml_config = {}
DODAY_API = DodayApiLib(**yaml_config)
# if yaml_config["chpt_api_lib"]:
# 	CHPT_API = DodayApiLib(doday_api_lib=yaml_config["chpt_api_lib"], api_type=DodayAPIType.chpt)


class QrcodeThread(QThread):
	finish_scan_signal = pyqtSignal(str)
	
	def __init__(self):
		super(QrcodeThread, self).__init__()
		self.qr_scan_timeout = yaml_config.get("qr_scan_timeout", 35)

	def thread_terminate(self):
		self.quit()
		self.wait()

	def qr_terminate(self):
		DODAY_API.terminate_qr_scan()

	def run(self):
		qr_data = DODAY_API.get_qr_scan_data_com(self.qr_scan_timeout)
		logging.info("[QRCode Get Data] qr data: "+str(qr_data))
		
		self.finish_scan_signal.emit(str(qr_data))










