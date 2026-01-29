import sys
N = int(input())

def dfs(i, j):
    stack = []
    cnt = 0
    
    stack.append([i, j])
    visited[i][j] = 1
    cnt+=1
    
    while(stack):
        item = stack.pop()
        k, m = item[0], item[1]
        # print("k, m:", k, m)
        if (k+1 < N):
            if (visited[k+1][m] == 0 and graph[k+1][m] == "1"):
                stack.append([k+1, m]); cnt+=1; visited[k+1][m] = 1
                
        if (m+1 < N):
            if (visited[k][m+1] == 0 and graph[k][m+1] == "1"):
                stack.append([k, m+1]); cnt+=1; visited[k][m+1] = 1
                
        if (k-1 >= 0):
            if (visited[k-1][m] == 0 and graph[k-1][m] == "1"):
                stack.append([k-1, m]); cnt+=1; visited[k-1][m] = 1
                
        if (m-1 >= 0):
            if (visited[k][m-1] == 0 and graph[k][m-1] == "1"):
                stack.append([k, m-1]); cnt+=1; visited[k][m-1] = 1
    
    # print("cnt:",cnt)            
    return cnt

        
        

graph = [[] for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    graph[i] = sys.stdin.readline()
    
# 정상 입력 확인
# print()
# for i in range(1, N+1):
#     print(graph[i], end = "")

result = []
for i in range(N):
    for j in range(N):
        if (visited[i][j] == 0 and graph[i][j] == "1"):
            result.append(dfs(i, j))
            
result.sort()
len_res = len(result)

# 결과 출력
print(len_res)
for i in range(len_res):
    print(result[i])
