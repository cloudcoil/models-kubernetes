import pytest


def test_import():
    try:
        import cloudcoil.models.kubernetes as kubernetes
    except Exception as e:
        pytest.fail(f"Unexpected error: {e}")