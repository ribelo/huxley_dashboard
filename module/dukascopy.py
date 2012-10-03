#-*- coding: utf-8-*-

import csv
import os
import pytz
import urllib.request
import datetime

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from settings import *

from ui.DukasInput_ui import Ui_DukasDialog


class DukasDialog(QDialog):
    # if HxSDashboard.preferences.settings:
    #     socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050)
    #     socket.socket = socks.socksocket

    def __init__(self, parrent):
        QWidget.__init__(self, parrent)
        self.parrent = parrent
        self.setModal(True)
        self.ui = Ui_DukasDialog()
        self.ui.setupUi(self)
        self.ui.ok_button.clicked.connect(self.ok_button_clicked)

        self.main_symbol = self.ui.main_symbol.currentText()
        self.sister_symbol = self.ui.sister_symbol.currentText()
        self.candles = self.ui.candle_count.value()
        self.max_candles = self.ui.max_candles.value()
        self.mirror = self.ui.mirror_sister.checkState()

        self.ui.main_symbol.currentIndexChanged.connect(self.on_value_changed)
        self.ui.sister_symbol.currentIndexChanged.connect(self.on_value_changed)
        self.ui.candle_count.valueChanged.connect(self.on_value_changed)
        self.ui.max_candles.valueChanged.connect(self.on_value_changed)
        self.ui.mirror_sister.stateChanged.connect(self.on_value_changed)

    def ok_button_clicked(self):
        self.close()
        # self.downloadFirstCross = DownloadDataThread(self.main_symbol, self.candles, self.max_candles, False)
        downloadDukasData(self.main_symbol, self.candles, self.max_candles, False)
        self.downloadFirstCross = QTimer(self)
        self.downloadFirstCross.timeout.connect(lambda: downloadDukasData(self.main_symbol, self.candles, self.max_candles, False))

    def on_value_changed(self):
        self.main_symbol = self.ui.main_symbol.currentText()
        self.sister_symbol = self.ui.sister_symbol.currentText()
        self.candles = self.ui.candle_count.value()
        self.max_candles = self.ui.max_candles.value()
        self.mirror = self.ui.mirror_sister.checkState()


class DownloadDataThread(QThread):
    """docstring for DownloadDataThread"""
    def __init__(self, cross, candle_count, max_candles, mirror):
        # super(DownloadDataThread, self).__init__()
        QThread.__init__(self)
        self.cross = cross
        self.candle_count = candle_count
        self.max_candles = max_candles
        self.mirror = mirror
        self.downloader = QTimer(self)
        self.downloader.timeout.connect(lambda: downloadDukasData(self.cross, self.candle_count, self.max_candles, self.mirror))

    def run(self):
        downloadDukasData(self.cross, self.candle_count, self.max_candles, self.mirror)
        self.downloader.start(1000 * 60)


