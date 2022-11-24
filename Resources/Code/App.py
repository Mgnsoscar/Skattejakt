from Resources.Code.customQtWidgets import *

class Main(mywindow):

    def __init__(self, *args, **kwargs):

        mywindow.__init__(self, *args, **kwargs)
        # Add Background Picture
        self.blurframe.addstyle('image','border-image: url("Resources/Images/background.jpg");')

        self.frame = myframe(self.mainframe["2"], "v", "frame", add=True, color=(255, 255, 255, 100), radius=10)
        self.frame.setFixedSize(0,0)

        self.animation = Animation(lambda: self.opening())
        self.animation.start()

        self.currentx = 0
        self.currenty = 0


    def opening(self):

        if self.currenty <= 900 and self.currentx <=1400:
            self.frame.setFixedSize(self.currentx, self.currenty)
            self.currentx +=56
            self.currenty +=36
        else:
            self.animation.stop()




class Animation(qc.QTimer):
    def __init__(self, parentFunction, *args, **kwargs):
        qc.QTimer.__init__(self, *args, **kwargs)
        self.setInterval(int(1000/60))                # 20 fps
        self.timeout.connect(parentFunction)




