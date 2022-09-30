from hasNDigits import hasNDigits

def anyNumberOfDigitsGenerator(piGenerator, numberOfDigits):

    proxNumber = 0
    for i in range(numberOfDigits):
        nextDigit = next(piGenerator)
        proxNumber = proxNumber * 10 + nextDigit

    if hasNDigits(proxNumber, numberOfDigits):
        yield proxNumber

    for d in piGenerator:
        proxNumber = proxNumber % (10 ** (numberOfDigits-1))
        proxNumber = proxNumber * 10 + d
        yield proxNumber


