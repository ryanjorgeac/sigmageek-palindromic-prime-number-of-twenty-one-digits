from digitsSequenceIterator import iterator

def test_digitsSequenceIterator1():
    x = iterator(0, 1000000)
    y = next(x)
    assert y == (0, 1000000)

def test_digitsSequenceIterator2():
    x = iterator(0, 1000000)
    y = next(x)
    z = next(x)
    assert z == (1000000, 1000000)

def test_digitsSequenceIterator3():
    x = iterator(0, 1000000)
    y = next(x)
    z = next(x)
    w = next(x)
    assert w == (2000000, 1000000)

if __name__ == "__main__":
    test_digitsSequenceIterator2()