# Sistema de Cadastro de Pessoas

Sistema desktop desenvolvido em Python e PySide6 para realizar o cadastro de pessoas, com validação de informações, consulta automática de endereço pelo CEP e armazenamento dos dados em um banco de dados MySQL.

## 📋 O que é necessário para executar o projeto

Antes de executar o sistema, é necessário ter instalado:

- Python 3;
- Visual Studio Code (VS Code);
- MySQL Server;
- MySQL Workbench;
- Extensão Python no VS Code;
- Biblioteca PySide6;
- Biblioteca mysql-connector-python;
- Conexão com a internet para realizar a consulta de CEP.

O projeto utiliza a API ViaCEP para consultar os dados do endereço.

---

# 📁 Estrutura do projeto

O projeto está organizado nos seguintes arquivos:

```text
ATV8/
├── cadastro.py
├── janela.py
├── validacoes.py
├── cep.py
├── banco.py
├── tabela.py
├── estilo.css
└── README.md