import pytest

from applications.countexercise import countexercise

def test_count_zeros():
    assert countexercise([0,0,0],0)==3

#print(count.count([0,0,0],0))