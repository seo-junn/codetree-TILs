import sys

n = int(sys.stdin.readline())
vals = list(map(int,sys.stdin.readline().split()))

profit = 0
get_val = sys.maxsize

for val in vals:
    if get_val > val:
        get_val = val
    else:
        profit = max(profit,val-get_val)

print(profit)