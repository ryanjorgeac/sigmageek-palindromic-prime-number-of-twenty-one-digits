from isPrime import isPrime

def test_isPrime_correct1():
    x = isPrime(13)
    assert x == True

def test_isPrime_correct2():
    x = isPrime(97)
    assert x == True

def test_isPrime_correct3():
    x = isPrime(179)
    assert x == True
    
def test_isPrime_correct4():
    x = isPrime(1381)
    assert x == True

def test_isPrime_correct5():
    x = isPrime(7919)
    assert x == True


def test_isPrime_false1():
    x = isPrime(15)
    assert x == False

def test_isPrime_false2():
    x = isPrime(1)
    assert x == False

def test_isPrime_false3():
    x = isPrime(5000)
    assert x == False

def test_isPrime_false4():
    x = isPrime(14)
    assert x == False

def test_isPrime_false5():
    x = isPrime(201002)
    assert x == False