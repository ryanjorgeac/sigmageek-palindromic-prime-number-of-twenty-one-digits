
def iterator(start, numberOfDigits):
    startPlace = start
    while True:
        yield tuple((startPlace, numberOfDigits))
        startPlace += numberOfDigits