CREATE DATABASE cadastro_pessoas;
USE cadastro_pessoas;

CREATE TABLE pessoas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    tipo_documento VARCHAR(5) NOT NULL,
    documento VARCHAR(18) NOT NULL,
    email VARCHAR(100) NOT NULL,
    celular VARCHAR(20) NOT NULL,
    cep VARCHAR(9) NOT NULL,
    logradouro VARCHAR(150) NOT NULL,
    numero VARCHAR(10) NOT NULL,
    complemento VARCHAR(100),
    bairro VARCHAR(100) NOT NULL,
    cidade VARCHAR(100) NOT NULL,
    estado VARCHAR(2) NOT NULL
);

SHOW TABLES;
SELECT * FROM pessoas;