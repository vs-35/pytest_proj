import pytest
from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([1, 3, 5, 7], -1, "test") != "default"
    assert arrs.get([1, 2, 3, 4], 3, "test") == 4


def test_get_empt_list():
    with pytest.raises(IndexError):
        arrs.get([], 0, "test")


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([], 1) == []
    assert arrs.my_slice([1, 2, 3], -5) == [1, 2, 3]
    assert arrs.my_slice([1, 2, 3], -2) == [2, 3]

def test_slise_NameError():
    with pytest.raises(NameError):
        arrs.my_slice(([1, 2, 3], a, b))
