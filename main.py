import piGenerator
from isPalindromic import isPalindromic
from isPrime import isPrime
from twentyOneDigitsGenerator import twentyOneDigitsGenerator

if __name__ == "__main__":
    generator = piGenerator()
    x = twentyOneDigitsGenerator(generator)
    i = 0
    for number in x:
        if i > 1000000:
            print("I have excedeed my limit. Please, use a better generator.")
            break
        if isPalindromic(number) and isPrime(number):
            print(i)
            print(number)
            break
        i+=1