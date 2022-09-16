import requests

def piGenerator(start):
    startPlace = start
    while True:
        request = requests.get(f'https://api.pi.delivery/v1/pi?start={startPlace}&numberOfDigits=1000')
        for i in request.json()['content']:
            yield int(i)
        startPlace = startPlace + 1000