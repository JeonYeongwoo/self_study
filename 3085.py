# 3085 번 문제
# 다 찾기 가로 세로 한번씩

def bigger(a,b):
    if (a>=b):
        return a
    return b;


def max_candy_num(index, control):
    global mixed_arr
    #control = 0 : 가로 / 1 : 세로 체크
    current_candy = None
    max_count = 1
    cur_count = 1
    if control == 0:
        for i in range(N): # 현재 행의 맥스 캔디 값 찾기
            if (current_candy != mixed_arr[index][i]): # 검사하던 캔디랑 다른거인경우, 체크하는 걸 바꾸고 카운트 다시
                current_candy = mixed_arr[index][i]
                max_count = bigger(max_count, cur_count)
                cur_count = 1;
            else:     
                cur_count += 1;
    else :
        for i in range(N):
            if (current_candy != mixed_arr[i][index]): # 검사하던 캔디랑 다른거인경우, 체크하는 걸 바꾸고 카운트 다시
                current_candy = mixed_arr[i][index]
                max_count = bigger(max_count, cur_count)
                cur_count = 1;
            else:     
                cur_count += 1;
                
    max_count = bigger(max_count, cur_count)
    return max_count
      
def mix(i, j, index):
    # ========= 1차 시도 실패 ==============
    # global arr;
    # global mixed_arr 
    # mixed_arr = arr;
    
    #1) mixed_arr = arr 때문에 “복사”가 아니라 “같은 보드”를 같이 씀
    # mix()에서 mixed_arr = arr로 해버리면,
    # mixed_arr는 arr의 복사본이 아니라
    # arr 그 자체를 가리키는 별명(참조) 이 돼.
    # 그래서 한 번 섞을 때마다 원본 arr가 계속 바뀌고,
    # 다음 테스트 케이스(다른 자리 교환)도 원본이 이미 망가진 상태에서 또 섞게 돼.
    # → “한 번만 바꿔보고 최대 길이 측정”이 아니라 “계속 누적 변형된 보드”를 검사하게 됨.
    # 2) 세로(혹은 가로) 스왑 코드가 실제로는 “두 칸을 같은 값으로 만들어버림”
    # index == 1(세로 치환이라고 쓴 부분)에서:
    # 먼저 mixed_arr[i][j]에 오른쪽 값을 넣고,
    # 그 다음 줄에서 mixed_arr[i][j+1] = mixed_arr[i][j] 해버려서

    # 결과적으로 두 칸이 둘 다 같은 문자가 돼버려.
    # =================================================
    
    # 고친 코드
    global mixed_arr 
    mixed_arr = [row[:] for row in arr] # 이렇게 해야 행이 복제됨
    
            
    temp = mixed_arr[i][j];
    if (index == 0): # 인덱스 0이면 가로 치환
        mixed_arr[i][j] =  mixed_arr[i+1][j]
        mixed_arr[i+1][j] = temp;
    else : #인덱스 1이면 세로 치환 
        mixed_arr[i][j] = mixed_arr[i][j+1]
        mixed_arr[i][j+1] = temp
        
    
          


N = int(input()) # 인풋 개수

arr = [['A' for _ in range(N)] for _ in range(N)]
mixed_arr = [['A' for _ in range(N)] for _ in range(N)]
max = 0;

for i in range(N):
#   arr[i] = list(input().split()) << 이렇게 하면 한글자씩 저장 x, 한 문장으로 그냥 대체되어 버림
    inp = input()
    arr[i] = list(inp)
    
for k in range(N-1):
    for l in range(N): 
        # 가로 믹스
        mix(k, l, 0)
        for i in range(N): # i 루프문이 한 배열에 대한 맥스값 확인임.
            for j in range(2):
                check_candy_max = max_candy_num(i, j)
                max = bigger(max, check_candy_max)
                
    for l in range(N):
        # 세로 믹스
        mix(l, k, 1)
        for i in range(N): # i 루프문이 한 배열에 대한 맥스값 확인임.
            for j in range(2):
                check_candy_max = max_candy_num(i, j)
                max = bigger(max, check_candy_max)   
        
        
print(max)
