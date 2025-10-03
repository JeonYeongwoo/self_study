inp = list(0 for i in range(9))

for i in range(9):
    inp[i] = int(input())

ans = list(0 for i in range(7))
    
        

# 7번 반복문 시행. 
# 각 단계 : 탐색하지 않은 인덱스를 하나씩 증가시킴  --> 이전 단계의 인덱스 '다음' 인덱스만 탐색 
#                  (이전 for문 탐색 범위가 n 번째라면... 그 다음 for문의 탐색 범위는 n + 1 번째부터..)
# 모든 단계를 탐색함. for (인덱스1, 인덱스2) --> 에서 인덱스 2는 마지막으로 탐색할 인덱스 의미.
# 마지막 단계는 각 인덱스가 2,3,4,5,6,7,8 << 의 인덱스인 경우이므로 해당 숫자가 각 탐색의 마지막 탐색 인덱스
for a in range(0,3):
    ans[0] = inp[a]
    for b in range(a+1,4):
        ans[1] = inp[b]
        for c in range(b+1,5):
            ans[2] = inp[c]
            
            for d in range(c+1,6):
                ans[3] = inp[d]
                
                for e in range(d+1,7):
                    ans[4] = inp[e]
                    
                    for f in range(e+1,8):
                        ans[5] = inp[f]
                        
                        for g in range(f+1,9):
                            ans[6] = inp[g]
                            sum = 0
                            for h in range(0, 7):
                                sum += ans[h]

                            if (sum == 100): 
                                ans.sort();  # 소팅 함수 -> 추후에 구현해보기. 합병 정렬 및 퀵 정렬.
                                for h in range(len(ans)):
                                    print(ans[h])   
                                exit(0)
                            
           

