from PIL import Image, ImageOps
import io

class SpriteManager:
    #(X_inicial, Y_inicial, X_final, Y_final)
    COORDINATES = {"Talking": [(204,328,241,384)],
                    "Holding": [(259,387,307,443)],
                    "Ball": [(647,462,695,511),(584,463,632,512),(711,462,759,511)]
                    }
    def __init__(self,image_path):
        self.buffer = io.BytesIO()
        
        self.imgSpriteSheet = Image.open(image_path)
        
        self.saveImage()

        self.callback = []

    def cleanStream(self,state):
        self.buffer.seek(0)
        self.buffer.truncate(0)
        self.COORDINATES[state][0].save(self.buffer,append_images=self.COORDINATES[id][1:],duration=50,loop=0,format="GIF",optmize=True)
        

    def saveImage(self):
        for images, name in self.COORDINATES.items():
            frameList = []
            for frames in images:
                frm = self.imgSpriteSheet.crop(frames)
                frm = ImageOps.scale(frm,1.3)
                frameList.append(frm)
            self.COORDINATES[name] = frameList

    def getImage(self):
        self.buffer.seek(0)
        return self.buffer.getvalue()

    def setState(self,state):
        self.cleanStream(state)
        self.call()
    
    def addCallback(self,action):
        self.callback.append(action)

    def call(self):
        for callback in self.callback:
            callback()
