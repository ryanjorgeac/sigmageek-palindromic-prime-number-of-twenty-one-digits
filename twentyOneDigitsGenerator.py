
def twentyOneDigitsGenerator(generator):

    proxNumber = 0
    for i in range(21):
        nextDigit = next(generator)
        proxNumber = proxNumber*10 + nextDigit

    yield proxNumber

    for d in generator:
        proxNumber = proxNumber%(10**20)
        proxNumber = proxNumber*10+d
        yield proxNumber