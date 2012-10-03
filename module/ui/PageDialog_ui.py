# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PageDialog.ui'
#
# Created: Mon Jul 23 23:33:21 2012
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_PageDialog(object):
    def setupUi(self, PageDialog):
        PageDialog.setObjectName(_fromUtf8("PageDialog"))
        PageDialog.resize(370, 221)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PageDialog.sizePolicy().hasHeightForWidth())
        PageDialog.setSizePolicy(sizePolicy)
        PageDialog.setMinimumSize(QtCore.QSize(370, 200))
        PageDialog.setMaximumSize(QtCore.QSize(370, 221))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/actions/add-files-to-archive.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        PageDialog.setWindowIcon(icon)
        PageDialog.setSizeGripEnabled(False)
        PageDialog.setModal(False)
        self.gridLayout_2 = QtGui.QGridLayout(PageDialog)
        self.gridLayout_2.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.cross_1 = QtGui.QLineEdit(PageDialog)
        self.cross_1.setObjectName(_fromUtf8("cross_1"))
        self.gridLayout.addWidget(self.cross_1, 1, 0, 1, 1)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.formLayout.setMargin(6)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.cancel_button = QtGui.QPushButton(PageDialog)
        self.cancel_button.setMinimumSize(QtCore.QSize(100, 0))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/actions/gtk-cancel.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cancel_button.setIcon(icon1)
        self.cancel_button.setObjectName(_fromUtf8("cancel_button"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.cancel_button)
        self.ok_button = QtGui.QPushButton(PageDialog)
        self.ok_button.setMinimumSize(QtCore.QSize(100, 0))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/actions/dialog-apply.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ok_button.setIcon(icon2)
        self.ok_button.setDefault(False)
        self.ok_button.setObjectName(_fromUtf8("ok_button"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.ok_button)
        self.gridLayout.addLayout(self.formLayout, 4, 0, 1, 3)
        self.cross_2_button = QtGui.QPushButton(PageDialog)
        self.cross_2_button.setMinimumSize(QtCore.QSize(100, 0))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/actions/document-new.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cross_2_button.setIcon(icon3)
        self.cross_2_button.setObjectName(_fromUtf8("cross_2_button"))
        self.gridLayout.addWidget(self.cross_2_button, 2, 2, 1, 1)
        self.broker_name = QtGui.QLineEdit(PageDialog)
        self.broker_name.setObjectName(_fromUtf8("broker_name"))
        self.gridLayout.addWidget(self.broker_name, 0, 0, 1, 3)
        self.cross_1_button = QtGui.QPushButton(PageDialog)
        self.cross_1_button.setMinimumSize(QtCore.QSize(100, 0))
        self.cross_1_button.setMaximumSize(QtCore.QSize(100, 100))
        self.cross_1_button.setIcon(icon3)
        self.cross_1_button.setObjectName(_fromUtf8("cross_1_button"))
        self.gridLayout.addWidget(self.cross_1_button, 1, 2, 1, 1)
        self.mirror_sister = QtGui.QRadioButton(PageDialog)
        self.mirror_sister.setObjectName(_fromUtf8("mirror_sister"))
        self.gridLayout.addWidget(self.mirror_sister, 3, 2, 1, 1)
        self.cross_2 = QtGui.QLineEdit(PageDialog)
        self.cross_2.setObjectName(_fromUtf8("cross_2"))
        self.gridLayout.addWidget(self.cross_2, 2, 0, 2, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(PageDialog)
        QtCore.QObject.connect(self.cancel_button, QtCore.SIGNAL(_fromUtf8("clicked()")), PageDialog.close)
        QtCore.QMetaObject.connectSlotsByName(PageDialog)

    def retranslateUi(self, PageDialog):
        PageDialog.setWindowTitle(QtGui.QApplication.translate("PageDialog", "DataFeed Input", None, QtGui.QApplication.UnicodeUTF8))
        self.cross_1.setText(QtGui.QApplication.translate("PageDialog", "Main_Symbol", None, QtGui.QApplication.UnicodeUTF8))
        self.cancel_button.setText(QtGui.QApplication.translate("PageDialog", "&Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.ok_button.setText(QtGui.QApplication.translate("PageDialog", "&OK", None, QtGui.QApplication.UnicodeUTF8))
        self.cross_2_button.setText(QtGui.QApplication.translate("PageDialog", "AddPath", None, QtGui.QApplication.UnicodeUTF8))
        self.broker_name.setText(QtGui.QApplication.translate("PageDialog", "Broker_Name", None, QtGui.QApplication.UnicodeUTF8))
        self.cross_1_button.setText(QtGui.QApplication.translate("PageDialog", "AddPath", None, QtGui.QApplication.UnicodeUTF8))
        self.mirror_sister.setText(QtGui.QApplication.translate("PageDialog", "mirror", None, QtGui.QApplication.UnicodeUTF8))
        self.cross_2.setText(QtGui.QApplication.translate("PageDialog", "Sister_Symbol", None, QtGui.QApplication.UnicodeUTF8))

from . import elementary_rc
