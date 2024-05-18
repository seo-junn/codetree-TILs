n1,n2 = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

for i in range(n1-n2+1):
    find = True
    for j in range(n2):
        if A[i+j] != B[j]:
            find = False
            break
    if find: break

print("Yes" if find else "No")