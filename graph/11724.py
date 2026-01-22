# bfs 를 진행하면서 visited를 기록하고
# bfs 할때마다 카운트를 함으로써, 연결 요소 개수 탐색이 가능함.
from collections import deque

# N, M = map(int, input().split()) << 시간 초과 난대서 인풋 형태 검색하여 바꿈
import sys
N,M=map(int,sys.stdin.readline().split())
# 왜 sys를 이용해 아웃풋을 산출하는 것이 더 빠른지 찾아볼 필요.

connected = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]

def bfs(V): # 따라서 재호출 없는 bfs 진행
    visited[V] = 1
    queue = deque()
    for u in connected[V]:
        if (visited[u] == 0):
            visited[u] = 1
            queue.append(u)
    
    while(queue):
        V = queue.popleft()
        for u in connected[V]:
            if (visited[u] == 0):
                visited[u] = 1
                queue.append(u)

for _ in range(M):
    i1, i2 = map(int,sys.stdin.readline().split())
    connected[i1].append(i2)
    connected[i2].append(i1)

# for i in range(1, N+1):
#     print (connected[i])    

result = 0
for i in range(1, N+1):
    if (visited[i] == 0):
        bfs(i)
        result+=1
        
print(result)
        
    

    
