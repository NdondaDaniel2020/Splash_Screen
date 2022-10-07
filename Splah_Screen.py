from PySide6 import QtCore, QtGui, QtWidgets
import sys

class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        SplashScreen.setObjectName("SplashScreen3")
        SplashScreen.resize(594, 309)
        SplashScreen.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        SplashScreen.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.centralwidget = QtWidgets.QWidget(SplashScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.drop_shaow_frame = QtWidgets.QFrame(self.centralwidget)
        self.drop_shaow_frame.setStyleSheet("QFrame{\n"
"background-color: rgb(56, 58, 89);\n"
"color:rgb(220, 220, 220);\n"
"border-radius:10px;\n"
"}")
        self.drop_shaow_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.drop_shaow_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.drop_shaow_frame.setObjectName("drop_shaow_frame")
        self.label_Title = QtWidgets.QLabel(self.drop_shaow_frame)
        self.label_Title.setGeometry(QtCore.QRect(0, 60, 581, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(40)
        self.label_Title.setFont(font)
        self.label_Title.setStyleSheet("color: rgb(254, 121, 199);")
        self.label_Title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Title.setObjectName("label_Title")
        self.label_Description = QtWidgets.QLabel(self.drop_shaow_frame)
        self.label_Description.setGeometry(QtCore.QRect(0, 120, 581, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.label_Description.setFont(font)
        self.label_Description.setStyleSheet("color: rgb(98, 114, 164);")
        self.label_Description.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Description.setObjectName("label_Description")
        self.progressBar = QtWidgets.QProgressBar(self.drop_shaow_frame)
        self.progressBar.setGeometry(QtCore.QRect(50, 200, 481, 23))
        self.progressBar.setStyleSheet("QProgressBar {\n"
"    background-color: rgb(98, 114, 164);\n"
"    color: rgb(200, 200, 200);\n"
"    border-style:none;\n"
"    border-radius:10px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"border-radius:10px;\n"
"background-color: qlineargradient(spread:pad, x1:0.00568182, y1:0.478, x2:1, y2:0.483, stop:0 rgba(254, 121, 199, 255), stop:1 rgba(170, 85, 255, 255));\n"
"}")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.label_londing = QtWidgets.QLabel(self.drop_shaow_frame)
        self.label_londing.setGeometry(QtCore.QRect(0, 230, 581, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.label_londing.setFont(font)
        self.label_londing.setStyleSheet("color: rgb(98, 114, 164);")
        self.label_londing.setAlignment(QtCore.Qt.AlignCenter)
        self.label_londing.setObjectName("label_londing")
        self.label_creats = QtWidgets.QLabel(self.drop_shaow_frame)
        self.label_creats.setGeometry(QtCore.QRect(390, 260, 181, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.label_creats.setFont(font)
        self.label_creats.setStyleSheet("color: rgb(98, 114, 164);")
        self.label_creats.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_creats.setObjectName("label_creats")
        self.verticalLayout.addWidget(self.drop_shaow_frame)
        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)
        QtCore.QMetaObject.connectSlotsByName(SplashScreen)

    def retranslateUi(self, SplashScreen):
        _translate = QtCore.QCoreApplication.translate
        SplashScreen.setWindowTitle(_translate("SplashScreen3", "MainWindow"))
        self.label_Title.setText(_translate("SplashScreen3", "<strong>YOUR</strong> APP NAME"))
        self.label_Description.setText(_translate("SplashScreen3", "<strong>APP</strong> DESCRIPTION"))
        self.label_londing.setText(_translate("SplashScreen3", "loanding..."))
        self.label_creats.setText(_translate("SplashScreen3", "<Strong>Created</Strong>: Ndonda D.  Matondo"))


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    SplashScreen = QtWidgets.QMainWindow()
    ui = Ui_SplashScreen()
    ui.setupUi(SplashScreen)
    SplashScreen.show()
    sys.exit(app.exec_())
