from main import *
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.ticker
from matplotlib.patches import FancyBboxPatch
from matplotlib.widgets import Button

''' __________________________  Parameter Decelerations __________________________ '''
global selection, queue, queue_settings, ani_dictionary
selection, queue, queue_settings = [], [], []  # var.s for storing user selected par.
ani_dictionary = {}  # list of menu elements to be animated

global help_open, video_open, hide
# flags to specify which functions have been completed
hide = []
video_open = False
help_open = False

global data_position, frameCount, timeFrame, past_back, past_forward, data_progression, program_running, list_length
global data_check, zoom, scroll, entry_left, entry_right, position_time, zoom_changed, lines_in_file, frame_max, slider_step, progress_on
data_position = 0  # position in the data_array list (containing the par. data_array and time)
frameCount = 0  # current frame of the video
timeFrame = 0  # holds the position of the data_array list item that corresponds to the next video frame
data_progression = 1
program_running = False
data_check = False
zoom = False
scroll = False
list_length = 0
entry_left = 0
entry_right = 0
position_time = 0
zoom_changed = False
lines_in_file = 0
frame_max = 0
slider_step = 0
progress_on = False
past_back, past_forward = False, False  # if the previous action was a manual frame change

global path_icon, path_video, hide_changed
path_icon = os.getcwd() + "\\" + "icons\\"  # path to the icon folder
path_video = None  # holds the file path to the video
hide_changed = True

