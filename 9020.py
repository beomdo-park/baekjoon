import sys

T = int(sys.stdin.readline())
for i in range(T):
    N = int(sys.stdin.readline())

    prime = []
    a = [False, False] + [True] * (N - 1)
    for i in range(1, int(N**0.5) + 1):
        if a[i] == True:
            for j in range(2 * i, N + 1, i):
                a[j] = False
    prime = [i for i in range(2, N + 1) if a[i]]

    absolute_difference_function = lambda list_value: abs(list_value - int(N / 2))
    closest_value = min(prime, key=absolute_difference_function)

    mid = (
        prime.index(closest_value)
        if closest_value <= N
        else prime.index(closest_value) - 1
    )
    b = int(0)

    for i in range(mid, -1, -1):
        for j in range(mid, len(prime)):
            sum = prime[i] + prime[j]
            if sum == N:
                print(prime[i], prime[j])
                b = 1
                break
            elif sum > N:
                break
        if b == 1:
            break
