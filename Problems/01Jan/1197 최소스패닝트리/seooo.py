
# 특정 원소가 속한 집합 찾기
# 사이클이 존재하는지 확인하는데 사용됨
def find(x):
    # 루트 노드가 아니라면, 루트 노드를 찾을때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

# 두 원소(간선이 연결된 노드)가 속한 집합을 합치기
# 즉, 간선이 연결되어 있는 노드는 같은 집합으로 되어야 하기에
# 같은 집합으로 합치기
def union(a, b):
    # 두 노드의 루트 노드를 찾음.
    # 보통 루트 노드는 집합의 가장 작은 원소
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(Union 연산)의 개수 입력받기
v, e = map(int, input().split())
# 인덱스 0번을 안쓰려고
parent = [0] * (v+1) # 부모 테이블 초기화하기

# 모든 간선을 담을 리스트와, 최종 비용을 담을 변수
edges = []
result = 0

# 부모 테이블에서, 부모를 자기 자신으로 초기화
# 1~v까지
for i in range(1, v+1):
    parent[i] = i

# 모든 간선에 대한 정보를 입력 받기
for _ in range(e):
    a, b, cost = map(int, input().split())

    #  비용순으로 정렬하기 위해서 튜플의 첫번째 원소를 비용으로 설정
    edges.append((cost, a, b))

# 간선을 비용순으로 정렬
edges.sort()

# 간선을 하나씩 확인하며
for edge in edges:
    cost, a, b = edge

    # 사이클이 발생하지 않는 경우 >> 두 노드의 루트노드가 다르면 사이클이 발생X
    if find(a) != find(b):
        # 두 노드를 하나의 집합으로 연결하고
        union(a, b)
        result += cost
print(result)