''' Class: UI_Functions
 | ------------------------------
 | Description:
 |     Creates and sets up main window along with calling functions
 |     based on button trigger events. It also contains a callback
 |     function when drawing the plot. 
'''
class UI_Functions(MainWindow):

    """ Function: repaint_button
     | ------------------------------
     | Description:
     |     Repaints menu buttons after events are fulfilled.
     |
     | Parameter(s):
     |     button - which menu button is being referenced
     |     image - contains the path to the icon file
    """
    def repaint_button(button, image):
        icon = QIcon()
        icon.addFile(image, QSize(), QIcon.Normal, QIcon.Off)
        button.setIcon(icon)
        button.repaint()

    """ Function: settings_adjustment
     | ------------------------------
     | Description:
     |     Presents the settings list options at the start.
    """
    def settings_adjustment(self):
        list = self.ui.listSettings
        height = 0
        qlistwidgetitem = list.item(0)
        qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", '  ' + 'Plot Scrolling', None))
        marker = QIcon()
        marker.addFile(path_icon + "listItems/scrollMarkerOff.png", QSize(), QIcon.Normal, QIcon.Off)
        marker.addFile(path_icon + "listItems/scrollMarkerOn.png", QSize(), QIcon.Selected, QIcon.Off)
        qlistwidgetitem.setIcon(marker)
        qlistwidgetitem = list.item(1)
        qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", '  ' + 'Progress Bar', None))
        marker = QIcon()
        marker.addFile(path_icon + "listItems/progressMarkerOff.png", QSize(), QIcon.Normal, QIcon.Off)
        marker.addFile(path_icon + "listItems/progressMarkerOn.png", QSize(), QIcon.Selected, QIcon.Off)
        qlistwidgetitem.setIcon(marker)
        UI_Functions.animate_menu(self, 'aniList', self.ui.listSettings.height(), 25 * 2,
                                self.ui.listSettings, 1200,
                                b"maximumSize")
        self.ui.listSettings.setEditTriggers(QAbstractItemView.SelectedClicked)
        self.ui.listSettings.setStyleSheet(u"QListWidget{\n"
                                         "	background-color: rgb(30, 30, 30);\n"
                                         "	font: 10pt 'ProximaNova-Medium';\n"
                                         "	border-left : 20px solid rgb(30, 30, 30);\n"
                                         "	color: rgb(125, 125, 125);\n"
                                         "}\n"
                                         "\n"
                                         "QListWidget::item {\n"
                                         "	font: 10pt 'ProximaNova-Medium';\n"
                                         "	border-left : 5px solid rgb(30, 30, 30);\n"
                                         "}\n"
                                         "\n"
                                         "QListWidget::item:hover {\n"
                                         "	background-color: rgb(30, 30, 30);\n"
                                         "	color: rgb(220, 220, 220);	\n"
                                         "}\n"
                                         "\n"
                                         "QListWidget::item:selected {\n"
                                         "	background-color: rgb(30, 30, 30);\n"
                                         "	color: rgb(230, 230, 230);	\n"
                                         "}\n"
                                         "")
        self.ui.Label_Settings.setStyleSheet(u"QPushButton {\n"
                                               "	color: rgb(179, 179, 179);\n"
                                               "	font: 10pt 'Proxima Nova Lt';\n"
                                               "	background-color: rgb(30, 30, 30);\n"
                                               "	border: 0px solid;\n"
                                               "}\n"
                                               "")

    """ Function: settings_selection
     | ------------------------------
     | Description:
     |     Handles press event on list items. Places selection
     |     into a list that will determine which elements to be
     |     displayed. Also sets the selection limit to 3.
    """
    def settings_selection(self, enable):
        global scroll, progress_on
        item = self.ui.listSettings.currentItem().text()
        item_rect = self.ui.listSettings.visualItemRect(self.ui.listSettings.currentItem())
        item = item.strip()
        if item == 'Plot Scrolling':
            if scroll:
                print('turn scrolling off')
                scroll = False
            else:
                print('turn scrolling on')
                scroll = True
        elif item == 'Progress Bar':
            if progress_on:
                print('turn progress bar off')
                progress_on = False
            else:
                print('turn progress bar on')
                progress_on = True

    """ Function: file_import
     | ------------------------------
     | Description:
     |     Imports the RMC plot file with a file dialog. 
     |     Reads only the first line in the file to extract 
     |     information such as: 
     |     data_array elements, units, and list variables.
     |
     | Return:
     |     Updates Import Data icon after completion, then 
     |     calls list adjustment function.
    """
    def file_import(self, enable):
        filename = QFileDialog.getOpenFileName(None, " File dialog ", "", "CSV files (*.csv)")
        if filename != ('', ''):  # if the process was canceled
            self.ui.Btn_Import.setStyleSheet(u"QPushButton {\n"
            "	color: rgb(230, 230, 230);\n"
            "	background-color: rgb(30, 30, 30);\n"
            "	border: 0px solid;\n"
            "	font: 11pt 'Gotham';}\n"
            "QPushButton:hover {\n"
            "	color: rgb(250, 250, 250);\n"
            "}")
            global dataPath  # contains the path to rmc plot file
            dataPath = filename[0]
            with open(dataPath) as file:
                reader = csv.reader(file, delimiter=',')
                column = len(next(reader))  # count the number of columns
                file.seek(0)  # return to the beginning of the file
                global variable  # a list containing column positions of axis0 elements
                variable = [-1] * 7  # [ [Time] [Actual Pos.] [Actual Velocity] [Control Output] [Actual Force] [Actual Pressure] ]
                global data_unit  # a list containing data_array element units
                data_unit = [None] * 7
                global entries
                entries = []  # a list containing data_array items that can be displayed from the plot file
                for row in reader:
                    for x in range(0, (column - 1)):
                        if 'Time (sec)' in row[x]:
                            variable[0] = x
                            data_unit[0] = row[x].split()[-1]
                        elif 'Axis0 Actual Position' in row[x]:
                            variable[1] = x
                            data_unit[1] = row[x].split()[-1]
                            entries.append('Position')
                        elif 'Axis0 Actual Velocity' in row[x]:
                            variable[2] = x
                            data_unit[2] = row[x].split()[-1]
                            entries.append('Velocity')
                        elif 'Axis0 Control Output' in row[x]:
                            variable[3] = x
                            data_unit[3] = row[x].split()[-1]
                            entries.append('Control Output')
                        elif 'Axis0 Actual Force' in row[x]:
                            variable[4] = x
                            data_unit[4] = row[x].split()[-1]
                            entries.append('Force')
                        elif 'Axis0 Actual Pressure' in row[x]:
                            variable[5] = x
                            data_unit[5] = row[x].split()[-1]
                            entries.append('Pressure')
                        else:
                            variable[6] = str(x)
                    break  # after axis0 elements have been read, exit
            file.close()
            UI_Functions.repaint_button(self.ui.Btn_Import, path_icon + "importDataOn.png")  # update import file icon
            UI_Functions.list_adjustment(self)

    """ Function: list_adjustment
     | ------------------------------
     | Description:
     |     Adjusts the list in menu with elements from the file.
     |     The add_marker function is also called to add color 
     |     coded markers to all the elements.
    """
    def list_adjustment(self):
        list = self.ui.listWidget
        height = 0
        for i in range(0, len(entries)):
            qlistwidgetitem = list.item(i)
            qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", '  ' + entries[i], None))
            UI_Functions.add_marker(self, qlistwidgetitem, entries[i])
        UI_Functions.animate_menu(self, 'aniEmpty', self.ui.Empty.height(), 0, self.ui.Empty, 800,
                                b"maximumSize")
        UI_Functions.animate_menu(self, 'aniList', self.ui.listWidget.height(), 25 * len(entries),
                                self.ui.listWidget, 1200,
                                b"maximumSize")
        for i in range(len(entries), 7):
            list.takeItem(i)
        self.ui.listWidget.setEditTriggers(QAbstractItemView.SelectedClicked)
        self.ui.listWidget.setStyleSheet(u"QListWidget{\n"
                                         "	background-color: rgb(30, 30, 30);\n"
                                         "	font: 10pt 'ProximaNova-Medium';\n"
                                         "	border-left : 20px solid rgb(30, 30, 30);\n"
                                         "	color: rgb(125, 125, 125);\n"
                                         "}\n"
                                         "\n"
                                         "QListWidget::item {\n"
                                         "	font: 10pt 'ProximaNova-Medium';\n"
                                         "	border-left : 5px solid rgb(30, 30, 30);\n"
                                         "}\n"
                                         "\n"
                                         "QListWidget::item:hover {\n"
                                         "	background-color: rgb(30, 30, 30);\n"
                                         "	color: rgb(220, 220, 220);	\n"
                                         "}\n"
                                         "\n"
                                         "QListWidget::item:selected {\n"
                                         "	background-color: rgb(30, 30, 30);\n"
                                         "	color: rgb(230, 230, 230);	\n"
                                         "}\n"
                                         "")
        self.ui.Label_Parameters.setStyleSheet(u"QPushButton {\n"
                                               "	color: rgb(179, 179, 179);\n"
                                               "	font: 10pt 'Proxima Nova Lt';\n"
                                               "	background-color: rgb(30, 30, 30);\n"
                                               "	border: 0px solid;\n"
                                               "}\n"
                                               "")

    """ Function: add_marker
     | ------------------------------
     | Description:
     |     Adjusts the listwidget with elements from the file.
     |     The add_marker function is also called to add color 
     |     coded markers to all the elements.
     |
     | Parameter(s):
     |     qlistwidgetitem - reference to current list widget item
     |     entry - parameter title
    """
    def add_marker(self, qlistwidgetitem, entry):
        marker = QIcon()
        marker.addFile(path_icon + "listItems/greyMarker.png", QSize(), QIcon.Normal, QIcon.Off)
        if entry == 'Position':
            marker.addFile(path_icon + "listItems/redMarker.png", QSize(), QIcon.Selected, QIcon.Off)
        elif entry == 'Velocity':
            marker.addFile(path_icon + "listItems/yellowMarker.png", QSize(), QIcon.Selected, QIcon.Off)
        elif entry == 'Control Output':
            marker.addFile(path_icon + "listItems/purpleMarker.png", QSize(), QIcon.Selected, QIcon.Off)
        elif entry == 'Force':
            marker.addFile(path_icon + "listItems/blueMarker.png", QSize(), QIcon.Selected, QIcon.Off)
        elif entry == 'Pressure':
            marker.addFile(path_icon + "listItems/limeMarker.png", QSize(), QIcon.Selected, QIcon.Off)
        qlistwidgetitem.setIcon(marker)

    """ Function: queue_parameters
     | ------------------------------
     | Description:
     |     Handles press event on list items. Places selection
     |     into a list that will determine which elements to be
     |     displayed. Also sets the selection limit to 3.
    """
    def queue_parameters(self, enable):
        if len(queue) > 0:
            pass
        else:
            item = self.ui.listWidget.currentItem().text()
            item_rect = self.ui.listWidget.visualItemRect(self.ui.listWidget.currentItem())
            item = item.strip()
            if item == 'Empty':
                QTest.mouseClick(self.ui.listWidget.viewport(), Qt.LeftButton, Qt.NoModifier, item_rect.center())
            else:
                if item in selection:
                    selection.remove(item)
                    queue.clear()
                else:
                    selection.append(item)
                    queue.clear()
                if len(selection) > 3:
                    selection.remove(item)
                    queue.append(0)
                    QTest.mouseClick(self.ui.listWidget.viewport(), Qt.LeftButton, Qt.NoModifier, item_rect.center())
        queue.clear()

    """ Function: video_import
     | ------------------------------
     | Description:
     |     Repaints menu buttons after events are fulfilled.
     |
     | Parameter(s):
     |     width - width (pixels) of main monitor
     |     height - height (pixels) of main monitor
    """
    def video_import(self, enable, width, height):
        global video_open
        fileVideo = QFileDialog.getOpenFileName(None, " File dialog ", "", "Video files (*.mov *.mp4 *.avi)")
        if fileVideo != ('', ''):
            self.ui.Btn_Video.setStyleSheet(u"QPushButton {\n"
            "	color: rgb(230, 230, 230);\n"
            "	background-color: rgb(30, 30, 30);\n"
            "	border: 0px solid;\n"
            "	font: 11pt 'Gotham';}\n"
            "QPushButton:hover {\n"
            "	color: rgb(250, 250, 250);\n"
            "}")
            global path_video
            path_video = fileVideo[0]
            global frameList
            frameList = []
            frameList = self.open_dialog(path_video, width, height)
            print('length of frameList: ' + str(len(frameList)))
            video_open = True
        elif not video_open:
            path_video = None
            UI_Functions.repaint_button(self.ui.Btn_Video, path_icon + "video_import.png")

    """ Function: scroll_toggle
     | ------------------------------
     | Description:
     |     Toggles the scroll functionality of the plot
    """
    def scroll_toggle(self, enable):
        global scroll
        if scroll:
            scroll = False
            self.ui.Btn_Scroll.setStyleSheet(u"QPushButton {\n"
                "	color: rgb(179, 179, 179);\n"
                "	background-color: rgb(30, 30, 30);\n"
                "	border: 0px solid;\n"
                "	font: 11pt 'Gotham';}\n"
                "QPushButton:hover {\n"
                "	color: rgb(220, 220, 220);\n"
                "}")
            UI_Functions.repaint_button(self.ui.Btn_Scroll, path_icon + "scroll.png")
        else:
            scroll = True
            self.ui.Btn_Scroll.setStyleSheet(u"QPushButton {\n"
                "	color: rgb(230, 230, 230);\n"
                "	background-color: rgb(30, 30, 30);\n"
                "	border: 0px solid;\n"
                "	font: 11pt 'Gotham';}\n"
                "QPushButton:hover {\n"
                "	color: rgb(250, 250, 250);\n"
                "}")
            UI_Functions.repaint_button(self.ui.Btn_Scroll, path_icon + "scrollOn.png")

    """ Function: run_help
     | ------------------------------
     | Description:
     |     Expands help menu upon button press. If the menu
     |     is already open then it will collapse the menu.
     |
     | Parameter(s):
     |     help_open - flag for checking if menu is open
     |     program_running - checks if the program is running,
     |     if so, it will prevent the menu from collapsing
    """
    def run_help(self, enable):
        print('inside run help')
        global program_running, help_open
        print('program_running',program_running)
        print('help open',help_open)
        if not help_open:
            self.ui.Btn_Help.setStyleSheet(u"QPushButton {\n"
            "	color: rgb(230, 230, 230);\n"
            "	background-color: rgb(30, 30, 30);\n"
            "	border: 0px solid;\n"
            "	font: 11pt 'Gotham';}\n"
            "QPushButton:hover {\n"
            "	color: rgb(250, 250, 250);\n"
            "}")
            if program_running:
                UI_Functions.animate_menu(self, 'aniProcess', 0, 40, self.ui.Label_Process, 0, b"maximumSize")
                UI_Functions.animate_menu(self, 'aniPList', 0, 125, self.ui.listHelpProcess, 0, b"maximumSize")
                UI_Functions.animate_menu(self, 'aniControls', 0, 40, self.ui.Label_Controls, 0, b"maximumSize")
                UI_Functions.animate_menu(self, 'aniCList', 0, 125, self.ui.listHelpControls, 0, b"maximumSize")
                UI_Functions.animate_menu(self, 'aniProcessLine', 0, 3, self.ui.Line_Process, 0, b"maximumSize")
                UI_Functions.animate_menu(self, 'aniControlsLine', 0, 3, self.ui.Line_Controls, 0, b"maximumSize")
                UI_Functions.repaint_button(self.ui.Btn_Help, path_icon + "helpOn.png")
            else:
                UI_Functions.animate_menu(self, 'aniProcess', 0, 40, self.ui.Label_Process, 700, b"maximumSize")
                UI_Functions.animate_menu(self, 'aniPList', 0, 125, self.ui.listHelpProcess, 1000, b"maximumSize")
                UI_Functions.animate_menu(self, 'aniControls', 0, 40, self.ui.Label_Controls, 700, b"maximumSize")
                UI_Functions.animate_menu(self, 'aniCList', 0, 125, self.ui.listHelpControls, 1000, b"maximumSize")
                UI_Functions.animate_menu(self, 'aniProcessLine', 0, 3, self.ui.Line_Process, 80, b"maximumSize")
                UI_Functions.animate_menu(self, 'aniControlsLine', 0, 3, self.ui.Line_Controls, 80, b"maximumSize")
                UI_Functions.repaint_button(self.ui.Btn_Help, path_icon + "helpOn.png")
            help_open = True

        else:
            self.ui.Btn_Help.setStyleSheet(u"QPushButton {\n"
            "	color: rgb(179, 179, 179);\n"
            "	background-color: rgb(30, 30, 30);\n"
            "	border: 0px solid;\n"
            "	font: 11pt 'Gotham';}\n"
            "QPushButton:hover {\n"
            "	color: rgb(220, 220, 220);\n"
            "}")
            UI_Functions.animate_menu(self, 'aniProcess', 40, 0, self.ui.Label_Process, 0, b"maximumSize")
            UI_Functions.animate_menu(self, 'aniPList', 125, 0, self.ui.listHelpProcess, 0, b"maximumSize")
            UI_Functions.animate_menu(self, 'aniControls', 40, 0, self.ui.Label_Controls, 0, b"maximumSize")
            UI_Functions.animate_menu(self, 'aniCList', 125, 0, self.ui.listHelpControls, 0, b"maximumSize")
            UI_Functions.animate_menu(self, 'aniProcessLine', 3, 0, self.ui.Line_Process, 0, b"maximumSize")
            UI_Functions.animate_menu(self, 'aniControlsLine', 3, 0, self.ui.Line_Controls, 0, b"maximumSize")
            UI_Functions.repaint_button(self.ui.Btn_Help, path_icon + "help.png")
            help_open = False

    """ Function: animate_menu
     | ------------------------------
     | Description:
     |     Animates menu items, expanding and collapsing.
     |
     | Parameter(s):
     |     x - list element
     |     start - start position
     |     end - ending position
     |     object - reference to menu item
     |     duration - length of animation (ms)
     |     size - maximumSize or minimumHeight
    """
    def animate_menu(self, x, start, end, object, duration, size):
        ani_dictionary[x] = QPropertyAnimation(object, size)
        ani_dictionary[x].setDuration(duration)
        ani_dictionary[x].setStartValue(QSize(180,start))
        ani_dictionary[x].setEndValue(QSize(180,end))
        ani_dictionary[x].setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        ani_dictionary[x].start()

    """ Function: run_check
     | ------------------------------
     | Description:
     |     Final check before running program. Checks to see
     |     if video file was imported along with data_array, likewise
     |     checks to see if parameters were selected.
     |
     | Parameter(s):
     |     button - which menu button is being referenced
     |     image - contains the path to the icon file
    """
    def run_check(self, enable, width, height):
        global help_open, program_running
        if path_video == None:
            msg = QMessageBox()
            msg.setText("video file not imported")
            msg.setWindowTitle('Exception')
            msg.setWindowOpacity(0.95)
            icon = QIcon()
            icon.addFile(u"../../Desktop/GUI/Logo.png", QSize(), QIcon.Normal, QIcon.Off)
            msg.setWindowIcon(icon)
            msg.setIcon(QMessageBox.Warning)
            msg.setStyleSheet("background-color: rgb(45, 45, 45); color: rgb(255, 255, 255)")
            msg.exec_()

        elif len(selection) == 0:
            msg = QMessageBox()
            msg.setText("parameters not selected")
            msg.setWindowTitle('Exception')
            msg.setWindowOpacity(0.95)
            icon = QIcon()
            icon.addFile(u"../../Desktop/GUI/Logo.png", QSize(), QIcon.Normal, QIcon.Off)
            msg.setWindowIcon(icon)
            msg.setIcon(QMessageBox.Warning)
            msg.setStyleSheet("background-color: rgb(45, 45, 45); color: rgb(255, 255, 255)")
            msg.exec_()
        else:
            program_running = True
            if not help_open:
                UI_Functions.run_help(self, True)
            self.ui.Btn_Run.setStyleSheet(u"QPushButton {\n"
            "	color: rgb(230, 230, 230);\n"
            "	background-color: rgb(30, 30, 30);\n"
            "	border: 0px solid;\n"
            "	font: 11pt 'Gotham';}\n")
            UI_Functions.repaint_button(self.ui.Btn_Run, path_icon + "run_programOn.png")
            UI_Functions.run_program(self, width, height)

    """ Function: processFile
     | ------------------------------
     | Description:
     |     Imports data_array from selected parameters. 
     |
     | Return:
     |     calls selected_info upon completion to pull 
     |     additional information such as min & max values,
     |     units, and labels.
    """
    def processFile(self):
        with open(dataPath) as file:
            lines_in_file = 0
            edge_array = list(range(-1000,0)) + list(range(0,1001))
            edge_array_decimal = []
            for number in edge_array:
                edge_array_decimal.append(round(number*.001,3))
            reader = csv.reader(file, delimiter=',')
            len(next(reader))  # Read first line and count columns
            time_data, x_data, position, velocity, control, force, pressure = [], [], [], [], [], [], []
            for row in reader:
                time_data.append(row[variable[0]])
                x_data.append(int(float(row[variable[0]])*1000))
                for item in selection:
                    if item == 'Position':
                        position.append(float(row[variable[1]]))
                    elif item == 'Velocity':
                        velocity.append(float(row[variable[2]]))
                    elif item == 'Control Output':
                        control.append(float(row[variable[3]]))
                    elif item == 'Force':
                        force.append(float(row[variable[4]]))
                    elif item == 'Pressure':
                        pressure.append(float(row[variable[5]]))
                lines_in_file += 1
            file.close()
        # 1000 elements added before and after for the edges of the plot
        time_data = edge_array_decimal[0:1000] + time_data + edge_array_decimal[1000:2001] 
        x_data = edge_array[0:1000] + x_data + edge_array[1000:2001]
        UI_Functions.selected_info(self, time_data, x_data, position, velocity, force, control, pressure)
        return lines_in_file


    """ Function: selected_info
     | ------------------------------
     | Description: 
     |     Pulls additional information from selected 
     |     parameter data_array such as min & max values,
     |     units, and labels.
     |
     | Parameter(s):
     |     Included are all the available parameters, 
     |     however, only the selected parameters will be 
     |     analyzed.
    """
    def selected_info(self, time_data, x_data, position, velocity, force, control, pressure):
        global minValue, maxValue, yUnits, yLabels, lines_in_file
        maxValue, minValue, yUnits, yLabels = [], [], [], []
        global time_array, data_array, x_array
        time_array = np.array(time_data)
        time_data.clear()
        data_array = [None]*len(selection)
        x_array = np.array(x_data)
        x_data.clear()
        i = 0
        for item in selection:
                    if item == 'Position':
                        yLabels.append('Position')
                        yUnits.append(data_unit[1])
                        minValue.append(round(min(position)))
                        maxValue.append(round(max(position)))
                        position = position[-1001:-1] + position + position[0:1001]
                        data_array[i] = np.array(position)
                        i += 1
                        position.clear()
                    elif item == 'Velocity':
                        yLabels.append('Velocity')
                        yUnits.append(data_unit[2])
                        minValue.append(round(min(velocity)))
                        maxValue.append(round(max(velocity)))
                        velocity = velocity[-1001:-1] + velocity + velocity[0:1001]
                        data_array[i] = np.array(velocity)
                        i += 1
                        velocity.clear()
                    elif item == 'Control Output':
                        yLabels.append('Control Output')
                        yUnits.append(data_unit[3])
                        minValue.append(round(min(control)))
                        maxValue.append(round(max(control)))
                        control = control[-1001:-1] + control + control[0:1001]
                        data_array[i] = np.array(control)
                        i += 1
                        control.clear()
                    elif item == 'Force':
                        yLabels.append('Force')
                        yUnits.append(data_unit[4])
                        minValue.append(round(min(force)))
                        maxValue.append(round(max(force)))
                        force = force[-1001:-1] + force + force[0:1001]
                        data_array[i] = np.array(force)
                        i += 1
                        force.clear()
                    elif item == 'Pressure':
                        yLabels.append('Pressure')
                        yUnits.append(data_unit[5])
                        minValue.append(round(min(pressure)))
                        maxValue.append(round(max(pressure)))
                        pressure = pressure[-1001:-1] + pressure + pressure[0:1001]
                        data_array[i] = np.array(pressure)
                        i += 1
                        pressure.clear()


    """ Function: run_program
     | ------------------------------
     | Description:
     |     If previous checks are passed, the program will
     |     then begin executing. This function creates the
     |     video and plot widget which will be executed in 
     |     a separate thread.
     |
     | Parameter(s):
     |     width - width of main screen (pixels), used to scale video
     |     height - height of main screen (pixels), used to scale video
    """
    def run_program(self, width, height):
        UI_Functions.collapse_menu(self)
        global lines_in_file, frame_max
        lines_in_file = UI_Functions.processFile(self) # number of data_array entries
        frame_max = frameList.pop() 
        fps = frameList.pop()
        width = frameList.pop()
        amount_selected = len(selection)

        self.myFig = Custom_Fig_Canvas()
        layout = QtWidgets.QVBoxLayout()
        self.video_size = QSize(width, int(height*.57))
        video = QtWidgets.QLabel()
        video.setFixedSize(self.video_size)
        layout.addWidget(video)
        layout.addWidget(self.myFig)
        self.ui.MplWidget.setLayout(layout)
        self.ui.resizeWindow(width+70+180, height)

        data_send_thread = threading.Thread(name='data_send_thread', target=data_send_loop, daemon=True,
                                        args=(self.add_data_callback_left, self.add_data_callback_right, data_array, frameList, 
                                        video, fps, amount_selected, self.ui, self.add_x_axis_callback_left, self.add_x_axis_callback_right, self))
        data_send_thread.start()

    """ Function: collapse_menu
     | ------------------------------
     | Description:
     |     Collapses the side menu when Run Program has
     |     been initiated.
     |
     | Parameter(s):
     |     help_open - flag for checking if menu is open
     |     program_running - checks if the program is running,
     |     if so, it will prevent the menu from collapsing
    """
    def collapse_menu(self):
        self.ui.Btn_Video.setMaximumSize(0,0)
        self.ui.verticalLayout_4.removeWidget(self.ui.Btn_Video)
        self.ui.Btn_Run.setMaximumSize(0,0)
        self.ui.verticalLayout_4.removeWidget(self.ui.Empty)
        self.ui.Empty.setMaximumSize(0,0)
        self.ui.Btn_Help.setMaximumSize(0,0)
        self.ui.verticalLayout_4.removeWidget(self.ui.Btn_Help)
        self.ui.verticalLayout_4.removeWidget(self.ui.Btn_Run)
        self.ui.Btn_Import.setMaximumSize(0,0)
        self.ui.verticalLayout_4.removeWidget(self.ui.Btn_Import)
        self.ui.Label_Parameters.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.ui.verticalLayout_4.removeWidget(self.ui.Label_Parameters)
        self.ui.Label_Settings.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.ui.verticalLayout_4.removeWidget(self.ui.Label_Settings)
        self.ui.verticalLayout_4.removeWidget(self.ui.Btn_Video)
        self.ui.Line_Parameters.setMaximumSize(0,0)
        self.ui.Line_Settings.setMaximumSize(0,0)
        self.ui.verticalLayout_4.removeWidget(self.ui.Line_Parameters)
        self.ui.verticalLayout_4.removeItem(self.ui.Space_HP)
        self.ui.verticalLayout_4.removeItem(self.ui.Space_PL)
        self.ui.verticalLayout_4.removeItem(self.ui.Space_CurrL)     
        self.ui.verticalLayout_4.removeItem(self.ui.Space_PP) 
        self.ui.verticalLayout_4.removeItem(self.ui.Space_PS)
        self.ui.verticalLayout_4.removeItem(self.ui.Space_HL)        
        self.ui.repaint_button(self.ui.Btn_Video, None)
        self.ui.Btn_Video.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.ui.repaint_button(self.ui.Btn_Import, None)
        self.ui.Btn_Import.setText(QCoreApplication.translate("MainWindow", u"", None))
        for i in range(0, len(entries)):
            qlistwidgetitem = self.ui.listWidget.item(i)
            qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", '', None))
            qlistwidgetitem.setIcon(QIcon())
        for i in range(0, 7):
            self.ui.listWidget.takeItem(i)
        UI_Functions.animate_menu(self, 'aniList', self.ui.listWidget.height(), 0,
                                self.ui.listWidget, 1200, b"maximumSize")
        self.ui.verticalLayout_4.removeWidget(self.ui.listWidget)
        UI_Functions.animate_menu(self, 'aniList', self.ui.listSettings.height(), 0,
                                self.ui.listSettings, 1200, b"maximumSize")
        self.ui.verticalLayout_4.removeWidget(self.ui.listSettings)
        self.ui.verticalLayout_5.setContentsMargins(35, 30, 35, 0) #left, top, right, bottom
        

