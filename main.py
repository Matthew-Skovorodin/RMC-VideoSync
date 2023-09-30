# IMPORT PYSIDE2
import sys # sys.exit used to safely exit from the program in case of generation of an exception
import os # os.getcwd() used to grab current working directory
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import * # provides many basic Qt functions, ex. QPropertyAnimation
from PySide2.QtGui import * # GUI functionality
from PySide2.QtWidgets import * # provides a set of UI elements

# IMPORT MATPLOTLIB
import matplotlib # handles all our plotting 
import matplotlib.pyplot as plt
from matplotlib.animation import TimedAnimation
from matplotlib.lines import Line2D
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

# IMPORT SECONDARY LIBRARIES
import csv # library for processing .csv files efficiently 
import warnings # avoids screen geometry warning
import time # used to delay time between user inputs, and to slow video playback
import threading # spawns another thread to handle video playback
import numpy as np # useful for list manipulation
import keyboard # keyboard input from user
import cv2 # opencv library handles video import and playback

# GUI FILES & FUNCTION(S)
from ui_main import Ui_MainWindow
from ui_loading import Ui_Dialog as Form
from ui_functions import * # ui_functions handles all user input

# ignores error when capturing screen dimensions
warnings.filterwarnings("ignore", category=DeprecationWarning) 

''' Class: MainWindow
 | ------------------------------
 | Description:
 |     Creates and sets up main window along with calling functions
 |     based on button trigger events. It also contains a callback
 |     function when drawing the plot. 
'''
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Grab screen resolution for sizing the video widget
        screen_resolution = app.desktop().screenGeometry()
        width, height = screen_resolution.width(), screen_resolution.height()

        # Initialize UI elements
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Toggle Menu Event Connectors
        self.ui.Btn_Video.clicked.connect(lambda: UI_Functions.video_import(self, True, width, height))
        self.ui.Btn_Import.clicked.connect(lambda: UI_Functions.file_import(self, True))
        self.ui.listWidget.itemClicked.connect(lambda: UI_Functions.queue_parameters(self, True))
        self.ui.listSettings.itemClicked.connect(lambda: UI_Functions.settings_selection(self, True))
        self.ui.Btn_Run.clicked.connect(lambda: UI_Functions.run_check(self, True, width, height))
        self.ui.Btn_Help.clicked.connect(lambda: UI_Functions.run_help(self, True))
        self.show()

        # Startup Menu Animation
        self.setup_startup_menu_animation(width, height)

    def setup_startup_menu_animation(self, width, height):
        UI_Functions.settings_adjustment(self)
        animations = [
            ('aniParameters', 0, 40, self.ui.Label_Parameters, 800, b"maximumSize"),
            ('aniParametersLine', 0, 1, self.ui.Line_Parameters, 100, b"maximumSize"),
            ('aniSettings', 0, 40, self.ui.Label_Settings, 800, b"maximumSize"),
            ('aniSettingsLine', 0, 1, self.ui.Line_Settings, 100, b"maximumSize"),
            ('aniEmpty', 0, 40, self.ui.Empty, 800, b"maximumSize")
        ]
        for ani_name, start_val, end_val, target_widget, duration, attr in animations:
            UI_Functions.animate_menu(self, ani_name, start_val, end_val, target_widget, duration, attr)

    def add_data_callback_left(self, value):
        self.myFig.add_data_left(value)

    def add_data_callback_right(self, value):
        self.myFig.add_data_right(value)

    def add_x_axis_callback_left(self, value):
        self.myFig.add_x_axis_left(value)

    def add_x_axis_callback_right(self, value):
        self.myFig.add_x_axis_right(value)

    def open_dialog(self, filePathVideo, width, height):
        dialog = QtWidgets.QDialog()
        dialog.ui = Form()
        frameList = dialog.ui.setupUi(self.ui, dialog, filePathVideo, width, height)
        dialog.exec_()
        result = frameList.result_queue.get()
        return result


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setAttribute(Qt.AA_DisableWindowContextHelpButton)
    window = MainWindow()
    sys.exit(app.exec_())