from collections import deque
import sys
"""
전형적인 위상정렬 문제이다.
A번 학생이 B번 학생보다 반드시 먼저 앞에와야 하는 상황이 주어지기 때문에,
A -> B를 만족시키면서 정렬을 해야 하기 때문이다.
 
위상정렬의 과정은 다음과 같다.
진입차수가 0인 정점을 큐에 삽입
큐에서 원소를 꺼내 해당 원소와 연결된 간선을 모두 제거
제거한 후에 진입차수가 0인 정점을 큐에 삽입 이후 2~3의 과정을 반복

이를 해당 문제에 적용해보자.
다음과 같은 입력이 주어졌다고 해보자.
학생들은 4명이 있고 다음과 같은 조건이 주어졌다.
4 -> 2
3 -> 1
4번은 반드시 2번앞에 와야 하므로 4 -> 2 로의 간선이 존재하므로 2번의 진입차수는 1이 되며
3번은 반드시 1번앞에 와야 하므로 3 -> 1 로의 간선이 존재하므로 1번의 진입차수는 1이 된다.
 
먼저, 진입차수가 0인 3번과 4번을 큐에 넣은 다음 ( 3번과 4번을 먼저 줄 세우겠다는 뜻 )
큐에서 먼저 3을 꺼내 3과 연결된 간선들을 제거한다.
3은 이미 줄을 섰으므로 3 다음에 와야 할 것들은 언제와도 무방)
따라서 위상정렬로 위의 방식대로 해결한 풀이는 다음과 같다.
"""

input = sys.stdin.readline

v, e= map(int, input().split())

graph = [[] for _ in range(v+1)] # 전체 그래프, 0번을 생략
indegree = [0 for _ in range(v+1)]  # 진입 차수 


for _ in range(e):
    a,b = map(int, input().split())
    graph[a].append(b)
    indegree[b] +=1
    
def solution():
    queue = deque() # 큐
    answer = [] # 정답

    for i in range(1, v+1):
        if indegree[i] ==0: # 진입차수가 0 이면 큐에 넣어서 줄을 세우주자
            queue.append(i)

    while queue:
        tmp = queue.popleft() # 차수가 0인것 답에 넣어주고 
        answer.append(tmp) # 연결 되있는것 부터 살펴보자 
        
         # 차수가 0인 vertex 와 연결된 vertex 가져옴 
        for i in graph[tmp]:
            indegree[i] -= 1
            if indegree[i] == 0:
                queue.append(i)
    print(*answer)
    return None 

solution()
