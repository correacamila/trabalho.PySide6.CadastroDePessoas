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

O projeto está organizado nos seguintes arquivos (normalmente em ordem alfabética):

```text
ATV8/
⤷ banco.py: realiza conexão com o MySQL e salva/consulta os cadastros
⤷ cadastro.py: inicia e carrega o estilo
⤷ cep.py: faz a consulta da API
⤷ estilo.css: tem a aparência
⤷ janela.py: a janela com as interações
⤷ README.md: passo a passo do funcionamento do sistema
⤷ SQL.sql: código para a tabela no MySQL
⤷ tabela.py: tabela para consulta dos cadastros
⤷ validacoes.py: validações de cada dado

```

# ▶️ Passo a passo para executar

## 1. Configurar o banco de dados

Primeiro, abra o **MySQL Workbench**.

Abra o arquivo `SQL.sql` que está na pasta do projeto e copie todo o código que está escrito nele e cole no MySQL Workbench.
Depois, execute o código para criar o banco de dados e a tabela necessários para o funcionamento do sistema.

---

## 2. Abrir o projeto

Depois de configurar o banco de dados, abra a pasta `ATV8` no **Visual Studio Code**.

Abra um **terminal integrado** dentro da pasta `ATV8`.

---

## 3. Criar o ambiente virtual

No terminal, digite:

```powershell
python -m venv venv
venv\Scripts\Activate
pip install PySide6
pip install mysql-connector-python

```

```text
**!IMPORTANTE: no banco.py, em conectar() coloque o usuário e senha do seu MySQL

Por fim, para executar a janela, digite:

'''powershell
python cadastro.py

**Pronto! Aproveite o sistema! 🍦💗