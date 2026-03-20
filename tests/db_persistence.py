from pydantic import networks


class SqliteAsync(networks.AnyUrl):
    _constraints = networks.UrlConstraints(
        allowed_schemes=["sqlite", "sqlite+aiosqlite"],
        default_path="/:memory:",
    )


