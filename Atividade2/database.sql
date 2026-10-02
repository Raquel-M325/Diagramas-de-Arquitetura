CREATE TABLE IF NOT EXISTS Usuario (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    perfil TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    senha TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS Categoria (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    descricao TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS Projeto (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    descricao TEXT NOT NULL,
    data_criacao TEXT NOT NULL DEFAULT CURRENT_DATE,
    resumo TEXT NOT NULL,
    categoria_id INTEGER NOT NULL,
    orientador_id INTEGER NOT NULL,
    FOREIGN KEY (categoria_id) REFERENCES Categoria(id),
    FOREIGN KEY (orientador_id) REFERENCES Usuario(id)
);