# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\calc.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_calc(object):
    def setupUi(self, calc):
        calc.setObjectName("calc")
        calc.resize(547, 444)
        calc.setSizeGripEnabled(True)
        calc.setModal(True)
        self.value_0 = QtWidgets.QPushButton(calc)
        self.value_0.setGeometry(QtCore.QRect(10, 387, 111, 51))
        self.value_0.setAutoDefault(False)
        self.value_0.setObjectName("value_0")
        self.add = QtWidgets.QPushButton(calc)
        self.add.setGeometry(QtCore.QRect(380, 150, 161, 41))
        self.add.setAutoDefault(False)
        self.add.setObjectName("add")
        self.value_4 = QtWidgets.QPushButton(calc)
        self.value_4.setGeometry(QtCore.QRect(10, 230, 111, 71))
        self.value_4.setAutoDefault(False)
        self.value_4.setObjectName("value_4")
        self.sub = QtWidgets.QPushButton(calc)
        self.sub.setGeometry(QtCore.QRect(380, 200, 161, 41))
        self.sub.setAutoDefault(False)
        self.sub.setObjectName("sub")
        self.value_2 = QtWidgets.QPushButton(calc)
        self.value_2.setGeometry(QtCore.QRect(130, 150, 121, 71))
        self.value_2.setAutoDefault(False)
        self.value_2.setObjectName("value_2")
        self.value_3 = QtWidgets.QPushButton(calc)
        self.value_3.setGeometry(QtCore.QRect(260, 150, 111, 71))
        self.value_3.setAutoDefault(False)
        self.value_3.setObjectName("value_3")
        self.value_9 = QtWidgets.QPushButton(calc)
        self.value_9.setGeometry(QtCore.QRect(260, 310, 111, 71))
        self.value_9.setAutoDefault(False)
        self.value_9.setObjectName("value_9")
        self.value_1 = QtWidgets.QPushButton(calc)
        self.value_1.setGeometry(QtCore.QRect(10, 150, 111, 71))
        self.value_1.setAutoDefault(False)
        self.value_1.setObjectName("value_1")
        self.value_7 = QtWidgets.QPushButton(calc)
        self.value_7.setGeometry(QtCore.QRect(10, 310, 111, 71))
        self.value_7.setAutoDefault(False)
        self.value_7.setObjectName("value_7")
        self.div = QtWidgets.QPushButton(calc)
        self.div.setGeometry(QtCore.QRect(380, 300, 161, 41))
        self.div.setAutoDefault(False)
        self.div.setObjectName("div")
        self.value_6 = QtWidgets.QPushButton(calc)
        self.value_6.setGeometry(QtCore.QRect(260, 230, 111, 71))
        self.value_6.setAutoDefault(False)
        self.value_6.setObjectName("value_6")
        self.value_5 = QtWidgets.QPushButton(calc)
        self.value_5.setGeometry(QtCore.QRect(130, 230, 121, 71))
        self.value_5.setAutoDefault(False)
        self.value_5.setObjectName("value_5")
        self.mul = QtWidgets.QPushButton(calc)
        self.mul.setGeometry(QtCore.QRect(380, 250, 161, 41))
        self.mul.setAutoDefault(False)
        self.mul.setObjectName("mul")
        self.calc_display = QtWidgets.QLCDNumber(calc)
        self.calc_display.setGeometry(QtCore.QRect(11, 11, 531, 131))
        self.calc_display.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.calc_display.setSmallDecimalPoint(True)
        self.calc_display.setProperty("value", 0.0)
        self.calc_display.setObjectName("calc_display")
        self.value_8 = QtWidgets.QPushButton(calc)
        self.value_8.setGeometry(QtCore.QRect(130, 310, 121, 71))
        self.value_8.setAutoDefault(False)
        self.value_8.setObjectName("value_8")
        self.clear_p = QtWidgets.QPushButton(calc)
        self.clear_p.setGeometry(QtCore.QRect(260, 387, 111, 51))
        self.clear_p.setAutoDefault(False)
        self.clear_p.setObjectName("clear_p")
        self.equals = QtWidgets.QPushButton(calc)
        self.equals.setGeometry(QtCore.QRect(380, 350, 161, 41))
        self.equals.setAutoDefault(False)
        self.equals.setDefault(True)
        self.equals.setObjectName("equals")
        self.clear_a = QtWidgets.QPushButton(calc)
        self.clear_a.setGeometry(QtCore.QRect(380, 397, 161, 41))
        self.clear_a.setAutoDefault(False)
        self.clear_a.setObjectName("clear_a")
        self.decimal = QtWidgets.QPushButton(calc)
        self.decimal.setGeometry(QtCore.QRect(130, 387, 121, 51))
        self.decimal.setAutoDefault(False)
        self.decimal.setObjectName("decimal")

        self.retranslateUi(calc)
        QtCore.QMetaObject.connectSlotsByName(calc)
        calc.setTabOrder(self.value_1, self.value_2)
        calc.setTabOrder(self.value_2, self.value_3)
        calc.setTabOrder(self.value_3, self.value_4)
        calc.setTabOrder(self.value_4, self.value_5)
        calc.setTabOrder(self.value_5, self.value_6)
        calc.setTabOrder(self.value_6, self.value_7)
        calc.setTabOrder(self.value_7, self.value_8)
        calc.setTabOrder(self.value_8, self.value_9)
        calc.setTabOrder(self.value_9, self.value_0)
        calc.setTabOrder(self.value_0, self.equals)
        calc.setTabOrder(self.equals, self.add)
        calc.setTabOrder(self.add, self.sub)
        calc.setTabOrder(self.sub, self.mul)
        calc.setTabOrder(self.mul, self.div)

    def retranslateUi(self, calc):
        _translate = QtCore.QCoreApplication.translate
        calc.setWindowTitle(_translate("calc", "xCalc"))
        self.value_0.setText(_translate("calc", "0"))
        self.add.setText(_translate("calc", "+"))
        self.value_4.setText(_translate("calc", "4"))
        self.sub.setText(_translate("calc", "-"))
        self.value_2.setText(_translate("calc", "2"))
        self.value_3.setText(_translate("calc", "3"))
        self.value_9.setText(_translate("calc", "9"))
        self.value_1.setText(_translate("calc", "1"))
        self.value_7.setText(_translate("calc", "7"))
        self.div.setText(_translate("calc", "/"))
        self.value_6.setText(_translate("calc", "6"))
        self.value_5.setText(_translate("calc", "5"))
        self.mul.setText(_translate("calc", "*"))
        self.value_8.setText(_translate("calc", "8"))
        self.clear_p.setText(_translate("calc", "C"))
        self.equals.setText(_translate("calc", "="))
        self.clear_a.setText(_translate("calc", "AC"))
        self.decimal.setText(_translate("calc", "."))

