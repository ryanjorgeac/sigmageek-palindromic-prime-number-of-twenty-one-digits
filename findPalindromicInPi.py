import piGenerator
import anyNumberOfDigitsGenerator
import isPrime
import isPalindromic
import time
from hasNDigits import hasNDigits
from Either import *

def findPalindromicInPi(start, end, numberOfDigits):
    generator = piGenerator.piGenerator(start, end)
    x = anyNumberOfDigitsGenerator.anyNumberOfDigitsGenerator(generator, numberOfDigits)
    i = start
    for number in x:
        if isPrime.isPrime(number) and hasNDigits(number, numberOfDigits) and isPalindromic.isPalindromic(number):
            return Right((number, i))
        i += 1
    return Left((start, end))
