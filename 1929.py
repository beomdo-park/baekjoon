import sys

M, N = map(int, sys.stdin.readline().split())

prime = []

a = [False, False] + [True] * (N - 1)
for i in range(1, N + 1):
    if a[i] == True:
        prime.append(i)
        for j in range(2 * i, N + 1, i):
            a[j] = False
i = 0
while True:
    try:
        if M <= prime[i] <= N:
            print(prime[i])

        i += 1
    except IndexError:
        break
