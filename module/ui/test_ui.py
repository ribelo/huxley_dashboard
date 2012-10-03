# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created: Mon Sep  3 21:29:51 2012
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(591, 438)
        self.tableWidget = QtGui.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(40, 80, 511, 231))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(4)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(1, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(2, 2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(3, 3, item)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(QtGui.QApplication.translate("Form", "Nowy wiersz", None, QtGui.QApplication.UnicodeUTF8))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(QtGui.QApplication.translate("Form", "1", None, QtGui.QApplication.UnicodeUTF8))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(QtGui.QApplication.translate("Form", "2", None, QtGui.QApplication.UnicodeUTF8))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(QtGui.QApplication.translate("Form", "4", None, QtGui.QApplication.UnicodeUTF8))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(QtGui.QApplication.translate("Form", "Nowa kolumna", None, QtGui.QApplication.UnicodeUTF8))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(QtGui.QApplication.translate("Form", "a", None, QtGui.QApplication.UnicodeUTF8))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(QtGui.QApplication.translate("Form", "b", None, QtGui.QApplication.UnicodeUTF8))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(QtGui.QApplication.translate("Form", "d", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(QtGui.QApplication.translate("Form", "sex", None, QtGui.QApplication.UnicodeUTF8))
        item = self.tableWidget.item(1, 1)
        item.setText(QtGui.QApplication.translate("Form", "sex1", None, QtGui.QApplication.UnicodeUTF8))
        item = self.tableWidget.item(2, 2)
        item.setText(QtGui.QApplication.translate("Form", "sex2", None, QtGui.QApplication.UnicodeUTF8))
        item = self.tableWidget.item(3, 3)
        item.setText(QtGui.QApplication.translate("Form", "sex3", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.setSortingEnabled(__sortingEnabled)

