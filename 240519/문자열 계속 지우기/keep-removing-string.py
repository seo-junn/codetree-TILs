A = input()
B = input()

while len(A) >= len(B):
    find = False
    for i in range(len(A)-len(B)+1):
        temp = True
        for j in range(len(B)):
            if A[i+j] != B[j]:
                temp = False
                break
        if temp:
            find = True
            A = A[:i] + A[i+len(B):]
            break
    if not find: break

print(A)