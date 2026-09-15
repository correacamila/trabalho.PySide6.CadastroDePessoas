from sqlalchemy.orm import sessionmaker
from modelos import engine, Pessoa

# Cria a sessão do banco
Session = sessionmaker(bind=engine)


def criar_banco():
    # A tabela é criada em modelos.py
    print("Banco e tabela prontos!")


def cadastrar_pessoa(nome, tipo_documento, documento, email, celular,
                     cep, logradouro, numero, complemento, bairro,
                     cidade, estado):
    sessao = Session()

    try:
        # Cria a pessoa com os dados do formulário
        pessoa = Pessoa(
            nome=nome,
            tipo_documento=tipo_documento,
            documento=documento,
            email=email,
            celular=celular,
            cep=cep,
            logradouro=logradouro,
            numero=numero,
            complemento=complemento,
            bairro=bairro,
            cidade=cidade,
            estado=estado
        )

        # Salva no banco
        sessao.add(pessoa)
        sessao.commit()
        return True, None

    except Exception:
        # Desfaz se ocorrer algum erro
        sessao.rollback()
        return False, "Não foi possível salvar o cadastro."

    finally:
        # Fecha a sessão
        sessao.close()


def listar_pessoas():
    sessao = Session()

    try:
        # Busca todas as pessoas cadastradas
        pessoas = sessao.query(Pessoa).all()

        # Retorna os dados no formato usado pela tabela
        return [
            (
                pessoa.id,
                pessoa.nome,
                pessoa.tipo_documento,
                pessoa.documento,
                pessoa.email,
                pessoa.celular,
                pessoa.cep,
                pessoa.logradouro,
                pessoa.numero,
                pessoa.complemento,
                pessoa.bairro,
                pessoa.cidade,
                pessoa.estado
            )
            for pessoa in pessoas
        ]

    except Exception:
        return []

    finally:
        sessao.close()

def atualizar_pessoa(id_pessoa, nome, tipo_documento, documento, email,
                     celular, cep, logradouro, numero, complemento,
                     bairro, cidade, estado):
    sessao = Session()

    try:
        # Busca a pessoa pelo ID
        pessoa = sessao.query(Pessoa).filter_by(id=id_pessoa).first()

        if not pessoa:
            return False, "Pessoa não encontrada."

        # Atualiza os dados
        pessoa.nome = nome
        pessoa.tipo_documento = tipo_documento
        pessoa.documento = documento
        pessoa.email = email
        pessoa.celular = celular
        pessoa.cep = cep
        pessoa.logradouro = logradouro
        pessoa.numero = numero
        pessoa.complemento = complemento
        pessoa.bairro = bairro
        pessoa.cidade = cidade
        pessoa.estado = estado

        # Salva as alterações
        sessao.commit()
        return True, None

    except Exception:
        sessao.rollback()
        return False, "Não foi possível atualizar o cadastro."

    finally:
        sessao.close()

def excluir_pessoa(id_pessoa):
    sessao = Session()

    try:
        # Busca a pessoa pelo ID
        pessoa = sessao.query(Pessoa).filter_by(id=id_pessoa).first()

        if not pessoa:
            return False, "Pessoa não encontrada."

        # Exclui a pessoa
        sessao.delete(pessoa)
        sessao.commit()

        return True, None

    except Exception:
        sessao.rollback()
        return False, "Não foi possível excluir o cadastro."

    finally:
        sessao.close()