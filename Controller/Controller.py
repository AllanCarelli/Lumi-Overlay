from pynput import mouse
from PySide6.QtCore import Signal, QObject

class MouseReceiver(QObject):
    load_image = Signal(object)
    def __init__(self, view, model):
        super().__init__()
        self.model = model
        self.view = view
        self.load_image.connect(self.view.changeImage)
        self.listener = mouse.Listener(on_click=self.clickHandler)
        self.listener.start()
    def stop(self):
        self.listener.stop()
    def clickHandler(self):
        image = self.model.getNewImage()
        self.load_image.emit(image)
        