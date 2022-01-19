import sys

input = sys.stdin.readline

for testcase in range(int(input())):

    num_note1 = int(input())
    note1 = set(map(int, input().split()))
    num_note2 = int(input())
    note2 = list(map(int, input().split()))

    for num in note2:
        if num in note1:
            print(1)
        else:
            print(0)