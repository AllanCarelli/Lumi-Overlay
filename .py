from PySide6.QtWidgets import *
from PySide6 import QtCore
from PySide6.QtGui import QPixmap
from pynput import mouse

class MinhaJanela(QMainWindow):
    def __init__(self):
        super().__init__()

        # Configuração das imagens para o overlay
        self.img_atual = 0
        self.imgs = [QPixmap("teste.png"),QPixmap("teste2.png")]

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
        self.imagem.setPixmap(QPixmap("teste.png"))
        self.layout.addWidget(self.imagem,alignment=QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignBottom)
        
        # Deixar a janela transparente e por cima
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setWindowFlag(QtCore.Qt.WindowType.WindowStaysOnTopHint)

        # A partir disso é apenas detecção de cliques

        listener = mouse.Listener(on_click=self.mousePressEvent)
        listener.start()
    def mousePressEvent(self):
        if self.img_atual == 0:
            self.img_atual = 1
            self.imagem.setPixmap(self.imgs[self.img_atual])
        else:
            self.img_atual = 0
            self.imagem.setPixmap(self.imgs[self.img_atual])


# Só instanciando tudo para executar
app = QApplication([])
janela = MinhaJanela()
janela.show()
app.exec()