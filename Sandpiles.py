from PyQt5 import QtCore, QtGui, QtWidgets

import sys
import cv2
import numpy

from PIL import Image

class Ui_MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        self.setupUi(self)

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
        self.Builder_1 = QtWidgets.QLabel(self.Builder_Group)
        self.Builder_1.setGeometry(QtCore.QRect(20, 60, 25, 25))
        self.Builder_1.setStyleSheet("Background: rgb(255, 0, 0)\n"
                                     "")
        self.Builder_1.setAlignment(QtCore.Qt.AlignCenter)
        self.Builder_1.setObjectName("Builder_1")
        self.Builder_2 = QtWidgets.QLabel(self.Builder_Group)
        self.Builder_2.setGeometry(QtCore.QRect(50, 60, 25, 25))
        self.Builder_2.setStyleSheet("Background: rgb(0, 0, 255)\n"
                                     "")
        self.Builder_2.setAlignment(QtCore.Qt.AlignCenter)
        self.Builder_2.setObjectName("Builder_2")
        self.Builder_3 = QtWidgets.QLabel(self.Builder_Group)
        self.Builder_3.setGeometry(QtCore.QRect(80, 60, 25, 25))
        self.Builder_3.setStyleSheet("Background: rgb(255, 255, 0)\n"
                                     "")
        self.Builder_3.setAlignment(QtCore.Qt.AlignCenter)
        self.Builder_3.setObjectName("Builder_3")
        self.Builder_4 = QtWidgets.QLabel(self.Builder_Group)
        self.Builder_4.setGeometry(QtCore.QRect(110, 60, 25, 25))
        self.Builder_4.setStyleSheet("Background: rgb(0, 255, 0)\n"
                                     "")
        self.Builder_4.setAlignment(QtCore.Qt.AlignCenter)
        self.Builder_4.setObjectName("Builder_4")
        self.Builder_5 = QtWidgets.QLabel(self.Builder_Group)
        self.Builder_5.setGeometry(QtCore.QRect(140, 60, 25, 25))
        self.Builder_5.setStyleSheet("Background: rgb(170, 0, 255)\n"
                                     "")
        self.Builder_5.setAlignment(QtCore.Qt.AlignCenter)
        self.Builder_5.setObjectName("Builder_5")
        self.Builder_6 = QtWidgets.QLabel(self.Builder_Group)
        self.Builder_6.setGeometry(QtCore.QRect(170, 60, 25, 25))
        self.Builder_6.setStyleSheet("Background: rgb(255, 85, 0)\n"
                                     "")
        self.Builder_6.setAlignment(QtCore.Qt.AlignCenter)
        self.Builder_6.setObjectName("Builder_6")
        self.Builder_7 = QtWidgets.QLabel(self.Builder_Group)
        self.Builder_7.setGeometry(QtCore.QRect(200, 60, 25, 25))
        self.Builder_7.setStyleSheet("Background: rgb(255, 85, 127)\n"
                                     "")
        self.Builder_7.setAlignment(QtCore.Qt.AlignCenter)
        self.Builder_7.setObjectName("Builder_7")
        self.Builder_8 = QtWidgets.QLabel(self.Builder_Group)
        self.Builder_8.setGeometry(QtCore.QRect(230, 60, 25, 25))
        self.Builder_8.setStyleSheet("Background: rgb(170, 170, 127)\n"
                                     "")
        self.Builder_8.setAlignment(QtCore.Qt.AlignCenter)
        self.Builder_8.setObjectName("Builder_8")
        self.Builder_9 = QtWidgets.QLabel(self.Builder_Group)
        self.Builder_9.setGeometry(QtCore.QRect(260, 60, 25, 25))
        self.Builder_9.setStyleSheet("Background: rgb(255, 255, 255)\n"
                                     "")
        self.Builder_9.setAlignment(QtCore.Qt.AlignCenter)
        self.Builder_9.setObjectName("Builder_9")
        self.Main_Label = QtWidgets.QLabel(self.centralwidget)
        self.Main_Label.setGeometry(QtCore.QRect(10, 10, 299, 299))
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
        self.Left_Right = QtWidgets.QPushButton(self.Nav_Group)
        self.Left_Right.setGeometry(QtCore.QRect(100, 56, 25, 25))
        self.Left_Right.setObjectName("Left_Right")
        self.Nav_Left = QtWidgets.QPushButton(self.Nav_Group)
        self.Nav_Left.setGeometry(QtCore.QRect(40, 56, 25, 25))
        self.Nav_Left.setObjectName("Nav_Left")
        self.Left_Down = QtWidgets.QPushButton(self.Nav_Group)
        self.Left_Down.setGeometry(QtCore.QRect(70, 86, 25, 25))
        self.Left_Down.setObjectName("Left_Down")
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


        #Functional Code
        m = cv2.imread("Blank.bmp")
        h, w, bpp = numpy.shape(m)

        print("yo")
        print("width", str(w))
        print("height", str(h))
        print("bpp", str(bpp))

        print(m[1][1])

        m[20][20][0] = 100
        m[20][20][1] = 100
        m[20][20][2] = 100

        cv2.waitKey(0)

        im = Image.fromarray(m)
        im.save("Blank2.bmp")

        self.Main_Label.setPixmap(QtGui.QPixmap("./Blank2.bmp"))

    #Also QtDesigner Output
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Builder_Group.setTitle(_translate("MainWindow", "Sandpile Builder"))
        self.Builder_Label.setText(_translate("MainWindow", "Sandpile Limit (1-9)"))
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
        self.Left_Right.setText(_translate("MainWindow", "R"))
        self.Nav_Left.setText(_translate("MainWindow", "L"))
        self.Left_Down.setText(_translate("MainWindow", "D"))
        self.Nav_X_Line.setText(_translate("MainWindow", "50"))
        self.Nav_Y_Line.setText(_translate("MainWindow", "50"))
        self.Nav_X_Lab.setText(_translate("MainWindow", "X"))
        self.Nav_Y_Lab.setText(_translate("MainWindow", "Y"))
        self.Nav_Select.setText(_translate("MainWindow", "Select"))
        self.Control_Group.setTitle(_translate("MainWindow", "Controls"))
        self.Control_Begin.setText(_translate("MainWindow", "Begin!"))
        self.Control_Clear.setText(_translate("MainWindow", "Clear"))
        self.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    start = Ui_MainWindow()

    sys.exit(app.exec_())
