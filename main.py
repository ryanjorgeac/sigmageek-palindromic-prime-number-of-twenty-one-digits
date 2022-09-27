import piGenerator
from isPalindromic import isPalindromic
from isPrime import isPrime
from anyNumberOfDigitsGenerator import anyNumberOfDigitsGenerator

if __name__ == "__main__":
    generator = piGenerator.piGenerator(0, 1000000)
    x = anyNumberOfDigitsGenerator(generator, 21)
    i = 0
    for number in x:
        if number % 2 != 0:
            if number % 5 != 0:
                if isPalindromic(number) and isPrime(number):
                    print(i)
                    print("Palindromic and prime Founder: ", number)
                    break
        elif i == 1000000:
            print(number, "posição: ", i)
            break
        i += 1
