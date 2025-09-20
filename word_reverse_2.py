inputs = input();
stack = list();
stackTop = -1;

parenthesisRecognized = 0; # 0 is not detected, 1 is detected 

def printReverseWord():
    global stackTop, stack;
    while(stackTop != -1):
        print(stack[stackTop], end='');
        stack.pop();
        stackTop -= 1;
    
    
for j in range(len(inputs)):
    token = inputs[j]
    
    if (token == '<' and parenthesisRecognized == 0):
        printReverseWord();
        
    if (token == '<' or parenthesisRecognized == 1):
        parenthesisRecognized = 1;
                
        print(token, end = ''); 
        if (token == '>'):
            parenthesisRecognized = 0;
        continue;
                    
            
    if (token == ' '):
        printReverseWord();
        print(' ', end='');
    else:
        stackTop += 1;
        stack.append(token);   
         
printReverseWord();  print();
    