from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QMessageBox, QMainWindow, QShortcut
from PyQt5.QtGui import QKeySequence
from PyQt5.QtCore import pyqtSlot, QRunnable, QThreadPool
import sys
from mainwindow import *
from neumorphism import NeumorphismEffect
from database_connect import Database
from datetime import datetime
from PyQtWorker import Worker
import time
import RPi.GPIO as GPIO
import subprocess

#QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)


class Main(QMainWindow): #MAIN WINDOW
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.bg_colour = '#FFFFFF'  
        self.neumorphismEffect()
        self.databaseConnect()
        self.ui.button_start0.clicked.connect(lambda: self.display(1))
        self.ui.button_back1.clicked.connect(lambda: self.display(0))
        self.ui.button_back2.clicked.connect(lambda: self.projectPageButtons("back"))
        self.ui.button_back4.clicked.connect(lambda: self.display(1))
        self.ui.button_back3.clicked.connect(lambda: self.stepPageButtons("back"))
        self.ui.button_projects1.clicked.connect(lambda: self.updateProjectList())
        self.ui.button_refresh2_1.clicked.connect(lambda: self.updateProjectList())
        self.ui.button_tutorials1.clicked.connect(lambda: self.updateTutorialsList())
        self.ui.button_refresh2_2.clicked.connect(lambda: self.updateTutorialsList())
        self.ui.button_settings1.clicked.connect(lambda: self.clearLayout(self.ui.verticalLayout_project_list,"projects"))
        self.ui.button_refresh2.clicked.connect(lambda: self.projectPageButtons("refresh"))
        self.ui.button_refresh3.clicked.connect(lambda: self.stepPageButtons("refresh"))
        self.ui.button_refresh4.clicked.connect(lambda: self.updateTutorialSteps(self.current_tutorial_index, self.tutorials[self.current_tutorial_index][0]))
        self.ui.button_run2.clicked.connect(lambda: self.projectPageButtons("run"))
        self.ui.button_run3.clicked.connect(lambda: self.stepPageButtons("run"))
        self.ui.button_power0.clicked.connect(lambda: self.display(5))
        self.ui.button_power1.clicked.connect(lambda: self.display(5))
        self.ui.button_power2.clicked.connect(lambda: self.display(5))
        self.ui.button_power3.clicked.connect(lambda: self.display(5))
        self.ui.button_power4.clicked.connect(lambda: self.display(5))
        self.ui.button_wakeup.clicked.connect(lambda: self.display(0))
        self.shortcut = QShortcut(QKeySequence("Ctrl+E"), self)
        self.shortcut.activated.connect(sys.exit)

        self.threadpool = QThreadPool()

        QtWidgets.QScroller.grabGesture(self.ui.scrollArea_project_list.viewport(), QtWidgets.QScroller.LeftMouseButtonGesture)
        QtWidgets.QScroller.grabGesture(self.ui.scrollArea.viewport(), QtWidgets.QScroller.LeftMouseButtonGesture)
        QtWidgets.QScroller.grabGesture(self.ui.scrollArea_2.viewport(), QtWidgets.QScroller.LeftMouseButtonGesture)
        self.list_projectframe = []
        self.list_projecttitle = []
        self.list_projectdesc = []
        self.list_projectbutton = []
        self.list_projectgrid = []
        self.project_frame_count=0
        self.list_tutorialsframe = []
        self.list_tutorialsbutton = []
        self.list_tutorialstitle = []
        self.list_tutorialsdesc = []
        self.list_tutorialsgrid = []
        self.tutorials_frame_count = 0
        self.code_running = 0
        self.list_stepframe = []
        self.list_stepno = []
        self.list_stepdesc = []
        self.list_stepbutton = []
        self.list_stepgrid = []
        self.tutorials = []
        self.step_frame_count=0
        self.user_id = 3
        self.updateProjectList()
        self.setName()
        self.ui.scrollArea_project_list.setStyleSheet("background-colour: transparent;")
        self.ui.scrollArea_tutorials_list.setStyleSheet("background-colour: transparent;")
        self.ui.scrollArea.setStyleSheet("background-colour: transparent;")
        self.ui.scrollArea_2.setStyleSheet("background-colour: transparent;")




    def neumorphismEffect(self):
        self.ui.button_start0.setGraphicsEffect(NeumorphismEffect(color=QtGui.QColor(self.bg_colour),clipRadius=10, distance=10))
        self.ui.button_logout0.setGraphicsEffect(NeumorphismEffect(color=QtGui.QColor(self.bg_colour),clipRadius=10, distance=10))
        self.ui.button_refresh2.setGraphicsEffect(NeumorphismEffect(color=QtGui.QColor(self.bg_colour),clipRadius=10, distance=10))
        self.ui.button_refresh3.setGraphicsEffect(NeumorphismEffect(color=QtGui.QColor(self.bg_colour),clipRadius=10, distance=10))
        self.ui.button_refresh4.setGraphicsEffect(NeumorphismEffect(color=QtGui.QColor(self.bg_colour),clipRadius=10, distance=10))
        self.ui.button_refresh2_1.setGraphicsEffect(NeumorphismEffect(color=QtGui.QColor(self.bg_colour),clipRadius=5, distance=5))
        self.ui.button_refresh2_2.setGraphicsEffect(NeumorphismEffect(color=QtGui.QColor(self.bg_colour),clipRadius=5, distance=5))
        self.ui.frame_debug2.setGraphicsEffect(NeumorphismEffect(color=QtGui.QColor(self.bg_colour),clipRadius=10, distance=10))
        self.ui.frame_debug3.setGraphicsEffect(NeumorphismEffect(color=QtGui.QColor(self.bg_colour),clipRadius=10, distance=10))
        self.ui.frame.setGraphicsEffect(NeumorphismEffect(color=QtGui.QColor(self.bg_colour),clipRadius=10, distance=10,origin=QtCore.Qt.BottomLeftCorner))

    def setName(self):
        try:
            self.f_name = self.dbConnection.getName(self.user_id)
            self.ui.label_name0.setText(self.f_name)
        except:
            print('error setting name')
            self.ui.label_name0.setText("")

    def addEntry(self, index, id, title, description, calltype):
        description = (description[:50] + '...') if len(description)>52 else description

        frame_entry = QtWidgets.QFrame(self.ui.scrollAreaWidgetContents_project_list)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(frame_entry.sizePolicy().hasHeightForWidth())
        frame_entry.setSizePolicy(sizePolicy)
        frame_entry.setMinimumSize(QtCore.QSize(250, 75))
        frame_entry.setMaximumSize(QtCore.QSize(250, 75))
        frame_entry.setStyleSheet("QFrame {\n"
        "        \n"
        "    background-color: #FFFFFF;\n"
        "    border-radius: 5px;\n"
        "\n"
        "}")
        frame_entry.setFrameShape(QtWidgets.QFrame.StyledPanel)
        frame_entry.setFrameShadow(QtWidgets.QFrame.Raised)
        frame_entry.setObjectName("frame_entry")
        gridLayout_entry = QtWidgets.QGridLayout(frame_entry)
        gridLayout_entry.setVerticalSpacing(2)
        gridLayout_entry.setContentsMargins(10, 10, 0, 10)
        gridLayout_entry.setObjectName("gridLayout_entry")
        label_entry_title = QtWidgets.QLabel(frame_entry)
        font = QtGui.QFont()
        font.setFamily("Raleway")
        font.setPointSize(10)
        label_entry_title.setFont(font)
        label_entry_title.setObjectName("label_entry_title")
        label_entry_title.setAlignment(QtCore.Qt.AlignTop)
        gridLayout_entry.addWidget(label_entry_title, 0, 0, 1, 1)
        label_entry_desc = QtWidgets.QLabel(frame_entry)
        font = QtGui.QFont()
        font.setFamily("Raleway")
        font.setPointSize(8)
        label_entry_desc.setWordWrap(True)
        label_entry_desc.setFont(font)
        label_entry_desc.setObjectName("label_entry_desc")
        label_entry_desc.setAlignment(QtCore.Qt.AlignTop)
        gridLayout_entry.addWidget(label_entry_desc, 1, 0, 1, 1)
        button_entry = QtWidgets.QPushButton(frame_entry)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(button_entry.sizePolicy().hasHeightForWidth())
        button_entry.setSizePolicy(sizePolicy)
        button_entry.setMinimumSize(QtCore.QSize(75, 0))
        font = QtGui.QFont()
        font.setFamily("7 Raleway")
        font.setPointSize(5)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        button_entry.setFont(font)
        button_entry.setStyleSheet("QPushButton:hover{\n"
        "        \n"
        "}\n"
        "\n"
        "QPushButton {\n"
        "\n"
        "        border-radius: 5px;\n"
        "\n"
        "        background-color: #FFFFFF;\n"
        "        font: regular large \"Raleway\";\n"
        "        height: 30px;\n"
        "}\n"
        "\n"
        "\n"
        "\n"
        "\n"
        "QPushButton:pressed {\n"
        "              background-color: #E0E0E0;\n"
        "}\n"
        "\n"
        "QPushButton:on {\n"
        "       \n"
        "}\n"
        "\n"
        "QPushButton:disabled {\n"
        "        \n"
        "}")
        button_entry.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Images/right-arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        button_entry.setIcon(icon)
        button_entry.setIconSize(QtCore.QSize(40,40))
        button_entry.setObjectName("button_entry")
        button_entry.clicked.connect(lambda: self.entryClick(index,id,calltype))
        gridLayout_entry.addWidget(button_entry, 0, 1, 2, 1)
        label_entry_title.setText(title)
        label_entry_desc.setText(description)

        frame_entry.setGraphicsEffect(NeumorphismEffect(color=QtGui.QColor("#FFFFFF"),clipRadius=10, distance=10))

        

        if calltype == "projects":
            self.ui.verticalLayout_project_list.addWidget(frame_entry)
            self.list_projectframe.append(frame_entry)
            self.list_projectbutton.append(button_entry)
            self.list_projecttitle.append(label_entry_title)
            self.list_projectdesc.append(label_entry_desc)
            self.list_projectgrid.append(gridLayout_entry)
            self.project_frame_count+=1
        elif calltype == "tutorials":
            self.ui.verticalLayout_tutorials_list.addWidget(frame_entry)
            self.list_tutorialsframe.append(frame_entry)
            self.list_tutorialsbutton.append(button_entry)
            self.list_tutorialstitle.append(label_entry_title)
            self.list_tutorialsdesc.append(label_entry_desc)
            self.list_tutorialsgrid.append(gridLayout_entry)
            self.tutorials_frame_count+=1

        print('project add')
        print(self.list_projectframe)

    def clearLayout(self,layout,calltype=None):
        print("clearing" +str(layout))
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.clearLayout(item.layout(),calltype)
        if calltype == "projects":
            self.list_projectframe = []
            self.list_projecttitle = []
            self.list_projectdesc = []
            self.list_projectbutton = []
            self.list_projectgrid = []
            self.project_frame_count=0
        elif calltype == "tutorials":
            self.list_tutorialsframe = []
            self.list_tutorialsbutton = []
            self.list_tutorialstitle = []
            self.list_tutorialsdesc = []
            self.list_tutorialsgrid = []
            self.tutorials_frame_count = 0
        elif calltype == "tutorial-step":
            self.list_stepframe = []
            self.list_stepno = []
            self.list_stepbutton = []
            self.list_stepgrid = []
            self.step_frame_count=0
    def databaseConnect(self):
        self.dbConnection = Database()
    def databaseClose(self):
        self.dbConnection.connectionClose()

    def updateProjectList(self):
        self.display(1)
        self.displayHome(0)
        self.clearLayout(self.ui.verticalLayout_project_list,"projects")
        try:
            self.projects = self.dbConnection.getProjects(self.user_id)
            if self.projects == []:
                self.scrollAreaNotify("It looks like you haven't started any projects yet!", "projects")
        except:
            print('connection ERROR')
            if self.projects == []:
                print('no projects stored ERROR')
                self.scrollAreaNotify("Cannot connect!", "projects")
                return
            pass
        for i, project in enumerate(self.projects):
            self.addEntry(i, project[0],project[1],project[2], "projects")
        print('projects added')

    def updateTutorialsList(self):
        self.displayHome(1)
        self.clearLayout(self.ui.verticalLayout_tutorials_list,"tutorials")
        try:
            self.tutorials, self.tutorials_steps = self.dbConnection.getTutorials(self.user_id)
            if self.tutorials == []:
                self.scrollAreaNotify("It looks like you haven't started any tutorials yet!", "tutorials")

        except:
            print('connection ERROR')
            if self.tutorials == []:
                print('no tutorials stored ERROR')
                self.scrollAreaNotify("Cannot connect!", "tutorials")
                return
            pass
        for i, tutorial in enumerate(self.tutorials):
            (project_id,title,description,slug) = tutorial
            self.addEntry(i, project_id, title, description, "tutorials")
        print('tutorials added')

    def updateTutorialSteps(self, index, tutorial_id):
        try:
            self.tutorials_steps[tutorial_id] = self.dbConnection.getTutorialSteps(self.user_id,tutorial_id)
        except:
            print("Connection ERROR")
        (project_id,title,description,slug) = self.tutorials[index]
        title = (title[:30] + '...') if len(title)>32 else title
        description = (description[:50] + '...') if len(description)>52 else description
        self.ui.label_title4.setText(title)
        self.ui.label_desc4.setWordWrap(True)
        self.ui.label_desc4.setText(description)
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        self.ui.label_lastupdate4.setText("Last Updated: "+current_time)
        self.clearLayout(self.ui.verticalLayout_step_list, "tutorial-step")
        tutorial_steps = self.tutorials_steps[project_id]
        #print(tutorial_steps)
        for step in tutorial_steps:
            step_no = step[2]
            #print(step_no)
            self.addTutorialStep(index, project_id, step_no)

    def process_error(self, message):
        print(message)
        for i in range(len(message)):
            if message[i-1:i] == '\n':
                error_location = message[i:]

            elif message[i-4:i] == 'line':
                line_location = message[i+1:i+6]

        for i in range(len(error_location)):
            if error_location[i-1:i] == ":":
                error = error_location[:i-1]
                break

        for i in range(len(line_location)):
            if line_location[i] == ",":
                line = line_location[:i]
                break
    
        return error, line

    def addTutorialStep(self, index, project_id, step_no):

        print(str(step_no) + " added")
        frame_entry = QtWidgets.QFrame(self.ui.scrollAreaWidgetContents_step_list)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(frame_entry.sizePolicy().hasHeightForWidth())
        frame_entry.setSizePolicy(sizePolicy)
        frame_entry.setMinimumSize(QtCore.QSize(250, 75))
        frame_entry.setMaximumSize(QtCore.QSize(250, 75))
        frame_entry.setStyleSheet("QFrame {\n"
        "        \n"
        "    background-color: #FFFFFF;\n"
        "    border-radius: 5px;\n"
        "\n"
        "}")
        frame_entry.setFrameShape(QtWidgets.QFrame.StyledPanel)
        frame_entry.setFrameShadow(QtWidgets.QFrame.Raised)
        frame_entry.setObjectName("frame_entry")
        gridLayout_entry = QtWidgets.QGridLayout(frame_entry)
        gridLayout_entry.setVerticalSpacing(2)
        gridLayout_entry.setContentsMargins(10, 10, 0, 10)
        gridLayout_entry.setObjectName("gridLayout_entry")
        label_step_no = QtWidgets.QLabel(frame_entry)
        font = QtGui.QFont()
        font.setFamily("Raleway")
        font.setPointSize(10)
        label_step_no.setFont(font)
        label_step_no.setObjectName("label_entry_title")
        label_step_no.setAlignment(QtCore.Qt.AlignVCenter)
        gridLayout_entry.addWidget(label_step_no, 0, 0, 2, 1)
        button_entry = QtWidgets.QPushButton(frame_entry)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(button_entry.sizePolicy().hasHeightForWidth())
        button_entry.setSizePolicy(sizePolicy)
        button_entry.setMinimumSize(QtCore.QSize(75, 0))
        font = QtGui.QFont()
        font.setFamily("7 Raleway")
        font.setPointSize(5)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        button_entry.setFont(font)
        button_entry.setStyleSheet("QPushButton:hover{\n"
        "        \n"
        "}\n"
        "\n"
        "QPushButton {\n"
        "\n"
        "        border-radius: 5px;\n"
        "\n"
        "        background-color: #FFFFFF;\n"
        "        font: regular large \"Raleway\";\n"
        "        height: 30px;\n"
        "}\n"
        "\n"
        "\n"
        "\n"
        "\n"
        "QPushButton:pressed {\n"
        "               background-color: #E0E0E0;\n"
        "}\n"
        "\n"
        "QPushButton:on {\n"
        "       \n"
        "}\n"
        "\n"
        "QPushButton:disabled {\n"
        "        \n"
        "}")
        button_entry.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Images/right-arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        button_entry.setIcon(icon)
        button_entry.setIconSize(QtCore.QSize(30,30))
        button_entry.setObjectName("button_entry")
        button_entry.clicked.connect(lambda: self.entryClick(index, id, "tutorial-step", step_no))
        gridLayout_entry.addWidget(button_entry, 0, 1, 2, 1)
        label_step_no.setText(str(step_no))

        frame_entry.setGraphicsEffect(NeumorphismEffect(color=QtGui.QColor("#ECF0F3"),clipRadius=10, distance=10))

        self.ui.verticalLayout_step_list.addWidget(frame_entry)
        self.list_stepframe.append(frame_entry)
        self.list_stepno.append(label_step_no)
        self.list_stepbutton.append(button_entry)
        self.list_stepgrid.append(gridLayout_entry)
        self.step_frame_count+=1

    def scrollAreaNotify(self, string, calltype):
        if calltype == 'projects':
            label_noentries = QtWidgets.QLabel(self.ui.scrollAreaWidgetContents_project_list)
        elif calltype == 'tutorials':
            label_noentries = QtWidgets.QLabel(self.ui.scrollAreaWidgetContents_tutorials_list)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(label_noentries.sizePolicy().hasHeightForWidth())
        label_noentries.setSizePolicy(sizePolicy)
        label_noentries.setMaximumSize(QtCore.QSize(155555, 50))
        font = QtGui.QFont()
        label_noentries.setWordWrap(True)
        font.setFamily("Raleway")
        font.setPointSize(8)
        label_noentries.setFont(font)
        label_noentries.setObjectName("label_noentries")
        label_noentries.setText(string)
        if calltype == 'projects':
            self.ui.verticalLayout_project_list.addWidget(label_noentries)
        elif calltype == 'tutorials':
            self.ui.verticalLayout_tutorials_list.addWidget(label_noentries)
    
    def entryClick(self, index, id, calltype, step_no=None):
        if calltype == 'projects':
            self.projectPage(index)
        elif calltype == 'tutorials':
            self.current_tutorial_index = index
            self.updateTutorialSteps(index, id)
            self.display(4)
        elif calltype == 'tutorial-step':
            self.current_tutorial_step_no = step_no
            self.updateStepPage()
            self.display(3)

    def projectPage(self, index):
        self.currProj = self.projects[index]
        self.ui.label_debugpanel2.setText(" ")
        (id, title, desc, code) = self.currProj
        title = (title[:30] + '...') if len(title)>32 else title
        self.ui.label_title2.setText(title)
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        self.ui.label_lastupdate2.setText("Last Updated: "+current_time)
        with open(f'current_project.py', 'w') as fp: 
                fp.write(code)
        #print(id, title, desc, code)
        self.display(2)

    def updateProjectPage(self):
        id = self.currProj[0]
        self.ui.label_debugpanel2.setText("")
        
        try:
            self.currProj = self.dbConnection.getSingleProject(id)
            (id, title, desc, code) = self.currProj
            title = (title[:30] + '...') if len(title)>32 else title
            self.ui.label_title2.setText(title)
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            self.ui.label_lastupdate2.setText("Last Updated: "+current_time)
            with open(f'current_project.py', 'w') as fp: 
                fp.write(code)
        except:
            print('connection ERROR')
            pass
    
    def updateStepPage(self):
        self.ui.label_debugpanel3.setText("")
        try:
            (project_id,title,description,slug) = self.tutorials[self.current_tutorial_index]
            self.updateTutorialSteps(self.current_tutorial_index, project_id)
            code = [self.tutorials_steps[project_id][x] for x in range(len(self.tutorials_steps[project_id])) if self.tutorials_steps[project_id][x][2] == self.current_tutorial_step_no][0][0]
            self.ui.label_title3.setText("{} - Step {}".format(title, str(self.current_tutorial_step_no)))
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            self.ui.label_lastupdate3.setText("Last Updated: "+current_time)
            with open(f'current_step.py', 'w') as fp: 
                #print(code)
                fp.write(code)
        except:
            print('connection ERROR')
            pass

    def executeCode(self, file):
        self.proc = subprocess.Popen(["python3", file], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.proc.wait()
        return (self.interrupted, self.proc.communicate())

    def killCode(self,channel):
        self.interrupted = 1
        try:
            self.proc.kill()
        except:
            print("ERROR cancelling code")

    def setupInterrupt(self):
        GPIO.setmode(GPIO.BOARD)
        interrupt_pin = 10
        self.interrupted = 0
        GPIO.setup(interrupt_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(interrupt_pin, GPIO.FALLING, callback=self.killCode, bouncetime=300)

    def resetGPIO(self):
        GPIO.setwarnings(False)
        GPIO.cleanup()
        GPIO.setmode(GPIO.BOARD)

    def projectPageButtons(self, calltype):
        if self.code_running == 0:
            if calltype == "refresh":
                self.updateProjectPage()
            elif calltype == "back":
                self.display(1)
            elif calltype == "run":
                self.runProjectCode()
        else:
            print('code running')
            self.ui.button_run2.setChecked(True)

    def runProjectCode(self):
        self.worker = Worker(self.executeCode, "current_project.py")
        self.worker.signals.error.connect(self.errorProjectCode)
        self.worker.signals.result.connect(self.resultProjectCode)
        self.worker.signals.finished.connect(self.finishProjectCode)
        self.ui.button_run2.setChecked(True)
        self.code_running = 1
        self.resetGPIO()
        self.setupInterrupt()
        self.threadpool.start(self.worker)
 
    def finishProjectCode(self):
        print('code done')
        self.code_running = 0
        self.worker = None
        self.ui.button_run2.setChecked(False)
        
    def resultProjectCode(self, s):
        self.ui.label_debugpanel2.setText(s)
        self.ui.label_debugpanel2.setWordWrap(True)
        
    def errorProjectCode(self, s):
        self.code_running = 0
        self.ui.button_run2.setChecked(False)
        error, line_no = self.process_error(s)
        string = "There is a {} error in line {}".format(error, line_no)
        code = self.currProj[3]
        code_lines = code.splitlines()
        line = code_lines[int(line_no)-1]
        string += '\n Line: "'+ line + '"'
        self.ui.label_debugpanel2.setText(string)
        self.ui.label_debugpanel2.setWordWrap(True)

    def stepPageButtons(self, calltype):
        if self.code_running == 0:
            if calltype == "refresh":
                self.updateStepPage()
            elif calltype == "back":
                self.display(4)
            elif calltype == "run":
                self.runStepCode()
        else:
            print('code running')
            self.ui.button_run3.setChecked(True)


    def runStepCode(self):
        worker = Worker(self.executeCode, "current_step.py")
        worker.signals.error.connect(self.errorStepCode)
        worker.signals.finished.connect(self.finishStepCode)
        worker.signals.result.connect(self.resultStepCode)
        self.ui.button_run3.setChecked(True)
        self.code_running = 1
        self.resetGPIO()
        self.setupInterrupt()
        self.threadpool.start(worker)

    def errorStepCode(self, s):
        self.code_running = 0
        self.ui.button_run3.setChecked(False)
        error, line_no = self.process_error(s)
        string = "There is a {} error in line {}".format(error, line_no)
        code = [self.tutorials_steps[project_id][x] for x in range(len(self.tutorials_steps[project_id])) if self.tutorials_steps[project_id][x][2] == self.current_tutorial_step_no][0][0]
        code_lines = code.splitlines()
        line = code_lines[int(line_no)-1]
        string += '\n Line: "'+ line + '"'
        self.ui.label_debugpanel3.setText(string)
        self.ui.label_debugpanel3.setWordWrap(True)
        
    def resultStepCode(self, s):
        self.ui.label_debugpanel3.setText(s)
        self.ui.label_debugpanel3.setWordWrap(True)

    def finishStepCode(self):
        print('code done')
        self.code_running = 0
        self.ui.button_run3.setChecked(False)
        
    def displayHome(self,i):
        #display the chosen stacked widget ie the page of the gui for the home screen
        print('setting home index', i)
        self.ui.stackedWidget_home_menu.setCurrentIndex(i)

    def display(self,i):
        #display the chosen stacked widget ie the page of the gui
        print('setting index', i)
        self.ui.stackedWidget.setCurrentIndex(i)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = Main()
    window.display(0)
    window.show()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
    sys.exit(app.exec_())