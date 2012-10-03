# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DukasInput.ui'
#
# Created: Thu Aug  9 18:21:41 2012
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DukasDialog(object):
    def setupUi(self, DukasDialog):
        DukasDialog.setObjectName(_fromUtf8("DukasDialog"))
        DukasDialog.setWindowModality(QtCore.Qt.WindowModal)
        DukasDialog.resize(295, 233)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DukasDialog.sizePolicy().hasHeightForWidth())
        DukasDialog.setSizePolicy(sizePolicy)
        DukasDialog.setMinimumSize(QtCore.QSize(295, 233))
        DukasDialog.setMaximumSize(QtCore.QSize(295, 233))
        self.verticalLayout = QtGui.QVBoxLayout(DukasDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(DukasDialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.candle_count = QtGui.QSpinBox(DukasDialog)
        self.candle_count.setMinimum(1)
        self.candle_count.setMaximum(999999)
        self.candle_count.setProperty("value", 100000)
        self.candle_count.setObjectName(_fromUtf8("candle_count"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.candle_count)
        self.label_3 = QtGui.QLabel(DukasDialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.max_candles = QtGui.QSpinBox(DukasDialog)
        self.max_candles.setMaximum(9999999)
        self.max_candles.setProperty("value", 1000000)
        self.max_candles.setObjectName(_fromUtf8("max_candles"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.max_candles)
        self.label_4 = QtGui.QLabel(DukasDialog)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_4)
        self.main_symbol = QtGui.QComboBox(DukasDialog)
        self.main_symbol.setFrame(True)
        self.main_symbol.setObjectName(_fromUtf8("main_symbol"))
        self.main_symbol.addItem(_fromUtf8(""))
        self.main_symbol.addItem(_fromUtf8(""))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.main_symbol)
        self.label_5 = QtGui.QLabel(DukasDialog)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_5)
        self.sister_symbol = QtGui.QComboBox(DukasDialog)
        self.sister_symbol.setObjectName(_fromUtf8("sister_symbol"))
        self.sister_symbol.addItem(_fromUtf8(""))
        self.sister_symbol.addItem(_fromUtf8(""))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.sister_symbol)
        self.label_2 = QtGui.QLabel(DukasDialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_2)
        self.mirror_sister = QtGui.QCheckBox(DukasDialog)
        self.mirror_sister.setText(_fromUtf8(""))
        self.mirror_sister.setChecked(True)
        self.mirror_sister.setTristate(False)
        self.mirror_sister.setObjectName(_fromUtf8("mirror_sister"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.mirror_sister)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(100, -1, -1, -1)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.cancel_button = QtGui.QPushButton(DukasDialog)
        self.cancel_button.setObjectName(_fromUtf8("cancel_button"))
        self.horizontalLayout.addWidget(self.cancel_button)
        self.ok_button = QtGui.QPushButton(DukasDialog)
        self.ok_button.setObjectName(_fromUtf8("ok_button"))
        self.horizontalLayout.addWidget(self.ok_button)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(DukasDialog)
        self.main_symbol.setCurrentIndex(0)
        self.sister_symbol.setCurrentIndex(0)
        QtCore.QObject.connect(self.cancel_button, QtCore.SIGNAL(_fromUtf8("clicked()")), DukasDialog.close)
        QtCore.QMetaObject.connectSlotsByName(DukasDialog)

    def retranslateUi(self, DukasDialog):
        DukasDialog.setWindowTitle(QtGui.QApplication.translate("DukasDialog", "Dukascopy Input", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("DukasDialog", "Candle Count:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("DukasDialog", "Max Stored Candles:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("DukasDialog", "Main Symbol:", None, QtGui.QApplication.UnicodeUTF8))
        self.main_symbol.setItemText(0, QtGui.QApplication.translate("DukasDialog", "EURUSD", None, QtGui.QApplication.UnicodeUTF8))
        self.main_symbol.setItemText(1, QtGui.QApplication.translate("DukasDialog", "USDCHF", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("DukasDialog", "Sister Symbol:", None, QtGui.QApplication.UnicodeUTF8))
        self.sister_symbol.setItemText(0, QtGui.QApplication.translate("DukasDialog", "USDCHF", None, QtGui.QApplication.UnicodeUTF8))
        self.sister_symbol.setItemText(1, QtGui.QApplication.translate("DukasDialog", "EURUSD", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("DukasDialog", "Mirror Sister Symbol:", None, QtGui.QApplication.UnicodeUTF8))
        self.cancel_button.setText(QtGui.QApplication.translate("DukasDialog", "&cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.ok_button.setText(QtGui.QApplication.translate("DukasDialog", "&ok", None, QtGui.QApplication.UnicodeUTF8))

