from PySide6.QtWidgets import QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout, QLabel
from banco import listar_pessoas

class TabelaPessoas(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Doce Neve - Pessoas")
        self.resize(900, 500)
        self.criar_interface()
        self.carregar_pessoas()

    def criar_interface(self):
        titulo = QLabel("Pessoas cadastradas")
        titulo.setObjectName("titulo")

        self.tabela = QTableWidget()
        self.tabela.setAlternatingRowColors(True)
        self.tabela.setSelectionBehavior(QTableWidget.SelectRows)
        self.tabela.setEditTriggers(QTableWidget.NoEditTriggers)
        self.tabela.horizontalHeader().setStretchLastSection(True)
        self.tabela.setColumnCount(13)
        self.tabela.setHorizontalHeaderLabels([
            "ID", "Nome", "Tipo", "Documento", "E-mail", "Celular",
            "CEP", "Logradouro", "Número", "Complemento", "Bairro",
            "Cidade", "Estado"
        ])

        layout = QVBoxLayout()
        layout.addWidget(titulo)
        layout.addWidget(self.tabela)

        self.setLayout(layout)

    def carregar_pessoas(self):
        pessoas = listar_pessoas()
        self.tabela.setRowCount(len(pessoas))

        for linha, pessoa in enumerate(pessoas):
            for coluna in range(13):
                self.tabela.setItem(linha, coluna, QTableWidgetItem(str(pessoa[coluna])))