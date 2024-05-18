min_val = 1000
max_val = -1000

for n in map(int,input().split()):
    if n == 999 or n == -999: break
    if n > max_val: max_val = n
    if n < min_val: min_val = n

print(max_val,min_val)