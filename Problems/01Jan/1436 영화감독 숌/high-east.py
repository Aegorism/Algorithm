# https://www.acmicpc.net/problem/1436

"""
[풀이]
처음에는 666, 1666, 2666, ... 6660, 6661 ... 이런 식으로 증가하는 패턴을 찾아서 풀려고 했는데,
찾지 못하는 예외 케이스 때문에 풀지 못했다.
그야말로 '브루트포스'로 풀어야 더 쉬운 문제였다...

[성능]
메모리 제한: 128MB, 시간 제한: 2s
메모리: 30864KB, 시간: 672ms, 코드 길이: 227B
"""


def get_movie_name(N):
    cnt = 0
    name = 666
    while True:
        if '666' in str(name):
            cnt += 1
        if cnt == N:
            break
        name += 1
    return name


print(get_movie_name(2))
