from PyQt5 import QtCore, QtGui, QtWidgets

import sys
import cv2
import numpy

from PIL import Image

from functools import partial

class Ui_MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        self.setupUi(self)


    #Repurpose QLabel (eyllanesc)

    class ClickLabel(QtWidgets.QLabel):
        clicked = QtCore.pyqtSignal()

        def mousePressEvent(self, event):
            self.clicked.emit()
            QtWidgets.QLabel.mousePressEvent(self, event)

    #QtDesigner Output
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(628, 321)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Builder_Group = QtWidgets.QGroupBox(self.centralwidget)
        self.Builder_Group.setGeometry(QtCore.QRect(320, 10, 301, 101))
        self.Builder_Group.setAutoFillBackground(True)
        self.Builder_Group.setObjectName("Builder_Group")
        self.Builder_Label = QtWidgets.QLabel(self.Builder_Group)
        self.Builder_Label.setGeometry(QtCore.QRect(20, 20, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Builder_Label.setFont(font)
        self.Builder_Label.setObjectName("Builder_Label")
        self.Builder_Line = QtWidgets.QLineEdit(self.Builder_Group)
        self.Builder_Line.setGeometry(QtCore.QRect(170, 21, 21, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Builder_Line.setFont(font)
        self.Builder_Line.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.Builder_Line.setObjectName("Builder_Line")
        self.Builder_1 = Ui_MainWindow.ClickLabel(self.Builder_Group)
        self.Builder_1.setGeometry(QtCore.QRect(20, 60, 25, 25))
        self.Builder_1.setStyleSheet("Background: rgb(255, 0, 0)\n"
                                     "")
        self.Builder_1.setAlignment(QtCore.Qt.AlignCenter)
        self.Builder_1.setObjectName("Builder_1")
        self.Builder_2 = Ui_MainWindow.ClickLabel(self.Builder_Group)
        self.Builder_2.setGeometry(QtCore.QRect(50, 60, 25, 25))
        self.Builder_2.setStyleSheet("Background: rgb(0, 0, 255)\n"
                                     "")
        self.Builder_2.setAlignment(QtCore.Qt.AlignCenter)
        self.Builder_2.setObjectName("Builder_2")
        self.Builder_3 = Ui_MainWindow.ClickLabel(self.Builder_Group)
        self.Builder_3.setGeometry(QtCore.QRect(80, 60, 25, 25))
        self.Builder_3.setStyleSheet("Background: rgb(255, 255, 0)\n"
                                     "")
        self.Builder_3.setAlignment(QtCore.Qt.AlignCenter)
        self.Builder_3.setObjectName("Builder_3")
        self.Builder_4 = Ui_MainWindow.ClickLabel(self.Builder_Group)
        self.Builder_4.setGeometry(QtCore.QRect(110, 60, 25, 25))
        self.Builder_4.setStyleSheet("Background: rgb(0, 255, 0)\n"
                                     "")
        self.Builder_4.setAlignment(QtCore.Qt.AlignCenter)
        self.Builder_4.setObjectName("Builder_4")
        self.Builder_5 = Ui_MainWindow.ClickLabel(self.Builder_Group)
        self.Builder_5.setGeometry(QtCore.QRect(140, 60, 25, 25))
        self.Builder_5.setStyleSheet("Background: rgb(170, 0, 255)\n"
                                     "")
        self.Builder_5.setAlignment(QtCore.Qt.AlignCenter)
        self.Builder_5.setObjectName("Builder_5")
        self.Builder_6 = Ui_MainWindow.ClickLabel(self.Builder_Group)
        self.Builder_6.setGeometry(QtCore.QRect(170, 60, 25, 25))
        self.Builder_6.setStyleSheet("Background: rgb(255, 85, 0)\n"
                                     "")
        self.Builder_6.setAlignment(QtCore.Qt.AlignCenter)
        self.Builder_6.setObjectName("Builder_6")
        self.Builder_7 = Ui_MainWindow.ClickLabel(self.Builder_Group)
        self.Builder_7.setGeometry(QtCore.QRect(200, 60, 25, 25))
        self.Builder_7.setStyleSheet("Background: rgb(255, 85, 127)\n"
                                     "")
        self.Builder_7.setAlignment(QtCore.Qt.AlignCenter)
        self.Builder_7.setObjectName("Builder_7")
        self.Builder_8 = Ui_MainWindow.ClickLabel(self.Builder_Group)
        self.Builder_8.setGeometry(QtCore.QRect(230, 60, 25, 25))
        self.Builder_8.setStyleSheet("Background: rgb(170, 170, 127)\n"
                                     "")
        self.Builder_8.setAlignment(QtCore.Qt.AlignCenter)
        self.Builder_8.setObjectName("Builder_8")
        self.Builder_9 = Ui_MainWindow.ClickLabel(self.Builder_Group)
        self.Builder_9.setGeometry(QtCore.QRect(260, 60, 25, 25))
        self.Builder_9.setStyleSheet("Background: rgb(255, 255, 255)\n"
                                     "")
        self.Builder_9.setAlignment(QtCore.Qt.AlignCenter)
        self.Builder_9.setObjectName("Builder_9")
        self.Main_Label = QtWidgets.QLabel(self.centralwidget)
        self.Main_Label.setGeometry(QtCore.QRect(10, 10, 300, 300))
        self.Main_Label.setText("")
        self.Main_Label.setPixmap(QtGui.QPixmap("/Blank.bmp"))
        self.Main_Label.setObjectName("Main_Label")
        self.Nav_Group = QtWidgets.QGroupBox(self.centralwidget)
        self.Nav_Group.setGeometry(QtCore.QRect(320, 120, 301, 121))
        self.Nav_Group.setObjectName("Nav_Group")
        self.Nav_Centre = QtWidgets.QPushButton(self.Nav_Group)
        self.Nav_Centre.setGeometry(QtCore.QRect(70, 56, 25, 25))
        self.Nav_Centre.setObjectName("Nav_Centre")
        self.Nav_Up = QtWidgets.QPushButton(self.Nav_Group)
        self.Nav_Up.setGeometry(QtCore.QRect(70, 26, 25, 25))
        self.Nav_Up.setObjectName("Nav_Up")
        self.Nav_Right = QtWidgets.QPushButton(self.Nav_Group)
        self.Nav_Right.setGeometry(QtCore.QRect(100, 56, 25, 25))
        self.Nav_Right.setObjectName("Nav_Right")
        self.Nav_Left = QtWidgets.QPushButton(self.Nav_Group)
        self.Nav_Left.setGeometry(QtCore.QRect(40, 56, 25, 25))
        self.Nav_Left.setObjectName("Nav_Left")
        self.Nav_Down = QtWidgets.QPushButton(self.Nav_Group)
        self.Nav_Down.setGeometry(QtCore.QRect(70, 86, 25, 25))
        self.Nav_Down.setObjectName("Nav_Down")
        self.Nav_X_Line = QtWidgets.QLineEdit(self.Nav_Group)
        self.Nav_X_Line.setGeometry(QtCore.QRect(178, 36, 31, 20))
        self.Nav_X_Line.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.Nav_X_Line.setObjectName("Nav_X_Line")
        self.Nav_Y_Line = QtWidgets.QLineEdit(self.Nav_Group)
        self.Nav_Y_Line.setGeometry(QtCore.QRect(218, 36, 31, 20))
        self.Nav_Y_Line.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.Nav_Y_Line.setObjectName("Nav_Y_Line")
        self.Nav_X_Lab = QtWidgets.QLabel(self.Nav_Group)
        self.Nav_X_Lab.setGeometry(QtCore.QRect(190, 56, 16, 16))
        self.Nav_X_Lab.setObjectName("Nav_X_Lab")
        self.Nav_Y_Lab = QtWidgets.QLabel(self.Nav_Group)
        self.Nav_Y_Lab.setGeometry(QtCore.QRect(230, 56, 16, 16))
        self.Nav_Y_Lab.setObjectName("Nav_Y_Lab")
        self.Nav_Select = QtWidgets.QPushButton(self.Nav_Group)
        self.Nav_Select.setGeometry(QtCore.QRect(176, 76, 76, 23))
        self.Nav_Select.setObjectName("Nav_Select")
        self.Control_Group = QtWidgets.QGroupBox(self.centralwidget)
        self.Control_Group.setGeometry(QtCore.QRect(320, 250, 301, 60))
        self.Control_Group.setObjectName("Control_Group")
        self.Control_Begin = QtWidgets.QPushButton(self.Control_Group)
        self.Control_Begin.setGeometry(QtCore.QRect(10, 20, 131, 31))
        self.Control_Begin.setObjectName("Control_Begin")
        self.Control_Clear = QtWidgets.QPushButton(self.Control_Group)
        self.Control_Clear.setGeometry(QtCore.QRect(160, 20, 131, 31))
        self.Control_Clear.setObjectName("Control_Clear")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #Connections
        self.Nav_Up.clicked.connect(self.MoveUp)
        self.Nav_Down.clicked.connect(self.MoveDown)
        self.Nav_Left.clicked.connect(self.MoveLeft)
        self.Nav_Right.clicked.connect(self.MoveRight)
        self.Nav_Centre.clicked.connect(self.MoveCentre)
        self.Nav_Select.clicked.connect(self.MoveSelect)
        self.Builder_1.clicked.connect(partial(self.ChangeColour, self.Builder_1))
        self.Builder_2.clicked.connect(partial(self.ChangeColour, self.Builder_2))
        self.Builder_3.clicked.connect(partial(self.ChangeColour, self.Builder_3))
        self.Builder_4.clicked.connect(partial(self.ChangeColour, self.Builder_4))
        self.Builder_5.clicked.connect(partial(self.ChangeColour, self.Builder_5))
        self.Builder_6.clicked.connect(partial(self.ChangeColour, self.Builder_6))
        self.Builder_7.clicked.connect(partial(self.ChangeColour, self.Builder_7))
        self.Builder_8.clicked.connect(partial(self.ChangeColour, self.Builder_8))
        self.Builder_9.clicked.connect(partial(self.ChangeColour, self.Builder_9))

    def ReadMatrix(self):
        global m
        global CoreMat

        for x in range(100):
            for y in range(100):
                for x2 in range((x*3)+1-1,(x*3)+1+2):
                    for y2 in range((y*3)+1-1,(y*3)+1+2):
                        m[x2][y2] = CoreMat[x][y]

    def MoveUp(self):
        self.Nav_X_Line.setText(str(int(self.Nav_X_Line.text())+1))
        x = int(self.Nav_X_Line.text())*3+1
        y = int(self.Nav_Y_Line.text())*3+1
        self.DrawCursor(x,y)

    def MoveDown(self):
        self.Nav_X_Line.setText(str(int(self.Nav_X_Line.text())-1))
        x = int(self.Nav_X_Line.text())*3+1
        y = int(self.Nav_Y_Line.text())*3+1
        self.DrawCursor(x,y)

    def MoveLeft(self):
        self.Nav_Y_Line.setText(str(int(self.Nav_Y_Line.text())-1))
        x = int(self.Nav_X_Line.text())*3+1
        y = int(self.Nav_Y_Line.text())*3+1
        self.DrawCursor(x,y)

    def MoveRight(self):
        self.Nav_Y_Line.setText(str(int(self.Nav_Y_Line.text())+1))
        x = int(self.Nav_X_Line.text())*3+1
        y = int(self.Nav_Y_Line.text())*3+1
        self.DrawCursor(x,y)

    def MoveCentre(self):
        self.Nav_Y_Line.setText(str(50))
        self.Nav_X_Line.setText(str(50))
        self.DrawCursor(151,151)

    def MoveSelect(self):
        x = int(self.Nav_X_Line.text())*3+1
        y = int(self.Nav_Y_Line.text())*3+1
        self.DrawCursor(x,y)

    def DrawCursor(self,x,y):

        self.ReadMatrix()

        for x2 in range(x-2,x+3):
            for y2 in range(y-2,y+3):
                if not ((x2 == x-1 or x2 == x or x2 == x+1) and (y2 == y-1 or y2 == y or y2 == y+1)):
                    m[x2][y2][0] = 100
                    m[x2][y2][1] = 100
                    m[x2][y2][2] = 100


        cv2.waitKey(10)

        im = Image.fromarray(m)
        im.save("Blank2.bmp")

        self.Main_Label.setPixmap(QtGui.QPixmap("./Blank2.bmp"))

    def ChangeColour(self, sourcelabel):
        print(sourcelabel.text())

        color = QtWidgets.QColorDialog.getColor()
        print(color.name())
        sourcelabel.setStyleSheet("Background: "+color.name()+"\n")

        print(CurrColour)

    #Also QtDesigner Output
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Builder_Group.setTitle(_translate("MainWindow", "Sandpile Builder"))
        self.Builder_Label.setText(_translate("MainWindow", "Sandpile Limit (3-9)"))
        self.Builder_Line.setText(_translate("MainWindow", "4"))
        self.Builder_1.setText(_translate("MainWindow", "1"))
        self.Builder_2.setText(_translate("MainWindow", "2"))
        self.Builder_3.setText(_translate("MainWindow", "3"))
        self.Builder_4.setText(_translate("MainWindow", "4"))
        self.Builder_5.setText(_translate("MainWindow", "5"))
        self.Builder_6.setText(_translate("MainWindow", "6"))
        self.Builder_7.setText(_translate("MainWindow", "7"))
        self.Builder_8.setText(_translate("MainWindow", "8"))
        self.Builder_9.setText(_translate("MainWindow", "9"))
        self.Nav_Group.setTitle(_translate("MainWindow", "Navigation"))
        self.Nav_Centre.setText(_translate("MainWindow", "C"))
        self.Nav_Up.setText(_translate("MainWindow", "U"))
        self.Nav_Right.setText(_translate("MainWindow", "R"))
        self.Nav_Left.setText(_translate("MainWindow", "L"))
        self.Nav_Down.setText(_translate("MainWindow", "D"))
        self.Nav_X_Line.setText(_translate("MainWindow", "50"))
        self.Nav_Y_Line.setText(_translate("MainWindow", "50"))
        self.Nav_X_Lab.setText(_translate("MainWindow", "X"))
        self.Nav_Y_Lab.setText(_translate("MainWindow", "Y"))
        self.Nav_Select.setText(_translate("MainWindow", "Select"))
        self.Control_Group.setTitle(_translate("MainWindow", "Controls"))
        self.Control_Begin.setText(_translate("MainWindow", "Begin!"))
        self.Control_Clear.setText(_translate("MainWindow", "Clear"))
        self.show()

        #Initial Globals
        global CurrColour
        global m
        global CoreMat
        CurrColour = 1

        #Core 100x100 Matrix
        CoreMat = [[(0,0,0)]*100 for i in range(100)]

        #Functional Code
        m = cv2.imread("Blank.bmp")

        self.ReadMatrix()
        im = Image.fromarray(m)
        im.save("Blank2.bmp")

        self.Main_Label.setPixmap(QtGui.QPixmap("./Blank2.bmp"))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    start = Ui_MainWindow()

    sys.exit(app.exec_())
