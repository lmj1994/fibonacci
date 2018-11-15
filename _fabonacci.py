def fibonacci(n):
    return _fibonacci_(n)


def _fibonacci_(n):
    result = 0
    if n == 0:
        result = 1
    elif n == 1:
        result = 1
    else:
        result = _fibonacci_(n - 1) + _fibonacci_(n - 2)
    return result


# N = int(input('please input the N = '))
# print(' the #%d fibonacci number is : %d' % (N, fibonacci(N)))

if __name__ == '__main__':
    from timeit import default_timer as timer
    for i in range(0, 40):
        start = timer()
        fibonacci(i)
        end = timer()
        print(end - start)

