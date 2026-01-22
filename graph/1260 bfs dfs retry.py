# 1260 인터넷 풀이 참고하고 기억해서 적음
# 3번 더 풀어보기

from collections import deque

def bfs(V):
    queue = deque()
    visited[V] = 1
    print(V, end = " ")
    for u in nodes[V]:
        if (visited[u] == 0):
            visited[u] = 1
            queue.append(u)
    
    while(queue):
        V = queue.popleft()
        print(V, end = " ")
        for u in nodes[V]:
            if (visited[u] == 0):
                visited[u] = 1
                queue.append(u)
            
    
    
def dfs(V):
    visited[V] = 1
    print(V, end = " ")
    for u in nodes[V]:
        if (visited[u] == 0):
            visited[u] == 1
            dfs(u)
    


N, M, V = map(int, input().split())

nodes = [[] for _ in range (N+1) ]
visited = [False for _ in range(N+1)]


for _ in range(M):
    i1, i2 = map(int, input().split())
    nodes[i1].append(i2)
    nodes[i2].append(i1)
    
for i in range(1, N+1):
    nodes[i].sort()
    # print(nodes[i])

dfs(V) # 정상

print()
for i in range(1, N+1):
    visited[i] = 0

bfs(V)

#============ 정상 작동 =============