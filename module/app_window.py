#-*- coding: utf-8-*-

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from ui.MainWindow_ui import Ui_DashboardWindow

class HxScDashboard(QMainWindow):

    def __init__(self):
        #=======================================================================
        # Main Layout Initialization
        #=======================================================================
        QWidget.__init__(self)
        self.ui = Ui_DashboardWindow()
        self.ui.setupUi(self)
        self.docky = QDockWidget()
        self.tab_view = QTabWidget()
        self.ui.main_layout.addWidget(self.tab_view)
        #=======================================================================
        # Preferences Initialization
        #=======================================================================
        self.tables = {}
        self.preferences = Preferences(self)
        self.ui.actionPreferences.triggered.connect(self.preferences.exec_)
        #=======================================================================
        # DataFeed Initialization
        #=======================================================================
        self.ui.actionAdd_CSV.triggered.connect(self.addBroker)
        self.ui.actionAdd_DukasCopy.triggered.connect(self.addDukas)
        self.ui.actionPlay.toggled.connect(self.play)
        #=======================================================================
        # Main Loop Initialization
        #=======================================================================
        self.analyze = WRB()
        self.loop = QTimer(self)
        self.loop.timeout.connect(lambda: self.analyze.main_loop())

    def addPage(self, broker, cross_1, cross_2):
        hbox = QVBoxLayout()
        self.tables[broker] = {cross_1: TableBox(cross_1), cross_2: TableBox(cross_2)}
        hbox.addWidget(self.tables[broker][cross_1])
        hbox.addWidget(self.tables[broker][cross_2])
        layout = QWidget()
        layout.setLayout(hbox)
        self.tab_view.addTab(layout, broker)
        self.updateTable()

    def addBroker(self):
        self.dialog = Page_Dialog(self)
        self.dialog.ui.cross_1_button.clicked.connect(lambda: self.openFileDialog('cross_1'))
        self.dialog.ui.cross_2_button.clicked.connect(lambda: self.openFileDialog('cross_2'))
        self.dialog.ui.ok_button.clicked.connect(self.addDatabase)
        self.dialog.exec_()

    def addDukas(self):
        self.dukas = DukasDialog(self)
        self.dukas.exec_()

    def openFileDialog(self, cross):
        if cross == 'cross_1':
            self.tmp_path_1 = QFileDialog().getOpenFileName(self, 'Open file', '/home')
            if self.dialog.ui.cross_1.text() == 'Main_Symbol':
                name = self.tmp_path_1.split('/')[-1].split('.')[0]
                self.dialog.ui.cross_1.setText(name)

        if cross == 'cross_2':
            self.tmp_path_2 = QFileDialog().getOpenFileName(self, 'Open file', '/home')
            if self.dialog.ui.cross_2.text() == 'Sister_Symbol':
                name = self.tmp_path_2.split('/')[-1].split('.')[0]
                self.dialog.ui.cross_2.setText(name)

    def addDatabase(self):
        self.dialog.close()
        broker_name = self.dialog.ui.broker_name.text()
        cross_1 = self.dialog.ui.cross_1.text()
        cross_2 = self.dialog.ui.cross_2.text()
        mirror = self.dialog.ui.mirror_sister.isChecked()
        if not broker_name in Candle.db:
            Candle.db[broker_name] = {}
        if not cross_1 in Candle.db[broker_name]:
            Candle.db[broker_name][cross_1] = {'path': '{0}.csv'.format(cross_1), 'mirror': False, 'quote': {}}
            Candle.db[broker_name][cross_1]['quote'] = []
            Candle.db[broker_name][cross_1]['signal'] = {'WRB': [], 'ZONE': [], 'AJCTR': [], 'APAOR': [], 'STR': [], 'FVB': []}
            Candle.db[broker_name][cross_2] = {'path': '{0}.csv'.format(cross_1), 'mirror': mirror, 'quote': {}}
            Candle.db[broker_name][cross_2]['quote'] = []
            Candle.db[broker_name][cross_2]['signal'] = {'WRB': [], 'ZONE': [], 'AJCTR': [], 'APAOR': [], 'STR': [], 'FVB': []}

        self.addPage(broker_name, cross_1, cross_2)
        self.updateQuote()

    def updateQuote(self):
        format = '%Y-%m-%d %H:%M:%S'
        for broker in list(Candle.db.keys()):
            for symbol, path in Candle.db[broker]['path'].items():
                with open(path, 'rt') as textfile:
                    quote = list(csv.reader(textfile, delimiter=';'))
                    quote.reverse()
                    # Check data
                    if not Candle.db[broker][symbol]['mirror']:
                        Candle.db[broker][symbol]['quote'].append((roundTime(datetime.datetime.strptime(row[0], format)), float(row[1]), float(row[2]), float(row[3]), float(row[4]), float(row[5])))
                    else:
                        Candle.db[broker][symbol]['quote'].append((roundTime(datetime.datetime.strptime(row[0], format)), float(row[1]), float(row[5]), float(row[4]), float(row[3]), float(row[2])))

    def updateTable(self):
        table = self.tables['dukas']['EURUSD'].table
        item = QTableWidgetItem()
        item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        item.setText('sexsex')
        table.setItem(3, 3, item)

    def play(self):
        if not self.loop.isActive():
            self.analyze.main_loop()
            self.loop.start(1000 * 60)
        else:
            self.loop.stop()


