barcount = 0; # 표시된 총 개수 체크
bar_stacked = 0; # 레이저 밑에 놓인 바
parenthesis_stack = list();
bar_sig = 0;

inp = input(); # 1. input 확인


def split():
    global barcount;
    # 현재까지 놓여있는 bar이 하나씩 복사되는 느낌 
    barcount += bar_stacked; 
    
#2. 인풋 길이 확인, 및 현재 확인중 문자 표시
len_inp = len(inp); current = 0;

#3 하나씩 검사하며 로직 진행
for i in range(len_inp):
    current = inp[i];
    
    if(current == '('):
        if(bar_sig == 0):
            bar_sig = 1;
        else:
            barcount +=1;
            bar_stacked += 1;
            parenthesis_stack.append('(');
    elif(current == ')'):
        if (bar_sig == 1):
            bar_sig = 0;  
            split();
        else :
            bar_stacked -= 1;
            parenthesis_stack.pop(bar_stacked);
            
print(barcount);