cnt = 0

for _ in range(int(input())):
    avg = sum(map(int,input().split()))/4
    if avg >= 60:
        cnt += 1
        print("pass")
    else:
        print("fail")

print(cnt)