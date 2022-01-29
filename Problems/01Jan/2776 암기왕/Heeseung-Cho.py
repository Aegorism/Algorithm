import sys

input = sys.stdin.readline

for _ in range(int(input())):

    M = int(input())
    list1 = set(map(int, input().split()))
    N = int(input())
    list2 = list(map(int, input().split()))

    for num in list2:
        print(1 if num in list1 else 0)