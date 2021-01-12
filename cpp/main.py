import time
import random

if __name__ == '__main__':
    N = 1_000_000
    a = [0]*N
    b = [0]*N

    for i in range(0, N):
        a[i] = random.randint(1, 10)
        b[i] = random.randint(1, 10)

    start = time.time_ns()

    for i in range(0, N):
        a[i] = a[i] + b[i]

    end = time.time_ns()

    # Compared to C++
    print((end-start)/440837)

    print('Elapsed time: ', end - start)



