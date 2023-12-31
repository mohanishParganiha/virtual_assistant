# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'progressdialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import os 
import sys

class Ui_SplashWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        splash_img_path = "./resource/splashScreen1.png"
        MainWindow.setStyleSheet(
            "#frame{\n"
            f"background-image:url({splash_img_path});"
            "border-style:none;\n"
            "}\n"
            "#label{\n"
            "color: rgb(255, 255, 255);\n"
            "}\n"
            "#progressBar{\n"
            "background-color: qlineargradient(spread:pad, x1:0, y1:0.551045, x2:1, y2:0.568, stop:0 rgba(47, 183, 195, 255), stop:1 rgba(48, 77, 137, 255));\n"
            "border-style:none;\n"
            "border-radius:10px;\n"
            "}\n"
            "#progressBar::chunk{\n"
            "background-color: qlineargradient(spread:pad, x1:0, y1:0.551045, x2:1, y2:0.568, stop:0 rgba(50, 46, 122, 255), stop:1 rgba(46, 187, 197, 255));\n"
            "border-style:none;\n"
            "border-radius:10px;\n"
            "}"
            )
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.progressBar = QtWidgets.QProgressBar(self.frame)
        self.progressBar.setGeometry(QtCore.QRect(10, 550, 781, 20))
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.label = QtWidgets.QLabel(self.frame)
        # self.label.setText('Closing Please Wait')
        # self.label.setStyleSheet(
        #     'font-family:"Courier New";\n'
        #     'font-size:52px;'
        #     'font-weight:600;'
        #     )
        self.label.setGeometry(QtCore.QRect(10, 110, 781, 200))
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
        self.horizontalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.animateClosing()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        # self.label.setText(_translate("MainWindow", "Closing please wait a moment"))

    def animateClosing(self,duration = 4000):
        self.animation = QtCore.QPropertyAnimation(self.progressBar,b"value")
        self.animation.setDuration(duration)
        self.animation.setStartValue(0)
        self.animation.setEndValue(100)
        self.animation.start()
        self.animation.finished.emit()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_SplashWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
