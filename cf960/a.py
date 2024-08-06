for _ in range(int(input())):
    n = int(input())
    nums = list(map(int,input().split()))
    nums.sort()
    itr = 1
    for i in range(n-1,0,-1):
        if nums[i]<nums[i-1]:
            break
        itr+=1
    if itr%2!=0:
        print("YES")
    else:
        print("NO") 