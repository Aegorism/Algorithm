from itertools import combinations
import sys

# 한줄씩 읽는 코드
input = sys.stdin.readline 
# n=카드의 갯수, m=숫자 합 max
n, m = map(int, input().split())

num = list(map(int, input().split()))

combi = list(combinations(num, 3))
result = 0
for i in combi:
    count = 0
    for number in i:
        count += number # sum(number)로 대체 가능
    
    if count > result and count <= m:
        result = count

print(result)
