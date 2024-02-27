import sys
import time
import json
import subprocess
import _thread
import logging
import threading

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

# from util.file_helper import *
# from util.menu_helper import *
# from page.page_all_import import *
from page_handler import PageHandler
# from gadgethiServerUtils.GadgethiClient import *
# from DodayUtils.clienttools.DodayWebsocketClient import *

# # Online Menu Pull Utils
# def pull_online_menu(**configs):
#     client = GadgetHiClient(**configs)
#     response = client.client_get("online_cloud_server_http_url", {"service":"menu","operation":"get_turkey_menu","store_id":configs["store_id"], 
#         "menu_name": configs["menu_name"]}, gauth=True)
#     try:
#         data = json.loads(response)["message"]
#         write_yaml(configs["main_menu_path"], data, sort_keys=False)
#     except Exception as e:
#         logging.info("[Pull Online Menu] Failed to Get Online Menu: "+str(e))
#         pass

# def pull_online_availability(**configs):
#     client = GadgetHiClient(**configs)
#     response = client.client_get("online_cloud_server_http_url", {"service":"menu","operation":"get_doday_availability","store_id":configs["store_id"]}, gauth=True)
#     with configs["avail_lock"]:
#         try:
#             data = json.loads(response)["message"]
#             write_yaml(configs["availability_path"], data)
#         except Exception as e:
#             logging.info("[Pull Online Availability] Failed to Get Online Availability: "+str(e))
#             pass

# # It defines the websocket client message handler
# def handle_websocket_message(message, **configs):
#     """
#     Decode the message from websocket and handle 
#     it just like the service of a server.
#     """
#     operation = message["operation"]
#     logging.info("[Websocket Message Client] "+ str(message))
#     if operation == "sync_avail":
#         # Pull online availability
#         with configs["avail_lock"]:
#             write_yaml(configs["availability_path"], message["avail_data"])

def main():
    """
    Run main function
    """
    # init_log(LOG_FILE_PATH)

    # configs = {}
    # yaml_config = turkey_load_config()
    # configs.update(yaml_config)

    # # New Availability scheme
    # # Might need recovery method after disconnection
    # configs["avail_lock"] = threading.Lock()
    # wsclient = DodayWebsocketClient(**configs)
    # wsclient.assign_msg_handler(handle_websocket_message, **configs)
    # _thread.start_new_thread(wsclient.receiving, ())

    # pull_online_menu(**configs)
    # pull_online_availability(**configs)


    app = QApplication(sys.argv)

    test = PageHandler()
    # test = PageHandler(**configs)
    test.general_switch_page(test.page_main, test.page_main)()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()