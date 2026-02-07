# 1759
L, C = map(int, input().split()) # L : 길이

# char_list = []
char_list = input().split()
char_list.sort()

# 모음 종류
kinds = {'a', 'e', 'i', 'o', 'u'}

loop_cnt = 0;

stack = []
vowel = 0 # 모음
consonant = 0 # 자음

# 글자 맵핑
char_kind = [0 for _ in range(C)]
for i in range(C):
    # 0은 자음, 1은 모음으로 저장
    if (char_list[i] in kinds):
        char_kind[i] = 1; 

# ================== 아래를 고쳐야 함 =====================

def dfs(start):
    global loop_cnt, vowel, consonant
    loop_cnt += 1 # 루프 카운트는 여기서 되야 함.
    
    for i in range(start, C-L+loop_cnt):   
        if (len(stack) < L): # 4 이하에선 돌긴 함
            # ======= 아이템 어펜드 ======
            stack.append(char_list[i])
            if (char_kind[i] == 1): 
                vowel += 1
            else : 
                consonant += 1
                
            # 재귀 깊이 만큼만 호출되도록 이부분 추가
            if (loop_cnt < L):
                dfs(i+1)
        
        if (loop_cnt == L):
            if (vowel >= 1 and consonant >= 2):
                print(''.join(stack)) 
                
        popped = stack.pop()
        # print("pop: ",popped, end = " ")
        if (popped in kinds):
            vowel -=1
        else:
            consonant -=1
    loop_cnt-= 1
# ===============================
        
# 재귀 깊이 표현할 땐 함수 시작 부분에 깊이 카운트 변수 +1. 마지막 부분에 -1 하는 부분을 둬야 함.
# 재귀 깊이를 표현하는 변수를 다른 변수와 혼용해서 사용하지 말 것.
#  >>>> 반복문에서 재귀 깊이를 사용하는 변수를 지속적으로 사용해서 문제 풀이가 늦어짐. 

# 재귀 최대 깊이 이상만큼 호출되지 않기 위해선 로직이 추가적으로 필요함.
dfs(0)
            