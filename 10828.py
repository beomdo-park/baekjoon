import sys

N = int(input())
stack = []

for i in range(N):
    user = sys.stdin.readline()

    if "push" in user:
        a = int(user[5:])
        stack.append(a)
    elif "pop" in user:
        if not stack:
            print(-1)
        else:
            print(stack.pop())
    elif "size" in user:
        print(len(stack))
    elif "empty" in user:
        if not stack:
            print(1)
        else:
            print(0)
    elif "top" in user:
        if not stack:
            print(-1)
        else:
            print(stack[-1])
