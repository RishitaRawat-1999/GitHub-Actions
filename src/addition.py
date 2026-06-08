# app.py
# This is a test commit
# Forked Branch for testing Github Actions
def add(a, b):
    return a + b

def test_add():
    assert add(1, 2) == 3
    assert add(1, -1) == 0

#Added substration
def sub(c, d):
    return c - d

def test_sub():
    assert sub(5, 2) == 3
