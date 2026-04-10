from View.View import MinhaJanela
from Model.Model import Model
from Controller.Controller import MouseReceiver
from PySide6.QtWidgets import QApplication
import sys


class Main:
    
    def __init__(self):
        self.model = Model()

        self.controller = MouseReceiver(self.model)

        self.view = MinhaJanela(self.model)
        self.view.show()

        self.model.addCallbackImage(self.view.changeImage)

        app.aboutToQuit.connect(self.controller.stop)

        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    Main()
    app.exec()