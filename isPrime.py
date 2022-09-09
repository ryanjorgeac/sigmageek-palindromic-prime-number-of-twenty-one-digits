from math import sqrt

def isPrime(number: int) -> bool:
    prime = False
    if number > 1:
        prime = True
        for i in range(2, int(sqrt(number)) + 1):
            if number % i == 0:
                prime = False
                break

    return prime
