T = int(input()) # 테스트 케이스

N = list() # 계산할 인풋 저장 리스트

for i in range(0, T):
    temp = int(input())
    if (temp> 11 or temp < 0):
        exit(1)
    
    N.append(temp)

ans = list(1 for i in range (12))
ans[0] = 1; ans[1] = 1; ans[2] = 2; ans[3] = 4;
# 이유는 모름, 그림판으로 2 3 4 5 경우의 수 계산 시
# 1, 2, 4, 7, 13 ... 의 패턴 나옴
# 이전 3개의 합이 그 An = An-1 + An-2 + An-3 패턴 이용

for i in range(4, 12):
    ans[i]= ans[i-1] + ans[i-2] + ans[i-3];
    
for i in range(T):
    # N[i] 는 해당 테스트 케이스에서 찾으려는 수의 인덱스임. ans[인덱스] 출력 위해 이값을 인덱스로 출력
    print(ans[N[i]]) 