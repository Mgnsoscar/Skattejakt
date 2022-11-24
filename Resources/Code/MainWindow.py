from PyQt5 import QtWidgets as qw, QtCore as qc, QtGui as qg, uic
from Resources.Code.customQtWidgets import *
from BlurWindow.blurWindow import blur

class MainWindow(qw.QMainWindow):
    def __init__(self, frameless=None,  transparent=None,   windowBlur=None,  size=None,  color=None, radius=None,  barHeight=None, text=None, Credits=None):

        # Bool to know if the window is maximized or normal
        self.maximized = False

        # initialize the main window, remove frames, make translucent, set size
        qw.QMainWindow.__init__(self), self.setObjectName("main")

        #### Init a centralwidget, add to main, init central frame, add to central widget
        self.cw = mywidget(     self,       "v",            radius=10)
        self.cw.addstyle("background-color", "background-color: rgba(0,0,0,0);")
        self.cf = myframe(      self.cw,    "v",    "cf",   add=True,   radius=10,  color=(0, 0, 0, 100))
        self.setCentralWidget(  self.cw)  # ,  self.cf.addstyle("image", "border-image: url(:/images/Background3.jpg);")

        #### Create 3 main frames
        mainframe = {}
        mainframe["1"] = myframe(self.cf, "h", f"mainframe1", add=True)
        mainframe["2"] = myframe(self.cf, "g", f"mainframe2", add=True)
        mainframe["3"] = myframe(self.cf, "h", f"mainframe3", add=True)

        mainframe["1"].customradius(9, 9, 0, 0),    mainframe["1"].setFixedHeight(20), mainframe["1"].bg(0, 0, 0, 100)
        mainframe["3"].customradius(0, 0, 10, 10),  mainframe["3"].setFixedHeight(20), mainframe["2"].margins(10, 10, 10, 0)
        mainframe["2"].spacing(10)
        self.mainframe = mainframe

        #### Create 3 frames in the top mainframe
        topframe = {}
        for i in range(1, 4):
            topframe[str(i)] = myframe(mainframe["1"], "h", f"topframe{i}", add=True)

        topframe["3"].setFixedWidth(200),           topframe["3"].margins(135, 0, 0, 0)
        topframe["1"].customradius(0, 0, 10, 0),    topframe["1"].setFixedWidth(500)
        self.topframe = topframe

        #### Create three buttons in the top right frame, set radius, individual colors, hover- and pressed color
        button = {}
        for i in range(1, 4):
            button[str(i)] = mybutton(topframe["3"], objectName=f"button{i}",   radius=7,   add=True, align="center")
            button[str(i)].setFixedSize(14, 14)

        button["1"].bg(255, 255, 0, 255),   button["1"].hcolor(255, 255, 0, 150),   button["1"].pcolor(255, 255, 0, 50)
        button["2"].bg(0, 255, 0, 255),     button["2"].hcolor(0, 255, 0, 150),     button["2"].pcolor(0, 255, 0, 50)
        button["3"].bg(255, 0, 0, 255),     button["3"].hcolor(255, 0, 0, 150),     button["3"].pcolor(255, 0, 0, 50)
        self.button = button

        #### Create a title label
        self.title = mylabel(topframe["1"],     font=("Roboto", "Light", 100),  size=15,        add=True,       align="left")
        topframe["1"].margins(10, 0, 0, 0)

        #### Create 2 frames in the bottom mainframe
        btmframe = {}
        for i in range(1, 3):
            btmframe[str(i)] = myframe(mainframe["3"], "v", f"btmframe{i}",     add=True)
        btmframe["2"].setFixedWidth(20)

        #### Create a label with credits
        self.credits = mylabel(btmframe["1"],  font=("Roboto", "Italic", 50),   size=13,        add=True,   color=(255, 255, 255, 100))
        btmframe["1"].margins(5, 0, 0, 0)

        #### Add size-grip to the bottom right corner
        sizegrip = qw.QSizeGrip(btmframe["2"])
        sizegrip.setStyleSheet("background-color: rgba(0,0,0,0);"),     btmframe["2"].lay.addWidget(sizegrip, 0,qc.Qt.AlignBottom)

        # Init some customizeable styles:
        if Credits != None:
            self.credits.setText(Credits)
        if frameless == True:
            self.setWindowFlags(qc.Qt.FramelessWindowHint)
            if radius != None:
                x1, x2, x3, x4 = radius[0],radius[1],radius[2],radius[3]
                self.cf.customradius(x1,x2,x3,x4),  self.mainframe["1"].customradius(x1,x2, 0, 0),  self.mainframe["3"].customradius(0, 0, x3, x4)
            if barHeight!=None:
                self.mainframe["1"].setFixedHeight(barHeight)
            if text!=None:
                self.title.setText(text)
        else:
            self.mainframe["1"].setFixedHeight(0), self.cf.customradius(0, 0, 0, 0)
            if text!=None:
                self.setWindowTitle(text)
        if transparent == True:
            self.setAttribute(qc.Qt.WA_TranslucentBackground)
        if windowBlur == True:
            hWnd = self.winId()
            blur(hWnd)
        if color != None:
            r, g, b, a = color[0], color[1], color[2], color[3]
            self.cf.bg(r, g, b, a)
        if size != None:
            x, y = size[0], size[1]
            self.resize(x, y)
        else:
            self.resize(1500, 1000)

        # Link some functions
        self.mainframe["1"].mouseMoveEvent = self.moveWindow
        functions.buttonconfig(self)















    # Make sure the window can be moved
    def moveWindow(self,event):

            if event.buttons() == qc.Qt.LeftButton:

                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

    # Define function every time the mouse is pressed
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

class functions(MainWindow):

    def max_restore(self):

        if self.maximized == False:
            self.cw.radius(0),      self.cf.radius(0),          self.mainframe["1"].customradius(0, 0, 0, 0),       self.showMaximized()
            self.maximized = True

        else:
            self.cw.radius(10),     self.cf.radius(10),         self.mainframe["1"].customradius(10, 10, 0, 0),     self.showNormal()
            self.resize(self.width() + 1, self.height() + 1)
            self.maximized = False

    def buttonconfig(self):
        # close/maximize/minimize buttons:
        self.button["1"].clicked.connect(self.showMinimized),   self.button["2"].clicked.connect(lambda: functions.max_restore(self))
        self.button["3"].clicked.connect(self.close)