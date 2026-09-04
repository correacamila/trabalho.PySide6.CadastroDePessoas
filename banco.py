import mysql.connector
from mysql.connector import Error

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="atv8",
        password="SenhaAtv8",
        database="cadastro_pessoas"
    )

def cadastrar_pessoa(nome, tipo_documento, documento, email, celular, cep, logradouro, numero, complemento, bairro, cidade, estado):
    conexao = None
    cursor = None
    try:
        # tenta conectar ao banco e criar o cursor
        conexao = conectar()
        cursor = conexao.cursor()

        # comando SQL para inserir os dados da pessoa
        sql = """
        INSERT INTO pessoas
        (nome, tipo_documento, documento, email, celular, cep, logradouro, numero, complemento, bairro, cidade, estado)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        # valores que serão enviados para o banco
        valores = (nome, tipo_documento, documento, email, celular, cep, logradouro, numero, complemento, bairro, cidade, estado)

        cursor.execute(sql, valores)
        conexao.commit()

        # informa que o cadastro foi realizado
        return True, None

    except Error:
        # mostra uma mensagem caso aconteça algum erro no banco
        return False, "Não foi possível salvar o cadastro. Verifique a conexão com o banco de dados."

    finally:
        # fecha o cursor e a conexão com o banco
        if cursor:
            cursor.close()

        if conexao and conexao.is_connected():
            conexao.close()

def listar_pessoas():
    conexao = None
    cursor = None

    try:
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM pessoas")
        pessoas = cursor.fetchall()

        return pessoas

    except Error:
        return []

    finally:
        if cursor:
            cursor.close()

        if conexao and conexao.is_connected():
            conexao.close()