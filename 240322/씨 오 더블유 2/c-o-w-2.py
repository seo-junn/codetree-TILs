n = int(input())
line = input().strip()

count = 0
for i in range(n):
    if line[i] == 'C':
        for j in range(i+1,n):
            if line[j] == 'O':
                for k in range(j+1,n):
                    if line[k] == 'W':
                        count += 1

print(count)