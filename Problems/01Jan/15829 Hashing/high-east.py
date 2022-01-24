"""
https://www.acmicpc.net/problem/15829

[풀이]
문제에 나와있는 식을 그대로 구현했다.
내장 함수인 ascii_lowercase를 사용하면, 알파벳을 쉽게 얻을 수 있다.

----
[성능]
메모리 제한: 512MB, 시간 제한: 1s
메모리: 33484KB, 시간: 136ms, 코드길이: 272B
"""

from string import ascii_lowercase


def hashing(key: str, r=31, M=1234567891):
    seq = {word: i for i, word in enumerate(ascii_lowercase, 1)}
    res = 0
    for i, x in enumerate(key):
        res += seq[x] * r ** i
    return res % M


input()
print(hashing(input()))
