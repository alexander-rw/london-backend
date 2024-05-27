from python_src.add import add
import pytest

@pytest.mark.unit
def test_addition():
    assert add(1, 2) == 3