''' Class: Custom_Fig_Canvas
 | ------------------------------
 | Description:
 |     Initializes the plot and begins the animation.
'''
class Custom_Fig_Canvas(FigureCanvas, TimedAnimation):
    def __init__(self):
        global scroll, progress_on
        self.amount_selected = len(selection)
        self.added_data_left = [[0 for x in range(1)] for y in range(self.amount_selected)] # the arrays we will be sending information to 
        self.added_data_right = [[0 for x in range(1)] for y in range(self.amount_selected)] # these will be combined and will make up the line 
        self.added_data = [[0 for x in range(1)] for y in range(self.amount_selected)] 
        self.data_length = [[0 for x in range(1)] for y in range(self.amount_selected+1)] 
        print('added data',self.added_data)
        self.added_x_axis_left, self.added_x_axis_right, self.added_x_axis = [], [], []
        self.lines = [None]*self.amount_selected
        
        ''' _______________  Font Settings _______________ '''
        font_ticks = Path(mpl.get_data_path(), os.getcwd() + "\\" + "fonts\ClearSans-Bold.ttf")
        font_text = Path(mpl.get_data_path(), os.getcwd() + "\\" + "fonts\ClearSans-Bold.ttf")

        # Window & plot formatting
        plt.rcParams['toolbar'] = 'None'
        plt.rcParams['axes.linewidth'] = 2.0
        plt.rc('xtick', labelsize=9)  # Font size of the tick labels
        plt.rc('ytick', labelsize=9)  # Font size of the tick labels

        # The data_array 
        self.xlim = 201 # we begin with 201 samples
        self.samples = np.linspace(0, 1000, num = 1001)
        self.fig = plt.figure()

        # this creates the lines in the x-axis along with the progress bar
        if progress_on:
            slider_horizontal_lines_axis = self.fig.add_axes([0, .905, 2, 0.135], facecolor = 'none') # left, bottom, width, height
            slider_horizontal_lines_axis.set_xlim(0, self.xlim - 1)
            self.slider = slider_horizontal_lines_axis.add_patch(FancyBboxPatch((.38,.14),49.6,.2, boxstyle='square', 
            facecolor="#838f9f", edgecolor="none", alpha=0.5)) # x,y,width,height
            for x in range (1,311):
                slider_horizontal_lines_axis.add_patch(FancyBboxPatch((.325*x-.02,.14),0,.4, boxstyle='round, pad=0.08', facecolor="#2d2f30", edgecolor="none", alpha=0.5)) # inside of slider
            Custom_Fig_Canvas.spine_editor(self, slider_horizontal_lines_axis, 'left', 'none', 'right', False)
            slider_horizontal_lines_axis.axis('off')

        # initializes the plot
        self.ax1 = self.fig.add_subplot(111)
        self.text_data = []
        self.text_parameter = []
        self.parameter_text_backup = []

        # for each parameter, a new y-axis, line, and text elements are constructed
        for x in range(0, self.amount_selected):
            if x == 0:
                color = Custom_Fig_Canvas.markerColor(self, selection[0], x)
                global y_range
                y_range = [(minValue[0] - maxValue[0] / 4.5), (maxValue[0] + maxValue[0] / 4.5)]
                self.ax1.set_ylim(y_range)
                Custom_Fig_Canvas.spine_editor(self, self.ax1, 'left', color[1], 'right', True)
                self.ax1.tick_params(axis='x', colors='#ffffff', direction="in", length=0, pad=9)
                self.ax1.xaxis.set_ticks_position('top') 
                self.ax1.tick_params(axis='y', colors='#d8d8d8', direction="in", length=0, pad=-15)
                for tick in self.ax1.yaxis.get_majorticklabels():
                    tick.set_horizontalalignment("left")
                    tick.set_verticalalignment("bottom")
                last_tick = tick
                plt.grid(b=True, which='major', color='#d1d6dd', linestyle='-.', alpha=0.15, linewidth=0.9, dash_capstyle='round', dashes=(12, 6))
                plt.xticks(font=font_ticks, fontsize=12, color='#e8e8e8', alpha=0.5)
                text_data_position_y = 0.793
                data_marker_position_y = text_data_position_y - 0.01
                data_marker_edge_position_y = text_data_position_y - 0.03
                data_position_x = 0.50625
                data_marker_position_x = data_position_x - 0.006
                parameter_spacing, self.parameter_text_backup = Custom_Fig_Canvas.measure_space(self, yLabels[0], self.parameter_text_backup)
                parameter_position_x = Custom_Fig_Canvas.measure_offset(self, yLabels[0])
                parameter_marker_position_x = parameter_position_x -.017
                self.text_data = Custom_Fig_Canvas.create_text(self, self.ax1, text_data_position_y, data_marker_position_y, 
                                data_marker_edge_position_y, data_marker_position_x, data_position_x, font_text, color[1], self.text_data, None)
                self.text_parameter = Custom_Fig_Canvas.create_text(self, self.ax1, text_data_position_y, data_marker_position_y, 
                                data_marker_edge_position_y, parameter_marker_position_x, parameter_position_x, font_text, color[1], self.text_parameter, parameter_spacing)
                plt.subplots_adjust(left=.0067, right=.998, top=0.915, bottom=0.07)
                self.lines[0] = Line2D([], [], color=color[1], linewidth=2.5)
                self.ax1.add_line(self.lines[0])
                self.lines[0].set_alpha(0.7)


            elif x == 1:
                color = Custom_Fig_Canvas.markerColor(self, selection[1], x)
                ax2 = self.ax1.twinx()
                y_range1 = [(minValue[1] - maxValue[1] / 5), (maxValue[1] + maxValue[1] / 5)]
                ax2.set_ylim(y_range1)
                ticks = Custom_Fig_Canvas.rangeFunction(self, self.ax1.get_ylim(), ax2.get_ylim())
                ax2.yaxis.set_major_locator(matplotlib.ticker.FixedLocator(ticks))
                Custom_Fig_Canvas.spine_editor(self, ax2, 'right', color[1], 'left', True)
                text_data_position_y += -0.2
                data_marker_position_y = text_data_position_y - 0.01
                data_marker_edge_position_y = text_data_position_y - 0.03
                self.text_data = Custom_Fig_Canvas.create_text(self, self.ax1, text_data_position_y, data_marker_position_y, 
                                data_marker_edge_position_y, data_marker_position_x, data_position_x, font_text, color[1], self.text_data, None)
                parameter_spacing, self.parameter_text_backup = Custom_Fig_Canvas.measure_space(self, yLabels[1], self.parameter_text_backup)
                parameter_position_x = Custom_Fig_Canvas.measure_offset(self, yLabels[1])
                parameter_marker_position_x = parameter_position_x -.017
                self.text_parameter = Custom_Fig_Canvas.create_text(self, self.ax1, text_data_position_y, data_marker_position_y, 
                                data_marker_edge_position_y, parameter_marker_position_x, parameter_position_x, font_text, color[1], self.text_parameter, parameter_spacing)              
                plt.subplots_adjust(left=0.0067, right=0.995, top=0.915, bottom=0.07)
                ax2.tick_params(axis='y', colors='#d8d8d8', direction="in", length=0, pad=-15)
                for tick in ax2.yaxis.get_majorticklabels():
                    tick.set_horizontalalignment("right")
                    tick.set_verticalalignment("bottom")
                tick.set_visible(False)
                self.lines[1] = Line2D([], [], color=color[1], linewidth=2.5)
                ax2.add_line(self.lines[1])
                self.lines[1].set_alpha(0.7)               

            elif x == 2:
                color = Custom_Fig_Canvas.markerColor(self, selection[2], x)
                ax3 = self.ax1.twinx()
                y_range2 = [(minValue[2] - maxValue[2] / 5), (maxValue[2] + maxValue[2] / 5)]
                ax3.set_ylim(y_range2)
                ticks = Custom_Fig_Canvas.rangeFunction(self, self.ax1.get_ylim(), ax3.get_ylim())
                ax3.yaxis.set_major_locator(matplotlib.ticker.FixedLocator(ticks))
                ax3.yaxis.set_ticks_position('right') 
                ax3.tick_params(axis='y', colors='#aeadab')
                Custom_Fig_Canvas.spine_editor(self, ax3, 'right', color[1], 'left', True)
                ax3.spines['right'].set_position(('outward', -80))
                text_data_position_y += -0.2
                data_marker_position_y = text_data_position_y - 0.01
                data_marker_edge_position_y = text_data_position_y - 0.03
                self.text_data = Custom_Fig_Canvas.create_text(self, self.ax1, text_data_position_y, data_marker_position_y, 
                                data_marker_edge_position_y, data_marker_position_x, data_position_x, font_text, color[1], self.text_data, None)
                ax3.tick_params(axis='y', colors='#d8d8d8', direction="in", length=0, pad=-15)
                parameter_spacing, self.parameter_text_backup = Custom_Fig_Canvas.measure_space(self, yLabels[2], self.parameter_text_backup)
                parameter_position_x = Custom_Fig_Canvas.measure_offset(self, yLabels[2])
                parameter_marker_position_x = parameter_position_x -.017
                self.text_parameter = Custom_Fig_Canvas.create_text(self, self.ax1, text_data_position_y, data_marker_position_y, 
                data_marker_edge_position_y, parameter_marker_position_x, parameter_position_x, font_text, color[1], self.text_parameter, parameter_spacing)                
                for tick in ax3.yaxis.get_majorticklabels():
                    tick.set_horizontalalignment("right")
                    tick.set_verticalalignment("bottom")
                tick.set_visible(False)
                self.lines[2] = Line2D([], [], color=color[1], linewidth=2.5)
                ax3.add_line(self.lines[2])
                self.lines[2].set_alpha(0.7)

            last_tick.set_visible(False)
            plt.yticks(font=font_ticks, fontsize=12, color='#ffffff', alpha=0.6)
            
        text_data_position_y += -0.2
        data_marker_position_y = text_data_position_y - 0.01
        data_marker_edge_position_y = text_data_position_y - 0.03
        self.text_data = Custom_Fig_Canvas.create_text(self, self.ax1, text_data_position_y, data_marker_position_y, 
                                data_marker_edge_position_y, data_marker_position_x, data_position_x, font_text, "#666666", self.text_data, None)
        parameter_spacing, self.parameter_text_backup = Custom_Fig_Canvas.measure_space(self, 'Time ', self.parameter_text_backup)
        parameter_position_x = Custom_Fig_Canvas.measure_offset(self, 'Time ')
        parameter_marker_position_x = parameter_position_x -.015
        self.text_parameter = Custom_Fig_Canvas.create_text(self, self.ax1, text_data_position_y, data_marker_position_y, 
                data_marker_edge_position_y, parameter_marker_position_x, parameter_position_x, font_text, "#666666", self.text_parameter, parameter_spacing)                
        plt.figure(figsize=(40, 6))
        plt.gcf().subplots_adjust(bottom=0.15)
        self.fig.set_facecolor('#232323')  # Outer border
        self.ax1.patch.set_facecolor('#1e1e1e')  # Inner window
        self.ax1.set_xlim(self.samples[0],self.samples[200])
        
        # these elements are added to create a subtle border around the plot
        plot_background_axis = self.fig.add_axes([0, 0.045, 1, 1], facecolor = 'none') # left, bottom, width, height
        plot_background_axis.add_patch(FancyBboxPatch((.502,.0275),0,.833, boxstyle='round, pad=0.001', facecolor="#d1d6dd", edgecolor="none", alpha=0.35)) 
        plot_background_axis.add_patch(FancyBboxPatch((.01,.0275),.981,.833, boxstyle='round, pad=0.008', facecolor="none", edgecolor="#1a1a1a", linewidth = 4.5))
        plot_background_axis.add_patch(FancyBboxPatch((.01,.0275),.981,.91, boxstyle='round, pad=0.008', facecolor="none", edgecolor="#1a1a1a", linewidth = 4.5)) 
        
        Custom_Fig_Canvas.spine_editor(self, plot_background_axis, 'left', 'none', 'right', False)
        plot_background_axis.axis('off')
        if progress_on:
            slider_background_axis = self.fig.add_axes([0, .91, 2, 0.13], facecolor = 'none') # left, bottom, width, height
            slider_background_axis.set_xlim(0, self.xlim - 1)
            Custom_Fig_Canvas.spine_editor(self, slider_background_axis, 'left', 'none', 'right', False)
            slider_background_axis.axis('off')
            slider_background_axis.add_patch(FancyBboxPatch
            ((.59,.2),98.85,.28, boxstyle='round, pad=0.1', facecolor="none",
            edgecolor="#292929", linewidth = 3)) # x,y,width,height
            slider_background_axis.add_patch(FancyBboxPatch
            ((.3,.14),99.4,.4, boxstyle='round, pad=0.1', facecolor="none",
            edgecolor="#1a1a1a", linewidth = 4)) # outer bevel of slider 4b4b4b original color   

        self.fig.canvas.callbacks.connect('button_press_event', on_click)

        FigureCanvas.__init__(self, self.fig)
        TimedAnimation.__init__(self, self.fig, interval=0, blit=not scroll)
        self.fig.canvas.mpl_connect('button_press_event', on_click)

    ''' creates lists with spacing needed for color coded line and text box '''
    def measure_space(self, text, parameter_text_rebound):
        spaces = [] 
        spaces.append('      ') # left and right borders
        spaces.append('')
        for i in range(1, len(text)):
            spaces[0] += ' '
        for i in range(1, len(spaces[0])):
            spaces[1] += '                        '
        spaces.append(text)
        parameter_text_rebound.append(spaces[0])
        parameter_text_rebound.append(spaces[1])
        parameter_text_rebound.append(text)
        return spaces, parameter_text_rebound

    ''' returns the proper offset needed to shift text left/right '''
    def measure_offset(self, text):
        offset = 0.50825 # left and right borderss
        text_length = len(text)
        if text_length == 5:
            offset += -.0435
        elif text_length == 8:
            offset += -.0582
        elif text_length == 14:
            offset += -.091
        return offset

    ''' these colors will be used in various plot elements '''
    def markerColor(self, entry, num):
        color = []
        if entry == 'Position': # Position will result in a red line
            color.append('#c62b2b')
            color.append('#a02424')
        elif entry == 'Velocity': # Velocity will reult in a blue line 
            color.append('#ffb525')
            color.append('#f87f3c') 
        elif entry == 'Control Output': # Control Output will reult in a purple line  
            color.append('#ac97fd')
            color.append('#8264ce')
        elif entry == 'Force': # Force will reult in a yellow line 
            color.append('#496fa7')
            color.append('#5fbffc')
        elif entry == 'Pressure': # Pressure will reult in a lime line 
            color.append('#d6ed17')
            color.append('#b0c40c')         
        return color

    ''' part of the design process of having color coded, properly weighted spines '''
    def spine_editor(self, axis, visible_spine, color, hidden_spine, visible):
        axis.spines['top'].set_visible(False)
        axis.spines['bottom'].set_visible(False)
        axis.spines[hidden_spine].set_visible(False)
        if visible:
            axis.spines[visible_spine].set_color(color)
            axis.spines[visible_spine].set_alpha(0.75)
            axis.spines[visible_spine].set_linewidth(3)

    ''' creates the text objects we will be referencing and writing to '''
    def create_text(self, axis, text_position_y, marker_position_y, marker_edge_position_y, marker_position_x, position_x, font_text, color, text, entry):
        if entry == None:
            entry = []
            entry.append('               ')
            entry.append('                                                                                                                                                                                                                                                                                                                                                   ')
            entry.append('')
        text.append(axis.text(marker_position_x, marker_position_y, entry[0], font=font_text, color='none', fontsize=25,
                        transform=axis.transAxes,
                        bbox=dict(boxstyle='round', facecolor='#484848', edgecolor='none', alpha=0.19, pad=0.08)))
        text.append(axis.text(marker_position_x, marker_edge_position_y, entry[1], 
                        font=font_text, color='none', fontsize=1,transform=axis.transAxes,
                        bbox=dict(boxstyle='round', facecolor=color, edgecolor='none', alpha=0.7, pad=0.9)))
        text.append(axis.text(position_x, text_position_y, entry[2], font=font_text, color='#e8e8e8', fontsize=12, alpha=0.6,
                transform=axis.transAxes, bbox=dict(boxstyle='round', facecolor='none', edgecolor='none')))
        return(text)

    ''' this function is used to align the y-axis' amongst eachother '''
    def rangeFunction(self, l, l2):
        tick_range = lambda x : l2[0]+(x-l[0])/(l[1]-l[0])*(l2[1]-l2[0])
        ticks = tick_range(self.ax1.get_yticks())
        return ticks

    '''  returns a new sequence of frame information '''
    def new_frame_seq(self):
        return iter(range(self.samples.size))

    ''' initializes drawn lines and text '''
    def _init_draw(self):
        text = []
        for data_label in self.text_data:
            text.append(data_label)

        for parameter_label in self.text_parameter:
            text.append(parameter_label)

        for t in text:
            t.set_text('')

        for l in self.lines:
            l.set_data([],[])

    ''' appends data to the left and right sides of a list that will be combined to construct the plot'''
    def add_data_left(self, value):
        global entry_left
        if entry_left >= self.amount_selected:
            entry_left = 0
        self.added_data_left[entry_left] = value + self.added_data_left[entry_left]
        entry_left += 1

    def add_data_right(self, value):
        global entry_right
        if entry_right >= self.amount_selected:
            entry_right = 0
        self.added_data_right[entry_right] = self.added_data_right[entry_right] + value
        entry_right += 1

    def add_x_axis_left(self, value):
        self.added_x_axis_left = value + self.added_x_axis_left
    
    def add_x_axis_right(self, value):
        self.added_x_axis_right = self.added_x_axis_right + value


    ''' Extends the _step() method for the TimedAnimation class '''
    def _step(self, *args):
        try:
            TimedAnimation._step(self, *args)
        except Exception as e:
            self.abc += 1
            print(str(self.abc))
            TimedAnimation._stop(self)
            pass

    """ Function: _draw_frame
     | ------------------------------
     | Description:
     |     pulls data_array from added_data and added_time and updates
     |     the line and text resources of the plot.
    """
    def _draw_frame(self, framedata):
        global data_progression, data_check, zoom, selection, scroll, position_time, zoom_changed, hide_changed, slider_step
        self._drawn_artists = []

        if hide_changed:
            if len(hide) > 0 and len(hide) != 3:
                for x in range(0, len(self.text_parameter)):
                    self.text_parameter[x].set_text('')
                    self._drawn_artists.append(self.text_parameter[x]) 
                if len(hide) == 2:
                    for x in range(0, len(self.text_data)):
                        self.text_data[x].set_text('')
                        self._drawn_artists.append(self.text_data[x]) 
            else:
                for x in range(0, len(self.text_parameter)):
                    self.text_parameter[x].set_text(self.parameter_text_backup[x])
                    self._drawn_artists.append(self.text_parameter[x]) 
                
        if zoom:
            packet_size = 500
            total_size = 1000
        else:
            packet_size = 100
            total_size = 200

        if data_check == True:
            self.lines[0].set_linewidth(2)
            for i in range(0,self.amount_selected):
                if zoom:
                    self.added_data[i] = self.added_data_left[i][-(packet_size+3):-2] + self.added_data_right[i][1:(packet_size+2)]
                    self.lines[i].set_linewidth(2)
                else:
                    self.added_data[i] = self.added_data_left[i][-(packet_size+2):-2] + self.added_data_right[i][1:(packet_size+2)]
                    self.lines[i].set_linewidth(2.5)
            if scroll:
                self.added_x_axis = self.added_x_axis_left[-(packet_size+2):-1] + self.added_x_axis_right[0:(packet_size+1)]
            if len(self.added_data[0]) > (total_size):
                if scroll and len(self.added_x_axis) >= total_size:
                    self.ax1.set_xlim(self.added_x_axis[0], self.added_x_axis[total_size])
                    ticks = self.ax1.get_xticks()*.001
                    new_datalist = ["{:.3f}".format(value) for value in ticks]
                    self.ax1.set_xticklabels(new_datalist)
                    for i in range(0,self.amount_selected):
                        self.lines[i].set_data(self.added_x_axis[0:(total_size+1)],self.added_data[i][0:(total_size+1)])
                        self._drawn_artists.append(self.lines[i])
                elif not scroll:
                    if zoom_changed:
                        self.ax1.set_xlim(self.samples[0], self.samples[total_size])
                        zoom_changed = False
                    for i in range(0,self.amount_selected):
                        self.lines[i].set_data(self.samples[0:(total_size+1)],self.added_data[i][0:(total_size+1)])
                        self._drawn_artists.append(self.lines[i])
                if progress_on:
                    self.slider.set_bounds(0.38, 0.14, slider_step*(position_time-1000), .2)
                    self._drawn_artists.append(self.slider)
                
                if len(hide) != 2 and len(hide) != 3:
                    i, x, entry = 0, 0, 0
                    time_begin = len(self.text_data)-4
                    while i < len(self.text_data)-1: # data_array
                        if i >= time_begin: # time
                            time_string = '   %.2f ' % float(time_array[position_time]) + ' sec '
                            time_spacing, empty_string = Custom_Fig_Canvas.measure_space(self, time_string[:len(time_string)-4], self.parameter_text_backup)
                            if self.data_length[entry] != len(time_string) or hide_changed:
                                for x in range(0,2):
                                    self.text_data[i+x].set_text(time_spacing[x])
                                    self._drawn_artists.append(self.text_data[i+x])
                                    self.data_length[entry] = len(time_string)
                            self.text_data[i+2].set_text(time_string)
                            self._drawn_artists.append(self.text_data[i+2])
                            break
                        data_string = '   %.4f ' % float(self.added_data[entry][(packet_size)]) + yUnits[entry]
                        data_spacing, empty_string = Custom_Fig_Canvas.measure_space(self, data_string[:len(data_string)-2], self.parameter_text_backup)
                        if self.data_length[entry] != len(data_string) or hide_changed:
                            for x in range(0,2):
                                self.text_data[i+x].set_text(data_spacing[x])
                                self._drawn_artists.append(self.text_data[i+x])
                                self.data_length[entry] = len(data_string)
                        self.text_data[i+2].set_text(data_string)
                        self._drawn_artists.append(self.text_data[i+2])
                        i += 3
                        entry += 1

        hide_changed = False                
        data_progression = 1
        data_check = False
        self.added_data_left = [[0 for x in range(1)] for y in range(self.amount_selected)] 
        self.added_data_right = [[0 for x in range(1)] for y in range(self.amount_selected)] 
        self.added_data = [[0 for x in range(1)] for y in range(self.amount_selected)] 
        if scroll:
            self.added_x_axis_left.clear()
            self.added_x_axis_right.clear()
            self.added_x_axis.clear()
        self._drawn_artists.clear()
        

