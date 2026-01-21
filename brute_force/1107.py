# 고려 못한 반례
# 1555
# 3
# 0 1 9
# -> 작은 수부터 출력해서 찾음
# 고려 못했던 케이스  
# 0
# 1
# 0
# 1 
# 처음에 while 문 조건을 a-diff >0 -> if문 조건으로 바꿔서 해결
import math
# 각 숫자에 대해 숫자 활성화 돼잇으면 +1
inp = input() # 이동하려는 채널

M = int(input()) # 고장난 버튼 개수

activated = [1 for _ in range(10)]
result = 0

if (M != 0):
    broken = list(map(int, input().split()))
    for b in broken:
        activated[b] = 0

# 모든 버튼이 비활성화 된 경우, 그냥 100 빼기
if (M == 10):
    print(abs(int(inp) - 100))
    exit(0)


# closest_number = []
# for i in range(len(inp)):
#     cur = int(inp[i])
#     check = 10
    
#     if(activated[cur] == 1):
#         closest_number.append(f'{cur}')
#         result = result + 1
#         continue
#     else:
#         min = 9
#         for j in range(10):
#             if (activated[j] == 1):
#                 if (min > abs(cur - j)):
#                     min = abs(cur-j)
#                     check = j            
#         closest_number.append(f'{check}')
#         result = result + 1

# # int(''.join(inp)) << 이렇게 하면 숫자로 변형 가능 << gpt
# print("closest number is: ", closest_number)
# result += abs(int(inp) - int(''.join(closest_number))) # 80000 에 안되넹

# result_min_above = 0
# min_above = []    
# if (activated[1] == 1):
#     min_above.append('1')
#     result_min_above += 1
#     i = 0
#     for i in range(9):
#         if (activated[i] == 1):
#             break
#     for j in range(len(inp)):
#         result_min_above += 1
#         min_above.append(f'{i}')
#     print("min_above: ", min_above)
#     result_min_above += abs(int(inp) - int(''.join(min_above)))
#     print("result_min_above: ", result_min_above)
    
#     if (result >= result_min_above):
#         result = result_min_above

def check_possible(str):
    for c in str:
        check = int(c)
        if (activated[check] == 0):
            return False

    return True



a = int(inp)
diff = 0;
ans = 0;
        # 고려 못했던 케이스  
        # 0
        # 1
        # 0
        # 1 
while (True):
    check_1 = str(a+ diff)
    check_2 = str(a-diff)
    
    # if (a+diff <=500000):
    if (a-diff >=0): # 작은 수가 먼저 와야 하므로 이렇게 적기
        # 원래는 순서 반대로 적었음..
        # 하단의 반례 보고 고침
            # 1555
            # 3
            # 0 1 9
        if (check_possible(check_2)):
                ans = int(check_2)
                break
    if(check_possible(check_1)):
            ans = int(check_1)
            break
    
    diff +=1
# print(ans)
result = abs(a-ans) + len(str(ans))


result_no_button = abs(int(inp) - 100)

if (result_no_button < result):
    result = result_no_button
    
print(result)
            