from PySide6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem, QPushButton, QMessageBox, QLineEdit, QHeaderView, QAbstractItemView)
from banco import listar_pessoas, excluir_pessoa
from pdf import gerar_pdf

class TabelaPessoas(QWidget):
    def __init__(self, ao_editar=None):
        super().__init__()

        # Função recebida para editar uma pessoa
        self.ao_editar = ao_editar

        self.setWindowTitle("Pessoas cadastradas")
        self.resize(1720, 500)

        # Cria a tabela
        self.tabela = QTableWidget()
        self.tabela.setColumnCount(13)
        # Permite selecionar a linha inteira
        self.tabela.setSelectionBehavior(QAbstractItemView.SelectRows)

        # Permite selecionar apenas uma pessoa por vez
        self.tabela.setSelectionMode(QAbstractItemView.SingleSelection)

        self.tabela.setHorizontalHeaderLabels([
            "ID", "Nome", "Tipo", "Documento", "E-mail",
            "Celular", "CEP", "Logradouro", "Número",
            "Complemento", "Bairro", "Cidade", "Estado"
        ])

        # Ajusta a largura das colunas
        self.tabela.setColumnWidth(0, 40)    # ID
        self.tabela.setColumnWidth(1, 180)   # Nome
        self.tabela.setColumnWidth(2, 70)    # Tipo
        self.tabela.setColumnWidth(3, 140)   # Documento
        self.tabela.setColumnWidth(4, 200)   # E-mail
        self.tabela.setColumnWidth(5, 130)   # Celular
        self.tabela.setColumnWidth(6, 90)    # CEP
        self.tabela.setColumnWidth(7, 200)   # Logradouro
        self.tabela.setColumnWidth(8, 70)    # Número
        self.tabela.setColumnWidth(9, 150)   # Complemento
        self.tabela.setColumnWidth(10, 150)  # Bairro
        self.tabela.setColumnWidth(11, 150)  # Cidade
        self.tabela.setColumnWidth(12, 70)   # Estado


        # Organiza o layout
        layout = QVBoxLayout()

        # Barra de pesquisa por nome
        self.pesquisa = QLineEdit()
        self.pesquisa.setPlaceholderText("Pesquisar pessoa pelo nome...")
        self.pesquisa.textChanged.connect(self.filtrar_pessoas)
        layout.addWidget(self.pesquisa)

        layout.addWidget(self.tabela)

        # Cria uma linha para os botões
        botoes = QHBoxLayout()

        # Botão para editar
        self.botao_editar = QPushButton("Editar selecionado")
        self.botao_editar.clicked.connect(self.editar_selecionado)
        botoes.addWidget(self.botao_editar)

        # Botão para excluir
        self.botao_excluir = QPushButton("Excluir selecionado")
        self.botao_excluir.clicked.connect(self.excluir_selecionado)
        botoes.addWidget(self.botao_excluir)

        # Botão para gerar PDF
        self.botao_pdf = QPushButton("Gerar PDF")
        self.botao_pdf.clicked.connect(self.gerar_pdf_tabela)
        botoes.addWidget(self.botao_pdf)

        # Adiciona a linha de botões ao layout principal
        layout.addLayout(botoes)
        
        self.setLayout(layout)
        self.carregar_dados()

    def carregar_dados(self):
        # Busca os cadastros no banco
        pessoas = listar_pessoas()

        self.tabela.setRowCount(len(pessoas))

        # Coloca os dados na tabela
        for linha, pessoa in enumerate(pessoas):
            for coluna, valor in enumerate(pessoa):
                self.tabela.setItem(
                    linha,
                    coluna,
                    QTableWidgetItem(str(valor or ""))
                )

    def editar_selecionado(self):
        # Descobre qual linha está selecionada
        linha = self.tabela.currentRow()

        if linha < 0:
            QMessageBox.warning(
                self,
                "Atenção",
                "Selecione uma pessoa para editar."
            )
            return

        # Busca novamente os dados do banco
        pessoas = listar_pessoas()
        pessoa = pessoas[linha]

        # Envia a pessoa selecionada para o formulário
        if self.ao_editar:
            self.ao_editar(pessoa)

    def excluir_selecionado(self):
        # Descobre qual linha está selecionada
        linha = self.tabela.currentRow()

        if linha < 0:
            QMessageBox.warning(
                self,
                "Atenção",
                "Selecione uma pessoa para excluir."
            )
            return

        # Busca os dados da pessoa selecionada
        pessoas = listar_pessoas()
        pessoa = pessoas[linha]

        # Pega o ID da pessoa
        id_pessoa = pessoa[0]

        # Confirma antes de excluir
        caixa = QMessageBox(self)
        caixa.setWindowTitle("Confirmar exclusão")
        caixa.setText("Deseja realmente excluir esta pessoa?")
        caixa.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

        # Traduz os botões
        caixa.button(QMessageBox.Yes).setText("Sim")
        caixa.button(QMessageBox.No).setText("Não")

        resposta = caixa.exec()

        if resposta == QMessageBox.Yes:
            sucesso, erro = excluir_pessoa(id_pessoa)

            if sucesso:
                QMessageBox.information(
                    self,
                    "Sucesso",
                    "Cadastro excluído com sucesso!"
                )

                # Atualiza a tabela
                self.carregar_dados()
            else:
                QMessageBox.warning(self, "Erro", erro)

    def gerar_pdf_tabela(self):
        # Gera o arquivo PDF
        caminho = gerar_pdf()

        QMessageBox.information(
            self,
            "PDF gerado",
            f"PDF criado com sucesso!\n\nArquivo: {caminho}"
        )

    def filtrar_pessoas(self, texto):
        # Deixa o texto da pesquisa em letras minúsculas
        texto = texto.lower()

        # Percorre todas as linhas da tabela
        for linha in range(self.tabela.rowCount()):
            # Pega o nome da pessoa, que está na coluna 1
            item = self.tabela.item(linha, 1)

            if item:
                nome = item.text().lower()

                # Mostra a linha se o nome tiver o texto pesquisado
                mostrar = texto in nome
                self.tabela.setRowHidden(linha, not mostrar)