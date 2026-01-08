#백준 15988 문제

N = int(input())

input_values = [0 for _ in range(N)]
for i in range(0,N):
    input_values[i] = int(input())
    
dp = [0 for _ in range(1000001)]

dp[0] = 1
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, 1000001):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i-3]
    if dp[i] >          1000000009:
        dp[i] = dp[i] % 1000000009
    
for i in range(0,N):
    print(f"{dp[input_values[i]] % 1000000009}")