str = input();

count = list(-1 for i in range(26))
valid = list(0 for i in range(26))

a = 'a'

for i in range(len(str)):
    index = ord(str[i]) - ord(a);
    if (valid[index] == 0):
        valid[index] = 1;
        count[index] = i;
    
        

for i in range(len(count)):
    print(count[i], end = ' ')