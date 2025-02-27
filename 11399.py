import sys

N = int(sys.stdin.readline())

P = list(map(int, sys.stdin.readline().split()))

P.sort()

sum = 0

for i in range(N, 0, -1):

    sum += P[N - i] * i

print(sum)
