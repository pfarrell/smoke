import random
from string import ascii_lowercase, ascii_uppercase, digits, punctuation, ascii_letters

import pytest

from main import _lcase, _ucase, _num, _punc, _alpha

random.seed = 1

@pytest.mark.repeat(25)
def test_lcase():
    assert _lcase() in ascii_lowercase


def test_dist_lcase():
    d = {}
    for i in range(300):
        c = _lcase()
        if not d.get(c):
            d[c] = 1
        else:
            d[c] = d[c] + 1
    assert len(d.keys()) == 26


@pytest.mark.repeat(25)
def test_ucase():
    assert _ucase() in ascii_uppercase


def test_dist_ucase():
    d = {}
    for i in range(300):
        c = _ucase()
        if not d.get(c):
            d[c] = 1
        else:
            d[c] = d[c] + 1
    assert len(d.keys()) == 26


@pytest.mark.repeat(25)
def test_num():
    assert _num() in digits


def test_dist_num():
    d = {}
    for i in range(100):
        c = _num()
        if not d.get(c):
            d[c] = 1
        else:
            d[c] = d[c] + 1
    assert len(d.keys()) == 10


@pytest.mark.repeat(25)
def test_punc():
    assert _punc() in punctuation


def test_dist_punc():
    d = {}
    for i in range(300):
        c = _punc()
        if not d.get(c):
            d[c] = 1
        else:
            d[c] = d[c] + 1
    assert len(d.keys()) == 32


@pytest.mark.repeat(25)
def test_alpha():
    assert _alpha() in ascii_letters


def test_dist_alpha():
    d = {}
    for i in range(500):
        c = _alpha()
        if not d.get(c):
            d[c] = 1
        else:
            d[c] = d[c] + 1
    assert len(d.keys()) == 52
