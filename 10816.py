import sys
from collections import Counter

M = int(sys.stdin.readline())
data = Counter(sys.stdin.readline().split())
N = int(sys.stdin.readline())
find = sys.stdin.readline().split()
for i in find:
    print(data[i], end=" ")
