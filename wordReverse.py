trNum = input()

inputs = list();
stack = list();
stackTop = -1;

def printword():
    global stackTop, stack;
    while(stackTop != -1):
        print(stack[stackTop], end='');
        stack.pop();
        stackTop -= 1;
        
    

for i in range(int(trNum)): # ok
    inputs.append(input())
    
    
for i in range(int(trNum)):
    
    for j in range(len(inputs[i])):
        token = inputs[i][j]
        
        if (token == ' '):
            printword();
            print(' ', end='');
        else:
            stackTop += 1;
            stack.append(token);
            
    printword();  print();
    