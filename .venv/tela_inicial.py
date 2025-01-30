import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from patrimonio import Patrimonio
from localizacoes import Localizacao
from localizar_patrimonio import localizar_patrimonio

class TelaInicial(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gerenciar")
        self.setGeometry(300,200,200,150)
        self.layout_v = QVBoxLayout()

        self.label_titulo = QLabel("Clique para abrir a janela")
        self.button = QPushButton("Abrir Patrimônio")
        self.button2 = QPushButton("Abrir Localização")
        self.button3 = QPushButton("localizar Patrimônio")

        self.layout_v.addWidget(self.label_titulo)
        self.layout_v.addWidget(self.button)
        self.layout_v.addWidget(self.button2)
        self.layout_v.addWidget(self.button3)

        self.button.clicked.connect(self.abrir_cadastro)
        self.button2.clicked.connect(self.abrir_outro)
        self.button3.clicked.connect(self.abrir_local)

        self.setLayout(self.layout_v)

    def abrir_cadastro(self):
        self.pat = Patrimonio()
        self.pat.show()

    def abrir_outro(self):
        self.loc = Localizacao()
        self.loc.show()

    def abrir_local(self):
        self.loc = localizar_patrimonio()
        self.loc.show()

app = QApplication(sys.argv)
tela = TelaInicial()
tela.show()
app.exec()