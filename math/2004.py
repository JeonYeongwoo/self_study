n, m = map(int, input().split())

# 르장드르 공식 참고해서 구현

# 르장드르 공식 : "n! 에 대한 소수p 카운트" 는 n을 p의 1승, p의 2승, p의 3승 ... , p의 k승... 으로 나눈 값의 합과 같음.
# 즉, 200만 팩토리얼에 5가 얼마나 들어있을까 는 ==> 200만 을 5로 나눈 값 + 200만을 5^2로 나눈 값 + ... 200만을 5^k로 나눈 값 (5^k < 200만)이라는 가정 하에

divider_5 = []
divider_2 = []

i1 = 1
while(True):
    i1 *= 5
    if (i1 > 2000000000):
        break
    else: 
        divider_5.append(i1)
i2 = 1
while(True):
    i2 *= 2
    if (i2 > 2000000000):
        break
    else: 
        divider_2.append(i2)

len_5 = len(divider_5)
len_2 = len(divider_2)

# print(divider_2[12], divider_5[29])
# print(len_5, len_2)

# 5랑 2 카운트를 수행
def count_5_2(inp):
    count_5 = 0; count_2 = 0;
    # for i in range(inp, stop, -1):
    #     if (i %2 == 0 or i %5 == 0):
    #         temp = i
    #         while ((temp%2)== 0 or (temp%5) == 0 ):
    #             # print(temp)
    #             for j in range(len_5-1, -1, -1):
    #                 if (temp % divider_5[j] == 0):
    #                     temp //= divider_5[j] 
    #                     count_5 += j
    #                     break;
    #             for j in range(len_2-1, -1, -1):
    #                 # print("tried: ", divider_2[j])
    #                 if (temp % divider_2[j] == 0):
    #                     temp //= divider_2[j]
    #                     count_2 += j
    #                     break
    for i in range(len(divider_5)):
        count_5 += inp // divider_5[i]
    for i in range(len(divider_2)):
        count_2 += inp // divider_2[i]
    
    # print("count : ", count_5, count_2)
    return [count_5, count_2]
    



    

count_5 = 0
count_2 = 0

# nCm = n! / ((n-m)!* (m)!)
a1 = count_5_2(n)
a2 = count_5_2(m)
a3 = count_5_2(n-m)
# print(a1, a2)

count_5 = a1[0]- (a2[0] + a3[0])
count_2 = a1[1]- (a2[1] + a3[1])
# print(count_5, count_2)

# 답 출력
count_0 = 0
while (count_5 >0 and count_2 >0):
    count_0 += 1
    count_5 -= 1
    count_2 -= 1
    
print(count_0)