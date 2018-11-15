import numpy as np


def fibonacci(n):
    return _fibonacci_3(n)


def _fibonacci_3(n):
    result = 0
    A = np.mat('1 1;1 0')
    I = np.array([[1, 0], [0, 1]], dtype='int')
    if n == 0:
        result = 1
    else:
        #for i in range(1, n+1):
        I = A ** n
        result = I[0, 0]
    return result


if __name__ == '__main__':
    # N = int(input('please input the N = ' ))
    # print(' the #%d Fabonacci number is : %d' % (N, Fabonacci(N)))
    from timeit import default_timer as timer
    for i in range(0, 50):
        start = timer()
        for k in range(1, 100000):
            fibonacci(2 ** i)
        end = timer()
        print(end - start)
