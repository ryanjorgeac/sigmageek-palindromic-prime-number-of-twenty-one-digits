import piGenerator


def test_piGenerator_10_digits():
    x = piGenerator.piGenerator(0, 10)
    y = list(x)
    assert len(y) == 10

def test_piGenerator_more_than_1000_digits():
    x = piGenerator.piGenerator(0, 1050)
    y = list(x)
    assert len(y) == 1050

def test_piGenerator_more_than_5000_digits():
    x = piGenerator.piGenerator(0, 5000)
    y = list(x)
    assert len(y) == 5000


if __name__ == "__main__":
    test_piGenerator_more_than_5000_digits()