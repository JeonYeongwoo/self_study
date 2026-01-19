# 못풀어서 챗지피티 풀이 보고 구현만 해보았음.
# 제출은 x (추후 자력으로 풀이해본 후 풀리면 제출)

# ===================== 지피티 풀이 ============================
# 오케이 “코드 말고 알고리즘(절차)”만 딱 정리해줄게. (그래프 탐색 기준)
# DFS (Depth-First Search) 알고리즘
# 핵심: 한 갈래로 끝까지 파고들었다가 막히면 되돌아옴.
# 반복(스택) 버전 절차
# visited(방문표시) 준비 (전부 false)
# 시작 정점 s를 스택에 push
# 스택이 빌 때까지 반복:
# 스택에서 pop해서 v를 꺼냄
# v가 아직 방문 전이면:
# v를 방문 처리(visited[v]=true) + “방문 순서 기록/출력”
# v의 인접 정점들 중 방문 안 한 것들을 스택에 push
# 주의: “작은 번호부터 방문” 같은 조건이 있으면, 스택은 LIFO라서 역순으로 push해야 실제 방문이 정순으로 나옴
# 종료
# DFS의 느낌
# “현재 정점 → 다음으로 갈 수 있는 곳 하나 선택 → 계속 진행 → 더 못 가면 뒤로”
# BFS (Breadth-First Search) 알고리즘
# 핵심: 시작점에서 가까운 것부터 거리(레벨) 순서대로 넓게 퍼져나감.
# 큐 버전 절차
# visited 준비 (전부 false)
# 시작 정점 s를 방문 처리하고 큐에 enqueue
# 큐가 빌 때까지 반복:
# 큐에서 dequeue해서 v를 꺼냄
# v의 인접 정점 u들을 순회:
# u가 방문 전이면:
# u를 방문 처리(중복 enqueue 방지)
# u를 큐에 enqueue
# “방문 순서 기록/출력”
# 종료
# BFS의 느낌
# “거리 1짜리 전부 → 거리 2짜리 전부 → 거리 3짜리 전부…”
# ===========================================================

# bfs 문제
def dfs():
    stack = []
    stack.append(nodes[V])
    
    while(len(stack) != 0):
        v = stack.pop()
        if (v.visited == 0):
            v.visited = 1
            print(v.item, end=" ")
            for u in v.connected:
                if u.visited == 0:
                    stack.append(u)
    

def bfs():
    q = queue()
    q.push(nodes[V])
    nodes[V].visited = 1
    
    while(q.tail > q.head ):
        v = q.pop()
        print(v.item, end=" ")
        
        for u in v.connected:
            if (u.visited == 0):
                u.visited = 1;
                q.push(u)
        
    
    
    
N, M, V = map(int, input().split())

class queue:
    def __init__(self):
        self.queue = []
        self.head = 0
        self.tail = 0
    def push(self, item):
        self.queue.append(item)
        self.tail += 1;
        
    def pop(self):
        ret = self.queue[self.head]
        self.head += 1
        return ret
        

class Node :
    def __init__(self,item):
        self.item = item
        self.visited = 0
        self.connected = []
        
nodes = [None for i in range(N+1)]

# Graph 생성
for i in range(1, N+1):
    nodes[i] = Node(i);
    
for i in range(M):
    i1, i2 = map(int, input().split())
    nodes[i1].connected.append(nodes[i2])
    nodes[i2].connected.append(nodes[i1])
    
# 역순 저장
for i in range(1, N+1):
    nodes[i].connected.sort(key = lambda x : x.item, reverse = True)

dfs()

for i in range(1, N+1):
    nodes[i].visited = 0
    
print()
    
for i in range(1, N+1):
    nodes[i].connected.sort(key = lambda x : x.item)

bfs()