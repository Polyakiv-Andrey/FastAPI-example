from src.config.sand_grid import SandGridSettings


def test_sand_grid_structure():
    annotation = SandGridSettings.__annotations__
    expected_structure = {"SEND_GRID_API_KEY": str, "SEND_GRID_FROM_EMAIL": str}
    assert annotation == expected_structure
    for field, expected_type in expected_structure.items():
        assert annotation[field] == expected_type
