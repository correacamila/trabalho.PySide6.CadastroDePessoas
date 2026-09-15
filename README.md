# Sistema de Cadastro de Pessoas

Sistema desktop desenvolvido em Python e PySide6 para realizar o cadastro de pessoas, com validação de informações, consulta automática de endereço pelo CEP e armazenamento dos dados em um banco de dados SQLite.

---

# 📋 O que é necessário para executar o projeto

Antes de executar o sistema, é necessário ter instalado:

- Python 3;
- Visual Studio Code (VS Code);
- Extensão Python no VS Code;
- Biblioteca PySide6;
- Biblioteca SQLAlchemy;
- Biblioteca ReportLab;
- Conexão com a internet para realizar a consulta de CEP.

O projeto utiliza a API ViaCEP para consultar os dados do endereço.

---

# 📁 Estrutura do projeto

O projeto está organizado nos seguintes arquivos:

```text
ATV8/

⤷ banco.py: realiza as operações de cadastro, consulta, atualização e exclusão no banco

⤷ cadastro.py: inicia o sistema

⤷ cep.py: faz a consulta da API ViaCEP

⤷ estilo.css: contém a aparência da aplicação

⤷ janela.py: contém a janela principal e as interações do formulário

⤷ modelos.py: configura o banco SQLite e a tabela de pessoas

⤷ pdf.py: gera o PDF com os cadastros

⤷ README.md: explica o funcionamento e a execução do sistema

⤷ tabela.py: exibe os cadastros em uma tabela

⤷ validacoes.py: contém as validações dos dados

⤷ cadastro_pessoas.db: banco de dados SQLite utilizado pelo sistema

---

# ▶️ Passo a passo para executar

## 1. Abrir o projeto

Primeiro, abra a pasta `ATV8` no **Visual Studio Code**.

Depois, abra um **terminal integrado** dentro da pasta do projeto.

---

## 2. Criar o ambiente virtual

No terminal, digite:

```powershell
python -m venv venv
```

Para ativar o ambiente virtual no Windows, digite:

```powershell
venv\Scripts\Activate
```

---

## 3. Instalar as bibliotecas

Com o ambiente virtual ativado, instale as bibliotecas necessárias:

```powershell
pip install PySide6
pip install SQLAlchemy
pip install reportlab
```

---

## 4. Executar o sistema

Para abrir a janela principal, digite:

```powershell
python cadastro.py
```

### Pronto! Aproveite o sistema! 🍦💗

---

# ✨ Funcionalidades

O sistema possui as seguintes funcionalidades:

- 👤 Cadastro de pessoas;
- 🪪 Escolha entre CPF e CNPJ;
- ✅ Validação de CPF e CNPJ;
- 📧 Validação do formato do e-mail;
- 📱 Validação e formatação automática do celular;
- 📍 Validação e formatação automática do CEP;
- 🔎 Consulta automática de endereço através do CEP;
- 🏠 Preenchimento automático de logradouro, bairro, cidade e estado;
- ⚠️ Mensagens de erro quando algum dado é inválido;
- 🎯 Direcionamento para o campo que precisa ser corrigido;
- 💾 Salvamento dos cadastros no banco de dados SQLite;
- 🧹 Botão para limpar os campos do formulário;
- 📋 Visualização dos cadastros realizados em uma tabela;
- 🔎 Barra de pesquisa para filtrar pessoas pelo nome;
- ✏️ Atualização dos dados de uma pessoa cadastrada;
- 🗑️ Exclusão de pessoas cadastradas;
- ❓ Confirmação antes de excluir um cadastro;
- 📄 Geração de PDF com os dados da tabela;
- 🎨 Interface gráfica personalizada com CSS/QSS.
