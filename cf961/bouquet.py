for _ in range(int(input())):
    # n,m = map(int, input().split())
    # nums = list(map(int,input().split()))
    # nums.sort()
    # l, res, ans = 0, 0, 0
    # for r in range(n):
    #     res+=nums[r]
    #     while (l<=r and ((res>m) or (nums[r]-nums[l]>1)) ):
    #         res-=nums[l]
    #         l+=1
    #     ans=max(ans, res)
    # print(ans)
    # bouquet 2
    n,m = map(int, input().split())
    a = list(map(int,input().split()))
    c = list(map(int,input().split()))
    nums = []
    for i in a:
        while c>0:
            nums.append(i)
            c-=1
    nums.sort()
    l, res, ans = 0, 0, 0
    for r in range(n):
        res+=nums[r]
        while (l<=r and ((res>m) or (nums[r]-nums[l]>1)) ):
            res-=nums[l]
            l+=1
        ans=max(ans, res)
    print(ans)