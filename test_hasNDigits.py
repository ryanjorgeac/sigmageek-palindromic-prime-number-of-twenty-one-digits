import hasNDigits

def test_has1Digits():
    number = 5
    numberOfDigits = 1
    x = hasNDigits.hasNDigits(number, numberOfDigits)
    assert x

def test_has2Digits():
    number = 10
    numberOfDigits = 2
    x = hasNDigits.hasNDigits(number, numberOfDigits)
    assert x

def test_has3Digits():
    number = 920
    numberOfDigits = 3
    x = hasNDigits.hasNDigits(number, numberOfDigits)
    assert x

def test_has5Digits():
    number = 10000
    numberOfDigits = 5
    x = hasNDigits.hasNDigits(number, numberOfDigits)
    assert x

def test_has6Digits():
    number = 100000
    numberOfDigits = 6
    x = hasNDigits.hasNDigits(number, numberOfDigits)
    assert x