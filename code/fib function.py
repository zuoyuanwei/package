A = [0, 1]


def fib(n):
    for i in range(1, n):
        b = A[len(A)-1] + A[len(A)-2]
        A.append(b)
    print(A)
    return fib


fib(10)
