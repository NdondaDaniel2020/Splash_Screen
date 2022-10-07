import sys
import platform
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect,
                          QSize, QTime, QUrl, Qt, QEvent, QEasingCurve)
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from Splah_Screen import Ui_SplashScreen
from window import Ui_MainWindow

## variaveis globais
contador = 0


# a aplicação
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    # main window label
        QtCore.QTimer.singleShot(1500, lambda: self.ui.label.setText("<strong>THANKS</strong> FOR WATCHING"))
        QtCore.QTimer.singleShot(1500, lambda: self.setStyleSheet("background-color: #222; color: #FFF"))
        # QtCore.QTimer.singleShot(1500, lambda: self.ResizeMainWindow())

        # self.ui.pushButton.clicked.connect(self.ResizeMainWindow)


    def ResizeMainWindow(self):
        # creat animation
        width = 200
        heigth = 300
        self.animation = QPropertyAnimation(self, b"size")
        self.animation.setDuration(1000)
        self.animation.setEndValue(QSize(width, heigth))
        self.animation.setEasingCurve(QEasingCurve.Linear)
        self.animation.start()

# a SPLASH SCREEN
class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        ## UI / CODIGO DA INTERFACE
        #########################################################

        ## REMOVER O TITOLO E O BAR
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        ## Largar a sombra do efeito
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.drop_shaow_frame.setGraphicsEffect(self.shadow)

        ## QTamer ==> start
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)

        # Tempo estara em milicegundos
        self.timer.start(15)

        ## funcao que executa a janela
        self.show()

    ## funcoes da app
    ############################################################
    def progress(self):
        global contador
        # entrada de valores dp progress Bar
        self.ui.progressBar.setValue(contador)

        # saida do Splash Screen e a abertura da app
        if contador > 100:
            # para o temporisador
            self.timer.stop()

            # e mostrar a janela maain
            self.main = MainWindow()
            self.main.show()

            # FECHAR A SESH CREEN
            self.close()
        # inserir valor no contador
        contador += 1


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()
    sys.exit(app.exec_())