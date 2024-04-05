n = int(input())
lines = [tuple(map(int,input().split())) for _ in range(n)]
lines.sort(key=lambda x:(-x[1],x[0]))

end = lines[0][0]
count = 1
for i in range(1,n):
    if lines[i][1] < end:
        count += 1
        end = lines[i][0]

print(count)