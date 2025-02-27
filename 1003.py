t = int(input())
lst = []

for i in range(t):
    n = int(input())
    lst.append(n)


for n in lst:
    a = [1, 0]  # 0개수, 1개수
    b = [0, 1]
    c = [0, 0]
    if n == 1:
        print(b[0], b[1])
    elif n == 0:
        print(a[0], a[1])
    else:
        count = 1
        while count < n:
            c[0] = b[0] + a[0]
            c[1] = b[1] + a[1]
            a[0] = b[0]
            a[1] = b[1]
            b[0] = c[0]
            b[1] = c[1]
            count += 1
        print(c[0], c[1])
