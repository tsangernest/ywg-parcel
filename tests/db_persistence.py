from pydantic.networks import AnyUrl, UrlConstraints


class SqliteAsync(AnyUrl):
    _constraints = UrlConstraints(
        allowed_schemes=["sqlite", "sqlite+aiosqlite"],
        default_path="/:memory:",
    )


