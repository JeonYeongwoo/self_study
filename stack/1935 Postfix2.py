N = int(input()); # 1. 피연산자 개수 확인

inp = input() # 2. 계산식 확인
inp_len = len(inp); # 계산식 길이

alphabets = list(0 for i in range(26)); head = 0;
values = list(0 for i in range(26)); stack_top = -1; # 값 : 스택 이용

operand_stack = list();

a = 'A'; index = -1;

# 3. 변수 값 확인
for i in range(N):
    values[i] = int(input());

# 4. 로직 수행
for i in range(inp_len):
    current = inp[i]; # 현재 값 미리 계산
    val_for_insert = 0
    
    
    # 피연산자 확인 시 스택에 값 추가
    if ( 'A' <= current <= 'Z'):
        index = ord(inp[i]) - ord(a); # 인덱스 계산
        operand_stack.append(values[index]);
        stack_top += 1;
        head += 1;
    # 연산자 확인 시 스택에서 값 빼서 계산
    else:
        if (current == '+'):
            val_for_insert = operand_stack[stack_top-1] + operand_stack[stack_top];
        elif(current == '-'):
            val_for_insert = operand_stack[stack_top-1] - operand_stack[stack_top];
        elif(current == '*'):
            val_for_insert = operand_stack[stack_top-1] * operand_stack[stack_top];
        elif(current == '/'):
            val_for_insert = operand_stack[stack_top-1] / operand_stack[stack_top];
        elif(current == '%'):
            val_for_insert = operand_stack[stack_top-1] % operand_stack[stack_top];
            
        operand_stack.pop(stack_top); stack_top -= 1;
        
        operand_stack.pop(stack_top); stack_top -= 1;
        operand_stack.append(val_for_insert); stack_top += 1;
        
        
# round(number, 2) < 둘째자리까지 표시해주는 함수  
# 혹은 >> print(f"{number:.2f}") f"{operand_stack[0]:.2f}"
print(f"{operand_stack[0]:.2f}"); # 마지막 남은 값이 결괏값