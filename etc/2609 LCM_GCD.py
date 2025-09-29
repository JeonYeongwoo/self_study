# 틀려서 풀이 검색함.

# 원리 : 유클리드 호제법 : 두 수가 서로 상대방 수를 나누어 원하는 수 얻기
# r = a % b라면(단, a > b) a와 b의 최대공약수는 b와 r의 최대공약수
# b를 r로 나눈 나머지 r' 구하고, 다시 r을 r'으로 나눈 나머지 구하기 반복

a, b = map(int,input().split());

def gcd(a,b) :
    while (b>0):
        a, b = b, a%b;
    return a

def lcm(a,b):
    return int(a*b / gcd(a,b));

print(gcd(a,b))
print(lcm(a,b))
    