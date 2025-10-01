# 1463 dynamic programming 

dp = list(-1 for i in range(1000001))
dp[1] = 0; dp[2] = 1; dp[3] = 1; 
X = int(input())
# 검색한 힌트 
# 각 숫자를 1로 만드는 데 필요한 최소 연산 횟수를 저장하고, 
# 더 작은 수(예: 9, 5, 3)의 결과값을 활용하여 10을 1로 만드는 
# 최소 연산 횟수를 찾는 방식으로 문제를 해결할 수 있습니다. 
# 10의 경우에 `dp`은 다음 중 가장 작은 값이 됩니다
# dp[10] = dp[9] + 1
# dp[10] = dp[5] + 1
# dp[10] = dp[3] + 1

def min(param1, param2):
    min_val = None;
    if (param1 >= param2):
        min_val = param2;
    else:
        min_val = param1;
        
    return min_val;

for i in range( 4 ,1000001):
    if(dp[i] == -1 and ((i % 2) == 0)):
        if((i % 3 == 0)):
            # 2와 3 둘 다 나눠지는 경우에는 2로 나눠지는 경우,
            #3으로 나눠지는 경우와 모두 비교해야 함.
            dp[i] = min(
                min(dp[i-1] + 1, dp[int(i/2)] + 1), 
                min(dp[i-1] + 1, dp[int(i/3)] + 1)
                );
            continue;
        # 2로만 나눠지는 경우 
        dp[i] = min(dp[i-1] + 1, dp[int(i/2)] + 1);
    elif(dp[i] == -1 and (i % 3) == 0):
        # 3으로만 나눠지는 경우
        dp[i] = min(dp[i-1] + 1, dp[int(i/3)] + 1);
    else :
        dp[i] = dp[i-1] + 1

print(dp[X]);