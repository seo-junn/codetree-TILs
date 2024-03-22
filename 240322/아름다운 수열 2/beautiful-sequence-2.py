import copy

N, M = map(int,input().split())

A = list(map(int,input().split()))
B = list(sorted(map(int,input().split())))

def check(arr_A,arr_B):
    AA = copy.deepcopy(arr_A)
    AA.sort()
    if AA == arr_B: return True
    else: return False

ans = 0
for i in range(N-M+1):
    if check(A[i:i+M],B): ans += 1

print(ans)