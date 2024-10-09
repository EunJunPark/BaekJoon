N = int(input())
F = int(input())

currentN = N - (N % 100)
cnt = 0
result = 0

for i in range(cnt, F, 1):
    #print("cuttrentN: ", currentN)
    if currentN % F == 0 : 
        result = currentN % 100 
        break
    else: 
        currentN += 1 
 
print(f"{result:02}")