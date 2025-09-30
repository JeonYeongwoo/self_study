M, N = map(int,input().split()); # 인풋 값
primtCount = 0;

# 에라토스테네스 채로 미리 만들어놓음
primeMark = list(1 for i in range(1000001))
primeMark[0] = 0; primeMark[1] = 0; # 0과 1은 소수가 아님.
primes = list();

for i in range(0, 1000001):
    
    if (primeMark[i] == 1):
        # 1인 경우, 걸러지지 않았으므로, 소수임.
        # 1. 먼저 소수 리스트에 추가함.
        primes.append(i);
        checkLimit = int(1000000 / i);
        
        # 곱해지는 값에 있으면 소수 아님 -> 체로 거름
        for j in range(checkLimit): 
            primeMark[i*j] = 0;
        
    else : # if (primeNumbers[i] == 0):
        continue;
    

for i in range(len(primes)):
    if ( M <= primes[i]):
        if (primes[i]> N): # N보다 큰 경우? 그냥 종료 
            exit()
        print(primes[i])
    