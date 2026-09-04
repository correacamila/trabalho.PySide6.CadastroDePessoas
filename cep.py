import json
from urllib.request import urlopen
# importa o urlopen, que permite abrir um endereço da internet e fazer uma requisição para a API.
from urllib.error import HTTPError, URLError
# importa dois tipos de erro que podem acontecer durante a consulta

def consultar_cep(cep):
    # cria a função que será responsável por consultar um CEP (cep)
    try:
        # tenta executar o código abaixo.
        with urlopen(f"https://viacep.com.br/ws/{cep}/json/", timeout=5) as resposta:
            dados = json.loads(resposta.read().decode("utf-8"))
            # lê a resposta enviada pela API.
            # decode("utf-8") transforma os dados recebidos em texto.
            # json.loads() transforma o JSON em um dicionário Python

        if dados.get("erro"):
            # verifica se a API informou que o CEP não existe, o .get("erro") procura pela informação "erro" dentro dos dados e se existir e estiver indicando erro, entramos nesse if.
            return None, "CEP não encontrado."

        return dados, None
        # se não aconteceu nenhum erro, devolve as informações
    except HTTPError:
        # executa esta parte caso aconteça um erro HTTP.
        return None, "O serviço de CEP apresentou um erro."
        # não encerra o programa, apenas devolve uma mensagem explicando o problema.
    except URLError:
        # executa esta parte quando existe algum problema de conexão.
        return None, "Não foi possível consultar o CEP. Verifique sua conexão com a internet."
    except Exception:
        # captura outros erros inesperados que não foram tratados anteriormente.
        return None, "Não foi possível realizar a consulta do CEP."