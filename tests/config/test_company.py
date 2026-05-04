from src.config.company import CompanySettings


def test_company_settings_structure():
    annotations = CompanySettings.__annotations__
    expected_fields = {"company_name": str}
    assert annotations == expected_fields
    for field, expected_type in expected_fields.items():
        assert annotations[field] == expected_type


def test_company_settings_default_values():
    settings = CompanySettings()
    assert settings.company_name == "Test Company"
