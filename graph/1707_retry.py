# 예전에 풀고 다시 품

import sys

K = int(sys.stdin.readline()) # test case



answer_stack = []
# 테스트 케이스만큼 검사 진행

def dfs(connected, V, E):
    global answer_stack
    
    early_exit = 0
    color = [0 for _ in range(V+1)]
    stack_dfs = []
    
    
    for i in range(1, V+1):
        if (color[i] == 0):
            stack_dfs.append(i)
            color[i] = 1
            
        while (stack_dfs): # 여기에 color 검사 로직만 추가
            cur = stack_dfs.pop()
            for u in connected[cur]:
                if (color[u] == 0):
                    if (color[cur] == 1):
                        color[u] = -1
                    else:
                        color[u] = 1
                    stack_dfs.append(u)
                else:
                    if (color[cur] == color[u]):
                        answer_stack.append("NO")
                        return

    if (early_exit == 0):
        answer_stack.append("YES")

for _ in range(K):
    V, E = map(int, sys.stdin.readline().split()) # vertex / Edges
    
    connected = [[] for _ in range(V+1)] # 정점 갯수만큼 connected
    for _ in range(E): # 노드 저장
        i1, i2 = map(int, sys.stdin.readline().split())
        connected[i1].append(i2)
        connected[i2].append(i1)
        
    dfs(connected, V, E)

# 답 출력
for i in range(len(answer_stack)):
    print(answer_stack[i])