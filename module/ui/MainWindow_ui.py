# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created: Tue Sep  4 19:40:21 2012
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DashboardWindow(object):
    def setupUi(self, DashboardWindow):
        DashboardWindow.setObjectName(_fromUtf8("DashboardWindow"))
        DashboardWindow.resize(1040, 900)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DashboardWindow.sizePolicy().hasHeightForWidth())
        DashboardWindow.setSizePolicy(sizePolicy)
        DashboardWindow.setMinimumSize(QtCore.QSize(768, 300))
        DashboardWindow.setMaximumSize(QtCore.QSize(1280, 1024))
        DashboardWindow.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        DashboardWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/actions/gtk-apply.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DashboardWindow.setWindowIcon(icon)
        DashboardWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        DashboardWindow.setAnimated(True)
        DashboardWindow.setDocumentMode(False)
        DashboardWindow.setTabShape(QtGui.QTabWidget.Rounded)
        DashboardWindow.setDockNestingEnabled(False)
        self.centralwidget = QtGui.QWidget(DashboardWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.main_layout = QtGui.QGridLayout()
        self.main_layout.setObjectName(_fromUtf8("main_layout"))
        self.verticalLayout.addLayout(self.main_layout)
        DashboardWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QtGui.QToolBar(DashboardWindow)
        self.toolBar.setMovable(True)
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)
        self.toolBar.setFloatable(True)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        DashboardWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.statusBar = QtGui.QStatusBar(DashboardWindow)
        self.statusBar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.statusBar.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        DashboardWindow.setStatusBar(self.statusBar)
        self.actionAdd_CSV = QtGui.QAction(DashboardWindow)
        self.actionAdd_CSV.setChecked(False)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/actions/document-new.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAdd_CSV.setIcon(icon1)
        self.actionAdd_CSV.setIconVisibleInMenu(False)
        self.actionAdd_CSV.setObjectName(_fromUtf8("actionAdd_CSV"))
        self.actionPreferences = QtGui.QAction(DashboardWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/actions/gtk-execute.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPreferences.setIcon(icon2)
        self.actionPreferences.setObjectName(_fromUtf8("actionPreferences"))
        self.actionShow_Database = QtGui.QAction(DashboardWindow)
        self.actionShow_Database.setCheckable(False)
        self.actionShow_Database.setEnabled(True)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/actions/extract-archive.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionShow_Database.setIcon(icon3)
        self.actionShow_Database.setObjectName(_fromUtf8("actionShow_Database"))
        self.actionAdd_DukasCopy = QtGui.QAction(DashboardWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/actions/bookmarks_list_add.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAdd_DukasCopy.setIcon(icon4)
        self.actionAdd_DukasCopy.setObjectName(_fromUtf8("actionAdd_DukasCopy"))
        self.actionPlay = QtGui.QAction(DashboardWindow)
        self.actionPlay.setCheckable(True)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/actions/player_play.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPlay.setIcon(icon5)
        self.actionPlay.setObjectName(_fromUtf8("actionPlay"))
        self.toolBar.addAction(self.actionAdd_CSV)
        self.toolBar.addAction(self.actionAdd_DukasCopy)
        self.toolBar.addAction(self.actionShow_Database)
        self.toolBar.addAction(self.actionPreferences)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionPlay)

        self.retranslateUi(DashboardWindow)
        QtCore.QObject.connect(DashboardWindow, QtCore.SIGNAL(_fromUtf8("destroyed()")), DashboardWindow.close)
        QtCore.QMetaObject.connectSlotsByName(DashboardWindow)

    def retranslateUi(self, DashboardWindow):
        DashboardWindow.setWindowTitle(QtGui.QApplication.translate("DashboardWindow", "Huxley Dashboard", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("DashboardWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.statusBar.setStatusTip(QtGui.QApplication.translate("DashboardWindow", "Ooo ... It\'s me!", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAdd_CSV.setText(QtGui.QApplication.translate("DashboardWindow", "Add CSV", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAdd_CSV.setToolTip(QtGui.QApplication.translate("DashboardWindow", "Add CSV Database", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAdd_CSV.setStatusTip(QtGui.QApplication.translate("DashboardWindow", "Adds a SQL database from a file", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPreferences.setText(QtGui.QApplication.translate("DashboardWindow", "Preferences", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPreferences.setStatusTip(QtGui.QApplication.translate("DashboardWindow", "WRB Preferences", None, QtGui.QApplication.UnicodeUTF8))
        self.actionShow_Database.setText(QtGui.QApplication.translate("DashboardWindow", "Show Database", None, QtGui.QApplication.UnicodeUTF8))
        self.actionShow_Database.setToolTip(QtGui.QApplication.translate("DashboardWindow", "Show Database", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAdd_DukasCopy.setText(QtGui.QApplication.translate("DashboardWindow", "Add DukasCopy", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAdd_DukasCopy.setToolTip(QtGui.QApplication.translate("DashboardWindow", "Add DukasCopy Database", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPlay.setText(QtGui.QApplication.translate("DashboardWindow", "Play", None, QtGui.QApplication.UnicodeUTF8))

from . import elementary_rc
