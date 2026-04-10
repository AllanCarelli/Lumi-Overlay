from pathlib import Path

class Model:
    def __init__(self):
        self.__assets_dir = Path(".").absolute() / "Assets"
        self.__counter = 0
        self.__currentImage = self.__assets_dir / "teste.png"
        self.__callback = []
    def setNewImage(self):
        if self.__counter == 0:
            self.__counter = 1
            image = "teste2.png"
        elif self.__counter == 1:
            self.__counter = 0
            image = "teste.png"
        self.__currentImage = self.__assets_dir / image
        self.call()
    def getImage(self):
        return self.__currentImage
    def addCallback(self,action):
        self.__callback.append(action)
    def call(self):
        for callback in self.__callback:
            callback()