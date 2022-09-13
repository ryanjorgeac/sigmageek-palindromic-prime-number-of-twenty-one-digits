import requests

def piGenerator():
    startPlace = 1000000
    while True:
        request = requests.get('https://api.pi.delivery/v1/pi?start={}&numberOfDigits=1000'.format(startPlace))
        yield request.json()['content']
        startPlace = startPlace + 1000


# for i in range(2):
#     print(next(piGenerator()))