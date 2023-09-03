import pytest
import kaprekar as k


def test_kaprekar():
    assert k.kaprekar(1234) == 3


def test_kaprekar_6174():
    assert k.kaprekar(6174) == 0


def test_kaprekar_1111():
    assert k.kaprekar(1111) is None


def test_kaprekar_0000():
    assert k.kaprekar(0000) is None
