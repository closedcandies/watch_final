import sys  # sys нужен для передачи argv в QApplication
import time
from random import randint

from PyQt5 import QtWidgets
from PyQt5.QtGui import QTransform, QPixmap
from PyQt5 import QtCore

import design  # Это наш конвертированный файл дизайна

''''''
class ExampleApp(QtWidgets.QMainWindow, design.Ui_Form):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py

        super().__init__()
        self.j = None
        self.i = None
        self.flag = 0
        self.score = 0
        self.setupUi(self)  # Это нужно для инициализации нашего дизайнаUi_menu
        self.pushButton.clicked.connect(self.check)

    def check(self):

        tx = str(self.timeEdit.text())
        kp = list(map(int, tx.split(':')))
        if self.flag:
            if kp[0] == self.j and kp[1] == 58 - self.i:
                self.score += 1
                self.label3.setStyleSheet('color: rgb(0, 255, 0);')
                self.label3.setText("Верно")
            else:
                self.score -= 1
                if self.score < 0:
                    self.score = 0
                self.label3.setStyleSheet('color: rgb(255, 0, 0);')
                self.label3.setText("Неверно")
                if 58 - self.i <= 8 and self.j <= 7:
                    self.label4.setText("Правильный ответ: 0" + str(self.j) + ':0' + str(58 - self.i))
                elif 58 - self.i <= 8:
                    self.label4.setText("Правильный ответ: " + str(self.j) + ':0' + str(58 - self.i))
                elif self.j <= 7:
                    self.label4.setText("Правильный ответ: 0" + str(self.j) + ':' + str(58 - self.i))
                else:
                    self.label4.setText("Правильный ответ: " + str(self.j) + ':' + str(58 - self.i))
        else:
            if kp[1] == self.i + 1 and kp[0] == self.j:
                self.score += 1
                self.label3.setStyleSheet('color: rgb(0, 255, 0);')
                self.label3.setText("Верно")
            else:
                self.score -= 1
                if self.score < 0:
                    self.score = 0
                self.label3.setStyleSheet('color: rgb(255, 0, 0);')
                self.label3.setText("Неверно")
                if self.i <= 8 and self.j <= 7:
                    self.label4.setText("Правильный ответ: 0" + str(self.j) + ':0' + str(self.i + 1))
                elif self.i <= 8:
                    self.label4.setText("Правильный ответ: " + str(self.j) + ':0' + str(self.i + 1))
                elif self.j <= 7:
                    self.label4.setText("Правильный ответ: 0" + str(self.j) + ':' + str(self.i + 1))
                else:
                    self.label4.setText("Правильный ответ: " + str(self.j) + ':' + str(self.i + 1))
        self.label2.setText('Очки: ' + str(self.score))

        QtCore.QTimer.singleShot(3000, self.generator)
        #self.generator()

    def generator(self):
        self.label4.setText("")
        self.label3.setText("")
        self.flag = randint(0, 1)
        if self.flag:
            self.i = randint(0, len(spbes1) - 1)
            self.j = randint(0, len(spbes2) - 1)
            self.label.setText('Без ' + spbes1[self.i] + ' минут ' + spbes2[self.j])
        else:
            self.i = randint(0, len(spbes1) - 1)
            self.j = randint(0, len(spbes3) - 1)
            st = spbes2[self.i].capitalize()
            if self.i <= 3:
                if self.i == 0:
                    st = 'Одна'
                if self.i == 1:
                    st = 'Две'
                self.label.setText(spbes2[self.i].capitalize() + ' минуты ' + spbes1[self.j])
            else:

                self.label.setText(st + ' минут ' + spbes3[self.j])


def main():
    #app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.generator()
    window.show()  # Показываем окно
    #app.exec_()  # и запускаем приложение


spbes1 = ['двух', 'трех', 'четырёх', 'пяти', 'шести', 'семи', 'восьми', 'девяти', 'десяти', 'одиннадцати',
          'двеннадцати', 'тринадцати', 'четырндацати', 'пятнадцати', 'шестнадцати', 'восемьнадцати', 'девятнадцати',
          'двадцати']
spbes2 = ['один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять', 'одиннадцать',
          'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать', 'восемьнадцать']
spbes3 = ['первого', 'второго', 'третьего', 'четвёртого', 'пятого', 'шестого', 'седьмого', 'восьмого', 'девятого',
          'десятого', 'одиннадцатого']
if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем

    main()  # то запускаем функцию main()
