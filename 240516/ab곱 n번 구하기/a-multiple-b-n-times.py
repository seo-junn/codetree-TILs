for _ in range(int(input())):
    a,b = map(int,input().split())
    ans = 1
    for num in range(a,b+1): ans *= num
    print(ans)