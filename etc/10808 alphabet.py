str = input();

count = list(0 for i in range(26))

a = 'a'

for i in range(len(str)):
    count[ord(str[i]) - ord(a)] +=1;

for i in range(len(count)):
    print(count[i], end = ' ')