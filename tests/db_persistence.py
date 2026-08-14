from pydantic.networks import AnyUrl, MariaDBDsn, UrlConstraints


class SqliteAsync(AnyUrl):
    _constraints = UrlConstraints(
        allowed_schemes=["sqlite", "sqlite+aiosqlite"],
        default_path="/:memory:",
    )


class MariaDBAsync(MariaDBDsn):
        (MariaDBDsn
         ._constraints
         .allowed_schemes
         .append("mariadb+aiomysql"))

