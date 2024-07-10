import math
for _ in range(int(input())):
    n = int(input())
    if n&(n-1) == 0:
        #power of two
        print(0)
    else:
        k = int(math.ceil(math.log(n,2))) #math.log(n,2)
        f = (n-k) // 2
        print(k-4*f)