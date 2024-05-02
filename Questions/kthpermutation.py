"""Solve the kth permuation problem"""


def kth_permuation(n, k):
    permutation = []
    unused = [item + 1 for item in range(n)]
    fact = [1] * (n + 1)
    for i in range(1, n + 1):
        fact[i] = fact[i - 1] * i
    while n > 0:
        length = fact[n] // n
        i = k // length
        permutation.append(unused[i])
        unused.remove(unused[i])
        n -= 1
        k = k % length
    return permutation


def main():
    print(kth_permuation(4, 16))


if __name__ == "__main__":
    main()
