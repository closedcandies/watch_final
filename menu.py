from PyQt5 import QtWidgets, uic
import sys
import main_game
from PyQt5 import QtCore, QtGui, QtWidgets
from random import choice, randint
from second_game import *
from design import *


class Game_1(object):
    def setupUi(self, window):
        #window = QtWidgets.QMainWindow()
        win = main_game.Ui_MainWindow(window)
        score = 0

        win.setupUi()

        window.show()


class Game_2(object):
    def setupUi(self, menu):
        window = ExampleApp(menu)  # Создаём объект класса ExampleApp
        window.setupUi(menu)
        window.setup_button()
        #window.generator()
        menu.show()


class Ui_menu(object):
    def setupUi(self, menu):
        menu.setObjectName("menu")
        menu.resize(200, 400)
        self.label = QtWidgets.QLabel(menu)
        self.label.setGeometry(QtCore.QRect(60, 10, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QtWidgets.QWidget(menu)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 100, 161, 161))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.varmenu_1 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.varmenu_1.setFont(font)
        self.varmenu_1.setObjectName("varmenu_1")
        self.verticalLayout.addWidget(self.varmenu_1)
        self.varmenu_1.clicked.connect(self.show_window_1)
        self.varmenu_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.varmenu_2.setFont(font)
        self.varmenu_2.setObjectName("varmenu_2")
        self.verticalLayout.addWidget(self.varmenu_2)
        self.varmenu_2.clicked.connect(self.show_window_2)

        self.retranslateUi(menu)
        QtCore.QMetaObject.connectSlotsByName(menu)

    def retranslateUi(self, menu):
        _translate = QtCore.QCoreApplication.translate
        menu.setWindowTitle(_translate("menu", "Form"))
        self.label.setText(_translate("menu", "Меню"))
        self.varmenu_1.setText(_translate("menu", "Игрушка1"))
        self.varmenu_2.setText(_translate("menu", "Игрушка2"))

    def show_window_1(self):
        self.w1 = Game_1()
        win1 = QtWidgets.QMainWindow()
        self.w1.setupUi(win1)
        win1.show()

    def show_window_2(self):
        self.ui2 = ExampleApp()
        self.ui2.generator()
        self.ui2.show()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Ui_menu()
    win = QtWidgets.QMainWindow()
    ex.setupUi(win)
    win.show()
    sys.exit(app.exec_())