class TableBox(QGroupBox):
    def __init__(self, title):
        QWidget.__init__(self)
        self.setTitle(title)
        self.table = QTableWidget()
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.setSortingEnabled(False)
        self.table.horizontalHeader().setVisible(True)
        self.table.horizontalHeader().setCascadingSectionResizes(True)
        self.table.horizontalHeader().setHighlightSections(True)
        self.table.horizontalHeader().setSortIndicatorShown(False)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.verticalHeader().setVisible(True)
        self.table.verticalHeader().setCascadingSectionResizes(False)
        self.table.verticalHeader().setStretchLastSection(True)
        grid = QGridLayout()
        grid.addWidget(self.table)
        self.setLayout(grid)
        self.rows = (str(x) for x in Settings.options['timeframe'] if x != 0)
        self.columns = (x for x in Settings.options['signals'])
        self.items = {}
        self.addTable()
        self.setRowNames()
        self.setColumnNames()
        self.setItems()

    def addTable(self):
        self.table.setRowCount(len(self.rows))
        self.table.setColumnCount(len(self.columns))

    def setRowNames(self):
        for row in self.rows:
            item = QTableWidgetItem()
            item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            item.setText(str(row))
            self.table.setVerticalHeaderItem(self.rows.index(row), item)

    def setColumnNames(self):
        i = 0
        for column in self.columns:
            for k, v in column.items():
                if v[0] == True:
                    item = QTableWidgetItem()
                    item.setText(k)
                    self.table.setHorizontalHeaderItem(i, item)
                    i = i + 1
                    if v[1] == True:
                        item = QTableWidgetItem()
                        item.setText(k)
                        item.setText('Time Ago')
                        self.table.setHorizontalHeaderItem(i, item)
                        i = i + 1
                    if v[2] == True:
                        item = QTableWidgetItem()
                        item.setText(k)
                        item.setText('Pips Ago')
                        self.table.setHorizontalHeaderItem(i, item)
                        i = i + 1

    def setItems(self):
        x = 0
        y = 0
        for column in self.columns:
            self.items[str(list(column.keys())[0])] = x
            x = x + 1
        for row in self.rows:
            self.items[str(row)] = y
            y = y + 1


class Settings(object):
    """docstring for Settings"""
    options = {'tor': False, 'timer': 0, 'wrb_size': 0, 'candle_lookback': 0, 'timeframe': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'signals': (('Candle/WRB', [0, 0, 0]), ('C_Zone', [0, 0, 0]), ('L_Zone', [0, 0, 0]), ('AJCTR', [0, 0, 0]), ('APAOR', [0, 0, 0]), ('STR', [0, 0, 0]), ('FVB', [0, 0, 0]), ('VTR', [0, 0, 0]), ('Confirmation', [0, 0, 0]))}

    @staticmethod
    def load():
        Settings.options = json.load(open('config.wrb'))

    @staticmethod
    def save():
        json.dump(Settings.options, open('config.wrb', mode='w'), indent=4, sort_keys=True)


class Page_Dialog(QDialog):
    def __init__(self, parrent):
        QWidget.__init__(self, parrent)
        self.setModal(True)
        self.ui = Ui_PageDialog()
        self.ui.setupUi(self)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    wrb_app = HxScDashboard()
    wrb_app.show()
    sys.exit(app.exec_())
