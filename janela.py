from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QComboBox, QMessageBox, QFormLayout, QHBoxLayout, QVBoxLayout, QGroupBox
from validacoes import validar_cpf, validar_cnpj, validar_email, validar_celular, validar_cep, validar_nome
from cep import consultar_cep
from banco import cadastrar_pessoa
from tabela import TabelaPessoas

class CadastroPessoa(QWidget):
    # é a janela
    def __init__(self):
        super().__init__()
        # seguinte janela vai funcionar
        self.setWindowTitle("︶꒷꒦︶ ๋ ࣭.⭑🍨 Doce Neve - Cadastro de Pessoa⭑.  ๋︶꒦꒷︶")
        self.resize(700, 500)
        self.criar_interface()
        self.conectar_botoes()
        self.aplicar_mascaras()

    def criar_interface(self):
        # aparência da janela
        pessoal = QFormLayout()
        # layout para organizar os campos de cadastro

        self.nome = QLineEdit()
        self.nome.setPlaceholderText("Digite o nome completo")
        pessoal.addRow("Nome completo:", self.nome)
        # campo de texto para o nome.

        self.tipo_documento = QComboBox()
        self.tipo_documento.addItems(["CPF", "CNPJ"])

        self.documento = QLineEdit()
        self.documento.setPlaceholderText("Digite o CPF ou CNPJ")

        linha_documento = QHBoxLayout()
        linha_documento.addWidget(self.tipo_documento)
        linha_documento.addWidget(self.documento)
        pessoal.addRow("Documento:", linha_documento)
        # coloca o tipo de documento e o CPF/CNPJ na mesma linha.

        self.email = QLineEdit()
        self.email.setPlaceholderText("Digite o e-mail")

        self.celular = QLineEdit()
        self.celular.setPlaceholderText("Digite o celular")

        linha_contato = QHBoxLayout()
        linha_contato.addWidget(self.email)
        linha_contato.addWidget(self.celular)
        pessoal.addRow("E-mail / Celular:", linha_contato)
        # coloca e-mail e celular lado a lado.

        endereco = QFormLayout()
        # outro layout para organizar os campos de endereço.

        self.cep = QLineEdit()
        self.cep.setPlaceholderText("Digite o CEP")
        self.botao_cep = QPushButton("Consultar CEP")

        linha_cep = QHBoxLayout()
        linha_cep.addWidget(self.cep)
        linha_cep.addWidget(self.botao_cep)
        endereco.addRow("CEP:", linha_cep)
        # coloca o CEP e o botão de consulta na mesma linha.

        self.logradouro = QLineEdit()
        self.logradouro.setReadOnly(True)
        endereco.addRow("Logradouro:", self.logradouro)
        # campo para a rua, preenchido automaticamente pelo CEP.

        self.numero = QLineEdit()
        self.numero.setPlaceholderText("Número")

        self.complemento = QLineEdit()
        self.complemento.setPlaceholderText("Opcional")

        linha_numero = QHBoxLayout()
        linha_numero.addWidget(self.numero)
        linha_numero.addWidget(self.complemento)
        endereco.addRow("Número / Complemento:", linha_numero)
        # coloca número e complemento lado a lado.

        self.bairro = QLineEdit()
        self.bairro.setReadOnly(True)
        endereco.addRow("Bairro:", self.bairro)
        # campo para o bairro, preenchido automaticamente pelo CEP.

        self.cidade = QLineEdit()
        self.cidade.setReadOnly(True)

        self.estado = QComboBox()
        self.estado.addItems("AC AL AP AM BA CE DF ES GO MA MT MS MG PA PB PR PE PI RJ RN RS RO RR SC SP SE TO".split())

        linha_cidade = QHBoxLayout()
        linha_cidade.addWidget(self.cidade)
        linha_cidade.addWidget(self.estado)
        endereco.addRow("Cidade / Estado:", linha_cidade)
        # coloca cidade e estado lado a lado.

        grupo_pessoal = QGroupBox("Dados pessoais")
        grupo_pessoal.setLayout(pessoal)
        # cria uma caixa para agrupar os campos de dados pessoais.

        grupo_endereco = QGroupBox("Endereço")
        grupo_endereco.setLayout(endereco)
        # cria uma caixa para agrupar os campos de endereço.

        self.botao_cadastrar = QPushButton("Cadastrar")
        self.botao_limpar = QPushButton("Limpar")
        self.botao_tabela = QPushButton("Ver cadastros")
        # cria os botões para cadastrar, limpar os campos e ver os cadastros.

        botoes = QHBoxLayout()
        botoes.addWidget(self.botao_cadastrar)
        botoes.addWidget(self.botao_limpar)
        botoes.addWidget(self.botao_tabela)
        # organiza os três botões lado a lado.

        layout = QVBoxLayout()
        titulo = QLabel("Cadastro de Pessoa")
        titulo.setObjectName("titulo")
        layout.addWidget(titulo)
        layout.addWidget(grupo_pessoal)
        layout.addWidget(grupo_endereco)
        layout.addLayout(botoes)
        # organiza toda a janela verticalmente.

        self.setLayout(layout)
        # coloca o layout dentro da janela.

    def conectar_botoes(self):
        self.botao_cep.clicked.connect(self.consultar_endereco)
        # quando o botão "Consultar CEP" for clicado, chama a função consultar_endereco.
        self.botao_cadastrar.clicked.connect(self.cadastrar)
        # quando o botão "Cadastrar" for clicado, chama a função cadastrar.
        self.botao_limpar.clicked.connect(self.limpar)
        # quando o botão "Limpar" for clicado, chama a função limpar.
        self.botao_tabela.clicked.connect(self.abrir_tabela)
        # quando o botão "Ver cadastros" for clicado, chama a função para abrir a tabela.
        self.tipo_documento.currentTextChanged.connect(self.formatar_documento)
        # quando o usuário trocar entre CPF e CNPJ, chama a função formatar_documento, que permite mudar a função do documento de acordo com o tipo escolhido.
        

    def aplicar_mascaras(self):
        self.documento.textChanged.connect(self.formatar_documento)
        # sempre que o usuário digitar ou alterar o CPF/CNPJ, chama a função formatar_documento.
        self.cep.textChanged.connect(self.formatar_cep)
        # sempre que o usuário digitar ou alterar o CEP, chama a função formatar_cep.
        self.celular.textChanged.connect(self.formatar_celular)
        # sempre que o usuário digitar ou alterar o celular, chama a função formatar_celular.

    def formatar_documento(self):
        texto = "".join(filter(str.isdigit, self.documento.text()))
        # pega o que foi digitado no campo do documento e mantém somente os números, isso remove pontos, barras, hífens e qualquer outro caractere.

        if self.tipo_documento.currentText() == "CPF":
            # verifica se o tipo escolhido pelo usuário é CPF.
            texto = texto[:11]
            # limita o CPF a no máximo 11 números.

            if len(texto) > 9: 
                texto = texto[:9] + "-" + texto[9:]
            # quando houver mais de 9 números, coloca o hífen antes dos dois últimos números.
            if len(texto) > 6:
                texto = texto[:6] + "." + texto[6:]
            # quando houver mais de 6 números, coloca um ponto depois do sexto número.
            if len(texto) > 3: 
                texto = texto[:3] + "." + texto[3:]
            # quando houver mais de 3 números, coloca outro ponto depois do terceiro número.
        else:
            # se não for CPF, significa que o tipo escolhido é CNPJ.
            texto = texto[:14]
            # limita o CNPJ a no máximo 14 números.

            if len(texto) > 12: 
                texto = texto[:12] + "-" + texto[12:]
            # coloca o hífen antes dos dois últimos números.

            if len(texto) > 8: 
                texto = texto[:8] + "/" + texto[8:]
            # coloca a barra depois dos oito primeiros números.

            if len(texto) > 5: 
                texto = texto[:5] + "." + texto[5:]
            # coloca um ponto depois dos cinco primeiros números.

            if len(texto) > 2: 
                texto = texto[:2] + "." + texto[2:]
            # coloca outro ponto depois dos dois primeiros números.

        self.documento.blockSignals(True)
        # bloqueia temporariamente os sinais do campo, evita que fique executando a função repetidamente (é mais para o funcionamento, não interfere muito), até que tudo seja modificado.

        self.documento.setText(texto)
        # coloca o texto já formatado de volta no campo.

        self.documento.blockSignals(False)
        # libera novamente os sinais do campo.


    def formatar_cep(self):
        texto = "".join(filter(str.isdigit, self.cep.text()))[:8]
        # pega o texto digitado no CEP e mantém somente os números, também limita o CEP a 8 números.

        if len(texto) > 5: texto = texto[:5] + "-" + texto[5:]
        # quando houver mais de 5 números, coloca um hífen depois dos cinco primeiros.

        self.cep.blockSignals(True)
        self.cep.setText(texto)
        self.cep.blockSignals(False)
        # funciona igual ao dos CPF E CNPJ

    def formatar_celular(self):
        texto = "".join(filter(str.isdigit, self.celular.text()))[:11]
        # pega o texto digitado no celular e mantém somente os números,também limita o celular a 11 números.

        if len(texto) > 7:
            texto = f"({texto[:2]}) {texto[2:7]}-{texto[7:]}"
            # quando houver mais de 7 números, monta o celular completo.

        elif len(texto) > 2:
            texto = f"({texto[:2]}) {texto[2:]}"
            # enquanto o usuário ainda estiver digitando, coloca o DDD entre parênteses.

        self.celular.blockSignals(True)
        self.celular.setText(texto)
        self.celular.blockSignals(False)
        # funciona igual ao dos CPF E CNPJ também 

    def validar_dados(self):
        nome = self.nome.text().strip()
        documento = self.documento.text().strip()
        email = self.email.text().strip()
        celular = self.celular.text().strip()
        cep = self.cep.text().strip()
        numero = self.numero.text().strip()
        # pega todos os campos e remove espaços do começo e do final (e cria variáveis para as operações abaixo).

        if not nome:
            # verifica se o campo de nome está vazio.
            QMessageBox.warning(self, "Erro", "Informe o nome completo.")
            # mostra uma mensagem de aviso para o usuário.
            self.nome.setFocus()
            # coloca o foco do teclado no campo de nome, para o usuário saber onde precisa corrigir.
            return False
            # informa que a validação não foi aprovada.
        if not validar_nome(nome):
            # verifica se o nome possui pelo menos duas partes, usando a função validar_nome() do arquivo validacoes.py.
            QMessageBox.warning(self, "Erro", "Informe o nome completo.")
            # mostra uma mensagem avisando que o nome precisa ser completo.
            self.nome.setFocus()
            # coloca o foco novamente no campo de nome.
            return False
            # interrompe a validação porque o nome está incorreto.

        tipo = self.tipo_documento.currentText()
        # pega o tipo de documento escolhido no QComboBox, pode ser "CPF" ou "CNPJ".
        if not documento:
            # verifica se o campo CPF/CNPJ está vazio.
            QMessageBox.warning(self, "Erro", f"Informe o {tipo}.")
            # mostra uma mensagem dizendo qual documento precisa ser informado.
            self.documento.setFocus()
            return False
        if tipo == "CPF" and not validar_cpf(documento):
            # verifica se o tipo escolhido é CPF e se o CPF informado é inválido.
            QMessageBox.warning(self, "CPF inválido", "O CPF informado não é válido.")
            self.documento.setFocus()
            return False
        if tipo == "CNPJ" and not validar_cnpj(documento):
            # verifica se o tipo escolhido é CNPJ e se o CNPJ informado é inválido.
            QMessageBox.warning(self, "CNPJ inválido", "O CNPJ informado não é válido.")
            self.documento.setFocus()
            return False

        if not email:
            # verifica se o campo de e-mail está vazio.
            QMessageBox.warning(self, "Erro", "Informe o e-mail.")
            # mostra uma mensagem pedindo o e-mail.
            self.email.setFocus()
            return False
        if not validar_email(email):
            # verifica se o formato do e-mail está correto.
            QMessageBox.warning(self, "E-mail inválido", "Informe um e-mail válido.")
            self.email.setFocus()
            return False

        if not celular:
            # verifica se o campo de celular está vazio.
            QMessageBox.warning(self, "Erro", "Informe o celular.")
            # mostra uma mensagem pedindo o celular.
            self.celular.setFocus()
            return False
        if not validar_celular(celular):
            # verifica se o celular possui a quantidade correta de números.
            QMessageBox.warning(self, "Celular inválido", "Informe um celular válido.")
            self.celular.setFocus()
            return False

        if not cep:
            # verifica se o campo de CEP está vazio.
            QMessageBox.warning(self, "Erro", "Informe o CEP.")
            # mostra uma mensagem pedindo o CEP.
            self.cep.setFocus()
            return False
            
        if not validar_cep(cep):
            # verifica se o CEP possui 8 números.
            QMessageBox.warning(self, "CEP inválido", "O CEP deve possuir 8 números.")
            self.cep.setFocus()
            return False

        if not numero:
            # verifica se o número do endereço foi preenchido.
            QMessageBox.warning(self, "Erro", "Informe o número do endereço.")
            # mostra uma mensagem pedindo o número.
            self.numero.setFocus()
            return False

        return True
        # se chegar até aqui, significa que todas as validações deram certo.

    def consultar_endereco(self):
        cep = self.cep.text().strip()
        # pega o CEP digitado pelo usuário e remove espaços do começo e do final.
        if not validar_cep(cep):
            # verifica se o CEP possui 8 números.
            QMessageBox.warning(self, "CEP inválido", "Digite um CEP com 8 números.")
            # mostra uma mensagem informando como corrigir o CEP.
            self.cep.setFocus()
            return

        dados, erro = consultar_cep("".join(filter(str.isdigit, cep)))
        # remove a formatação do CEP e envia somente os números para a função consultar_cep(), dados receberá as informações do endereço e erro receberá uma possível mensagem de erro.

        if erro:
            # verifica se aconteceu algum erro durante a consulta.
            QMessageBox.warning(self, "Erro", erro)
            # mostra para o usuário a mensagem de erro recebida.
            self.cep.setFocus()
            return

        self.preencher_endereco(dados)
        # envia os dados encontrados para a função preencher_endereco(), essa função coloca as informações nos campos de endereço.

        QMessageBox.information(self, "CEP", "Endereço encontrado com sucesso!")
        # mostra uma mensagem informando que a consulta funcionou.

    def preencher_endereco(self, dados):
        self.logradouro.setText(dados.get("logradouro", ""))
        self.bairro.setText(dados.get("bairro", ""))
        self.cidade.setText(dados.get("localidade", ""))
        self.estado.setCurrentText(dados.get("uf", ""))
        # pega as informações da API e coloca nos campos de endereço, se algum dado não estiver disponível, coloca uma string vazia.

    def limpar(self):
        for campo in (self.nome, self.documento, self.email, self.celular, self.cep, self.logradouro, self.numero, self.complemento, self.bairro, self.cidade):
            campo.clear()
            # percorre todos os campos da lista e apaga o conteúdo de cada um.

        self.tipo_documento.setCurrentIndex(0)
        self.estado.setCurrentIndex(0)
        self.nome.setFocus()
        # depois de limpar os campos, coloca o foco do teclado no campo de nome e reseta os campos de seleção para a primeira opção.

    def cadastrar(self):
        if not self.validar_dados():
            return

        # tenta salvar os dados no banco
        sucesso, erro = cadastrar_pessoa(
            self.nome.text(),
            self.tipo_documento.currentText(),
            self.documento.text(),
            self.email.text(),
            self.celular.text(),
            self.cep.text(),
            self.logradouro.text(),
            self.numero.text(),
            self.complemento.text(),
            self.bairro.text(),
            self.cidade.text(),
            self.estado.currentText()
        )

        # se houver erro, mostra a mensagem e para o cadastro
        if not sucesso:
            QMessageBox.warning(self, "Erro", erro)
            return

        # mostra mensagem de sucesso e limpa os campos
        QMessageBox.information(self, "Cadastro", "Cadastro realizado com sucesso!")
        self.limpar()

    def abrir_tabela(self):
        self.tabela = TabelaPessoas()
        self.tabela.show()