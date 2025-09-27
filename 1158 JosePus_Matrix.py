N, K = map(int,input().split());

mat = list();
josephus = list();
index = 0;

if ( K > N ):
    exit();

for i in range(1,N+1):
    mat.append(i);

while (mat):
    index += K-1;  # gpt 도움받음. index += K; -> index -= K; 현 위치에서 n번째 이고, 시작 지점이 0번째라고 생각해야 하므로 K-1 만큼 더해줘야 함.
    
    div = len(mat)
    if (index >= div): # gpt 도움받음. if index >= div: -> index > div.. index == div 를 고려하지 못함.
        index %= div;
    
    ## print(mat[index], index, div ) 디버깅용 코드
    
    josephus.append(mat[index])
    mat.pop(index)
    

outputLength = len(josephus);

print('<', end = '')
for i in range(outputLength):
    if i != outputLength-1:
        print(josephus[i], end = ', ');
    else:
        print(josephus[i], end = '');
print('>', end = '')