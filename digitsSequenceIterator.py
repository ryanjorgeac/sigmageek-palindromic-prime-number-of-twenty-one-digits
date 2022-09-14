
def iterator(start, numberOfDigits):
    startPlace = start
    while True:
        yield (startPlace, numberOfDigits)
        startPlace += numberOfDigits