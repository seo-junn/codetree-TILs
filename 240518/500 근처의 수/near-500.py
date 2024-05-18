max_val,min_val = 0,1001

for n in map(int,input().split()):
    if n < 500:
        if n > max_val: max_val = n
    else:
        if n < min_val: min_val = n

print(max_val,min_val)