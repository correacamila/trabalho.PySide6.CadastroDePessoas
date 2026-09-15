from pathlib import Path
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base

# Define onde o banco será salvo
CAMINHO_BANCO = Path(__file__).resolve().parent / "cadastro_pessoas.db"

# Conecta ao SQLite
engine = create_engine(f"sqlite:///{CAMINHO_BANCO}")
Base = declarative_base()

# Define a tabela pessoas
class Pessoa(Base):
    __tablename__ = "pessoas"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    tipo_documento = Column(String(5), nullable=False)
    documento = Column(String(18), nullable=False)
    email = Column(String(100), nullable=False)
    celular = Column(String(20), nullable=False)
    cep = Column(String(9), nullable=False)
    logradouro = Column(String(150), nullable=False)
    numero = Column(String(10), nullable=False)
    complemento = Column(String(100))
    bairro = Column(String(100), nullable=False)
    cidade = Column(String(100), nullable=False)
    estado = Column(String(2), nullable=False)

# Cria a tabela caso ela ainda não exista
Base.metadata.create_all(engine)