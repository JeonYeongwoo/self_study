import sys

N = int(input())
answer = []

def search(search_index, cur_time, payment):
    # if (search_index == N):
    #         answer.append(payment)
    #         return
    for i in range(search_index, N+2):
        if (i == N+1):
            answer.append(payment)
            return
        
        if (i >= cur_time and end_time[i] < N+2):
            # print("added: ", i, cur_time, pay[i])
            search(i+1 ,end_time[i] , payment + pay[i])
        # else:
        #     print ("skip:", i, cur_time, pay[i])

end_time = [0 for _ in range(N+1)]
pay = [0 for _ in range(N+1)]
for i in range(1, N+1):
    i1, i2 = map (int, sys.stdin.readline().split())
    end_time[i] = i1 + i
    pay[i] = i2
    
# print(end_time, pay)
    
search(1, 1, 0)
answer.sort()
print(answer[len(answer) -1])
