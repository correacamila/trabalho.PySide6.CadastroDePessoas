import re

# Valida o nome
def validar_nome(nome):
    return bool(nome.strip()) and all(
        letra.isalpha() or letra.isspace()
        for letra in nome
    )
# Valida CPF ou CNPJ
def validar_documento(documento, tipo):
    numeros = re.sub(r"\D", "", documento)

    if tipo == "CPF":
        return len(numeros) == 11

    if tipo == "CNPJ":
        return len(numeros) == 14

    return False

# Valida CPF
def validar_cpf(documento):
    return validar_documento(documento, "CPF")


# Valida CNPJ
def validar_cnpj(documento):
    return validar_documento(documento, "CNPJ")

# Valida o e-mail
def validar_email(email):
    return bool(
        re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email)
    )

# Valida o celular
def validar_celular(celular):
    numeros = re.sub(r"\D", "", celular)
    return len(numeros) in (10, 11)

# Valida o CEP
def validar_cep(cep):
    numeros = re.sub(r"\D", "", cep)
    return len(numeros) == 8