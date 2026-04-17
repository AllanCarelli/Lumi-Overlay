from View.View import MinhaJanela
from Controller.Controller import Controller
from PySide6.QtWidgets import QApplication
import sys
from Model.SpriteManager import SpriteManager
from pathlib import Path


class Main:
    def __init__(self):
        
        self.spriteManager = SpriteManager(Path(".").absolute() / "Assets" / "Villain_Lumi.png")
        
        self.controller = Controller(self.spriteManager)
        

        self.view = MinhaJanela(self.spriteManager,self.controller)
        self.view.show()

        self.spriteManager.addCallback(self.view.changeImage)
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    Main()
    app.exec()