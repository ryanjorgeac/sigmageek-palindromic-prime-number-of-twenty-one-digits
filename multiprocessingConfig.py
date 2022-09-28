import multiprocessing
from multiprocessing import Pool
import time
import isPalindromic
import isPrime
from hasNDigits import hasNDigits
import piGenerator
import anyNumberOfDigitsGenerator


def findPalindromicInPi(start, end, numberOfDigits):
    generator = piGenerator.piGenerator(start, end)
    x = anyNumberOfDigitsGenerator.anyNumberOfDigitsGenerator(generator, numberOfDigits)
    i = start
    for number in x:
        assert hasNDigits(number, numberOfDigits)
        if isPrime.isPrime(number) and isPalindromic.isPalindromic(number):
            print("Palindromic and prime found: ", number, " and your position::: ", i)
            break
        i += 1


if __name__ == "__main__":
    start = time.perf_counter()
    with Pool() as p:
        # use the apply function
        pass

    p1 = multiprocessing.Process(target=findPalindromicInPi, args=(0, 100000, 5))
    p2 = multiprocessing.Process(target=findPalindromicInPi, args=(100000, 200000, 5))
    p3 = multiprocessing.Process(target=findPalindromicInPi, args=(100000, 300000, 5))

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()

    finish = time.perf_counter()

    print(f'Finished in {round(finish - start, 2)} second(s)')
