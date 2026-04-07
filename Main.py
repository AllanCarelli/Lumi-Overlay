from View.View import MinhaJanela
from Model.Model import Model
from Controller.Controller import MouseReceiver
from PySide6.QtWidgets import QApplication

class Main:
    
    def __init__(self):
        app = QApplication([])
        self.view = MinhaJanela()
        self.view.show()
        

        self.model = Model()

        self.controller = MouseReceiver(self.view,self.model)
        app.aboutToQuit.connect(self.controller.stop)

        app.exec()
if __name__ == "__main__":
    Main()