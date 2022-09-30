import hasNDigits
import piGenerator
from isPalindromic import isPalindromic
from isPrime import isPrime
from anyNumberOfDigitsGenerator import anyNumberOfDigitsGenerator
import requests
import time

if __name__ == "__main__":
    generator = piGenerator.piGenerator(0, 1000000)
    x = anyNumberOfDigitsGenerator(generator, 6)
    i = 0
    time1 = time.perf_counter()
    for number in x:
        if number % 2 != 0:
            if number % 5 != 0:
                if hasNDigits.hasNDigits(number, 6) and isPalindromic(number) and isPrime(number):
                    print("Palindromic and prime Founder: ", number, "and it's position:: ", i)
                    print("Time took: ", time.perf_counter() - time1)
                    break
        elif i == 1000000:
            print(number, "posição: ", i)
            break
        # print(number, "posição: ", i)
        i += 1


