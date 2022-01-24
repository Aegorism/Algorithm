# https://www.acmicpc.net/problem/2252

"""
[풀이]
위상 정렬로 풀면 된다.
위상 정렬은 순서가 정해져있는 작업을 수행할 때, 그 순서를 결정하기 위해 사용하는 알고리즘이다.
순서를 결정할 때, 주어진 조건에만 부합하면 되기 때문에 답이 여러가지일 수 있다.
구현을 위해서는 그래프와 진입차수에 대한 정보가 필요하다.

위상정렬에 대해 더 깊이 알고 싶다면 아래 링크를 참고하자.
https://blog.naver.com/ndb796/221236874984

[성능]
메모리 제한: 128MB, 시간 제한: 2s
메모리: 39728KB, 시간: 4184ms, 코드 길이: 972B
"""

from collections import deque


def topology_sort(graph, degree):
    """
    그래프와 진입차수(degree)를 인자로 받는다.
    """
    res = []

    # 시작점 찾기
    queue = deque([i for i in range(len(degree)) if degree[i] == 0])

    # 위상정렬은 모든 노드를 한 번씩 방문해야 끝남.
    for _ in range(len(graph)):
        # 모든 노드를 방문하기 전에 끝나면 위상 정렬이 불가능한 경우
        if len(queue) == 0:
            raise ValueError("위상 정렬이 불가능합니다.")

        x = queue.popleft()
        res.append(str(x + 1))
        for xx in graph[x]:
            degree[xx] -= 1
            if degree[xx] == 0:
                queue.append(xx)

    return " ".join(res)


# 엣지, 진입차수 구하기
N, M = map(int, input().split(" "))
graph = [[] for _ in range(N)]
degree = [0 for _ in range(N)]

for _ in range(M):
    x, y = map(int, input().split(" "))
    graph[x - 1].append(y - 1)
    degree[y - 1] += 1

# 위상정렬
print(topology_sort(graph, degree))
