import re

def validar_cpf(cpf):
    cpf = re.sub(r"\D", "", cpf)

    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    numeros = [int(numero) for numero in cpf]

    soma = 0
    for i in range(9):
        soma += numeros[i] * (10 - i)

    resto = soma % 11
    digito1 = 0 if resto < 2 else 11 - resto

    soma = 0
    for i in range(10):
        soma += numeros[i] * (11 - i)

    resto = soma % 11
    digito2 = 0 if resto < 2 else 11 - resto

    return numeros[9] == digito1 and numeros[10] == digito2


def validar_cnpj(cnpj):
    cnpj = re.sub(r"\D", "", cnpj)

    if len(cnpj) != 14 or cnpj == cnpj[0] * 14:
        return False

    numeros = [int(numero) for numero in cnpj]

    pesos = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    soma = 0

    for i in range(12):
        soma += numeros[i] * pesos[i]

    resto = soma % 11
    digito1 = 0 if resto < 2 else 11 - resto

    pesos = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    soma = 0

    for i in range(13):
        soma += numeros[i] * pesos[i]

    resto = soma % 11
    digito2 = 0 if resto < 2 else 11 - resto

    return numeros[12] == digito1 and numeros[13] == digito2


def validar_email(email):
    return re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", email) is not None
    # traduzindo: retorne uma regra padrão, tipo (deixe a expressão regular da seguinte forma "a partir daqui[não pode @ e nem \s(espaço em branco)] + @ obrigatório[] + . obrigatório[] + acabou a frase", variável email) retorne se estiver tudo correto.

def validar_celular(celular):
    celular = re.sub(r"\D", "", celular)
    # traduzindo: pegue o celular e remova tudo o que não for número
    return len(celular) in (10, 11)
    # conte quantos elementos são e verifique se sobraram 10 ou 11 números.

def validar_cep(cep):
    cep = re.sub(r"\D", "", cep)
    # remova o que não for número
    return len(cep) == 8
    # retorne uma conta de quantos elementos tem se for = a 8

def validar_nome(nome):
    return len(nome.strip().split()) >= 2
    # retorne contagem das partes (em nome.retire espaços em branco do começo e final().separe em partes()) se for maior ou igual a 2 (nome completo)