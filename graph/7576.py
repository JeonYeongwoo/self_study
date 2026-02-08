# 그냥 수치 조정해서 맞춤..

from collections import deque
import sys

def check_0(mat, M, N):
    for row in range(N):
        for col in range( M):
            if (mat[row][col] == 0):
                return True
    return False
    

def bfs(inp, M, N):
    queue_bfs = deque()
    flag_0_detected = 0
    
    cnt_update = 0
    
    cnt = 0
    cnt_queue = deque()
    if (M!= 1 and N != 1):
        for col in range(M):
            for row in range(N):
                if (inp[row][col] == 1):
                    queue_bfs.append([row, col])
                    cnt+= 1;
        cnt_queue.append(cnt)
        # print(cnt_queue)
        cnt_2 = 0
        cnt = 0
                    
    
        # print(stack_bfs)
        # 매번 루프에서 해야 하는 것
        while(queue_bfs ):
            if cnt_2 == 0:
                if (cnt_queue is None):
                    break
                cnt_2 = cnt_queue.popleft()
            
            cur = queue_bfs.popleft() # 왼쪽이 col, 오른쪽이 row
            if (cur[0] < N-1):
                if(inp[cur[0]+1][cur[1]] == 0):
                    inp[cur[0]+1][cur[1]]  = 1
                    queue_bfs.append([cur[0]+1, cur[1]])
                    cnt += 1
            if (cur[0] > 0):
                if(inp[cur[0]-1][cur[1]] == 0):
                    inp[cur[0]-1][cur[1]] = 1
                    queue_bfs.append([cur[0]-1, cur[1]])
                    cnt += 1
            if (cur[1] < M-1):
                if(inp[cur[0]][cur[1] +1] == 0):
                    inp[cur[0]][cur[1] +1] = 1
                    queue_bfs.append([cur[0], cur[1] +1])
                    cnt += 1
            if (cur[1] > 0):
                if(inp[cur[0]][cur[1] -1] == 0):
                    inp[cur[0]][cur[1] -1] = 1
                    queue_bfs.append([cur[0], cur[1] -1])
                    cnt += 1
            # 한 번 루프 지날 때마다 업데이트 카운트
            
                
            
            cnt_2 -= 1    
            if (cnt_2 == 0):
                # for row in range(N):
                #     print(inp[row])
                # print()
                if (cnt != 0):
                    cnt_queue.append(cnt)
                cnt = 0
                # print(queue_bfs)
                # print(cnt_queue)
                cnt_update += 1
        cnt_update -= 1
                
            
    elif (M == 1 and N != 1):
        # 시작. 1인 토마토들을 bfs 대상에 넣음
        for row in range(N):
            if (inp[row][0] == 1):
                queue_bfs.append([row, 0])
                cnt+= 1;
            cnt_queue.append(cnt)
            cnt_2 = 0
            cnt = 0
                    
        # print(queue_bfs)
        while(queue_bfs): # row를 변경시키면서 확인
            if cnt_2 == 0:
                if (cnt_queue is None):
                    break
                cnt_2 = cnt_queue.popleft()
            
            cur = queue_bfs.popleft()
            if (cur[0] < N-1):
                if(inp[cur[0]+1][0] == 0):
                    inp[cur[0]+1][0]  = 1
                    queue_bfs.append([cur[0] +1, 0 ])
                    cnt += 1
            if (cur[0] > 0):
                if(inp[cur[0]-1][0] == 0):
                    inp[cur[0]-1][0] = 1
                    queue_bfs.append([cur[0] -1, 0 ])
                    cnt += 1
            # 한 번 루프 지날 때마다 업데이트 카운트
            cnt_2 -= 1    
            if (cnt_2 == 0):
                # for row in range(N):
                #     print(inp[row])
                # print()
                if (cnt != 0):
                    cnt_queue.append(cnt)
                cnt = 0
                # print(queue_bfs)
                # print(cnt_queue)
                cnt_update += 1
        
    elif(M!= 1 and N == 1): # 하나의 row
        # 처음 들어가야 할 값
        for col in range( M-1):
            if (inp[0][col] == 1):
                queue_bfs.append([0, col])
                cnt+= 1;
            cnt_queue.append(cnt)
            cnt_2 = 0
            cnt = 0
                    
        while(queue_bfs): # row를 변경시키면서 확인
            if cnt_2 == 0:
                if (cnt_queue is None):
                    break
                cnt_2 = cnt_queue.popleft()
            cur = queue_bfs.popleft() # 왼쪽이 col, 오른쪽이 row
            if (cur[1] < M-1):
                if(inp[0][cur[1] +1] == 0):
                    inp[0][cur[1] +1] = 1
                    queue_bfs.append([0, cur[1] +1])
                    cnt += 1
            if (cur[1] > 0):
                if(inp[0][cur[1] -1] == 0):
                    inp[0][cur[1] -1] = 1
                    queue_bfs.append([0, cur[1] -1])
                    cnt += 1
            # 한 번 루프 지날 때마다 업데이트 카운트
            cnt_2 -= 1    
            if (cnt_2 == 0):
                # for row in range(N):
                #     print(inp[row])
                # print()
                if (cnt != 0):
                    cnt_queue.append(cnt)
                cnt = 0
                # print(queue_bfs)
                # print(cnt_queue)
                cnt_update += 1
        cnt_update -= 1
    else: # 1 x 1 인 경우
        if (inp[1][1] == 0):
            return -1
        else:
            return 0
        
    # print(inp)
    # 마지막에 0 남아있으면 실패
    flag_0_detected = check_0(inp, M, N)
    # print(flag_0_detected)
    if (flag_0_detected):
        return -1
    else:
        return cnt_update 
    
# 토마토 맵 크기
M, N = map(int, input().split()) #각각 col, row
 
tmt_mat = [[-1 for _ in range(M)]for _ in range(N)]

# 인풋 프린트
for row in range(N):
    tmt_mat[row] = list(map(int, sys.stdin.readline().split()))
# ================== ok ============================

print(bfs(tmt_mat, M, N))




