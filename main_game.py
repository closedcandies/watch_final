import time

from PyQt5 import QtCore, QtGui, QtWidgets
from random import choice, randint

IMAGES_AND_ANSWERS = {'patterns/9:00.jpg': '9:00', 'patterns/9:20.jpg': '9:20',
                      'patterns/11:10.jpg': '11:10', 'patterns/12:00.jpg': '12:00',
                      'patterns/13:00.jpg': '13:00', 'patterns/14:00.jpg': '14:00',
                      'patterns/15:00.jpg': '15:00', 'patterns/15:30.jpg': '15:30',
                      'patterns/15:35.jpg': '15:35', 'patterns/18:00.jpg': '18:00'}
ANSWERS = ['18:05', '14:10', '15:15', '11:25', '06:30', '9:40']

STRIKE = 10

class Ui_MainWindow(object):
    def __init__(self, mainWindow):
        self.result = 0
        self.MainWindow = mainWindow

    def setupUi(self):
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(650, 750)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MainWindow.sizePolicy().hasHeightForWidth())
        self.MainWindow.setSizePolicy(sizePolicy)
        self.MainWindow.setMinimumSize(QtCore.QSize(650, 750))
        self.MainWindow.setMaximumSize(QtCore.QSize(650, 750))
        self.centralwidget = QtWidgets.QWidget(self.MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(110, 480, 421, 181))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(1)
        self.gridLayout.setObjectName("gridLayout")
        self.var3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.var3.setFont(font)
        self.var3.setObjectName("var3")
        self.gridLayout.addWidget(self.var3, 2, 0, 1, 1)
        self.var2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.var2.setFont(font)
        self.var2.setObjectName("var2")
        self.gridLayout.addWidget(self.var2, 1, 0, 1, 1)
        self.var4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.var4.setFont(font)
        self.var4.setObjectName("var4")
        self.gridLayout.addWidget(self.var4, 3, 0, 1, 1)
        self.var1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.var1.setFont(font)
        self.var1.setObjectName("var1")
        self.gridLayout.addWidget(self.var1, 0, 0, 1, 1)
        self.ciferblat = QtWidgets.QLabel(self.centralwidget)
        self.ciferblat.setGeometry(QtCore.QRect(220, 160, 200, 200))
        self.ciferblat.setObjectName("ciferblat")
        self.MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self.MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.MainWindow.setStatusBar(self.statusbar)

        '''while self.score < 10:
            self.retranslateUi(MainWindow)
            self.score += self.result
            self.result = 0'''
        self.retranslateUi(self.MainWindow)

        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)

    def retranslateUi(self, MainWindow):
        '''_translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Игра"))
        self.var3.setText(_translate("MainWindow", "PushButton"))
        self.var2.setText(_translate("MainWindow", "PushButton"))
        self.var4.setText(_translate("MainWindow", "PushButton"))
        self.var1.setText(_translate("MainWindow", "PushButton"))
        self.ciferblat.setText(_translate("MainWindow", "TextLabel"))'''

        buttons = [self.var1, self.var2, self.var3, self.var4]

        image = choice(list(IMAGES_AND_ANSWERS.keys()))
        right_answer = IMAGES_AND_ANSWERS[image]
        self.right_button = choice(buttons)
        self.right_button.setText(right_answer)

        self.ciferblat.setPixmap(QtGui.QPixmap(image))

        wrong_answers = ANSWERS.copy()

        for button in buttons:
            if button != self.right_button:
                button.setText(wrong_answers.pop(randint(0, len(wrong_answers) - 1)))
        self.var1.clicked.connect(lambda x: self.check_answer(self.var1))
        self.var2.clicked.connect(lambda x: self.check_answer(self.var2))
        self.var3.clicked.connect(lambda x: self.check_answer(self.var3))
        self.var4.clicked.connect(lambda x: self.check_answer(self.var4))

    def check_answer(self, button):
        print('in check_answer')
        flag = 0
        if button == self.right_button:
            #   TODO: add music
            button.setStyleSheet("background-color : green")
            flag = 1
        else:
            button.setStyleSheet("background-color : red")
        self.result += flag
        self.MainWindow.repaint()
        self.MainWindow.show()
        if self.result < STRIKE:
            QtCore.QTimer.singleShot(500, self.setupUi)
        else:
            QtCore.QTimer.singleShot(500, self.MainWindow.hide)

