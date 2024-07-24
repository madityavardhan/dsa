for _ in range(int(input())):
    n, k = map(int,input().split())
    if k==0:
        print(0)
        continue
    res=1
    k-=n
    n-=1
    while k>=1:
        k-=n
        res+=1
        if k<1:
            break
        k-=n
        res+=1
        n-=1
    print(res)