''' data_signal_left will call the add_data_callback_left function,
    which appends latest data_array into added_data and added_time '''
class Communicate_Data_Left(QtCore.QObject):
    data_signal_left = QtCore.Signal(list)

class Communicate_Data_Right(QtCore.QObject):
    data_signal_right = QtCore.Signal(list)

class Communicate_X_Axis_Left(QtCore.QObject):
    x_axis_signal_left = QtCore.Signal(list)

class Communicate_X_Axis_Right(QtCore.QObject):
    x_axis_signal_right = QtCore.Signal(list)    


""" Function: on_click ********************
 | ------------------------------
 | Description:
 |     When a portion of the plot is clicked, this function will 
 |     check to see what part of the plot was pressed, and what 
 |     button was used.
"""
def on_click(event):
    global hide, zoom, zoom_changed, hide_changed
    if event.button == 1:
        if event.xdata < 0.505:
            hide_changed = True
            if len(hide) == 0:
                hide.append(0)
            elif len(hide) == 1:
                hide.append(0)
            elif len(hide) == 2:
                hide.append(0)
            else:
                hide.clear()
        elif event.xdata >= 0.505 and event.xdata <= 1:
            zoom_changed = True
            if zoom:
                zoom = False
            else:
                zoom = True


""" Function: data_send_loop
 | ------------------------------
 | Description:
 |     Updates our video playback and calls for the next 
 |     piece of data_array. This function checks for user input
 |     and updates the playback icon.
 |
 | Parameter(s):
 |     add_data_callback_left - sets up a signal mechanism to later emit data_array 
 |     data_array - contains all parameter data_array, passed into another function
 |     frameList - a list containing every video frame
 |     frame_max - number of frames in the frameList
 |     video - video widget
 |     fps - frames per second of video 
 |     lines_in_file - the number of data_array values
 |     ui - contains all ui elements of the main window
 |     amount_selected - changes varibles in accordance with selected parameters
"""
def data_send_loop(add_data_callback_left, add_data_callback_right, data_array, frameList, video, fps, amount_selected, 
ui, add_x_axis_callback_left, add_x_axis_callback_right, self):
    # ui.Btn_Playback.setText(u"Normal Playback         ")
    global lines_in_file, frame_max, list_length, slider_step
    iconNP, iconFF, iconF, iconR, iconP, iconS = QIcon(), QIcon(), QIcon(), QIcon(), QIcon(), QIcon()
    iconNP.addFile(path_icon + "videoPlay.png", QSize(), QIcon.Normal, QIcon.Off)
    iconFF.addFile(path_icon + "videoFF.png", QSize(), QIcon.Normal, QIcon.Off)
    iconF.addFile(path_icon + "videoForward.png", QSize(), QIcon.Normal, QIcon.Off)
    iconR.addFile(path_icon + "videoReverse.png", QSize(), QIcon.Normal, QIcon.Off)
    iconP.addFile(path_icon + "videoPause.png", QSize(), QIcon.Normal, QIcon.Off)
    iconS.addFile(path_icon + "videoSlow.png", QSize(), QIcon.Normal, QIcon.Off)
    # ui.Btn_Playback.setIcon(iconNP)

    # Setup the signal-slot mechanism.
    data_source_left = Communicate_Data_Left()
    data_source_left.data_signal_left.connect(add_data_callback_left)
    data_source_right = Communicate_Data_Right()
    data_source_right.data_signal_right.connect(add_data_callback_right)
    x_axis_source_left = Communicate_X_Axis_Left()
    x_axis_source_left.x_axis_signal_left.connect(add_x_axis_callback_left)
    x_axis_source_right = Communicate_X_Axis_Right()
    x_axis_source_right.x_axis_signal_right.connect(add_x_axis_callback_right)


    step = (1000 / fps)
    if (int(frame_max*step) > lines_in_file):
        frame_max = int(lines_in_file/step)
    elif (lines_in_file >  int(frame_max*step)):
        lines_in_file = int(frame_max*step)
    list_length = min(lines_in_file, frame_max*step)
    slider_step = 100/list_length

    print('step = %f, fps = %f' % (step, fps))
    print('lines in data_array file: ', lines_in_file)
    pause = False
    reverse = False
    forward = False
    fastForward = False
    slow = False

    while True:
        if keyboard.is_pressed("down arrow"):
            time.sleep(0.1)
            if fastForward:
                fastForward = False
                pause = False
            if not pause:
                if slow:
                    slow = False
                    # ui.Btn_Playback.setIcon(iconNP)
                    # ui.Btn_Playback.setText(u"Normal Playback         ")
                else:
                    slow = True
                    fastForward = False
                    # ui.Btn_Playback.setIcon(iconS)
                    # ui.Btn_Playback.setText(u"Slow Playback             ")

        if keyboard.is_pressed("up arrow"):
            time.sleep(0.1)
            if slow:
                slow = False
            if fastForward:
                fastForward = False
                pause = False
                # ui.Btn_Playback.setIcon(iconNP)
                # ui.Btn_Playback.setText(u"Normal Playback         ")
            else:
                fastForward = True
                pause = True
                # ui.Btn_Playback.setIcon(iconFF)
                # ui.Btn_Playback.setText(u"Fast Forward                ")
            time.sleep(0.05)

        if keyboard.is_pressed("left arrow"):
            if slow:
                slow = False
            # ui.Btn_Playback.setIcon(iconR)
            # ui.Btn_Playback.setText(u"Step Backward(s)        ")
            time.sleep(0.08)
            reverse = True
            pause = True
            fastForward = False

        if keyboard.is_pressed("right arrow"):
            if slow:
                slow = False
            # ui.Btn_Playback.setIcon(iconF)
            # ui.Btn_Playback.setText(u"Step Forward(s)           ")
            time.sleep(0.08)
            forward = True
            pause = True
            fastForward = False

        if keyboard.is_pressed(' '):
            time.sleep(0.1)
            if slow:
                slow = False
            if pause:
                pause = False
                # ui.Btn_Playback.setIcon(iconNP)
                # ui.Btn_Playback.setText(u"Normal Playback         ")
            else:
                pause = True
                # ui.Btn_Playback.setIcon(iconP)
                # ui.Btn_Playback.setText(u"Paused                           ")
            if fastForward:
                pause = True
                fastForward = False
                # ui.Btn_Playback.setIcon(iconP)
                # ui.Btn_Playback.setText(u"Paused                           ")
            time.sleep(0.05)

        if not pause:
            data_increment(data_array, frameList, video, step,
                          data_source_left, data_source_right, 3, slow, amount_selected, 
                           x_axis_source_left, x_axis_source_right)

        elif fastForward:
            data_increment(data_array, frameList, video, step,
                          data_source_left, data_source_right, 2, False, amount_selected, 
                           x_axis_source_left, x_axis_source_right)

        elif reverse:
            data_increment(data_array, frameList, video, step,
                          data_source_left, data_source_right, -1, False, amount_selected, 
                           x_axis_source_left, x_axis_source_right)
            reverse = False
            # ui.Btn_Playback.setText(u"Paused                           ")
            # ui.Btn_Playback.setIcon(iconP)

        elif forward:
            data_increment(data_array, frameList, video, step,
                          data_source_left, data_source_right, 1, False, amount_selected, 
                           x_axis_source_left, x_axis_source_right)
            forward = False
            # ui.Btn_Playback.setText(u"Paused                           ")
            # ui.Btn_Playback.setIcon(iconP)
        else:
            data_increment(data_array, frameList, video, step,
                          data_source_left, data_source_right, 4, False, amount_selected, 
                           x_axis_source_left, x_axis_source_right)

