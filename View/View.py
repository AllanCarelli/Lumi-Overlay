from PySide6.QtWidgets import *
from PySide6 import QtCore
from PySide6.QtGui import QPixmap


class MinhaJanela(QMainWindow):
    def __init__(self, model):
        super().__init__()

        self.model = model

        # Pega um objeto que representa as características da tela
        screen = self.screen()

        # Cria o widget central e faz ele ter o tamanho da tela
        widget_central = QWidget()
        self.setGeometry(QtCore.QRect(QtCore.QPoint(0,0),screen.size()))
        self.setCentralWidget(widget_central)
        
        # Cria o Layout (config padrão)
        self.layout = QVBoxLayout()
        widget_central.setLayout(self.layout)

        # Cria um label para guardar a imagem (Pixmap pq ela é melhor para exibir)
        self.imagem = QLabel("")
        self.imagem.setPixmap(QPixmap(self.model.getImage()))
        self.layout.addWidget(self.imagem,alignment=QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignBottom)
        
        # Deixar a janela transparente e por cima
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setWindowFlag(QtCore.Qt.WindowType.WindowStaysOnTopHint)



    def changeImage(self):
            self.imagem.setPixmap(QPixmap(self.model.getImage()))

