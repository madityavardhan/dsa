for _ in range(int(input())):
    x,y = map(int,input().split())
    if x==y:
        print("YES")
    elif x>y:
        if y+1 >= x:
            print("YES")
        else:
            print("NO")
    else:
        if x+2 >= y:
            print("YES")
        else:
            print("NO")