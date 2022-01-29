import sys

input = sys.stdin.readline
K, L = list(map(int, input().split()))
wait = dict()
for i in range(L):
    student = str(input().rstrip())
    if student not in wait.keys():
        wait[student] = i
    else:
        wait.pop(student, None)
        wait[student] = i

wait_dict = {val:key for key, val in wait.items()}
order = list(sorted(wait_dict.keys()))
for j in range(K):
    if j < len(wait_dict):
        print(wait_dict[order[j]])