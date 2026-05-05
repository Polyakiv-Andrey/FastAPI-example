from src.config.auth import AuthSettings


def test_auth_settings_structure():
    annotations = AuthSettings.__annotations__
    expected_structure = {
        "JWT_SECRET_KEY": str,
        "JWT_ALGORITHM": str,
        "ACCESS_TOKEN_EXPIRE_MINUTES": int,
        "REFRESH_TOKEN_EXPIRE_DAYS": int,
    }

    assert annotations == expected_structure

    for field, expected_type in expected_structure.items():
        assert annotations[field] is expected_type

    settings = AuthSettings(JWT_SECRET_KEY="test", _env_file=None)

    assert settings.JWT_ALGORITHM == "HS256"
    assert settings.ACCESS_TOKEN_EXPIRE_MINUTES == 30
    assert settings.REFRESH_TOKEN_EXPIRE_DAYS == 30
