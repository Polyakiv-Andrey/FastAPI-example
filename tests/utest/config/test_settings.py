from pydantic import SecretStr

from src.config.auth import AuthSettings
from src.config.company import CompanySettings
from src.config.db import DatabaseSettings
from src.config.logging import LoggerSettings
from src.config.sand_grid import SandGridSettings
from src.config.settings import Settings


def test_settings_structure():
    annotation = Settings.__annotations__
    expected_structure = {
        "API_V1_STR": str,
        "SECRET_KEY": SecretStr,
        "DEBUG": bool,
        "db": DatabaseSettings,
        "send_grid": SandGridSettings,
        "company": CompanySettings,
        "auth": AuthSettings,
        "logger": LoggerSettings,
    }
    assert annotation == expected_structure
    for field, expected_type in expected_structure.items():
        assert annotation[field] == expected_type
