# 지피티 코드
# 추후 공부하기
# 백준 제출 x
# 11724번 연결 요소 탐색
class Node:
    def __init__(self, item):
        self.item = item
        self.connected = []
        self.visited = 0
        self.added = 0

        self.valid = 0 # 활성화 안된 노드에 대해 탐색하는 것 방지
        
def dfs(start):
    stack = []
    stack.append(nodes[start])
    nodes[start].added= 1
    # nodes[start].visited = 1 << 이렇게 하면 탐색 안됨 주의. (처음 시작일 때 1로 마킹되어 코드가 돌아가지 않음)
    while(len(stack)!= 0):
        s = stack.pop()
        for u in s.connected:
            if (u.visited == 0):
                u.visited = 1
                u.added = 1
                stack.append(u)

# def dfs(V):
#     stack = []
#     stack.append(nodes[V])
    
#     while(len(stack) != 0):
#         v = stack.pop()
#         if (v.visited == 0):
#             v.visited = 1
#             # print(v.item, end=" ")
#             for u in v.connected:
#                 if u.visited == 0:
#                     stack.append(u)
                    
        
def connected_components():
    count = 0
    
    for i in range(1, N+1):
        if (nodes[i].visited == 0):
            dfs(nodes[i].item)
            count+=1
    print(count)



N, M = map(int, input().split())

nodes = [None for _ in range(N+1)]
for i in range(1, N + 1):            
    nodes[i] = Node(i)
    nodes[i].valid = 1

for _ in range(M):
    i1, i2 = map(int, input().split())
    nodes[i1].connected.append(nodes[i2])
    nodes[i2].connected.append(nodes[i1])
    
connected_components()


    