N = int(input())
#그림판으로 그려보면
#케이스는 두 가지로 나뉨

# 1. 맨 끝이 세로 2개로 세워진 경우 => 경우의 수는 n-2 번째와 동일
# 2. 맨 끝이 가로 1개로 세워진 경우 => 경우의 수는 n-1 번째와 동일

# 따라서 case(n) = case(n-1) + case (n-2) 임.

case = list(-1 for i in range(1001))
case[0] = 1; case[1] = 1; case[2] = 2 # gpt 도움 0번째 -> 아무것도 놓지 않는 방법. 1가지 경우의 수 존재.

for i in range (3, 1001): # gpt 도움 : 1000번째 인덱스에 값을 넣지 않음. -> 1001로 수정
    case[i] = case[i-1] + case[i-2];
    
print(case[N] % 10007);