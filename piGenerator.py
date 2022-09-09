import requests

def piGenerator():
    request = requests.get('https://api.pi.delivery/v1/pi?start=0&numberOfDigits=1000')
    return request.json()['content']

# print(piGenerator()[:21])


        