""" Function: data_increment
 | ------------------------------
 | Description:
 |     If previous checks are passed, the program will
 |     then begin executing. This function creates the
 |     video and plot widget which will be executed in 
 |     a separate thread.
 |
 | Parameter(s):
 |     data_array - contains all parameter data_array, passed into another function
 |     frameList - a list containing every video frame
 |     frame_max - number of frames in the frameList
 |     video - video widget
 |     lines_in_file - the number of data_array values
 |     step - the number of list items in between each video frame
 |     data_source_left - signal-slot mechanism, contains data_array signal call
 |     increment - specifies which setting to apply to video
       if = -1: step backward one frame
       if = 1: step forward
       if = 2: fast forward
       if = 3: normal playback
       if = 4: pause
 |     slow - if slow motion, adds extra pause to normal playback
"""
def data_increment(data_array, frameList, video, step, data_source_left, data_source_right, 
increment, slow, amount_selected, x_axis_source_left, x_axis_source_right):
    global data_position, frameCount, timeFrame, past_back, past_forward, data_progression, frame_max
    repeat = 2
    if increment == -1:  # step backward
        print('step back')
        if past_forward == True:
            past_forward = False
            data_position -= int(step)
            timeFrame -= step * 2
            frameCount -= 2
            if check_begin(frameCount, data_position) == 0:
                frameCount = int(frame_max - 1)
                data_position = int(frame_max * step) 
                timeFrame = math.ceil(frame_max * step - step)
            else:
                video.setPixmap(QPixmap.fromImage(frameList[frameCount]))
        data_position -= int(step)
        if check_begin(frameCount, data_position) == 0:
            frameCount = int(frame_max - 1)
            data_position = int(frame_max * step) 
            timeFrame = math.ceil(frame_max * step - step)
            video.setPixmap(QPixmap.fromImage(frameList[frameCount]))
        elif check_end(frameCount, data_position-2000) == 0:
            frameCount = 0
            data_position = 0
            timeFrame = 0
        try:
            signal_emit(data_source_left, data_source_right, x_axis_source_left, x_axis_source_right)
        except:
            exit(0)
        if data_position <= timeFrame:
            timeFrame -= step
            video.setPixmap(QPixmap.fromImage(frameList[frameCount]))
            frameCount -= 1
        past_back = True

    elif increment == 1:  # step forward
        print('step forward')
        if past_back == True:
            past_back = False
            data_position += int(step)
            timeFrame += step * 2
            frameCount += 2
            if check_end(frameCount, data_position-2000) == 0:
                frameCount = 0
                data_position = 0
                timeFrame = 0
            else:
                video.setPixmap(QPixmap.fromImage(frameList[frameCount]))

        data_position += int(step)
        if check_begin(frameCount, data_position) == 0:
            frameCount = int(frame_max - 1)
            data_position = int(frame_max * step) 
            timeFrame = math.ceil(frame_max * step - step)
        elif check_end(frameCount, data_position-2000) == 0:
            frameCount = 0
            data_position = 0
            timeFrame = 0
        try:
            signal_emit(data_source_left, data_source_right, x_axis_source_left, x_axis_source_right)
        except:
            exit(0)

        if data_position >= timeFrame:
            timeFrame += step
            video.setPixmap(QPixmap.fromImage(frameList[frameCount]))
            frameCount += 1
        past_forward = True

    elif increment == 2:  # fast forward
        for i in range(0, 4*repeat):
            data_position += 1
            if check_end(frameCount, data_position-2000) == 0:
                frameCount = 0
                data_position = 0
                timeFrame = 0
            try:
                signal_emit(data_source_left, data_source_right, x_axis_source_left, x_axis_source_right)
            except:
                exit(0)
            if data_position >= timeFrame:
                video.setPixmap(QPixmap.fromImage(frameList[frameCount]))
                timeFrame += step
                frameCount += 1

    elif increment == 3: # normal playback
        if slow:
            time.sleep(0.003)
        for i in range(0, repeat):
            data_position += 1
            # time.sleep(1)
            if check_end(frameCount, data_position-2000) == 0:
                frameCount = 0
                data_position = 0
                timeFrame = 0
            try:
                signal_emit(data_source_left, data_source_right, x_axis_source_left, x_axis_source_right)
            except:
                exit(0)

            if data_position >= timeFrame:
                video.setPixmap(QPixmap.fromImage(frameList[frameCount]))
                timeFrame += step
                frameCount += 1

    if increment != -1 or increment != 1:  # if we are not manually changing frames
        time.sleep(0.0001)


