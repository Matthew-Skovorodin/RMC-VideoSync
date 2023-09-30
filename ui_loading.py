import threading
import time
from time import perf_counter

import cv2
import qimage2ndarray
from PySide2 import QtWidgets, QtCore
from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
import queue
import os

''' Class: Ui_Dialog
 | ------------------------------
 | Description:
 |     Creates and sets up loading window along with handling 
 |     the processing of the imported video file
 | Return Value:
 |     videoFrames - contains all frames of the imported video
'''
class Ui_Dialog(object):
    global video
    video = None
    global frameList
    frameList = None
    global pathIcon, pathResources
    pathIcon = os.getcwd() + "\\" + "icons\\"
    pathResources = os.getcwd() + "\\" + "resources\\"

    def setupUi(self, menu, Dialog, filePathVideo, width, height):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(420, 200)
        Dialog.setMinimumSize(QSize(420, 200))
        Dialog.setMaximumSize(QSize(420, 200))
        Dialog.setWindowOpacity(0.950000000000000)
        Dialog.setStyleSheet(u"background-color:rgb(45, 45, 45)")
        self.horizontalLayout = QHBoxLayout(Dialog)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(Dialog)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(420, 200))
        self.stackedWidget.setMaximumSize(QSize(420, 200))
        self.LoadingWidget = QWidget()
        self.LoadingWidget.setObjectName(u"LoadingWidget")
        self.stackedWidget.addWidget(self.LoadingWidget)

        ''' Delta window icon '''
        DeltaLogo = QIcon()
        DeltaLogo.addFile(pathIcon + "logo.png", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(DeltaLogo)

        self.horizontalLayout.addWidget(self.stackedWidget)
        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
        Dialog.ui.createIcons()
        Dialog.ui.importLoadingBar()
        videoFrames = Dialog.ui.runThread(menu, Dialog, filePathVideo, width, height)
        return videoFrames

    ''' Imports loading bar video into a list of frames'''
    def importLoadingBar(self):
        capture = cv2.VideoCapture(pathResources + 'LoadingBar.avi')
        fps = int(capture.get(cv2.CAP_PROP_FPS))
        global frameListLoading
        frameListLoading = []
        frameCount = 0
        while True:
            _, frame = capture.read()
            resize = cv2.resize(frame, (420, 200))
            frameCount += 1
            resize = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frameListLoading.append(qimage2ndarray.array2qimage(resize))
            if frameCount == 106:
                capture.release()
                break

    """ Function: setWidget
     | ------------------------------
     | Description:
     |     Creates a widget that plays the loading animation.
    """
    def setWidget(self):
        layout = QtWidgets.QVBoxLayout()
        self.video_size = QSize(420, 200)
        global video
        video = QtWidgets.QLabel()
        video.setFixedSize(self.video_size)
        layout.addWidget(video)
        self.LoadingWidget.setLayout(layout)

    """ Function: runThread
     | ------------------------------
     | Description:
     |     Creates a separate thread for processing the video
     |     and updating the loading widget
     |
     | Parameter(s):
     |     menu - contains elements of the main window
     |     Dialog - contains elements of the loading window
     |     filePathVideo - path name of the selected video
     |     width - width of main screen (pixels), used to scale video
     |     height - height of main screen (pixels), used to scale video
    """
    def runThread(self, menu, Dialog, filePathVideo, width, height):
        Dialog.ui.setWidget()
        q = queue.Queue()
        myLoadingLoop = threading.Thread(name='myLoadingLoop', target=beginAnimation, daemon=True,
                                         args=(menu, Dialog, filePathVideo, q, width, height))
        myLoadingLoop.start()
        myLoadingLoop.result_queue = q
        return myLoadingLoop

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Video Transfer", None))

    """ Function: videoLoadingPulse
     | ------------------------------
     | Description:
     |     Updates the mainwindow video import icon, creates
     |     a pulsing effect that turns white when finished.
     |
     | Parameter(s):
     |     menu - contains elements of the main window
     |     tSum - current position (seconds) of upload animation
    """
    def videoLoadingPulse(self, menu, tSum):
        if tSum > 0.5:
            if tSum < 0.10:
                menu.Btn_Video.setIcon(icon1)
        if tSum > 0.10:
            if tSum < 0.15:
                menu.Btn_Video.setIcon(icon2)
        if tSum > 0.15:
            if tSum < 0.20:
                menu.Btn_Video.setIcon(icon3)
        if tSum > 0.20:
            if tSum < 0.30:
                menu.Btn_Video.setIcon(icon4)
        if tSum > 0.30:
            if tSum < 0.45:
                menu.Btn_Video.setIcon(icon5)
        if tSum > 0.45:
            if tSum < 0.8:
                menu.Btn_Video.setIcon(icon6)
        if tSum > 0.8:
            if tSum < 0.95:
                menu.Btn_Video.setIcon(icon5)
        if tSum > 0.95:
            if tSum < 1.0:
                menu.Btn_Video.setIcon(icon4)
        if tSum > 1.00:
            if tSum < 1.5:
                menu.Btn_Video.setIcon(icon3)
        if tSum > 1.5:
            if tSum < 1.1:
                menu.Btn_Video.setIcon(icon2)
        if tSum > 1.1:
            if tSum < 1.2:
                menu.Btn_Video.setIcon(icon1)
        if tSum > 1.2:
            if tSum < 1.55:
                menu.Btn_Video.setIcon(icon7)
        if tSum > 1.55:
            return 0
        return 1

    """ Function: createIcons
     | ------------------------------
     | Description:
     |     Loads import video icons into memory for pulse animation.
    """
    def createIcons(self):
        global icon1, icon2, icon3, icon4, icon5, icon6, icon7, icon8
        icon1 = QIcon()
        icon1.addFile(pathIcon + "importVideoLoading1.png", QSize(), QIcon.Normal, QIcon.Off)
        icon2 = QIcon()
        icon2.addFile(pathIcon + "importVideoLoading2.png", QSize(), QIcon.Normal, QIcon.Off)
        icon3 = QIcon()
        icon3.addFile(pathIcon + "importVideoLoading3.png", QSize(), QIcon.Normal, QIcon.Off)
        icon4 = QIcon()
        icon4.addFile(pathIcon + "importVideoLoading4.png", QSize(), QIcon.Normal, QIcon.Off)
        icon5 = QIcon()
        icon5.addFile(pathIcon + "importVideoLoading5.png", QSize(), QIcon.Normal, QIcon.Off)
        icon6 = QIcon()
        icon6.addFile(pathIcon + "importVideoLoading6.png", QSize(), QIcon.Normal, QIcon.Off)
        icon7 = QIcon()
        icon7.addFile(pathIcon + "importVideo.png", QSize(), QIcon.Normal, QIcon.Off)
        icon8 = QIcon()
        icon8.addFile(pathIcon + "importVideoOn.png", QSize(), QIcon.Normal, QIcon.Off)
        return

    def closeEvent(self):
        import sys
        sys.exit(0)

''' Class: Communicate
 | ------------------------------
 | Description:
 |     sets up the signal for loading animation.
'''
class Communicate(QtCore.QObject):
    data_signal = QtCore.Signal(str)

""" Function: beginAnimation
 | ------------------------------
 | Description:
 |     Processes video and updates the loading widget.
 |
 | Parameter(s):
 |     menu - contains elements of the main window
 |     Dialog - contains elements of the loading window
 |     filePathVideo - path name of the selected video
 |     q - places frames into a list that can be passed to ui_functions.py
 |     width - width of main screen (pixels), used to scale video
 |     height - height of main screen (pixels), used to scale video
"""
def beginAnimation(menu, Dialog, filePathVideo, q, width, height):
    mySrc = Communicate()
    for x in range(0, 3):
        video.setPixmap(QPixmap.fromImage(frameListLoading[x]))
        time.sleep(.0001)

    capture = cv2.VideoCapture(filePathVideo)
    fps = int(capture.get(cv2.CAP_PROP_FPS))
    frameMax = capture.get(cv2.CAP_PROP_FRAME_COUNT)
    width_video = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH)*.7)
    if width_video > width:
        width_video = width-70
    if width_video < width/2:
        width_video = int((width/2)-70)
    step = 105 / frameMax
    process = 0
    frameList = []
    frameCount = 0
    tStart = perf_counter()
    tEnd = 0
    tSum = 0
    i = 3
    while True:
        tStart = perf_counter()
        _, frame = capture.read()
        frameCount += 1
        resize = cv2.cvtColor(cv2.resize(frame, (width_video, int(height*.57)), 
                            interpolation =cv2.INTER_AREA), cv2.COLOR_BGR2RGB)
        frameList.append(qimage2ndarray.array2qimage(resize))

        if frameMax < 100:
            video.setPixmap(QPixmap.fromImage(frameListLoading[int(process)+2]))
            process += step
        else:
            process += step
            percent = process % 1
            if percent < step:
                if i == 105:
                    i = 104
                video.setPixmap(QPixmap.fromImage(frameListLoading[i]))
                i += 1

        if frameCount == frameMax:
            capture.release()
            menu.Btn_Video.setIcon(icon8)
            break

        ''' Timing for blinking video import icon '''
        tEnd = perf_counter() - tStart
        tSum += tEnd
        if Dialog.ui.videoLoadingPulse(menu, tSum) == 0:
            tSum = 0
    frameList.append(width_video)
    frameList.append(fps)
    frameList.append(frameMax)
    q.put(frameList)
    return frameList



