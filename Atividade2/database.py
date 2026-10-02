from __future__ import annotations

import os
import sqlite3
from abc import ABC, abstractmethod
from contextlib import contextmanager
from pathlib import Path
from typing import Iterator, Sequence


DEFAULT_DATABASE_PATH = Path(__file__).resolve().parent / "data" / "atividade2.db"
DEFAULT_SCHEMA_PATH = Path(__file__).resolve().parent / "database.sql"


class Database(ABC):
 
    @abstractmethod
    def initialize(self) -> None:
        """Cria ou atualiza as tabelas do banco."""

    @abstractmethod
    def execute(
        self, sql: str, parameters: Sequence[object] = ()
    ) -> sqlite3.Cursor:
        """Executa uma instrução parametrizada."""

    @abstractmethod
    def close(self) -> None:
        """Libera os recursos do banco."""


class SQLiteDatabase(Database):
    def __init__(
        self,
        database_path: Path | str | None = None,
        schema_path: Path | str | None = None,
    ) -> None:
        configured_path = os.getenv("DATABASE_PATH")
        self.database_path = Path(
            database_path or configured_path or DEFAULT_DATABASE_PATH
        ).expanduser()
        self.schema_path = Path(schema_path or DEFAULT_SCHEMA_PATH)
        self._connection: sqlite3.Connection | None = None

    def _get_connection(self) -> sqlite3.Connection:
        if self._connection is None:
            self.database_path.parent.mkdir(parents=True, exist_ok=True)
            self._connection = sqlite3.connect(self.database_path)
            self._connection.row_factory = sqlite3.Row
            self._connection.execute("PRAGMA foreign_keys = ON")
        return self._connection

    @contextmanager
    def connection(self) -> Iterator[sqlite3.Connection]:
        connection = self._get_connection()
        try:
            yield connection
            connection.commit()
        except Exception:
            connection.rollback()
            raise

    def initialize(self) -> None:
        schema = self.schema_path.read_text(encoding="utf-8")
        with self.connection() as connection:
            connection.executescript(schema)

    def execute(
        self, sql: str, parameters: Sequence[object] = ()
    ) -> sqlite3.Cursor:
        connection = self._get_connection()
        return connection.execute(sql, parameters)

    def close(self) -> None:
        if self._connection is not None:
            self._connection.close()
            self._connection = None

    def __enter__(self) -> SQLiteDatabase:
        return self

    def __exit__(self, exc_type: object, exc_value: object, traceback: object) -> None:
        self.close()


def create_database() -> SQLiteDatabase:
    return SQLiteDatabase()


if __name__ == "__main__":
    with create_database() as database:
        database.initialize()
        print(f"Banco SQLite inicializado em: {database.database_path}")


#quando forem usar, façam assim:

# from database import create_database

# with create_database() as database:
#     database.initialize()

#     with database.connection() as connection:
#         connection.execute(
#             """
#             INSERT INTO Categoria (descricao)
#             VALUES (?)
#             """,
#             ("Alguam categria",),
#         )