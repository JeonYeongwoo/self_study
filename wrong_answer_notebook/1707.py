# 하단 블로그의 아래 로직을 참고함
# https://hongjw1938.tistory.com/117
# 1. 최초 탐색 시작할 정점의 색상을 빨간색으로 칠한다.(숫자 1로 표현)
# 2. 최초 정점의 인접 정점의 색상을 파란색으로 칠한다.(숫자 -1로 표현)
# 3. 해당 인접 정점들을 차례로 탐색을 시작하며 자신과 인접한 정점을 빨간색으로 칠한다.(숫자 1로 표현)
# 4. 이와 같은 방식을 탐색을 지속하며 반복하여 2개의 색상으로 모두 칠한다.
# 5. 색상을 칠하다가 이웃 정점이 같은 색으로 칠해져 있다면 이분 그래프가 될 수 없다.

# 지피티 반례
# 1
# 2 1
# 1 2

import sys

K = int(input()) # 테스트 케이스

def bin_check(V, visited, connected):
    # 정점 및 간선의 개수
    
    # for i in range(1,V):
    for i in range(1,V+1): # 지피티로 체크한 오류..
        if(visited[i] == 0):
            stack = []
            visited[i] = 1
            stack.append(i);
            while (stack):
                index = stack.pop()
                if(visited[index] == 1):
                    for u in connected[index]:
                        if (visited[u] == 1):
                            print("NO")
                            return
                        
                        if(visited[u] == 0):
                            visited[u] = -1
                            stack.append(u)
                elif(visited[index] == -1):
                    for u in connected[index]:
                        if (visited[u] == -1):
                            print("NO")
                            return
                        
                        if(visited[u] == 0):
                            # visited[u] = -1 지피티가 잡은 오류..
                            visited[u] = 1
                            stack.append(u)
                            
    print("YES")
                    


cases = [[] for _ in range(K)]
for i in range(K):
    
    # each cases
    V, E = map(int, input().split())
    visited = [0 for _ in range(V+1)]; 
    connected =  [[] for _ in range(V+1)]

    # visited[1] = 1
    # 이것 때문에 오류남
    # 1
    # 2 1
    # 1 2

    # 그래프 
    for _ in range(E):
        i1, i2 = map(int, sys.stdin.readline().split())
        connected[i1].append(i2)
        connected[i2].append(i1)    
    # ===== end of case =====
    
    cases[i].append(V); cases[i].append(visited); cases[i].append(connected)
    
for i in range(K):
    bin_check(cases[i][0], cases[i][1], cases[i][2])