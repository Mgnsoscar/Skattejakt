import time

from Resources.Code.customQtWidgets import *
from PyQt5 import QtWidgets as qw, QtGui as qg, QtCore as qc, QtTest as qt

class Main(mywindow):

    def __init__(self, *args, **kwargs):

        mywindow.__init__(self, *args, **kwargs)
        self.max_restore()
        # Add Background Picture
        self.blurframe.addstyle('image','border-image: url("Resources/Images/background.jpg");')

        self.frame = myframe(self.mainframe["2"], "v", "frame", color=(255, 255, 255, 100), radius=10)
        self.mainframe["2"].lay.addWidget(self.frame)
        self.frame.setMaximumSize(0,0)
        self.label = mylabel(self.frame, "label", align="center", add=True)

        self.message1 = "For mange hundre år siden var denne byen et knutepunkt for vikinger som reiste nordfra mot" \
                        "mot england for å plyndre."



        #self.openingAnimation()

        texx = Animation(lambda: self.aniText())
        #texx.start()
        texx.start()


    def openingAnimation(self):

        # Frame pops up
        qt.QTest.qWait(1000)
        popup = qc.QPropertyAnimation(self.frame, b'maximumSize')
        popup.setEndValue(qc.QSize(int(self.mainframe["2"].width()*0.8), int(self.mainframe["2"].height()*0.8)))
        popup.setEasingCurve(qc.QEasingCurve.OutBounce)
        popup.setDuration(1200)
        popup.start()
        self.popup = popup

    def aniText(self):

        print("h")















class Animation(qc.QTimer):
    def __init__(self, parentFunction, *args, **kwargs):
        qc.QTimer.__init__(self, *args, **kwargs)
        self.setInterval(int(1000/60))                # 20 fps
        self.timeout.connect(parentFunction)




