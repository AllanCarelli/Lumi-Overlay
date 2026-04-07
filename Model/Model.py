from pathlib import Path

class Model:
    
    def __init__(self):
        self.counter = 0
        self.directory = Path(".")
    def getNewImage(self):
        if self.counter == 0:
            self.counter = 1
            return self.directory.absolute() / "Assets" / "teste2.png"
        elif self.counter == 1:
            self.counter = 0
            return self.directory.absolute() / "Assets" / "teste.png"
    def getFirstImage(self):
        return self.directory.absolute() / "Assets" / "teste2.png"