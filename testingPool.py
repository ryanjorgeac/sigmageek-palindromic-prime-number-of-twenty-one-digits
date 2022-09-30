from multiprocessing import Pool
import time
from poolArgsGenerator import poolArgsGenerator


def multiplying(x, y, z):
    print("X = ", x, ", Y =", y, ", Z = ", z)
    time.sleep(1)
    print("X = ", x, ", Y =", y, ", Z = ", z)
    return


if __name__ == "__main__":
    time1 = time.perf_counter()
    pool = Pool()
    print([pool.apply(multiplying, args=(x, y, z)) for x, y, z in poolArgsGenerator(5)])
    pool.close()
    pool.join()
    print("Time in parallel:", time.perf_counter() - time1)
