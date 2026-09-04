import sys
from PySide6.QtWidgets import QApplication
from janela import CadastroPessoa

app = QApplication(sys.argv)

with open("estilo.css", "r", encoding="utf-8") as arquivo:
    app.setStyleSheet(arquivo.read())
    # abre o arquivo do css e aplica o estilo.

janela = CadastroPessoa()
# cria uma nova janela usando a classe CadastroPessoa.
janela.show()
# mostra a janela na tela (sem o show(), a janela seria criada, mas não apareceria para o usuário.)
sys.exit(app.exec())
# inicia o funcionamento da aplicação e fica esperando as ações do usuário.