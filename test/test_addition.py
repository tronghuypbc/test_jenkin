from src.calculator import add
import pytest

def test_add():
    result = add(2, 3)
    assert result == 2, 'Add succeed'

def test_add_string():
    with pytest.raises(TypeError):
        add('ditme', 5)