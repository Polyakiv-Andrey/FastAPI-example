from src.config.logging import LoggerSettings


def test_loging_settings_structure():
    annotation = LoggerSettings.__annotations__
    expected_structure = {
        "LOKI_URL": str,
        "LEVEL": str,
        "APP_NAME": str,
        "ENV": str,
    }

    assert annotation == expected_structure
    for field, expected_type in expected_structure.items():
        assert annotation[field] is expected_type
