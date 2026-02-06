import sys

stack_answer = [] # 답 저장할 스택

def dfs(arg_map, w, h):
    visited = [[0 for _ in range(w)] for _ in range(h)] # visited 가 각각 저장되어야 하므로 생성
    stack_dfs = [] # dfs용 스택
    cnt_land = 0
    
    if (w != 1 and h != 1):
        for i in range(w): # col
            for j in range(h): # row
                # i,j 기반 dfs 시작
                if (arg_map[j][i] == 1 and visited[j][i] == 0):
                    cnt_land += 1 # 방문 되지 않은 1이 있다면 섬이 있다는 뜻임.
                    stack_dfs.append([j, i])
                    # print(stack_dfs)
                    
                    while(stack_dfs):
                        a = stack_dfs.pop()
                        col, row = a
                        # 4 가지 끝에 있는 경우 감안 # 이거 끝부분을 어떻게 검사할지 어캐하냐
                        if (row > 0):
                            if (arg_map[col][row-1] == 1 and visited[col][row-1] == 0):
                                stack_dfs.append([col, row-1])
                            if (col > 0):
                                if (arg_map[col-1][row-1] == 1 and visited[col-1][row-1] == 0):
                                    stack_dfs.append([col-1, row-1])
                                visited[col-1][row-1] = 1
                            visited[col][row-1]= 1
                        if (row < w-1):
                            if (arg_map[col][row+1] == 1 and visited[col][row+1] == 0):
                                stack_dfs.append([col, row+1])  
                            visited[col][row+1] = 1  
                            
                            if (col < h-1):
                                if (arg_map[col+1][row+1] == 1 and visited[col+1][row+1] == 0):
                                    stack_dfs.append([col+1, row+1] )
                                visited[col+1][row+1]  = 1
                            
                                
                        if (col > 0):
                            if (arg_map[col-1][row]== 1 and visited[col-1][row] == 0 ):
                                stack_dfs.append([col-1, row])
                            visited[col-1][row] = 1
                            if (row < w-1):
                                if (arg_map[col-1][row+1] == 1 and visited[col-1][row+1] == 0):
                                    stack_dfs.append([col-1, row+1])
                                visited[col-1][row+1] = 1
                        if (col < h-1):
                            if (arg_map[col+1][row] == 1 and visited[col+1][row] == 0 ):
                                stack_dfs.append([col+1, row] )
                            visited[col+1][row]  = 1
                            if (row > 0):
                                if (arg_map[col+1][row-1] == 1 and visited[col+1][row-1] == 0):
                                    stack_dfs.append([col+1, row-1])
                                visited[col+1][row-1] = 1
    elif (w == 1 and h == 1):
        cnt_land = arg_map[0][0]
    elif (w == 1 and h != 1):
        connected = 0;
        for i in range(w):
            if (arg_map[0][i] == 1):
                connected = 1
            else: # 0인 경우
                if (connected == 1):
                    cnt_land += 1
                connected = 0    
        
        if (connected == 1):
            cnt_land+= 1
        
    elif (w != 1 and h == 1):
        connected = 0;
        for i in range(w):
            if (arg_map[i][0] == 1):
                connected = 1
            else: # 0인 경우
                if (connected == 1):
                    cnt_land += 1
                connected = 0    
        
        if (connected == 1):
            cnt_land+= 1
    # 결과 저장
    stack_answer.append(cnt_land)
    

while (True):
    
    w, h = map(int, sys.stdin.readline().split())
    # print(w,h)
    if (w == 0 and h == 0):
        break;
    
    # 맵 초기화
    map_input = [[0 for _ in range(w)] for _ in range(h)]
    
    # 맵 생성
    for map_row in range(h):
        map_input[map_row] = list(map(int, sys.stdin.readline().split()))
        # for j in range(w):
        #     print(map_input[map_row][j], end = " ")
    
    # dfs로 맵 
    dfs(map_input, w, h)
    
    

# 저장한 정답 프린트
for i in range(len(stack_answer)):
    sys.stdout.write(str(stack_answer[i]) + '\n')
