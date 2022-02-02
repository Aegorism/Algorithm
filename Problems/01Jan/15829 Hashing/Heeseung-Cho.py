import sys

input = sys.stdin.readline
character = {chr(i):i-96 for i in range(ord('a'), ord('z') + 1)}
L = int(input())

str = str(input().rstrip())
sum = 0
for i in range(L):
    sum += character[str[i]]*31**i
_, ans = divmod(sum, 1234567891)
print(ans)