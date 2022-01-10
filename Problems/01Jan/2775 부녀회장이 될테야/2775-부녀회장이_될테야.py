# https://www.acmicpc.net/problem/2775

"""
[풀이]

f() = 해당 호실에 살고 있는 사람들의 수
f(k, n) = f(k, n-1) + f(k-1, n)
(단, k=0일 때는 f(k, n) = n이고, n=1일 때는 f(k, n) = 1이다.)
위 점화식을 구현해서 문제를 풀었음.
점화식은 트리 모형으로 문제를 그려보면 쉽게 알 수 있음 !

----
[예시]

f(1, 3) = f(1, 2) + f(0, 3)
        = f(1, 1) + f(0, 2) + f(0, 3)
        = 1 + 2 + 3
        = 6

----
[성능]
메모리 제한: 128MB, 시간 제한: 1s
메모리: 30860KB, 시간: 88ms, 코드길이: 281B

"""


def count_people(k, n):
    arr = list(range(1, n + 1))
    for _ in range(k):
        cur = 0
        for i in range(n):
            arr[i] += cur
            cur = arr[i]
    return arr[-1]


T = int(input())
for _ in range(T):
    print(count_people(int(input()), int(input())))
