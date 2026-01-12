N = int(input())
result = 0

# for i in range(1, N+1):
#     add = 1;
#     div = i;
#     while((div // 10) != 0):
#         add += 1;
#         div //= 10
#     result += add
    
# print(result)

min_list = [9, 90, 900, 9000, 90000, 900000, 9000000,90000000,900000000]

add = 1;
for i in range(len(min_list)):
    if (N - min_list[i] >= 0):
        result += add * min_list[i]
    else:
        result += add * N;
        break
    N -= min_list[i]
    add += 1
    
print(result)