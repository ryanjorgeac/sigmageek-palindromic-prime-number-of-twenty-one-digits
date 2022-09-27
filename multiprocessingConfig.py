import multiprocessing
from multiprocessing import Pool
import time
import isPalindromic
import isPrime
import piGenerator
import anyNumberOfDigitsGenerator

def moreMillion():
    million = 1000000
    yield million
    while True:
        million += 1000000
        yield million

def findPalindromicInPi(start, end, numberOfDigits):
    generator = piGenerator.piGenerator(start, end)
    x = anyNumberOfDigitsGenerator.anyNumberOfDigitsGenerator(generator, numberOfDigits)
    i = 0
    for number in x:
        print(number)
        i += 1

if __name__ == "__main__":
    # with Pool(3) as p:
    #
    #     generator = piGenerator.piGenerator(0, moreMillion().__next__())
    #     x = anyNumberOfDigitsGenerator.anyNumberOfDigitsGenerator(generator, 9)
    #     i = 0
    #     for number in x:
    #         if number % 2 != 0:
    #             if number % 5 != 0:
    #                 if isPalindromic.isPalindromic(number) and isPrime.isPrime(number):
    #                     print("Position::::::: ",i)
    #                     print("Palindromic and prime Founder: ", number)
    #                     print("Time: ", time.time())
    #                     break
    #
    #         elif i == 1000000:
    #             print(number, "position: ", i)
    #             print("Time (more million): ", time.time())
    #             break
    #         i += 1]
    start = time.perf_counter()

    p1 = multiprocessing.Process(target=findPalindromicInPi(0, 100, 4))
    p2 = multiprocessing.Process(target=findPalindromicInPi(50000, 100000, 4))
    p3 = multiprocessing.Process(target=findPalindromicInPi(100000, 150000, 4))

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()

    finish = time.perf_counter()

    print(f'Finished in {round(finish-start, 2)} second(s)')
