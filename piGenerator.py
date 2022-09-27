import requests

def piGenerator(start, length):
    startPlace = start
    remainingDigits = length
    while remainingDigits > 0:
        sizeOfDigits = min(remainingDigits, 1000)
        request = requests.get(f'https://api.pi.delivery/v1/pi?start={startPlace}&numberOfDigits={sizeOfDigits}')
        for i in request.json()['content']:
            yield int(i)
        startPlace += sizeOfDigits
        remainingDigits -= sizeOfDigits
