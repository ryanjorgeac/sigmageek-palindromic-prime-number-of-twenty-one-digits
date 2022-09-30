import findPalindromicInPi

def test_findPalindromic_3Digits():
    x = findPalindromicInPi.findPalindromicInPi(0, 500, 3)
    assert x == (383, 25)

def test_findPalindromic_5Digits():
    x = findPalindromicInPi.findPalindromicInPi(0, 500, 5)
    assert x == (38183, 488)

def test_findPalindromic_7Digits():
    x = findPalindromicInPi.findPalindromicInPi(0, 100000, 7)
    assert x == (9149419, 13901)

def test_findPalindromic_9Digits():
    x = findPalindromicInPi.findPalindromicInPi(0, 150000, 9)
    assert x == (318272813, 129079)

