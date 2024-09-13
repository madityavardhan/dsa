num = int(input())

projc = list(map(int, input().split()))

s, m = sum(projc), max(projc)
if s - m >= m:  
    print(s) 
print(2 * (s - m) + 1)  
