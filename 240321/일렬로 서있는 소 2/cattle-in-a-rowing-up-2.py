N = int(input())
cows = list(map(int,input().split()))

count = 0
for i in range(N):
    for j in range(i+1,N):
        if cows[i] <= cows[j]:
            for k in range(j+1,N):
                if cows[j] <= cows[k]:
                    count += 1

print(count)