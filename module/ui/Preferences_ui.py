# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Preferences.ui'
#
# Created: Tue Sep 18 15:58:37 2012
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Preferences_Dialog(object):
    def setupUi(self, Preferences_Dialog):
        Preferences_Dialog.setObjectName(_fromUtf8("Preferences_Dialog"))
        Preferences_Dialog.setWindowModality(QtCore.Qt.NonModal)
        Preferences_Dialog.setEnabled(True)
        Preferences_Dialog.resize(757, 464)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Preferences_Dialog.sizePolicy().hasHeightForWidth())
        Preferences_Dialog.setSizePolicy(sizePolicy)
        Preferences_Dialog.setMinimumSize(QtCore.QSize(757, 464))
        Preferences_Dialog.setMaximumSize(QtCore.QSize(16777215, 464))
        Preferences_Dialog.setFocusPolicy(QtCore.Qt.StrongFocus)
        Preferences_Dialog.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/actions/bonobo-component-browser.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Preferences_Dialog.setWindowIcon(icon)
        Preferences_Dialog.setModal(False)
        self.verticalLayout_5 = QtGui.QVBoxLayout(Preferences_Dialog)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.groupBox_2 = QtGui.QGroupBox(Preferences_Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMinimumSize(QtCore.QSize(124, 400))
        self.groupBox_2.setMaximumSize(QtCore.QSize(260, 600))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.row_0 = QtGui.QSpinBox(self.groupBox_2)
        self.row_0.setPrefix(_fromUtf8(""))
        self.row_0.setMaximum(43200)
        self.row_0.setProperty("value", 1)
        self.row_0.setObjectName(_fromUtf8("row_0"))
        self.verticalLayout_4.addWidget(self.row_0)
        self.row_1 = QtGui.QSpinBox(self.groupBox_2)
        self.row_1.setMaximum(43200)
        self.row_1.setProperty("value", 2)
        self.row_1.setObjectName(_fromUtf8("row_1"))
        self.verticalLayout_4.addWidget(self.row_1)
        self.row_2 = QtGui.QSpinBox(self.groupBox_2)
        self.row_2.setMaximum(43200)
        self.row_2.setProperty("value", 3)
        self.row_2.setObjectName(_fromUtf8("row_2"))
        self.verticalLayout_4.addWidget(self.row_2)
        self.row_3 = QtGui.QSpinBox(self.groupBox_2)
        self.row_3.setMaximum(43200)
        self.row_3.setProperty("value", 5)
        self.row_3.setObjectName(_fromUtf8("row_3"))
        self.verticalLayout_4.addWidget(self.row_3)
        self.row_4 = QtGui.QSpinBox(self.groupBox_2)
        self.row_4.setMaximum(43200)
        self.row_4.setProperty("value", 10)
        self.row_4.setObjectName(_fromUtf8("row_4"))
        self.verticalLayout_4.addWidget(self.row_4)
        self.row_5 = QtGui.QSpinBox(self.groupBox_2)
        self.row_5.setMaximum(43200)
        self.row_5.setProperty("value", 15)
        self.row_5.setObjectName(_fromUtf8("row_5"))
        self.verticalLayout_4.addWidget(self.row_5)
        self.row_6 = QtGui.QSpinBox(self.groupBox_2)
        self.row_6.setMaximum(43200)
        self.row_6.setProperty("value", 30)
        self.row_6.setObjectName(_fromUtf8("row_6"))
        self.verticalLayout_4.addWidget(self.row_6)
        self.row_7 = QtGui.QSpinBox(self.groupBox_2)
        self.row_7.setMaximum(43200)
        self.row_7.setProperty("value", 60)
        self.row_7.setObjectName(_fromUtf8("row_7"))
        self.verticalLayout_4.addWidget(self.row_7)
        self.row_8 = QtGui.QSpinBox(self.groupBox_2)
        self.row_8.setMaximum(43200)
        self.row_8.setProperty("value", 240)
        self.row_8.setObjectName(_fromUtf8("row_8"))
        self.verticalLayout_4.addWidget(self.row_8)
        self.row_9 = QtGui.QSpinBox(self.groupBox_2)
        self.row_9.setMaximum(43200)
        self.row_9.setProperty("value", 1440)
        self.row_9.setObjectName(_fromUtf8("row_9"))
        self.verticalLayout_4.addWidget(self.row_9)
        self.horizontalLayout_2.addWidget(self.groupBox_2)
        self.groupBox = QtGui.QGroupBox(Preferences_Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(342, 400))
        self.groupBox.setSizeIncrement(QtCore.QSize(1, 0))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.Candle = QtGui.QRadioButton(self.groupBox)
        self.Candle.setChecked(True)
        self.Candle.setAutoRepeat(False)
        self.Candle.setAutoExclusive(False)
        self.Candle.setObjectName(_fromUtf8("Candle"))
        self.verticalLayout.addWidget(self.Candle)
        self.C_Zone = QtGui.QRadioButton(self.groupBox)
        self.C_Zone.setChecked(True)
        self.C_Zone.setAutoRepeat(False)
        self.C_Zone.setAutoExclusive(False)
        self.C_Zone.setObjectName(_fromUtf8("C_Zone"))
        self.verticalLayout.addWidget(self.C_Zone)
        self.L_Zone = QtGui.QRadioButton(self.groupBox)
        self.L_Zone.setChecked(True)
        self.L_Zone.setAutoRepeat(False)
        self.L_Zone.setAutoExclusive(False)
        self.L_Zone.setObjectName(_fromUtf8("L_Zone"))
        self.verticalLayout.addWidget(self.L_Zone)
        self.AJCTR = QtGui.QRadioButton(self.groupBox)
        self.AJCTR.setChecked(True)
        self.AJCTR.setAutoRepeat(False)
        self.AJCTR.setAutoExclusive(False)
        self.AJCTR.setObjectName(_fromUtf8("AJCTR"))
        self.verticalLayout.addWidget(self.AJCTR)
        self.APAOR = QtGui.QRadioButton(self.groupBox)
        self.APAOR.setChecked(True)
        self.APAOR.setAutoRepeat(False)
        self.APAOR.setAutoExclusive(False)
        self.APAOR.setObjectName(_fromUtf8("APAOR"))
        self.verticalLayout.addWidget(self.APAOR)
        self.STR = QtGui.QRadioButton(self.groupBox)
        self.STR.setChecked(True)
        self.STR.setAutoRepeat(False)
        self.STR.setAutoExclusive(False)
        self.STR.setObjectName(_fromUtf8("STR"))
        self.verticalLayout.addWidget(self.STR)
        self.FVB = QtGui.QRadioButton(self.groupBox)
        self.FVB.setChecked(True)
        self.FVB.setAutoRepeat(False)
        self.FVB.setAutoExclusive(False)
        self.FVB.setObjectName(_fromUtf8("FVB"))
        self.verticalLayout.addWidget(self.FVB)
        self.VTR = QtGui.QRadioButton(self.groupBox)
        self.VTR.setEnabled(True)
        self.VTR.setCheckable(True)
        self.VTR.setChecked(True)
        self.VTR.setAutoRepeat(False)
        self.VTR.setAutoExclusive(False)
        self.VTR.setObjectName(_fromUtf8("VTR"))
        self.verticalLayout.addWidget(self.VTR)
        self.Confirmation = QtGui.QRadioButton(self.groupBox)
        self.Confirmation.setChecked(True)
        self.Confirmation.setObjectName(_fromUtf8("Confirmation"))
        self.verticalLayout.addWidget(self.Confirmation)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.Candle_Time = QtGui.QRadioButton(self.groupBox)
        self.Candle_Time.setAutoExclusive(False)
        self.Candle_Time.setObjectName(_fromUtf8("Candle_Time"))
        self.verticalLayout_2.addWidget(self.Candle_Time)
        self.C_Zone_Time = QtGui.QRadioButton(self.groupBox)
        self.C_Zone_Time.setAutoExclusive(False)
        self.C_Zone_Time.setObjectName(_fromUtf8("C_Zone_Time"))
        self.verticalLayout_2.addWidget(self.C_Zone_Time)
        self.L_Zone_Time = QtGui.QRadioButton(self.groupBox)
        self.L_Zone_Time.setAutoExclusive(False)
        self.L_Zone_Time.setObjectName(_fromUtf8("L_Zone_Time"))
        self.verticalLayout_2.addWidget(self.L_Zone_Time)
        self.AJCTR_Time = QtGui.QRadioButton(self.groupBox)
        self.AJCTR_Time.setAutoExclusive(False)
        self.AJCTR_Time.setObjectName(_fromUtf8("AJCTR_Time"))
        self.verticalLayout_2.addWidget(self.AJCTR_Time)
        self.APAOR_Time = QtGui.QRadioButton(self.groupBox)
        self.APAOR_Time.setAutoExclusive(False)
        self.APAOR_Time.setObjectName(_fromUtf8("APAOR_Time"))
        self.verticalLayout_2.addWidget(self.APAOR_Time)
        self.STR_Time = QtGui.QRadioButton(self.groupBox)
        self.STR_Time.setAutoExclusive(False)
        self.STR_Time.setObjectName(_fromUtf8("STR_Time"))
        self.verticalLayout_2.addWidget(self.STR_Time)
        self.FVB_Time = QtGui.QRadioButton(self.groupBox)
        self.FVB_Time.setAutoExclusive(False)
        self.FVB_Time.setObjectName(_fromUtf8("FVB_Time"))
        self.verticalLayout_2.addWidget(self.FVB_Time)
        self.VTR_Time = QtGui.QRadioButton(self.groupBox)
        self.VTR_Time.setAutoExclusive(False)
        self.VTR_Time.setObjectName(_fromUtf8("VTR_Time"))
        self.verticalLayout_2.addWidget(self.VTR_Time)
        self.Confirmation_Time = QtGui.QRadioButton(self.groupBox)
        self.Confirmation_Time.setObjectName(_fromUtf8("Confirmation_Time"))
        self.verticalLayout_2.addWidget(self.Confirmation_Time)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.Candle_Pip = QtGui.QRadioButton(self.groupBox)
        self.Candle_Pip.setAutoExclusive(False)
        self.Candle_Pip.setObjectName(_fromUtf8("Candle_Pip"))
        self.verticalLayout_3.addWidget(self.Candle_Pip)
        self.C_Zone_Pip = QtGui.QRadioButton(self.groupBox)
        self.C_Zone_Pip.setAutoExclusive(False)
        self.C_Zone_Pip.setObjectName(_fromUtf8("C_Zone_Pip"))
        self.verticalLayout_3.addWidget(self.C_Zone_Pip)
        self.L_Zone_Pip = QtGui.QRadioButton(self.groupBox)
        self.L_Zone_Pip.setAutoExclusive(False)
        self.L_Zone_Pip.setObjectName(_fromUtf8("L_Zone_Pip"))
        self.verticalLayout_3.addWidget(self.L_Zone_Pip)
        self.AJCTR_Pip = QtGui.QRadioButton(self.groupBox)
        self.AJCTR_Pip.setAutoExclusive(False)
        self.AJCTR_Pip.setObjectName(_fromUtf8("AJCTR_Pip"))
        self.verticalLayout_3.addWidget(self.AJCTR_Pip)
        self.APAOR_Pip = QtGui.QRadioButton(self.groupBox)
        self.APAOR_Pip.setAutoExclusive(False)
        self.APAOR_Pip.setObjectName(_fromUtf8("APAOR_Pip"))
        self.verticalLayout_3.addWidget(self.APAOR_Pip)
        self.STR_Pip = QtGui.QRadioButton(self.groupBox)
        self.STR_Pip.setAutoExclusive(False)
        self.STR_Pip.setObjectName(_fromUtf8("STR_Pip"))
        self.verticalLayout_3.addWidget(self.STR_Pip)
        self.FVB_Pip = QtGui.QRadioButton(self.groupBox)
        self.FVB_Pip.setAutoExclusive(False)
        self.FVB_Pip.setObjectName(_fromUtf8("FVB_Pip"))
        self.verticalLayout_3.addWidget(self.FVB_Pip)
        self.VTR_Pip = QtGui.QRadioButton(self.groupBox)
        self.VTR_Pip.setEnabled(True)
        self.VTR_Pip.setAutoExclusive(False)
        self.VTR_Pip.setObjectName(_fromUtf8("VTR_Pip"))
        self.verticalLayout_3.addWidget(self.VTR_Pip)
        self.Confirmation_Pip = QtGui.QRadioButton(self.groupBox)
        self.Confirmation_Pip.setObjectName(_fromUtf8("Confirmation_Pip"))
        self.verticalLayout_3.addWidget(self.Confirmation_Pip)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.horizontalLayout_2.addWidget(self.groupBox)
        self.groupBox_3 = QtGui.QGroupBox(Preferences_Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setMinimumSize(QtCore.QSize(260, 0))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.timer_label = QtGui.QLabel(self.groupBox_3)
        self.timer_label.setGeometry(QtCore.QRect(17, 52, 41, 21))
        self.timer_label.setObjectName(_fromUtf8("timer_label"))
        self.timer = QtGui.QSpinBox(self.groupBox_3)
        self.timer.setGeometry(QtCore.QRect(138, 52, 113, 31))
        self.timer.setFrame(True)
        self.timer.setReadOnly(False)
        self.timer.setButtonSymbols(QtGui.QAbstractSpinBox.UpDownArrows)
        self.timer.setSpecialValueText(_fromUtf8(""))
        self.timer.setAccelerated(False)
        self.timer.setKeyboardTracking(False)
        self.timer.setMinimum(12)
        self.timer.setMaximum(3600)
        self.timer.setSingleStep(12)
        self.timer.setProperty("value", 48)
        self.timer.setObjectName(_fromUtf8("timer"))
        self.torLabel = QtGui.QLabel(self.groupBox_3)
        self.torLabel.setGeometry(QtCore.QRect(17, 25, 23, 21))
        self.torLabel.setObjectName(_fromUtf8("torLabel"))
        self.torCheckBox = QtGui.QCheckBox(self.groupBox_3)
        self.torCheckBox.setGeometry(QtCore.QRect(138, 25, 18, 19))
        self.torCheckBox.setCheckable(True)
        self.torCheckBox.setChecked(False)
        self.torCheckBox.setAutoRepeat(False)
        self.torCheckBox.setObjectName(_fromUtf8("torCheckBox"))
        self.candleLookBackLabel = QtGui.QLabel(self.groupBox_3)
        self.candleLookBackLabel.setGeometry(QtCore.QRect(17, 126, 115, 21))
        self.candleLookBackLabel.setObjectName(_fromUtf8("candleLookBackLabel"))
        self.candle_lookback = QtGui.QSpinBox(self.groupBox_3)
        self.candle_lookback.setGeometry(QtCore.QRect(138, 126, 54, 31))
        self.candle_lookback.setMinimum(16)
        self.candle_lookback.setMaximum(512)
        self.candle_lookback.setSingleStep(16)
        self.candle_lookback.setProperty("value", 64)
        self.candle_lookback.setObjectName(_fromUtf8("candle_lookback"))
        self.wRBSizeLabel = QtGui.QLabel(self.groupBox_3)
        self.wRBSizeLabel.setGeometry(QtCore.QRect(17, 89, 65, 21))
        self.wRBSizeLabel.setObjectName(_fromUtf8("wRBSizeLabel"))
        self.wrb_size = QtGui.QSpinBox(self.groupBox_3)
        self.wrb_size.setGeometry(QtCore.QRect(138, 89, 45, 31))
        self.wrb_size.setMaximum(32)
        self.wrb_size.setProperty("value", 3)
        self.wrb_size.setObjectName(_fromUtf8("wrb_size"))
        self.horizontalLayout_2.addWidget(self.groupBox_3)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout_4.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.cancel_button = QtGui.QPushButton(Preferences_Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cancel_button.sizePolicy().hasHeightForWidth())
        self.cancel_button.setSizePolicy(sizePolicy)
        self.cancel_button.setMinimumSize(QtCore.QSize(124, 36))
        self.cancel_button.setMaximumSize(QtCore.QSize(124, 36))
        self.cancel_button.setSizeIncrement(QtCore.QSize(0, 0))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/actions/gtk-cancel.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cancel_button.setIcon(icon1)
        self.cancel_button.setCheckable(False)
        self.cancel_button.setObjectName(_fromUtf8("cancel_button"))
        self.horizontalLayout_4.addWidget(self.cancel_button)
        self.ok_button = QtGui.QPushButton(Preferences_Dialog)
        self.ok_button.setMinimumSize(QtCore.QSize(124, 36))
        self.ok_button.setMaximumSize(QtCore.QSize(124, 36))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/actions/dialog-apply.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ok_button.setIcon(icon2)
        self.ok_button.setObjectName(_fromUtf8("ok_button"))
        self.horizontalLayout_4.addWidget(self.ok_button)
        self.horizontalLayout_4.setStretch(1, 5)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)

        self.retranslateUi(Preferences_Dialog)
        QtCore.QObject.connect(self.Candle, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.Candle_Pip.setEnabled)
        QtCore.QObject.connect(self.C_Zone, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.C_Zone_Pip.setEnabled)
        QtCore.QObject.connect(self.L_Zone, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.L_Zone_Pip.setEnabled)
        QtCore.QObject.connect(self.AJCTR, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.AJCTR_Pip.setEnabled)
        QtCore.QObject.connect(self.APAOR, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.APAOR_Pip.setEnabled)
        QtCore.QObject.connect(self.STR, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.STR_Pip.setEnabled)
        QtCore.QObject.connect(self.FVB, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.FVB_Pip.setEnabled)
        QtCore.QObject.connect(self.Confirmation, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.Confirmation_Pip.setEnabled)
        QtCore.QObject.connect(self.VTR, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.VTR_Pip.setEnabled)
        QtCore.QObject.connect(self.Candle, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.Candle_Time.setEnabled)
        QtCore.QObject.connect(self.C_Zone, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.C_Zone_Time.setEnabled)
        QtCore.QObject.connect(self.L_Zone, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.L_Zone_Time.setEnabled)
        QtCore.QObject.connect(self.AJCTR, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.AJCTR_Time.setEnabled)
        QtCore.QObject.connect(self.APAOR, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.APAOR_Time.setEnabled)
        QtCore.QObject.connect(self.STR, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.STR_Time.setEnabled)
        QtCore.QObject.connect(self.FVB, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.FVB_Time.setEnabled)
        QtCore.QObject.connect(self.Confirmation, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.Confirmation_Time.setEnabled)
        QtCore.QObject.connect(self.VTR, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.VTR_Time.setEnabled)
        QtCore.QObject.connect(self.cancel_button, QtCore.SIGNAL(_fromUtf8("clicked()")), Preferences_Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Preferences_Dialog)
        Preferences_Dialog.setTabOrder(self.row_0, self.row_1)
        Preferences_Dialog.setTabOrder(self.row_1, self.row_2)
        Preferences_Dialog.setTabOrder(self.row_2, self.row_3)
        Preferences_Dialog.setTabOrder(self.row_3, self.row_4)
        Preferences_Dialog.setTabOrder(self.row_4, self.row_5)
        Preferences_Dialog.setTabOrder(self.row_5, self.row_6)
        Preferences_Dialog.setTabOrder(self.row_6, self.row_7)
        Preferences_Dialog.setTabOrder(self.row_7, self.row_8)
        Preferences_Dialog.setTabOrder(self.row_8, self.row_9)
        Preferences_Dialog.setTabOrder(self.row_9, self.Candle)
        Preferences_Dialog.setTabOrder(self.Candle, self.Candle_Time)
        Preferences_Dialog.setTabOrder(self.Candle_Time, self.Candle_Pip)
        Preferences_Dialog.setTabOrder(self.Candle_Pip, self.C_Zone)
        Preferences_Dialog.setTabOrder(self.C_Zone, self.C_Zone_Time)
        Preferences_Dialog.setTabOrder(self.C_Zone_Time, self.C_Zone_Pip)
        Preferences_Dialog.setTabOrder(self.C_Zone_Pip, self.L_Zone)
        Preferences_Dialog.setTabOrder(self.L_Zone, self.L_Zone_Time)
        Preferences_Dialog.setTabOrder(self.L_Zone_Time, self.L_Zone_Pip)
        Preferences_Dialog.setTabOrder(self.L_Zone_Pip, self.AJCTR)
        Preferences_Dialog.setTabOrder(self.AJCTR, self.AJCTR_Time)
        Preferences_Dialog.setTabOrder(self.AJCTR_Time, self.AJCTR_Pip)
        Preferences_Dialog.setTabOrder(self.AJCTR_Pip, self.APAOR)
        Preferences_Dialog.setTabOrder(self.APAOR, self.APAOR_Time)
        Preferences_Dialog.setTabOrder(self.APAOR_Time, self.APAOR_Pip)
        Preferences_Dialog.setTabOrder(self.APAOR_Pip, self.STR)
        Preferences_Dialog.setTabOrder(self.STR, self.STR_Time)
        Preferences_Dialog.setTabOrder(self.STR_Time, self.STR_Pip)
        Preferences_Dialog.setTabOrder(self.STR_Pip, self.FVB)
        Preferences_Dialog.setTabOrder(self.FVB, self.FVB_Time)
        Preferences_Dialog.setTabOrder(self.FVB_Time, self.FVB_Pip)
        Preferences_Dialog.setTabOrder(self.FVB_Pip, self.VTR)
        Preferences_Dialog.setTabOrder(self.VTR, self.VTR_Time)
        Preferences_Dialog.setTabOrder(self.VTR_Time, self.VTR_Pip)

    def retranslateUi(self, Preferences_Dialog):
        Preferences_Dialog.setWindowTitle(QtGui.QApplication.translate("Preferences_Dialog", "Preferences", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("Preferences_Dialog", "Row Timeframe", None, QtGui.QApplication.UnicodeUTF8))
        self.row_0.setSuffix(QtGui.QApplication.translate("Preferences_Dialog", " minutes", None, QtGui.QApplication.UnicodeUTF8))
        self.row_1.setSuffix(QtGui.QApplication.translate("Preferences_Dialog", " minutes", None, QtGui.QApplication.UnicodeUTF8))
        self.row_2.setSuffix(QtGui.QApplication.translate("Preferences_Dialog", " minutes", None, QtGui.QApplication.UnicodeUTF8))
        self.row_3.setSuffix(QtGui.QApplication.translate("Preferences_Dialog", " minutes", None, QtGui.QApplication.UnicodeUTF8))
        self.row_4.setSuffix(QtGui.QApplication.translate("Preferences_Dialog", " minutes", None, QtGui.QApplication.UnicodeUTF8))
        self.row_5.setSuffix(QtGui.QApplication.translate("Preferences_Dialog", " minutes", None, QtGui.QApplication.UnicodeUTF8))
        self.row_6.setSuffix(QtGui.QApplication.translate("Preferences_Dialog", " minutes", None, QtGui.QApplication.UnicodeUTF8))
        self.row_7.setSuffix(QtGui.QApplication.translate("Preferences_Dialog", " minutes", None, QtGui.QApplication.UnicodeUTF8))
        self.row_8.setSuffix(QtGui.QApplication.translate("Preferences_Dialog", " minutes", None, QtGui.QApplication.UnicodeUTF8))
        self.row_9.setSuffix(QtGui.QApplication.translate("Preferences_Dialog", " minutes", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Preferences_Dialog", "Column Signal", None, QtGui.QApplication.UnicodeUTF8))
        self.Candle.setText(QtGui.QApplication.translate("Preferences_Dialog", "Candle/WRB", None, QtGui.QApplication.UnicodeUTF8))
        self.C_Zone.setText(QtGui.QApplication.translate("Preferences_Dialog", "Closest Zone", None, QtGui.QApplication.UnicodeUTF8))
        self.L_Zone.setText(QtGui.QApplication.translate("Preferences_Dialog", "Lastet Zone", None, QtGui.QApplication.UnicodeUTF8))
        self.AJCTR.setText(QtGui.QApplication.translate("Preferences_Dialog", "AJCTR", None, QtGui.QApplication.UnicodeUTF8))
        self.APAOR.setText(QtGui.QApplication.translate("Preferences_Dialog", "APAOR", None, QtGui.QApplication.UnicodeUTF8))
        self.STR.setText(QtGui.QApplication.translate("Preferences_Dialog", "STR", None, QtGui.QApplication.UnicodeUTF8))
        self.FVB.setText(QtGui.QApplication.translate("Preferences_Dialog", "FVB", None, QtGui.QApplication.UnicodeUTF8))
        self.VTR.setText(QtGui.QApplication.translate("Preferences_Dialog", "VTR", None, QtGui.QApplication.UnicodeUTF8))
        self.Confirmation.setText(QtGui.QApplication.translate("Preferences_Dialog", "Confirmation", None, QtGui.QApplication.UnicodeUTF8))
        self.Candle_Time.setText(QtGui.QApplication.translate("Preferences_Dialog", "Times Ago", None, QtGui.QApplication.UnicodeUTF8))
        self.C_Zone_Time.setText(QtGui.QApplication.translate("Preferences_Dialog", "Times Ago", None, QtGui.QApplication.UnicodeUTF8))
        self.L_Zone_Time.setText(QtGui.QApplication.translate("Preferences_Dialog", "Times Ago", None, QtGui.QApplication.UnicodeUTF8))
        self.AJCTR_Time.setText(QtGui.QApplication.translate("Preferences_Dialog", "Times Ago", None, QtGui.QApplication.UnicodeUTF8))
        self.APAOR_Time.setText(QtGui.QApplication.translate("Preferences_Dialog", "Times Ago", None, QtGui.QApplication.UnicodeUTF8))
        self.STR_Time.setText(QtGui.QApplication.translate("Preferences_Dialog", "Times Ago", None, QtGui.QApplication.UnicodeUTF8))
        self.FVB_Time.setText(QtGui.QApplication.translate("Preferences_Dialog", "Times Ago", None, QtGui.QApplication.UnicodeUTF8))
        self.VTR_Time.setText(QtGui.QApplication.translate("Preferences_Dialog", "Times Ago", None, QtGui.QApplication.UnicodeUTF8))
        self.Confirmation_Time.setText(QtGui.QApplication.translate("Preferences_Dialog", "Times Ago", None, QtGui.QApplication.UnicodeUTF8))
        self.Candle_Pip.setText(QtGui.QApplication.translate("Preferences_Dialog", "Pips Ago", None, QtGui.QApplication.UnicodeUTF8))
        self.C_Zone_Pip.setText(QtGui.QApplication.translate("Preferences_Dialog", "Pips Ago", None, QtGui.QApplication.UnicodeUTF8))
        self.L_Zone_Pip.setText(QtGui.QApplication.translate("Preferences_Dialog", "Pips Ago", None, QtGui.QApplication.UnicodeUTF8))
        self.AJCTR_Pip.setText(QtGui.QApplication.translate("Preferences_Dialog", "Pips Ago", None, QtGui.QApplication.UnicodeUTF8))
        self.APAOR_Pip.setText(QtGui.QApplication.translate("Preferences_Dialog", "Pips Ago", None, QtGui.QApplication.UnicodeUTF8))
        self.STR_Pip.setText(QtGui.QApplication.translate("Preferences_Dialog", "Pips Ago", None, QtGui.QApplication.UnicodeUTF8))
        self.FVB_Pip.setText(QtGui.QApplication.translate("Preferences_Dialog", "Pips Ago", None, QtGui.QApplication.UnicodeUTF8))
        self.VTR_Pip.setText(QtGui.QApplication.translate("Preferences_Dialog", "Pips Ago", None, QtGui.QApplication.UnicodeUTF8))
        self.Confirmation_Pip.setText(QtGui.QApplication.translate("Preferences_Dialog", "Pips Ago", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("Preferences_Dialog", "Core", None, QtGui.QApplication.UnicodeUTF8))
        self.timer_label.setText(QtGui.QApplication.translate("Preferences_Dialog", "Timer:", None, QtGui.QApplication.UnicodeUTF8))
        self.timer.setSuffix(QtGui.QApplication.translate("Preferences_Dialog", " second", None, QtGui.QApplication.UnicodeUTF8))
        self.torLabel.setText(QtGui.QApplication.translate("Preferences_Dialog", "Tor", None, QtGui.QApplication.UnicodeUTF8))
        self.candleLookBackLabel.setText(QtGui.QApplication.translate("Preferences_Dialog", "Candle Look Back", None, QtGui.QApplication.UnicodeUTF8))
        self.wRBSizeLabel.setText(QtGui.QApplication.translate("Preferences_Dialog", "WRB Size", None, QtGui.QApplication.UnicodeUTF8))
        self.cancel_button.setText(QtGui.QApplication.translate("Preferences_Dialog", "&cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.ok_button.setText(QtGui.QApplication.translate("Preferences_Dialog", "&ok", None, QtGui.QApplication.UnicodeUTF8))

from . import elementary_rc