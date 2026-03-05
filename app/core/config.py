from pydantic import PostgresDsn, computed_field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    @computed_field
    @property
    def SQLALCHEMY_DATABASE_URI(self) -> PostgresDsn:
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


settings = Settings()

