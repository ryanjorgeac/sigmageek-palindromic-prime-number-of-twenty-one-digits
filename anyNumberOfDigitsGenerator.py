
def anyNumberOfDigitsGenerator(piGenerator, numberOfDigits):

    proxNumber = 0
    for i in range(numberOfDigits):
        nextDigit = next(piGenerator)
        proxNumber = proxNumber * 10 + nextDigit
        while proxNumber == 0:
            nextDigit = next(piGenerator)
            proxNumber = proxNumber * 10 + nextDigit

    yield proxNumber

    for d in piGenerator:
        proxNumber = proxNumber % (10 ** (numberOfDigits-1))
        proxNumber = proxNumber * 10 + d
        if proxNumber % (10 ** (numberOfDigits-1)) == proxNumber:
            continue

        yield proxNumber

