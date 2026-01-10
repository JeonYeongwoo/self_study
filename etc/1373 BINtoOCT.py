# 1373번
inp = input()

N = len(inp) -1

output = ""
for i in range (N, -1, -3):
    current = 0
    for j in range(i, i-3, -1):
        if (i - j < 0 or (j < 0) or (i < 0)):
            break      
        if inp[j] == "1":
            current += 2**(i - j)
    output = str(current) + output;

print(output)