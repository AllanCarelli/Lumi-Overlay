class Controller:
    def __init__(self,spriteManager):
        super().__init__()
        self.spriteManager = spriteManager
    def changeImage(self,state):
        self.spriteManager.setState(state)


        