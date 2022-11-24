from Resources.Code.customQtWidgets import *
from Resources.Code.App import Main
from PyQt5 import QtWidgets as qw
import sys

if __name__ == "__main__":
    application = qw.QApplication(sys.argv)
    Main = Main(transparent=True, frameless=True, windowBlur=True, color=(0, 0, 0, 120), radius=(10, 10, 10, 10), barHeight=25)

    Main.show()
    sys.exit(application.exec_())