from isPalindromic import isPalindromic


def test_isPalindromic_correct1():
    x = isPalindromic(121)
    assert x == True


def test_isPalindromic_correct2():
    x = isPalindromic(33333)
    assert x == True


def test_isPalindromic_correct3():
    x = isPalindromic(20022002)
    assert x == True


def test_isPalindromic_correct4():
    x = isPalindromic(444)
    assert x == True


def test_isPalindromic_correct5():
    x = isPalindromic(11)
    assert x == True


def test_isPalindromic_false1():
    x = isPalindromic(123)
    assert x == False


def test_isPalindromic_false2():
    x = isPalindromic(49020)
    assert x == False


def test_isPalindromic_false3():
    x = isPalindromic(121389479)
    assert x == False


def test_isPalindromic_false4():
    x = isPalindromic(4444445)
    assert x == False


def test_isPalindromic_false5():
    x = isPalindromic(940230)
    assert x == False
