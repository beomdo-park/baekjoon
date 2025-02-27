import sys

Deque = []


def pop_front():
    if empty():  # 비어있으면
        print(-1)
    else:
        print(Deque.pop(0))


def pop_back():
    if empty():  # 비어있으면
        print(-1)
    else:
        print(Deque.pop(-1))


def empty():
    return 1 if not Deque else 0


n = int(sys.stdin.readline())

for i in range(n):
    user = sys.stdin.readline()
    if "push_front" in user:
        Deque.insert(0, int(user.split()[1]))
    elif "push_back" in user:
        Deque.append(int(user.split()[1]))
    elif "pop_front" in user:
        pop_front()
    elif "pop_back" in user:
        pop_back()
    elif "size" in user:
        print(len(Deque))
    elif "empty" in user:
        print(empty())
    elif "front" in user:
        print(-1 if empty() else Deque[0])
    elif "back" in user:
        print(-1 if empty() else Deque[-1])
