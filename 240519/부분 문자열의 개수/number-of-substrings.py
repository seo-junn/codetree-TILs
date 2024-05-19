A = input()
B = input()
cnt = 0

for i in range(len(A)-1):
    if B == A[i:i+2]:
        cnt += 1

print(cnt)