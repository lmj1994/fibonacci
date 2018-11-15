def fibonacci(n):
    return _fibonacci_2(n)


def _fibonacci_2(n):
    result = 0
    fab = [0]*(n+2)
    fab[0] = 1
    fab[1] = 1
    if n == 0:
        result = 1
    elif n == 1:
        result = 1
    else:
        for i in range(2, n+1):
            fab[i] = fab[i-1]+fab[i-2]
            result = fab[i]
    return result


# N = int(input('please input the N = ' ))
# print(' the #%d fibonacci number is : %d' % (N, fibonacci(N)))


if __name__ == '__main__':
    # N = int(input('please input the N = ' ))
    # print(' the #%d Fabonacci number is : %d' % (N, Fabonacci(N)))
    from timeit import default_timer as timer
    for n in range(0, 50):
        start = timer()
        for k in range(1, 100000):
            fibonacci(2 ** n)
        end = timer()
        print(end - start)
