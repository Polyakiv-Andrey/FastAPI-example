from pydantic import SecretStr

from src.config.db import DatabaseSettings


def test_db_settings_structure():
    annotations = DatabaseSettings.__annotations__
    expected_structure = {
        "DB_NAME": str,
        "DB_USER": str,
        "DB_PASS": SecretStr,
        "DB_HOST": str,
        "DB_PORT": int,
    }
    assert annotations == expected_structure
    for field, expected_type in expected_structure.items():
        actual_type = annotations[field]
        assert actual_type is expected_type


def test_database_url(monkeypatch):
    monkeypatch.setenv("DB_NAME", "postgres")
    monkeypatch.setenv("DB_USER", "user")
    monkeypatch.setenv("DB_PASS", "password")
    monkeypatch.setenv("DB_HOST", "localhost")
    monkeypatch.setenv("DB_PORT", "5432")

    settings = DatabaseSettings(_env_file=None)
    assert settings.database_url == "postgresql+asyncpg://user:password@localhost:5432/postgres"
