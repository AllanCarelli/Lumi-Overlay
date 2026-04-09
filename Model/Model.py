from pathlib import Path

class Model:
    def __init__(self):
        self.assets_dir = Path(".").absolute() / "Assets"
        self.counter = 0
        self.currentImage = self.assets_dir / "teste.png"
        self.callback = []
    def setNewImage(self):
        if self.counter == 0:
            self.counter = 1
            image = "teste2.png"
        elif self.counter == 1:
            self.counter = 0
            image = "teste.png"
        self.currentImage = self.assets_dir / image
    def getImage(self):
        return self.currentImage
    def callback(self):
        for callback in self.callback:
            callback()