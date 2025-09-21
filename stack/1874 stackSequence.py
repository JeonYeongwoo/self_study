#입력할 행 수 전달
row = int(input())

inputList = list() #입력할 리스트
output = list() # 아웃풋 리스트

stack = list()
stackTop = -1; # 스택 탑 표시
stackNum = 1; # 스택에 들어갈 수 표시

# 인풋 받음
for i in range(row):
    inputList.append(int(input()))
    

for i in range(row):
    if (stackNum == inputList[i]): 
        stackTop += 1; stack.append(stackNum); stackNum += 1; output.append('+')
    
    if (stackNum < inputList[i]): # 스택에 들어간 값보다 인풋값 큰경우? 아직 안들어간 것. 따라서 넣음
        stackTop += 1; stack.append(stackNum); stackNum += 1; output.append('+')
        while(stack[stackTop] != inputList[i]):
            stackTop += 1; stack.append(stackNum); stackNum += 1;
            output.append('+')
            
        # 넣은 뒤 빼야 하니까 빼줌
        output.append('-'); stack.pop(); stackTop -= 1;
        
    elif (stack[stackTop] == inputList[i]):
        output.append('-');
        stack.pop();
        stackTop -= 1;
        
    else : # 스택에 들어간 top 값보다 현재 검사중 input이 작은 경우, 빼내도 원하는 수열 안나옴 따라서 no
        print('NO')
        exit(0)
        
for i in range(len(output)):
    print(output[i])