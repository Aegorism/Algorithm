# 위상정렬
import sys 
from collections import deque 

# 한줄씩 읽는 코드
input = sys.stdin.readline 
# n=노드의 수, m=간선의 수
n, m = map(int, input().split())

# 진입차수. 0번을 안쓸거기에 n+1로 하는것
indegree = [0] * (n+1)
graph = [[] for _ in range(n+1)]

for i in range(m):
    # a에서 b로의 간선
    a,b = map(int, input().split())
    # graph[a]에 a와 연결된 노드를 입력
    graph[a].append(b)
    indegree[b] += 1

def topology_sort():
    result = []
    queue = deque()

    for i in range(1, n+1):
        # 진입차수가 0인 노드라면
        # 시작 노드 찾기
        if indegree[i] == 0:
            queue.append(i)

    # queue가 empty가 될 때까지 실행
    while queue:
        # queue에 먼저 들어간 노드를 하나씩 빼면서 실행
        current = queue.popleft()
        result.append(current)

        # current(queue에서 뺀 노드값)과 연결된 노드 가져옴
        for i in graph[current]:
            # current로부터 나가는 간선 제거
            indegree[i] -= 1
            if indegree[i] == 0:
                queue.append(i)

    for i in result:
        print(i, end=' ')

topology_sort()