from pynput import mouse

class MouseReceiver:
    def __init__(self, model):
        super().__init__()
        self.model = model
        self.listener = mouse.Listener(on_click=self.clickHandler)
        self.listener.start()
    def stop(self):
        self.listener.stop()
    def clickHandler(self, *args):
        self.model.setNewImage()

        