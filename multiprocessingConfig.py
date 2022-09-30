from multiprocessing import Pool
import time
from aggregateNumbers import aggregateNumbers
from poolArgsGenerator import poolArgsGenerator
from findPalindromicInPi import findPalindromicInPi

if __name__ == "__main__":
    start = time.perf_counter()
    argsGenerator = poolArgsGenerator(21)
    interval = next(argsGenerator)
    with Pool() as p:
        # use the apply function
        while flag: # flag not set yet
            p.apply_async(findPalindromicInPi, args=interval, callback=aggregateNumbers)
            interval = next(argsGenerator)

