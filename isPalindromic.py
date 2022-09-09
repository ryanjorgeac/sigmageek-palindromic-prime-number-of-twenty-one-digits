
def isPalindromic(number: int) -> bool:
    strNumber = str(number)
    sizeStrNumber = len(strNumber)
    for i in range(sizeStrNumber//2):
        if strNumber[i] != strNumber[sizeStrNumber-1-i]:
            return False

    return True



