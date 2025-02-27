import sys

N = int(sys.stdin.readline())


def a(user):
    lst = []
    for i in user:
        lst.append(i)
        if lst[-2:] == ["(", ")"]:
            del lst[-2:]
    if lst:
        print("NO")
    else:
        print("YES")


for i in range(N):
    a(sys.stdin.readline().rstrip())
