import sys, math

N = int(input())
end_cond = (N // 2) + 1

answer = []

def min_dif(arg_team, start_index, depth):
    team_A = arg_team.copy()
    if (depth < end_cond):
        for i in range(start_index, N):
            team_A.append(i)
            min_dif(team_A, i+1, depth+1)
            team_A.pop()
    else:
        team_B = []
        for j in range(N):
            if (j not in team_A):
                team_B.append(j)
        # print("team_A:",team_A)
        # print("team_B:",team_B)
        # print("abs:", abs(sum_stats(team_A)- sum_stats(team_B)))
        answer.append(abs(sum_stats(team_A)- sum_stats(team_B)))
        return
            
        
            
            
    
def sum_stats(arr):
    sum = 0;
    # print("check: ", arr)
    for check_number in arr:
        for should_add in arr:
            if (should_add == check_number):
                continue
            sum += stats[check_number][should_add]
    
    return sum
    

stats = [[0 for _ in range(N)] for _ in range(N)]

for i in range(0, N):
    stats[i] = list(map(int, sys.stdin.readline().split()))
    
# for i in range(N):
#     for j in range(N):
#         print(stats[i][j], end = " ")
#     print()

min_dif([],0,1)
answer.sort()
# print(answer)
print(answer[0])
