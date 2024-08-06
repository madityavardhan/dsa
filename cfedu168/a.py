for _ in range(int(input())):
    s = input().strip()
    x=0
    for i in range(0,len(s)-1):
        if s[i]==s[i+1]:
            x=i+1
    res  = ""
    for i in range(len(s)+1):
        if i==x:
            res += chr(ord(s[x - 1]) - ord('a') + ord('0'))
        else:
            res += s[i - 1] if i > 0 else ""
    print(res)