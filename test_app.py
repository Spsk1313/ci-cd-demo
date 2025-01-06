import app
import numpy as np

def test_add():
    assert app.add(2, 3) == 5

def test_add_negative():
    assert app.add(-1, -2) == -3

def test_multiply():
    assert app.multiply(4, 4) == 16