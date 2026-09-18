import re

def validar_nome(nome):
    return bool(nome.strip()) and all(
        letra.isalpha() or letra.isspace()
        for letra in nome
    )

def validar_cpf(documento):
    cpf = re.sub(r"\D", "", documento)

    # CPF precisa ter 11 números
    if len(cpf) != 11:
        return False
    
    # Impede números repetidos, como 11111111111
    if cpf == cpf[0] * 11:
        return False

    # Calcula o primeiro dígito verificador
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)

    resto = soma % 11
    if resto < 2:
        primeiro_digito = 0
    else:
        primeiro_digito = 11 - resto

    # Confere o primeiro dígito
    if primeiro_digito != int(cpf[9]):
        return False

    # Calcula o segundo dígito verificador
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)

    resto = soma % 11
    if resto < 2:
        segundo_digito = 0
    else:
        segundo_digito = 11 - resto

    # Confere o segundo dígito
    if segundo_digito != int(cpf[10]):
        return False
    return True

def validar_cnpj(documento):
    cnpj = re.sub(r"\D", "", documento)

    # CNPJ precisa ter 14 números
    if len(cnpj) != 14:
        return False

    # Impede números repetidos
    if cnpj == cnpj[0] * 14:
        return False

    # Pesos usados no primeiro dígito
    pesos_primeiro = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    soma = 0

    for i in range(12):
        soma += int(cnpj[i]) * pesos_primeiro[i]

    resto = soma % 11
    if resto < 2:
        primeiro_digito = 0
    else:
        primeiro_digito = 11 - resto

    # Confere o primeiro dígito
    if primeiro_digito != int(cnpj[12]):
        return False

    # Pesos usados no segundo dígito
    pesos_segundo = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    soma = 0

    for i in range(13):
        soma += int(cnpj[i]) * pesos_segundo[i]

    resto = soma % 11
    if resto < 2:
        segundo_digito = 0
    else:
        segundo_digito = 11 - resto

    # Confere o segundo dígito
    if segundo_digito != int(cnpj[13]):
        return False
    return True

def validar_documento(documento, tipo):
    if tipo == "CPF":
        return validar_cpf(documento)

    if tipo == "CNPJ":
        return validar_cnpj(documento)
    return False

def validar_email(email):
    return bool(
        re.match(
            r"^[\w\.-]+@[\w\.-]+\.\w+$",
            email
        )
    )

def validar_celular(celular):
    numeros = re.sub(r"\D", "", celular)

    # Telefone precisa ter 10 ou 11 números
    if len(numeros) not in (10, 11):
        return False

    # Impede números repetidos, como 99999999999
    if numeros == numeros[0] * len(numeros):
        return False

    # Os dois primeiros números são o DDD
    ddd = int(numeros[:2])

    # DDD precisa estar entre 11 e 99
    if ddd < 11 or ddd > 99:
        return False

    # Celular brasileiro possui 11 números e começa com o número 9 depois do DDD
    if len(numeros) == 11:
        if numeros[2] != "9":
            return False
    return True

def validar_cep(cep):
    numeros = re.sub(r"\D", "", cep)
    return len(numeros) == 8