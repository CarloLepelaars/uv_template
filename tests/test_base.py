import pytest
from template.base import add

def test_base():
    assert add(2, 3) == 5