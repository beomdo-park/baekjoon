import sys

while True:
    M = int(sys.stdin.readline())
    N = M * 2
    if M == 0:
        break

    prime = []

    a = [False, False] + [True] * (N - 1)
    for i in range(1, N + 1):
        if a[i] == True:
            prime.append(i)
            for j in range(2 * i, N + 1, i):
                a[j] = False
    i = 0
    count = 0
    while True:
        try:
            if M < prime[i] <= N:
                count += 1

            i += 1
        except IndexError:
            break
    print(count)
