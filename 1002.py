import sys

T = int(sys.stdin.readline())
for i in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
    r = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

    # 중심과 거리가 같은 경우 무한개
    if x1 == x2 and y1 == y2 and r1 == r2:
        print("-1")
    # 중심이 같고 거리가 다른 경우   0개
    elif x1 == x2 and y1 == y2 and r1 != r2:
        print("0")

    # r1+r2== 중심사이 거리      1개
    elif r1 + r2 == r or abs(r1 - r2) == r:
        print("1")

    # r1+r2 > 중심사이 거리     2개
    elif r1 + r2 > r > abs(r1 - r2):
        print("2")
    else:
        print("0")