def downloadDukasData(cross):
    """Download Dukas Data and store it in file"""

    BASEFILE = 'dukas_{0}.csv'.format(cross.lower())
    BASEDIR = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(BASEDIR + '/../', 'data/', BASEFILE)

    date_output = settings('dukascopy.cfg', 'date_output')
    datetime_format = settings('dukascopy.cfg', 'datetime_format')
    delimiter = settings('dukascopy.cfg', 'delimiter')
    interval = settings('dukascopy.cfg', 'interval')
    symbol = settings('dukascopy.cfg', 'symbol', cross)
    system = settings('dukascopy.cfg', 'system')

    utc_now = roundTime(datetime.datetime.utcnow()).replace(tzinfo=pytz.utc)
    # cet_now = utc_now.astimezone(pytz.timezone('CET'))
    # start_date = utc_now.date().strftime(settings('dukascopy.cfg', 'date_input_format'))
    start_date = settings('dukascopy.cfg', 'start_date')

    # if cet_now.isoweekday() >= 5 and cet_now.hour >= 22 and cet_now.minute > 0:
    #     cet_now.replace(hour=22, minute=0)
    #     utc_now = cet_now.astimezone(pytz.timezone('UTC'))
    utc_now = utc_now.replace(tzinfo=None)

    stored_candles = 0
    candles_to_store = settings('dukascopy.cfg', 'min_candles')

    if os.path.exists(file_path):
        with open(file_path, mode='r') as f:
            quote = list(csv.reader(f, delimiter=';'))[::-1]
            stored_candles = len(quote) - 1
            last_saved_time = roundTime(datetime.datetime.strptime(quote[1][0], datetime_format))
            start_date = last_saved_time.strftime(settings('dukascopy.cfg', 'date_input_format'))
            day_shift = datetime.timedelta(1)
    else:
        with open(file_path, mode='w') as f:
            csv_writer = csv.writer(f, delimiter=';')
            csv_writer.writerow(['datetime', 'open', 'high', 'low', 'close', 'volume'])
            last_saved_time = datetime.datetime(1970, 1, 1)

    if last_saved_time < utc_now:
        print('Last stored candle is older than actual time')
    else:
        return

    while last_saved_time < utc_now or stored_candles < candles_to_store:
        chunk_size = max([min([settings('dukascopy.cfg', 'chunk_size'), (utc_now - last_saved_time).total_seconds() // 60]), 200])
        print('Downloading', chunk_size, 'starting from', start_date, 'last saved time', last_saved_time)
        url = 'http://www.dukascopy.com/freeApplets/exp/exp.php?fromD={0}&np={1}&interval={2}&DF={3}&Stock={4}&endSym={5}&split={6}'.format(start_date, chunk_size, interval, date_output, symbol, system, delimiter)

        succesfull_downloaded = False
        while not succesfull_downloaded:
            try:
                url_handle = urllib.request.urlopen(url)
            except urllib.error.URLError:
                print('connection error')
                return
            else:
                head_line = next(url_handle).decode('UTF-8').strip()
                if head_line.split(';')[0] != 'DATE':
                    print(head_line, head_line.split(';'))
                else:
                    succesfull_downloaded = True

        for line in url_handle:
            quote = line.decode('UTF-8').strip().split(';')
            try:
                date = roundTime(datetime.datetime.strptime(' '.join([quote[0], quote[1]]), datetime_format))
                date_str = datetime.datetime.strftime(date, datetime_format)
            except:
                raise
            finally:
                if date > last_saved_time:
                    day_shift = datetime.timedelta(1)
                    with open(file_path, mode='a') as f:
                        csv_writer = csv.writer(f, delimiter=';')
                        csv_writer.writerow([date_str, quote[3], quote[6], quote[5], quote[4], quote[2]])
                        last_saved_time = date
                        start_date = last_saved_time.strftime(settings('dukascopy.cfg', 'date_input_format'))
                elif date == last_saved_time:
                    start_date = (last_saved_time + day_shift).strftime(settings('dukascopy.cfg', 'date_input_format'))
                    day_shift += datetime.timedelta(1)


def roundTime(dt=None, roundTo=60):
    """Round a datetime object to any time laps in seconds
    dt : datetime.datetime object, default now.
    roundTo : Closest number of seconds to round to, default 1 minute.
    Author: Thierry Husson 2012 - Use it as you want but don't blame me.
    """
    if dt == None:
        dt = datetime.datetime.now()
    seconds = (dt - dt.min).seconds
    rounding = (seconds + roundTo / 2) // roundTo * roundTo
    return dt + datetime.timedelta(0, rounding - seconds, - dt.microsecond)

if __name__ == '__main__':
    import csv
    import os
    import pytz
    import urllib.request
    import datetime

    from PyQt4.QtGui import *
    from PyQt4.QtCore import *

    from settings import *

    from ui.DukasInput_ui import Ui_DukasDialog
    downloadDukasData('EURUSD')
