import cmath


def fibonacci(n):
    return _fibonacci_4(n)


def _fibonacci_4(n):
    result = 0
    if n == 0:
        result = 1
    elif n == 1:
        result = 1
    else:
        result = (((1 + 5 ** 0.5) / 2) ** (n+1) - ((1 - 5 ** 0.5) / 2) ** (n+1)) / 5 ** 0.5
    return int(result)


if __name__ == '__main__':
    # N = int(input('please input the N = ' ))
    # print(' the #%d Fabonacci number is : %d' % (N, Fabonacci(N)))
    from timeit import default_timer as timer
    for i in range(0, 50):
        start = timer()
        for k in range(1, 100000):
            fibonacci(2**i)
        end = timer()
        print(end - start)


