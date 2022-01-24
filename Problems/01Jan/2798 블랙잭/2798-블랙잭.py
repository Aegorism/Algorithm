"""
https://www.acmicpc.net/problem/2798

[풀이]
브루트 포스 방법으로 풀이했다.
가능한 모든 숫자의 조합을 모두 확인했다.

[성능]
메모리 제한: 128MB, 시간 제한: 1s
메모리: 29200KB, 120시간: ms, 코드 길이: 332B

[성능 기준]
- int 백만개 = 4MB
- 1초 = 1억번 연산 가능
- 참고로, 12! 이상이면 1억 초과함.
"""

import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())
num_list = map(int, sys.stdin.readline().split())

answer = 0

for c in combinations(num_list, 3):
    if answer < sum(c) <= M:
        answer = sum(c)
    if answer == M:
        break

print(answer)
