
import sys
import PyQt5


from PyQt5 import QtTest
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget,QFrame,QScrollArea,QGridLayout,QStackedWidget,QHBoxLayout,QFileDialog,QButtonGroup,QToolBar,QAction,QProgressBar
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal



wid = 1024
hit = 600

resetVal = 1

# ---------------------------------------------------------------------- MAIN WINDOW -------------------------------------------------------------------------

class MainWindow(QMainWindow):

    def __init__(self, parent=None):

        QMainWindow.__init__(self, parent)
        
        self.setGeometry(0,0,wid,hit)
        self.central_widget = QStackedWidget()

        toolbar = QToolBar("My main toolbar")
        self.addToolBar(toolbar)

        button_action = QAction("HOME", self) 
        button_action.setStatusTip("This is your Button")
        toolbar.addAction(button_action)

        self.button = QPushButton("Checklist") # Checklist
        self.button2 = QPushButton("Navigation") # Navigation
        self.button3 = QPushButton("Telemetry") # Telemetry
        self.button4 = QPushButton("Communications") # Communications
        self.button5 = QPushButton("Settings") # Settings
        self.button6 = QPushButton("Robot/RC") # Robot/RC

        self.HomeButtons = QWidget()
        lay = QGridLayout()
        lay.addWidget(self.button,0,0) # Checklist
        lay.addWidget(self.button2,0,1)
        lay.addWidget(self.button3,0,2)
        lay.addWidget(self.button4,1,0)
        lay.addWidget(self.button5,1,1)
        lay.addWidget(self.button6,1,2)
        self.HomeButtons.setLayout(lay)

        self.setCentralWidget(self.central_widget)
        
        self.nav_screen = Navigate(self)
        self.checklist = Checklist()
        self.telemetry = Tel()
        self.central_widget.addWidget(self.HomeButtons)
        self.central_widget.addWidget(self.nav_screen)
        self.central_widget.addWidget(self.checklist)
        self.central_widget.addWidget(self.telemetry)
        self.central_widget.setCurrentWidget(self.HomeButtons)
        
        def valChange():
            global resetVal
            resetVal = 2
            #print(resetVal)

        self.button.clicked.connect(lambda: self.central_widget.setCurrentWidget(self.checklist))
        self.button2.clicked.connect(lambda: self.central_widget.setCurrentWidget(self.nav_screen))
        self.button3.clicked.connect(lambda: self.central_widget.setCurrentWidget(self.telemetry))
        #self.button4.clicked.connect(self.oh_no)

        #mybutton.when_pressed = btpressed

        def goHome(self):
            self.nav_screen.clicked.connect(lambda: self.central_widget.setCurrentWidget(self.HomeButtons))

        button_action.triggered.connect(lambda: self.central_widget.setCurrentWidget(self.HomeButtons))
        button_action.triggered.connect(valChange)

    def execute_this_fn(self):
            print("Hello!")



# ---------------------------------------------------------------------- CHECKLIST -------------------------------------------------------------------------

class Checklist(QStackedWidget):

    clicked = pyqtSignal()

    def __init__(self, parent=None):
        super(Checklist, self).__init__(parent)
        layout = QVBoxLayout()
        listButtons = QWidget()
        buttonEmerg = QPushButton("EMERGENCY CHECKLIST")
        button2 = QPushButton("Mission Checklists")
        button3 = QPushButton("Pressure Lock Checklists")
        button4 = QPushButton("Comm Repair Checklists")
        layout.addWidget(buttonEmerg)
        layout.addWidget(button2)
        layout.addWidget(button3)
        layout.addWidget(button4)
        listButtons.setLayout(layout)


        checkLists = QButtonGroup()
        checkLists.addButton(button2, 0)
        checkLists.addButton(button3, 1)
        checkLists.addButton(button4, 2)

        def open_dialog_box(object):
            pathNames = ["./Checklists/MissionChecklist","./Checklists/PressureLockChecklist","./Checklists/CommChecklist"]
            dialog = QFileDialog()
            folderindex = checkLists.id(object)
            path = pathNames[folderindex]
            filename = QFileDialog.getOpenFileName(dialog, None ,path, None)
            path = filename[0]

            scroll = QScrollArea()
            scroll.setWidgetResizable(True)
            scroll.setGeometry(0,0,wid,hit) # CRITICAL

            inner = QFrame(scroll)
            inner.setLayout(QVBoxLayout())
            scroll.setWidget(inner) # CRITICAL

            with open(path, encoding="utf8", errors='ignore') as f:
                contents = f.read()     
            label = QLabel(contents)

            inner.layout().addWidget(label)
            self.addWidget(scroll)
            self.setCurrentWidget(scroll)


            
        button2.clicked.connect(lambda: open_dialog_box(button2))
        button3.clicked.connect(lambda: open_dialog_box(button3))
        button4.clicked.connect(lambda: open_dialog_box(button4))

        

        self.addWidget(listButtons)
        self.setCurrentWidget(listButtons)

    

# ---------------------------------------------------------------------- TELEMETRY -------------------------------------------------------------------------
    
class Tel(QWidget):

    clicked = pyqtSignal()

    def __init__(self, parent=None):
        super(Tel, self).__init__(parent)

        # creating progress bar
        self.pbar = QProgressBar(self)
        self.pbarenergy = QProgressBar(self)
  
        # setting its geometry
        self.pbar.setGeometry(100, 100, 200, 400)
        self.pbar.setStyleSheet("QProgressBar::chunk "
                          "{"
                          "background-color: green;"
                          "}")
        self.pbar.setOrientation(QtCore.Qt.Vertical)

        self.pbarenergy.setGeometry(400, 100, 200, 400)
        self.pbarenergy.setStyleSheet("QProgressBar::chunk "
                          "{"
                          "background-color: blue;"
                          "}")
        self.pbarenergy.setOrientation(QtCore.Qt.Vertical)
  
        # creating push button
        self.btn = QPushButton('Start', self)
  
        # changing its position
        self.btn.move(40, 40)
        self.pbar.setValue(100)
        self.pbarenergy.setValue(100)

        # adding action to push button
        self.btn.clicked.connect(self.doAction)

        # showing all the widgets
        self.show()

    def doAction(self):

        tankMax = 800 # liters
        avgRate = 50/60 # liters/minute
        OLevel = tankMax
        energyMax = 100
        energyrate = .2
        energy = energyMax
        
        while (OLevel > 0) | (energy>0):
            QtTest.QTest.qWait(10)
            OLevel = OLevel - avgRate
            percentage = int((OLevel/tankMax)*100)
            self.pbar.setValue(percentage)
            energy = energy - energyrate
            percent = int(energy)
            self.pbarenergy.setValue(percent)
        





# ---------------------------------------------------------------------- NAVIGATION -------------------------------------------------------------------------

class Navigate(QWidget):

    clicked = pyqtSignal()

    def __init__(self, parent=None):
        super(Navigate, self).__init__(parent)
        layout = QHBoxLayout()
        button = QPushButton("You are in Navigate Back Home!")
        layout.addWidget(button)
        self.setLayout(layout)
        button.clicked.connect(self.clicked.emit)


app = QApplication(sys.argv)
myWindow = MainWindow(None)
myWindow.show()
app.exec_()





