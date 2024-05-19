ans = 0

A = input()
B = input()

while ans < len(A) and A != B:
    ans += 1
    A = A[-1] + A[:-1]

print(ans if ans < len(A) else -1)