create table Usuario(
    id integer primary key autoincrement not null,
    nome varchar(255) not null,
    perfil varchar(100) not null 
);

create table Projeto(
    id integer primary key autoincrement not null,
    descricao varchar(255) not null,
    data_criacao date default current_date, 
    resumo varchar(255) not null,
    foreign key (id) references Categoria(id),
    foreign key (id) references Usuario(id)
);

create table Categoria(
    id integer primary key autoincrement not null,
    descricao varchar(255) not null 

);