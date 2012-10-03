import sys

sys.path.append('./module')
sys.path.append('./module/ui')

# import os

from app_window import *
from dukascopy import *
from forex import *


if __name__ == "__main__":

    app = QApplication(sys.argv)
    wrb_app = HxScDashboard()
    wrb_app.show()
    sys.exit(app.exec_())