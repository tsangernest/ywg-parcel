from functools import lru_cache
from pydantic import MariaDBDsn, PostgresDsn, computed_field
from pydantic_settings import BaseSettings

from tests.db_persistence import SqliteAsync


@lru_cache
class Settings(BaseSettings):
    @computed_field
    @property
    def SQLALCHEMY_DB_URI(self) -> PostgresDsn:
        """
        * I can't say I'm a fan of this pydantic setup.
        * 'host' parameter actually means the name of the docker compose.
           service or use the container_name (i.e., 'db' or 'postgresql')
        * 'path' parameter is the name of the db server.
        * IMO, it might be easier to use the raw string (i.e., using the
           connection string for datagrip.
        """
        return PostgresDsn.build(
            scheme="postgresql+psycopg",
            username="ywgparceluser",
            password="ywgparcelpass",
            host="postgresql",
            port=5432,
            path="ywgparcel",
        )

    @computed_field
    @property
    def SQLITE_DB_URI(self) -> SqliteAsync:
        """
        * Just wanted to integrate an async sqlite to pydantic network
        """
        return SqliteAsync.build(
            scheme="sqlite+aiosqlite",
            host="",
        )

    # @computed_field
    @property
    def SQL_MARIADB_URI(self):
        """
        *  Wanted to integrate an async mariadb to pydantic network
        """
        return f"mariadb+aiomysql://ywgparceluser:ywgparcelpass@mysql:3306"


settings = Settings()

