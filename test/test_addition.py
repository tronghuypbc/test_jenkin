from src.calculator import add, subtract
import pytest

def test_add():
    result = add(2, 3)
    assert result == 5, 'Add succeed'

def test_subtract():
    result = subtract(3, 1)
    assert result == 2

def test_add_string():
    with pytest.raises(TypeError):
        add('ditme', 5)