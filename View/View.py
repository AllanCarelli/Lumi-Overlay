from PySide6.QtWidgets import *
from PySide6 import QtCore
from PySide6.QtGui import QPixmap, QMovie




class MinhaJanela(QMainWindow):
    def __init__(self,spriteManager,controller):
        super().__init__()

        # guarda as referências do spritemanager e do model
        self.spriteManager = spriteManager
        self.controller = controller


        # DISGRAÇA VOU TER QUE FAZER ESSA JANELA SER MOVÍVEL NA RAÇA
        screen = self.screen()

        self.screen_h_f = screen.geometry().height() - 73
        self.screen_w_f = screen.geometry().width() - 49

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.gravity)

        self.oldPos = QtCore.QPoint(0,0)
        self.speedY = 0
        self.speedX = 0

        # Cria o widget central e faz ele ter o tamanho da tela
        widget_central = QWidget()
        # self.setGeometry(QtCore.QRect(QtCore.QPoint(0,0),QtCore.QSize(100,100)))
        self.setGeometry(screen.geometry())
        self.setCentralWidget(widget_central)
        
        # Cria o Layout (config padrão)
        # self.layout = QGridLayout()
        # widget_central.setLayout(self.layout)

        # Cria um label para guardar a imagem (Pixmap pq ela é melhor para exibir)
        self.imagem = QLabel("")
        self.imagem.setMovie(self.image(self.spriteManager.getImage()))
        self.imagem.movie().start()
        # self.layout.addWidget(self.imagem,alignment=QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignBottom)
        # self.layout.addWidget(self.imagem)
        self.imagem.setParent(widget_central)

        # Deixar a janela transparente e por cima
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setWindowFlag(QtCore.Qt.WindowType.WindowStaysOnTopHint)



    def changeImage(self):
        #Troca a imagem (chamada pelo callback do model)
        self.imagem.movie().stop()
        self.imagem.setMovie(self.image(self.spriteManager.getImage()))
        self.imagem.movie().start()

    def image(self,image_link):
        # Formatação para a imagem
        self.byteArray = QtCore.QByteArray(image_link)
        self.buffer = QtCore.QBuffer(self.byteArray)
        self.img = QMovie(self.buffer)
        self.img.setCacheMode(QMovie.CacheMode.CacheAll)
        # self.img.setScaledSize(QtCore.QSize(50,50))
        return self.img
    
    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        # Pega a pos inicial quando eu clico com o mouse para ser usada dps
        self.pressing = True
        self.startPos = QtCore.QPoint(13,5)

    def mouseMoveEvent(self, event):
        super().mouseMoveEvent(event)
        if self.pressing:
            # O move move a janela para a posição do mouse na tela inteira - a posição do mouse que começou, ou seja, bem na posição exata.
            "QtCore.QPoint(1075, 963)"
            self.speedY = event.position().toPoint().y() - self.oldPos.y()
            self.speedX = event.position().toPoint().x() - self.oldPos.x()
            print(self.speedX, self.speedY)
            self.oldPos = event.position().toPoint()
            if event.position().toPoint().y() >= 976:
                pass
            else:
                self.imagem.move(event.globalPosition().toPoint() - self.startPos)
            self.controller.changeImage("Holding")
            
    
    def mouseReleaseEvent(self, event):
        super().mouseReleaseEvent(event)
        self.pressing = False
        self.controller.changeImage("Ball")
        self.gForce = 0
        self.dislocation = 1 + self.gForce + self.speedY
        self.timer.start(15)

    def gravity(self):
        if self.pressing:
            self.timer.stop()
        if self.imagem.pos().y() <= self.screen_h_f:
            if self.imagem.pos().x() <= 0:
                self.speedX = self.speedX * -1 
                self.imagem.move(QtCore.QPoint(0,self.imagem.pos().y() + self.dislocation))
            elif self.imagem.pos().x() >= self.screen_w_f:
                self.speedX = self.speedX * -1    
                self.imagem.move(QtCore.QPoint(self.screen_w_f,self.imagem.pos().y() + self.dislocation))
            self.imagem.move(QtCore.QPoint(self.imagem.pos().x() + self.speedX,self.imagem.pos().y() + self.dislocation))
            self.dislocation += 1
            if self.speedX > 0:
                self.speedX -= 1
            if self.speedX < 0:
                self.speedX += 1
        
            
        else:
            self.imagem.move(QtCore.QPoint(self.imagem.pos().x(),self.screen_h_f))
            self.controller.changeImage("Talking")
            self.timer.stop()
