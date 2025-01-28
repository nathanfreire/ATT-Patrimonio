from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
import sys 

class Localizacao(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(500, 300, 400, 300)
        self.setWindowTitle("Localização do Patrimônio")
        self.layout_v = QVBoxLayout()

        self.label_id = QLabel("ID do Patrimônio:")
        self.label_id.setStyleSheet("QLabel{font-size:15pt}")
        
        self.edit_id = QLineEdit()
        self.edit_id.setStyleSheet("QLineEdit{font-size:15pt}")
        #------------------------------------------------------

        self.label_empresa = QLabel("Empresa do Patrimônio:")
        self.label_empresa.setStyleSheet("QLabel{font-size:15pt}")
        
        self.edit_empresa = QLineEdit()
        self.edit_empresa.setStyleSheet("QLineEdit{font-size:15pt}")
        #------------------------------------------------------

        self.label_logradouro = QLabel("Logradouro do Patrimônio:")
        self.label_logradouro.setStyleSheet("QLabel{font-size:15pt}")
        
        self.edit_logradouro = QLineEdit()
        self.edit_logradouro.setStyleSheet("QLineEdit{font-size:15pt}")
        #------------------------------------------------------

        self.label_numero = QLabel("Número do Patrimônio:")
        self.label_numero.setStyleSheet("QLabel{font-size:15pt}")
        
        self.edit_numero = QLineEdit()
        self.edit_numero.setStyleSheet("QLineEdit{font-size:15pt}")
        #------------------------------------------------------

        self.label_predio = QLabel("Prédio do Patrimônio:")
        self.label_predio.setStyleSheet("QLabel{font-size:15pt}")
        
        self.edit_predio = QLineEdit()
        self.edit_predio.setStyleSheet("QLineEdit{font-size:15pt}")
        #------------------------------------------------------

        self.label_andar = QLabel("Andar do Patrimônio:")
        self.label_andar.setStyleSheet("QLabel{font-size:15pt}")
    
        self.edit_andar = QLineEdit()
        self.edit_andar.setStyleSheet("QLineEdit{font-size:15pt}")
        #------------------------------------------------------

        self.label_sala = QLabel("Sala do Patrimônio:")
        self.label_sala.setStyleSheet("QLabel{font-size:15pt}")
    
        self.edit_sala = QLineEdit()
        self.edit_sala.setStyleSheet("QLineEdit{font-size:15pt}")
        #------------------------------------------------------

        self.button = QPushButton("Cadastrar")
        self.button.setStyleSheet("QPushButton{background-color:blue;color:white;font-size:20pt;font-weight:bold}")
        # Chamar a função de cadastro do cliente ao clicar no botão
        self.button.clicked.connect(self.cadastrar)
        #------------------------------------------------------

        # Adicionar a Label id e o lineedit ao layout certical
        self.layout_v.addWidget(self.label_id)
        self.layout_v.addWidget(self.edit_id)

        # Adicionar a Label números de série e o lineedit ao layout certical
        self.layout_v.addWidget(self.label_empresa)
        self.layout_v.addWidget(self.edit_empresa)

        # Acionar a Label nome do patrimônio e o lineedit ao layout certical
        self.layout_v.addWidget(self.label_logradouro)
        self.layout_v.addWidget(self.edit_logradouro)

        # Acionar a Label tipo e o lineedit ao layout certical
        self.layout_v.addWidget(self.label_numero)
        self.layout_v.addWidget(self.edit_numero)

         # Acionar a Label descrição e o lineedit ao layout certical
        self.layout_v.addWidget(self.label_predio)
        self.layout_v.addWidget(self.edit_predio)

         # Acionar a Label localização e o lineedit ao layout certical
        self.layout_v.addWidget(self.label_andar)
        self.layout_v.addWidget(self.edit_andar)

        # Acionar a Label data de fabricação e o lineedit ao layout certical
        self.layout_v.addWidget(self.label_sala)
        self.layout_v.addWidget(self.edit_sala)

        self.layout_v.addWidget(self.button)

        
        
        #adicionar o layout_v a tela
        self.setLayout(self.layout_v)

    def cadastrar(self):
        # Vamos criar uma variável que fara referencia ao um arquivo de texto
        arquivo = open("Patrimônio.txt","+a", encoding="utf8")
        arquivo.write(f"ID: {self.edit_id.text()}\n")
        arquivo.write(f"Empresa do Patrimônio: {self.edit_empresa.text()}\n")
        arquivo.write(f"Logradouro do Patrimônio: {self.edit_logradouro.text()}\n")
        arquivo.write(f"Número do Patrimônio: {self.edit_numero.text()}\n")
        arquivo.write(f"Prédio do Patrimônio: {self.edit_predio.text()}\n")
        arquivo.write(f"Andar do Patrimônio: {self.edit_andar.text()}\n")
        arquivo.write(f"Sala do Patrimônio: {self.edit_sala.text()}\n")
        arquivo.write("-------------------------------------------\n")
        arquivo.close()

#app = QApplication(sys.argv)
# Instancia da classe CadastroCliente para iniciar a janela
#tela = Localizacao()
# exibir a tela durante a execução
#tela.show()
# ao clicar no botão fechar a tela deve fechar e sair da memória
#app.exec()