""" Function: check_end
 | ------------------------------
 | Description:
 |     Check to see if the end of the data_array list or 
 |     video list has been reached.
 |
 | Parameter(s):
 |     frameCount - current position in list of video frames 
 |     frame_max - max position in list of video frames 
 |     data_position - current position in list of parameter data_array 
 |     lines_in_file - max position in list of parameter data_array 
"""
def check_end(frameCount, data_position):
    global lines_in_file, frame_max
    if frameCount >= frame_max:
        data_progression = 1
        return 0
    elif data_position  >= (lines_in_file - 1):
        data_progression = 1
        return 0
    return 1

""" Function: check_begin
 | ------------------------------
 | Description:
 |     Check to see if the beginning of the data_array 
 |     list or  video list has been reached.
 |
 | Parameter(s):
 |     frameCount - current position in list of video frames 
 |     data_position - current position in list of parameter data_array 
"""
def check_begin(frameCount, data_position):
    if frameCount <= 0:
        data_progression = 1
        return 0
    elif data_position <= 0:
        data_progression = 1
        return 0
    return 1

""" Function: signal_emit
 | ------------------------------
 | Description:
 |     Sends data in packets of 40-200 at a time.
"""
def signal_emit(data_left, data_right, x_left, x_right):
    global data_progression, data_check, scroll, selection, data_position, position_time
    current_position = data_position + 1000
    print('signal emit')
    while(data_progression <= 5):
        index = []
        initial_sub = 0
        
        if zoom: 
            packet_size = 200
        else:
            packet_size = 40

        if data_progression == 1:
            initial_sub = 1
            data_check = False

        index.append((current_position-data_progression-packet_size*data_progression))
        index.append(current_position-data_progression-packet_size*(data_progression-1))
        index.append(current_position-data_progression+packet_size*(data_progression-1))
        index.append((current_position-data_progression+packet_size*data_progression))
        if scroll:
            x_left.x_axis_signal_left.emit(x_array[index[0]:index[1]])
            x_right.x_axis_signal_right.emit(x_array[index[2]-initial_sub:index[3]])
        if data_progression == 1:
            position_time = current_position
        for i in range(0, len(selection)):
            data_left.data_signal_left.emit(data_array[i][index[0]:index[1]])
            data_right.data_signal_right.emit(data_array[i][index[2]-initial_sub:index[3]])

        initial_sub = 0
        data_progression += 1
        index.clear()

        if data_progression > 5:
            data_check = True



