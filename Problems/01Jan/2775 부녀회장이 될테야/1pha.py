import sys

input = sys.stdin.readline

for _case in range(int(input())):

    k, n = int(input()), int(input())

    apt = [_ for _ in range(1, n+1)]
    if k == 1:
        print(sum(apt))
    else:
        for floor in range(k):
            apt = [sum(apt[:i]) for i in range(1, n+1)]
        print(apt[-1])