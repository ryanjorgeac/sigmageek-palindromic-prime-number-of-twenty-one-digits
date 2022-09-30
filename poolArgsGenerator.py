
def poolArgsGenerator(numberOfDigits: int) -> tuple:
    numberOfDigits = numberOfDigits
    startNumbers = 0
    endNumbers = 120000

    yield (startNumbers, endNumbers, numberOfDigits)

    while True:
        startNumbers = endNumbers - numberOfDigits + 1
        endNumbers += 100000
        yield (startNumbers, endNumbers, numberOfDigits)