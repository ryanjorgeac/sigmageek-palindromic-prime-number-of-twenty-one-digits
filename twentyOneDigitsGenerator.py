

def twentyOneDigitsGenerator(piGenerator):

    proxNumber = int(piGenerator[:21])

    yield proxNumber

    for digitString in piGenerator[21:]:
        proxNumber = proxNumber%(10**20)
        proxNumber = proxNumber*10+int(digitString)
        yield proxNumber

