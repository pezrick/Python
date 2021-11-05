import pytest

from applications import counts

def test_count_zeros():
    assert counts.count([0,0,0], 0) == 3

def test_count_string():
    assert counts.count(["a","a","a"], "a") == 3