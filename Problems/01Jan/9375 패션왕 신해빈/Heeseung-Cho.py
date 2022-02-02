## Run shell file run_test.sh to check test case.
## If you want to add testcase, add to testcase.txt
import sys
from functools import reduce

input = sys.stdin.readline

for _ in range(int(input())):
    closet = dict()
    for _ in range(int(input())):
        _ , wear = input().split()
        if wear not in closet.keys():
            closet[wear] = 1
        else:
            closet[wear] += 1

    unique_closet = list(closet.values())
    print(reduce(lambda x, y: x*(y+1), [1] + unique_closet) - 1)