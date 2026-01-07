# 풀이 실패 _ 공부용 기록

# 오답 : 2번째 반복문에서 케이스를 절반만 고려하여, 최대 금액을 제대로 계산하지 못함.
# 반례: dp[1..3]이 완벽히 맞아도, j >= i/2만 보면 dp[4] 틀림

# 오답 코드
# for current in range(2, N+1): # i 장의 카드를 살 때 
#     for j in range(current+1, current//2-1, -1): # for j in range(1, current+1): 
#         max_price[current] = max(max_price[current], max_price[current-j] + int(CardPackPrices[j-1])) 


# gpt 답변
# i=4라고 하자. 가격이:

# P1 = 5
# P2 = 1
# P3 = 1
# P4 = 1

# 이때 작은 i들은 최적으로 잘 구해진다고 치면:

# dp[1] = 5
# dp[2] = 10 (1+1)
# dp[3] = 15 (1+1+1)
# 이제 dp[4]를 구할 때 “큰 쪽 절반만” 즉 j ∈ {2,3,4}만 보면:
# j=4: dp[0] + P4 = 0 + 1 = 1
# j=3: dp[1] + P3 = 5 + 1 = 6
# j=2: dp[2] + P2 = 10 + 1 = 11 ← (이게 최대)
# 그래서 dp[4]=11 이라고 결론 나옴.
# 근데 진짜 최적은 j=1일 때:
# j=1: dp[3] + P1 = 15 + 5 = 20
# 즉, dp[1..3]이 이미 정확해도 “j를 절반만 보면” dp[4]에서 최적을 놓쳐.
# N = int(input())




# 정답 코드 --> 백준엔 제출 x
CardPackPrices = input().split()

max_price = [0 for i in range(N+1)]

def max(a, b):
    if (a > b):
        return a
    else:
        return b


for current in range(1, N+1): # i 장의 카드를 살 때
    for j in range(0, current+1):
        max_price[current] = max(max_price[current], max_price[current-j] + int(CardPackPrices[j-1]))
        

print(max_price[N])






    