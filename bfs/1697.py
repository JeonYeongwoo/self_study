# 인터넷으로 검색.

# bfs를 통해 탐색한 경로가 최단 경로인 이유
# bfs를 이용해 특정 지점까지 도달하는 시간을 찾은 경우.
# 해당 시점까지 탐색한 경로는 모두 같은 비용을 요구하므로
# 결론적으로 해당 시점이 젤 빠르다..?

# 1697
# X-1, X+1, 2*X로 이동하는 것이므로
# bfs를 이용해 x-1, X+1, 2*x를 검색
# 매 번마다 추가될때마다 기록해서
# 빼면서 몇번째 탐색인지 기록하면 될듯함.

from collections import deque

N, K = map(int, input().split())
visited = [0 for _ in range(200001)]

visited[N] = 1; queue_bfs = deque(); queue_bfs.append(N)
count_for_bfs = deque()


cnt2 = 1
cnt = 0
loop = 0
while (queue_bfs):
    current = queue_bfs.popleft()
    
    if (current == K):
        print(loop)
        exit(0)
        
    
    if (current -1 >= 0):
        if (visited[current-1] == 0):
            visited[current-1] = 1
            queue_bfs.append(current-1)
            cnt += 1
    if (current +1 <= 200000): # 인덱스 에러 방지
        if (visited[current+1] == 0):
            visited[current+1] = 1
            queue_bfs.append(current+1)
            cnt += 1
    if (2*current <= 200000):
        if (visited[2*current] == 0):
            visited[2*current] = 1
            queue_bfs.append(2*current)
            cnt += 1
        
    cnt2 -= 1
    if (cnt2 == 0):
        count_for_bfs.append(cnt)
        cnt = 0
        cnt2 = count_for_bfs.popleft()
        loop +=1
        
        
        