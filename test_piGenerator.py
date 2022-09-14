import piGenerator


def test_piGenerator1():
    x = piGenerator.piGenerator(0)
    y = x.__next__()
    assert y == 3

def test_piGenerator2():
    x = piGenerator.piGenerator(0)
    y = 0
    for i in range(4):
        y += x.__next__()
    assert y == 9


if __name__ == "__main__":
    test_piGenerator2()