from sys import argv


def recurse_rabbit_question(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    else:
        return recurse_rabbit_question(n-2) + recurse_rabbit_question(n-1)


def memoized_recurse_rabbit_question(n, memo):
    memo[0] = 1
    memo[1] = 1
    return mr_helper(n, memo)


def mr_helper(n, memo):
    if n in memo:
        return memo[n]
    else:
        return mr_helper(n-2, memo) + mr_helper(n-1, memo)


def dp_rabbit_question(n, memo={}):
    if n in [0, 1]:
        return 1
    memo[0] = 1
    memo[1] = 1
    for i in range(2, n+1):
        memo[i] = memo[i-1] + memo[i-2]
    return memo[n]


def math_rabbit_question(n):
    c = 0
    for i in range(0, int(n/2) + 1):
        c += choose(n-i, i)
    return c


def choose(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))
    pass


def factorial(n):
    c = 1
    for i in range(1, n+1):
        c *= i
    return c


if __name__ == '__main__':
    math_rabbit_question(int(argv[1]))
