from poolArgsGenerator import poolArgsGenerator

def test_poolArgsGenerator_1():
    x = poolArgsGenerator(5)
    y = next(x)
    assert y == (0, 1000000, 5)

def test_poolArgsGenerator_2():
    x = poolArgsGenerator(5)
    y = next(x)
    z = next(x)
    assert z == (999996, 2000000, 5)

def test_poolArgsGenerator_3():
    x = poolArgsGenerator(9)
    y = next(x)
    z = next(x)
    assert z == (999992, 2000000, 9)

def test_poolArgsGenerator_using_for():
    x = poolArgsGenerator(21)
    y = ()
    for i in range(3):
        y = next(x)

    assert y == (1999980, 3000000, 21)

if __name__ == "__main__":
    test_poolArgsGenerator_using_for()