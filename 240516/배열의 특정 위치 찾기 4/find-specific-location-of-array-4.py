cnt, total = 0,0

for n in map(int,input().split()):
    if n:
        if n%2 == 0:
            cnt += 1
            total += n
    else:
        break

print(cnt,total)