import math
from math import factorial

def permutations_without_repeat(n):
    return factorial(n)

def permutations_with_repeat(n, repeats):
    denominator = 1
    for r in repeats:
        denominator *= factorial(r)
    return factorial(n) // denominator

def arrangements_without_repeat(n, k):
    if k > n:
        return 0
    return factorial(n) // factorial(n - k)

def arrangements_with_repeat(n, k):
    return n ** k

def combinations_without_repeat(n, k):
    if k > n:
        return 0
    return factorial(n) // (factorial(k) * factorial(n - k))

def combinations_with_repeat(n, k):
    return factorial(n + k - 1) // (factorial(k) * factorial(n - 1))


def main():
    ans1 = permutations_without_repeat(7)
    print('ans 1:', ans1)

    ans21 = combinations_without_repeat(10, 3) * combinations_without_repeat(7, 3)
    ans22 = combinations_without_repeat(6, 3) - arrangements_without_repeat(8, 2) * permutations_without_repeat(3)
    print('ans 2.1:', ans21)
    print('ans 2.2:', ans22)

    # Случай A: пика — король
    case_a = 1 * combinations_without_repeat(3, 2) * combinations_without_repeat(21, 2)

    # Случай B: пика — одна из дам
    case_b = 3 * 3 * combinations_without_repeat(21, 2)

    # Случай C: пика — не король и не дама
    case_c = 3 * combinations_without_repeat(3, 2) * 7 * 21

    ans3 = case_a + case_b + case_c

    print('ans 3:', ans3)


if __name__ == '__main__':
    main()
