# codefordes 962 problem a

for _ in range(int(input())):
    n = int(input())
    res = 0
    if n >= 4:
        res+=n//4
        n%=4
    if n>=2:
        res+=n//2
    print(res)