# 인터넷으로 검색.
# 참조 https://velog.io/@so_yeong/%EC%B5%9C%EB%8B%A8-%EA%B2%BD%EB%A1%9C-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98
# bfs 및 precedessors를 활용해 저장하면, 가중치 없는 경우 최단경로를 탐색할 수 있음 정도 참고함

# 1697 에 precedessors 를 저장할 수 있는 리스트 하나 더 넣기.
# 이후 precedessors 를 백트래킹하면서 스택에 저장
# ==> 마지막 answer_stack 출력하면 끝


from collections import deque

N, K = map(int, input().split())
visited = [0 for _ in range(200001)]
precedessors = [None for _ in range(200001)]

visited[N] = 1; queue_bfs = deque(); queue_bfs.append(N)
count_for_bfs = deque()


cnt2 = 1
cnt = 0
loop = 0
answer_stack = []
while (queue_bfs):
    current = queue_bfs.popleft()
    
    if (current == K):
        print(loop)
        
    
    if (current -1 >= 0):
        if (visited[current-1] == 0):
            visited[current-1] = 1
            queue_bfs.append(current-1)
            precedessors[current-1] = current
            cnt += 1
    if (current +1 <= 200000): # 인덱스 에러 방지
        if (visited[current+1] == 0):
            visited[current+1] = 1
            queue_bfs.append(current+1)
            precedessors[current+1] = current
            cnt += 1
    if (2*current <= 200000):
        if (visited[2*current] == 0):
            visited[2*current] = 1
            queue_bfs.append(2*current)
            precedessors[2*current] = current
            cnt += 1
        
    cnt2 -= 1
    if (cnt2 == 0):
        count_for_bfs.append(cnt)
        cnt = 0
        cnt2 = count_for_bfs.popleft()
        loop +=1
        
i = K 
while ( i != N):
    answer_stack.append(i)
    i = precedessors[i]

answer_stack.append(i)

while (answer_stack):
    print_item = answer_stack.pop()
    print(print_item, end = " ")