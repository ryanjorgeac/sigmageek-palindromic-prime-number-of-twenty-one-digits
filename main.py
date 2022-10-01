import hasNDigits
import piGenerator
from isPalindromic import isPalindromic
from isPrime import isPrime
from anyNumberOfDigitsGenerator import anyNumberOfDigitsGenerator
import requests
import time
import os
from poolArgsGenerator import poolArgsGenerator
from findPalindromicInPi import findPalindromicInPi

NUMBER_OF_DIGITS = ''

if __name__ == "__main__":
    argsGenerator = poolArgsGenerator(numberOfDigits=21)
    findPalindromicInPi(next(argsGenerator))



