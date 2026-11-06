from PIL import Image, ImageOps
import io
import os, sys

def rpath(relative_path):
    try:
        base = sys._MEIPASS
    except Exception:
        base = os.path.abspath(".")

    return os.path.join(base,relative_path)

class SpriteManager:
    def __init__(self):
        self.buffer = io.BytesIO()
        self.ballList = []
        self.img = Image.open(rpath("Assets\\Villain_Lumi.png"))
        self.coordinates = {"Talking": (204,328,241,384),
                            "Holding": (259,387,307,443),
                            "Ball": [(647,462,695,511),(584,463,632,512),(711,462,759,511)]}
        self.talkingImage = self.img.crop(self.coordinates["Talking"])
        self.holdingImage = self.img.crop(self.coordinates["Holding"])

        for images in self.coordinates["Ball"]:
            ball = self.img.crop(images)
            ball = ImageOps.scale(ball,1.3)
            self.ballList.append(ball)

        self.holdingImage = ImageOps.scale(self.holdingImage,1.3)
        self.talkingImage = ImageOps.scale(self.talkingImage,1.3)
        
        self.holdingImage.save(self.buffer, format="GIF")
        self.talkingImage.save(self.buffer, format="GIF")
        
        self.ballList[0].save(self.buffer, save_all=True, append_images=self.ballList[1:],duration=50,loop=0,format="GIF")
        self.state = "Holding"
        self.callback = []

    def getImage(self):
        self.buffer.seek(0)
        return self.buffer.getvalue()
    
    def cleanStream(self):
        if self.state == "Talking":
            self.buffer.seek(0)
            self.buffer.truncate(0)
            self.talkingImage.save(self.buffer, format="GIF")
        elif self.state == "Holding":
            self.buffer.seek(0)
            self.buffer.truncate(0)
            self.holdingImage.save(self.buffer, format="GIF")
        elif self.state == "Ball":
            self.buffer.seek(0)
            self.buffer.truncate(0)
            self.ballList[0].save(self.buffer,append_images=self.ballList[1:],duration=50,loop=0,format="GIF",optmize=True)
        

    def setState(self,state):
        self.state = state
        self.cleanStream()
        self.call()
    
    def addCallback(self,action):
        self.callback.append(action)

    def call(self):
        for callback in self.callback:
            callback()
