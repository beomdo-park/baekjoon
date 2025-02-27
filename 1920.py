import sys

N = int(sys.stdin.readline())
A = set(sys.stdin.readline().split())
M = int(sys.stdin.readline())


for i in sys.stdin.readline().split():
    if i in A:
        print(1)
    else:
        print(0)
